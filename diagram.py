import os
import platform
from graphviz import Digraph
from plantuml import PlantUML
from diagrams import Diagram, Cluster
from diagrams.programming.framework import Vue, Flask
from diagrams.onprem.database import Postgresql
from diagrams.onprem.inmemory import Redis
from diagrams.saas.ai import Openai
from diagrams.generic.device import Mobile
from diagrams.custom import Custom

# --- 1. 核心配置：自动选择中文字体 ---
def get_chinese_font():
    """根据操作系统自动选择一个可用的中文字体"""
    system = platform.system()
    if system == "Windows":
        return 'SimHei'
    elif system == "Darwin": # macOS
        return 'PingFang SC'
    elif system == "Linux":
        return 'WenQuanYi Zen Hei'
    else:
        print("警告：无法识别操作系统，将使用默认字体 'SimHei'，可能需要手动修改。")
        return 'SimHei'

CHINESE_FONT = get_chinese_font()
print(f"检测到操作系统: {platform.system()}, 将使用字体: {CHINESE_FONT}")


# --- 2. 函数：生成用户核心学习闭环流程图 ---
def create_flowchart(font_name):
    """使用 Graphviz 生成流程图"""
    print("--- 正在生成用户核心学习闭环流程图... ---")
    dot = Digraph(comment='AI Study Assistant - Core Loop')
    dot.attr(rankdir='TB', splines='ortho', nodesep='0.8', ranksep='1.2')
    
    dot.attr('node', fontname=font_name)
    dot.attr('edge', fontname=font_name)
    
    dot.attr('node', shape='box', style='rounded,filled', fontsize='12')
    user_action_color = '#E3F2FD'
    ai_process_color = '#E8F5E9'
    output_color = '#FFF3E0'
    feedback_color = '#F3E5F5'

    dot.node('A', '课堂学习', style='rounded,filled', fillcolor=user_action_color, shape='ellipse')
    dot.node('B', '输入\n课堂录音 & 错题', style='rounded,filled', fillcolor=user_action_color, shape='parallelogram')
    with dot.subgraph(name='cluster_ai') as c:
        c.attr(rank='same', style='invis')
        c.node('C1', '笔记助手\n(语音转写、知识点总结)', fillcolor=ai_process_color)
        c.node('C2', '错题本\n(OCR识别、智能诊断)', fillcolor=ai_process_color)
    dot.node('D', '个性化学习材料\n(心智图、错题解析、举一反三)', fillcolor=output_color, shape='Mdiamond')
    dot.node('E1', '学习仪表盘\n(对学生：可视化激励)', fillcolor=feedback_color)
    dot.node('E2', '学习周报\n(对家长/教师：数据洞察)', fillcolor=feedback_color)

    dot.edge('A', 'B', label='产生')
    dot.edge('B', 'C1', label='处理录音')
    dot.edge('B', 'C2', label='处理错题')
    dot.edge('C1', 'D')
    dot.edge('C2', 'D')
    dot.edge('D', 'E1', label='数据反馈')
    dot.edge('D', 'E2', label='数据反馈')
    dot.edge('E1', 'A', style='dashed', label='驱动新一轮学习')

    output_filename = '1_user_core_loop_flowchart'
    dot.render(output_filename, format='png', view=False, cleanup=True)
    print(f"流程图已生成: {output_filename}.png")


