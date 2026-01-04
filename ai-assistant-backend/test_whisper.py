import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import load_dataset

import os


device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = os.getenv('WHISPER_MODEL') or "openai/whisper-base"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    torch_dtype=torch_dtype,
    device=device,
)

dataset = load_dataset("distil-whisper/librispeech_long", "clean", split="validation")
sample = dataset[0]["audio"]

result = pipe(
    "C:\\Users\\qqrtq\\Documents\\GitHub\\computer-software\\test.mp3", 
    return_timestamps=True
)
print(result["text"])

##要转录本地音频文件，只需在调用管道时传递音频文件的路径：

#result = pipe("audio.mp3")
##可以通过将多个音频文件指定为列表并设置参数，并并行转录多个音频文件：batch_size

#result = pipe(["audio_1.mp3", "audio_2.mp3"], batch_size=2)

##Transformers兼容所有Whisper解码策略，如温度回退和对先前tokens的条件。以下示例演示了如何启用这些启发式：

#generate_kwargs = {
#    "max_new_tokens": 448,
#"num_beams": 1,
# "condition_on_prev_tokens": False,
#  "compression_ratio_threshold": 1.35,  # zlib compression ratio threshold (in token space)
#   "temperature": (0.0, 0.2, 0.4, 0.6, 0.8, 1.0),
#    "logprob_threshold": -1.0,
#   "no_speech_threshold": 0.6,
#    "return_timestamps": True,
#}

#result = pipe(sample, generate_kwargs=generate_kwargs)