<div align="center">

# AI Study Assistant

智能学习与个性化辅导平台 · Project 1

</div>

## 🎯 项目主题

- **目标用户**：初高中学生以及家长/教师支持群体。
- **核心痛点**：课堂难理解、课后难复盘、自律性不足。
- **解决方案**：提供“课中记录 + 课后复习 + 激励反馈”一体化 AI 学习伴侣。

## 🧩 模块概览

| 模块 | 说明 | AI/技术栈 |
| --- | --- | --- |
| Note Assistant | 课堂录音上传、自动转写 + 结构化关键点总结 | Whisper/Faster-Whisper · GPT 综述 |
| Mind Map View | 将知识点层级转为交互式心智图，辅助回顾 | Mermaid.js / MindElixir.js |
| Error Book Manager | 拍照/上传错题 → OCR 识别 → 分类解析与举一反三练习 | PaddleOCR / 云 OCR · LLM 题目分析 |
| Learning Dashboard | 展示学习时长、掌握度、复习进度与提醒 | Chart.js / ECharts · 日志聚合 |
| Parent View | 面向家长的学习周报、弱项提示与鼓励文案 | GPT 风格摘要 |

## 🏗️ 技术框架

- **前端**：Vue 3 + Vite + Pinia + Vue Router，配合 `base.css`/`main.css` 自定义柔和配色与玻璃拟态风格。
- **后端**：Flask (Blueprints) + Flask-CORS，后续可扩展 Celery+Redis 运行异步 AI 任务。
- **AI 能力**：语音转写 (Whisper/Deepgram)、OCR (PaddleOCR/百度 OCR)、LLM 总结/问答 (OpenAI、通义、百川等)。
- **数据存储**：PostgreSQL/MySQL 保存结构化数据，错题与讲义可结合 pgvector/Milvus 建相似度检索。

```
computer software/
├─ README.md                 # 项目说明（本文件）
├─ ai-assistant-backend/     # Flask API (语音转写/错题管理等)
└─ ai-assistant-frontend/    # Vue 3 Web App (学生、家长视图)
```

## 🚀 快速开始

```powershell
# 启动后端
cd "ai-assistant-backend"
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python app.py

# 启动前端
cd "ai-assistant-frontend"
npm install
npm run dev
```

> 默认后端监听 `http://localhost:3000`，前端 Vite Dev Server 运行在 `5173` 端口。根据需要在 `.env` 中配置 API 地址与 AI Key。

## 🌐 本地查看网页 & 测试结果

1. **确保服务已启动**：后端 `python app.py`（或 `flask run`）保持运行，前端目录执行 `npm run dev -- --host 0.0.0.0 --port 5173 --strictPort`。
2. **打开浏览器**：访问 `http://localhost:5173`，即可实时查看首页（Hero/模块目录/学习旅程）。修改 `src/` 下文件会自动热更新，方便调试当前“测试结果”。
3. **查看构建产出**：若需验证发布前效果，可以运行：

```powershell
cd "ai-assistant-frontend"
npm run build
npm run preview -- --host 0.0.0.0 --port 4173 --strictPort
```

随后访问 `http://localhost:4173`，即可体验与线上一致的静态构建版本。按 `Ctrl + C` 可退出对应服务。

## ☁️ 同步到 GitHub

1. **初始化或检查 Git 仓库**：在项目根目录（`computer software/`）运行 `git status`，确认 `.gitignore` 已过滤 `.venv/`、`node_modules/`、`dist/` 等文件。若尚未初始化，可执行 `git init`。
2. **配置提交信息**（首次使用 Git 可设置用户名/邮箱）：

```powershell
git config user.name "Your Name"
git config user.email "you@example.com"
```

3. **查看变更并提交**：

```powershell
git status
git add .
git commit -m "feat: initial AI study assistant"
```

4. **绑定远端仓库**：

```powershell
git remote add origin https://github.com/<your-account>/<repo-name>.git
git branch -M main
```

如已绑定，可用 `git remote -v` 查看。

5. **推送到 GitHub**：

```powershell
git push -u origin main
```

后续只需重复 “修改 → `git add` → `git commit -m "..."` → `git push`” 流程即可同步更新。需要换电脑或拉取团队修改时，在根目录执行 `git pull origin main`。

## 📅 迭代路线

1. **MVP**：完成 Note Assistant（音频上传→转写→摘要），Dashboard 显示基础统计。
2. **错题管理**：OCR + LLM 解析、错题分类与推送相似练习题。
3. **心智图 & 家长视图**：可视化知识树、周报生成以及激励机制（学习打卡、复习提醒）。
4. **多模态增强**：引入多模态 LLM、语音对话辅导、PWA/移动端适配。

## 🤝 贡献与后续

- 建议为前后端分别添加单元测试/端到端测试（Vitest、Pytest）。
> **提示**：完成一次安装后，今后每次重新打开终端只需 `cd "ai-assistant-backend"` 并执行 `venv\Scripts\activate` 进入虚拟环境，再运行 `python app.py` 或其他脚本。使用 `deactivate` 可退出虚拟环境。
- 可通过 Docker Compose 编排 Flask + Redis + 数据库 + 前端 Nginx 容器。
- 欢迎继续完善 API 文档、设计稿、数据标注流程或接入学校管理系统。

> 有任何想法/问题，直接在 README 中记录或开启 issue，方便团队协作。