# --- 3. 函数：生成 UML 用例图 (已修正) ---
def create_uml_diagram(font_name):
    """使用 PlantUML 生成 UML 用例图"""
    print("--- 正在生成 UML 用例图... ---")
    # 【修正】: 将 PlantUML 语法中所有的 { 和 } 分别替换为 {{ 和 }}
    plantuml_code = f"""
    @startuml
    ' 设置皮肤参数以获得更好看的外观
    skinparam actorStyle awesome
    skinparam usecase {{
        borderColor #2C3E50
        backgroundColor #BDC3C7
        arrowColor #2C3E50
    }}
    skinparam rectangle {{
        borderColor #2C3E50
        backgroundColor #ECF0F1
    }}
    ' 核心：设置默认字体为支持中文的字体
    skinparam defaultFontName "{font_name}"

    left to right direction

    actor "学生" as student
    actor "家长/教师" as guardian

    rectangle "AI 学习助手" {{
      usecase "管理课堂笔记" as UC1
      usecase "查看心智图" as UC2
      usecase "管理智能错题本" as UC3
      usecase "进行个性化练习" as UC4
      usecase "查看学习仪表盘" as UC5
      usecase "查看学生学习周报" as UC6
    }}

    student -- (UC1)
    student -- (UC2)
    student -- (UC3)
    student -- (UC4)
    student -- (UC5)

    guardian -- (UC6)
    @enduml
    """
    
    p = PlantUML(url="http://www.plantuml.com/plantuml")
    output_filename = '2_uml_use_case_diagram.png'
    try:
        with open(output_filename, 'wb') as f:
            f.write(p.processes(plantuml_code))
        print(f"UML用例图已生成: {output_filename}")
    except Exception as e:
        print(f"生成UML图失败，请检查网络连接或Java环境: {e}")


# --- 4. 函数：生成系统架构图 ---
def create_architecture_diagram(font_name):
    """使用 Diagrams 生成系统架构图"""
    print("--- 正在生成系统架构图... ---")
    
    graph_attr = {"fontname": font_name, "fontsize": "14", "bgcolor": "transparent"}
    node_attr = {"fontname": font_name, "fontsize": "12"}
    edge_attr = {"fontname": font_name, "fontsize": "10"}

    icon_path = "./icons"
    os.makedirs(icon_path, exist_ok=True)
    
    whisper_icon = os.path.join(icon_path, "whisper.png") if os.path.exists(os.path.join(icon_path, "whisper.png")) else None
    ocr_icon = os.path.join(icon_path, "paddleocr.png") if os.path.exists(os.path.join(icon_path, "paddleocr.png")) else None
    vector_icon = os.path.join(icon_path, "vector.png") if os.path.exists(os.path.join(icon_path, "vector.png")) else None

    with Diagram(
        "AI 学习助手 - 系统架构", 
        show=False, 
        filename="3_system_architecture_diagram",
        graph_attr=graph_attr,
        node_attr=node_attr,
        edge_attr=edge_attr
    ):
        user = Mobile("用户设备\n(Web 浏览器)")

        with Cluster("用户端 (Vue 3)"):
            frontend = Vue("Web 应用")

        with Cluster("后端应用服务 (Flask)"):
            backend = Flask("API 服务")
            redis = Redis("异步任务队列\n(Redis)")
            backend >> redis
            
        with Cluster("AI 能力层 (API)"):
            llm = Openai("大语言模型\n(GPT 系列)")
            speech_to_text = Custom("语音转写\n(Whisper)", whisper_icon) if whisper_icon else Openai("Whisper")
            ocr = Custom("图像识别\n(PaddleOCR)", ocr_icon) if ocr_icon else Openai("OCR")

        with Cluster("数据存储层 (Database)"):
            db_structured = Postgresql("结构化数据\n(PostgreSQL)")
            db_vector = Custom("向量数据库\n(pgvector)", vector_icon) if vector_icon else Postgresql("pgvector")
            db_structured - db_vector
        
        user >> frontend >> backend
        backend >> [speech_to_text, ocr, llm]
        backend >> db_structured
        backend >> db_vector

    print("系统架构图已生成: 3_system_architecture_diagram.png")


# --- 5. 主执行函数 ---
if __name__ == "__main__":
    create_flowchart(CHINESE_FONT)
    create_uml_diagram(CHINESE_FONT)
    create_architecture_diagram(CHINESE_FONT)
    
    print("\n所有图表生成完毕！")