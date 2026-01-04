import time
import nls
import os

# ================= 配置区 =================
URL = "wss://nls-gateway-cn-shanghai.aliyuncs.com/ws/v1"
APPKEY = os.getenv("ALI_NLS_APPKEY", "")  # 从控制台项目获取（不要写死在代码里）
TOKEN = os.getenv("ALI_NLS_TOKEN", "")    # 从控制台或代码获取（不要写死在代码里）

if not APPKEY or not TOKEN:
    raise RuntimeError(
        "未配置阿里云 NLS 凭证：请设置环境变量 ALI_NLS_APPKEY 与 ALI_NLS_TOKEN 后再运行该脚本"
    )

# ================= 回调函数 =================
class TestSt:
    def __init__(self, tid, test_file):
        self.__th = nls.NlsSpeechTranscriber(
            url=URL,
            token=TOKEN,
            appkey=APPKEY,
            on_sentence_begin=self.test_on_sentence_begin,
            on_sentence_end=self.test_on_sentence_end,
            on_start=self.test_on_start,
            on_result_changed=self.test_on_result_changed,
            on_completed=self.test_on_completed,
            on_error=self.test_on_error,
            on_close=self.test_on_close,
            callback_args=[tid]
        )
        self.__file = test_file

    def start(self):
        # 启动识别，开启中间结果（实时出字）
        self.__th.start(aformat="pcm",
                        enable_intermediate_result=True,
                        enable_punctuation_prediction=True,
                        enable_inverse_text_normalization=True)
        
        # 模拟读取音频流发送
        with open(self.__file, "rb") as f:
            self.__slices = zip(*(iter(f.read()),) * 640) # 每次发很小一段
            for i in self.__slices:
                self.__th.send_audio(bytes(i))
                time.sleep(0.01) # 模拟真实语速

        # 发送结束指令
        self.__th.stop()

    def test_on_sentence_begin(self, message, *args):
        print("句子开始:", message)

    def test_on_sentence_end(self, message, *args):
        print("句子结束 (最终结果):", message['payload']['result'])

    def test_on_result_changed(self, message, *args):
        print("中间结果 (变动中):", message['payload']['result'])

    def test_on_error(self, message, *args):
        print("出错了:", message)

    def test_on_close(self, *args):
        print("连接关闭")

    def test_on_start(self, message, *args):
        print("握手成功")

    def test_on_completed(self, message, *args):
        print("识别完成")

if __name__ == "__main__":
    # 请确保目录下有 test.pcm 或 test.wav (16000Hz, 16bit, Mono)
    t = TestSt("thread1", "test.pcm")
    t.start()