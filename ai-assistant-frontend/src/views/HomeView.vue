<script setup>
import { RouterLink } from 'vue-router'

const modules = [
  {
    name: '笔记助手',
    tag: '课堂笔记',
    icon: '🎧',
    description: '录音或上传音频，生成可编辑的转写文本；有文本后再一键 AI 总结要点与待办。',
    highlights: ['Whisper 语音转文字', '转写与总结解耦（先转写后总结）', '逐字稿可直接修改'],
    path: '/note-assistant'
  },
  {
    name: '思维导图',
    tag: '知识结构',
    icon: '🧠',
    description: '将层级化内容转化为可视化的知识结构视图，帮助梳理概念与关系。',
    highlights: ['可视化思维导图展示', '支持从学习内容生成结构', '与笔记/知识点串联'],
    path: '/mind-map'
  },
  {
    name: '错题本',
    tag: '错题管理',
    icon: '📚',
    description: '拍照或上传错题图片，自动 OCR 提取文字并进行题目分析，支持生成练习题。',
    highlights: ['OCR 提取题干（PaddleOCR）', 'LLM 题目分析与讲解', '自动生成练习题（quiz）'],
    path: '/error-book'
  },
  {
    name: '学习仪表盘',
    tag: '学习分析',
    icon: '📈',
    description: '汇总错题与学习数据，展示趋势与复习建议，辅助形成复盘闭环。',
    highlights: ['学习数据汇总', '按学科统计与趋势图', '复习建议与提醒'],
    path: '/dashboard'
  },
  {
    name: '家长视图',
    tag: '家长视角',
    icon: '👪',
    description: '面向家长的简洁视图：绑定学生账号后查看学习进度与提示。',
    highlights: ['家长绑定学生', '查看孩子列表与状态', '基于学习数据的可视化概览'],
    path: '/parent'
  }
]

const flowSteps = [
  {
    title: '01 · In-Class Capture',
    desc: '学生使用笔记助手录音或上传音频，停止后生成可编辑的转写文本。'
  },
  {
    title: '02 · After-Class Review',
    desc: '确认转写文本后，一键生成结构化总结与待办任务，辅助复盘。'
  },
  {
    title: '03 · Error-Driven Practice',
    desc: '题目拍照进错题本→ OCR/LLM 解析 → 推送举一反三练习。'
  },
  {
    title: '04 · Insights & Parent Report',
    desc: '仪表盘聚合学习数据，家长视图查看进度与建议。'
  }
]
</script>

<template>
  <section class="hero" id="hero">
    <p class="eyebrow">智能学习与个性化辅导</p>
    <h1>
      柔和而有力量的 <span>AI 学习伙伴</span>
    </h1>
    <p class="lead">
      面向初高中学生的个性化 AI 学习助手：覆盖课堂笔记、错题复盘、学习分析与家长视图，
      解决“难理解、难记忆、学习缺乏主动性”。
    </p>
    <div class="hero-actions">
      <a class="primary" href="#modules">查看功能目录</a>
      <a class="secondary" href="#flow">了解学习旅程</a>
    </div>
    <div class="hero-stats">
      <article>
        <p class="label">课堂笔记</p>
        <p class="value">笔记助手</p>
        <small>录音/上传 → 转写 → 总结</small>
      </article>
      <article>
        <p class="label">错题解析</p>
        <p class="value">错题本</p>
        <small>OCR + AI 分析 + 练习题</small>
      </article>
      <article>
        <p class="label">学习洞察</p>
        <p class="value">仪表盘</p>
        <small>趋势与复习建议</small>
      </article>
    </div>
  </section>

  <section class="modules" id="modules">
    <header>
      <p class="eyebrow">模块目录</p>
      <h2>学得更专注 · 记得更牢固 · 反馈更及时</h2>
      <p>覆盖课堂记录、知识结构、错题管理、数据洞察与家长沟通的全链路体验。</p>
    </header>
    <div class="module-grid">
      <article v-for="module in modules" :key="module.name">
        <div class="card-top">
          <span class="icon" aria-hidden="true">{{ module.icon }}</span>
          <span class="tag">{{ module.tag }}</span>
        </div>
        <h3>{{ module.name }}</h3>
        <p>{{ module.description }}</p>
        <ul>
          <li v-for="point in module.highlights" :key="point">{{ point }}</li>
        </ul>
        <RouterLink v-if="module.path" class="card-link" :to="module.path">
          前往 {{ module.name }}
        </RouterLink>
      </article>
    </div>
  </section>

  <section class="flow" id="flow">
    <header>
      <p class="eyebrow">学习旅程</p>
      <h2>从课堂触发到家长报告的闭环体验</h2>
      <p>每一步都有 AI 的辅助，也保留人性化的温度与鼓励。</p>
    </header>
    <div class="flow-grid">
      <article v-for="step in flowSteps" :key="step.title">
        <p class="step-title">{{ step.title }}</p>
        <p class="step-desc">{{ step.desc }}</p>
      </article>
    </div>
  </section>

  <section class="cta" id="cta">
    <div>
      <p class="eyebrow">Ready to Learn</p>
      <h2>让每一次课堂、每一道错题，都成为被看见的成长。</h2>
      <p>立即规划你的 AI Study Assistant，实现“Hard to understand → Easy to master”。</p>
    </div>
    <a href="mailto:hello@aistudyassistant.com" class="primary">预约演示</a>
  </section>
</template>

<style scoped>
:global(main) {
  display: contents;
}

.hero,
.modules,
.flow,
.cta {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 2rem;
  padding: clamp(1.8rem, 4vw, 3rem);
  margin-bottom: 2rem;
  box-shadow: 0 25px 60px rgba(21, 47, 89, 0.08);
  position: relative;
}

.hero {
  overflow: hidden;
}

.hero::after {
  content: '';
  position: absolute;
  right: 10%;
  top: 15%;
  width: 220px;
  height: 220px;
  background: radial-gradient(circle, rgba(111, 157, 236, 0.4), transparent 70%);
  filter: blur(6px);
  pointer-events: none;
}

.eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.2em;
  color: rgba(29, 60, 120, 0.7);
  font-size: 0.85rem;
  margin-bottom: 0.6rem;
}

h1 {
  font-size: clamp(2.1rem, 5vw, 3.5rem);
  color: #0f1d40;
  line-height: 1.2;
  margin-bottom: 1rem;
}

h1 span {
  background: linear-gradient(120deg, #6f9dec, #8bd4c8);
  -webkit-background-clip: text;
  color: transparent;
}

.lead {
  font-size: 1.1rem;
  color: rgba(16, 34, 68, 0.8);
  max-width: 640px;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin: 1.8rem 0 2.4rem;
}

.primary,
.secondary {
  border-radius: 999px;
  padding: 0.9rem 1.8rem;
  font-weight: 600;
  text-align: center;
}

.primary {
  background: linear-gradient(120deg, #6f9dec, #8bd4c8);
  color: #fff;
  box-shadow: 0 12px 30px rgba(85, 141, 214, 0.4);
}

.secondary {
  border: 1px solid rgba(17, 62, 125, 0.25);
  color: #0c2b53;
  background: rgba(255, 255, 255, 0.6);
}

.link-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.card-link {
  margin-top: auto;
  border-radius: 999px;
  padding: 0.6rem 1.2rem;
  border: 1px solid rgba(15, 39, 88, 0.2);
  background: rgba(255, 255, 255, 0.9);
  color: #0c2b53;
  font-weight: 600;
  text-align: center;
  transition: border 0.2s ease, box-shadow 0.2s ease;
}

.card-link:hover {
  border-color: rgba(111, 157, 236, 0.6);
  box-shadow: 0 8px 20px rgba(49, 90, 166, 0.15);
}

.hero-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1rem;
}

.hero-stats article {
  border-radius: 1.5rem;
  padding: 1.2rem;
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(111, 157, 236, 0.2);
}

.label {
  font-size: 0.85rem;
  color: rgba(20, 40, 70, 0.6);
}

.value {
  font-size: 1.6rem;
  font-weight: 700;
  color: #0f1d40;
}

.modules header,
.flow header,
.cta > div {
  margin-bottom: 1.5rem;
}

.modules h2,
.flow h2,
.cta h2 {
  color: #142048;
  margin-bottom: 0.4rem;
}

.module-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
  gap: 1.5rem;
}

.module-grid article {
  border-radius: 1.8rem;
  padding: 1.5rem;
  background: rgba(248, 251, 255, 0.9);
  border: 1px solid rgba(111, 157, 236, 0.16);
  min-height: 260px;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.card-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.icon {
  font-size: 1.8rem;
}

.tag {
  padding: 0.25rem 0.7rem;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.8);
  font-size: 0.8rem;
  color: #4a5c84;
}

.module-grid h3 {
  font-size: 1.2rem;
  color: #111b2e;
}

.module-grid p {
  flex: 1;
  color: rgba(16, 34, 68, 0.78);
}

.module-grid ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  font-size: 0.9rem;
  color: #1e2c50;
}

.module-grid li::before {
  content: '• ';
  color: #6f9dec;
}

.flow-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1rem;
}

.flow-grid article {
  border-radius: 1.5rem;
  padding: 1.4rem;
  border: 1px dashed rgba(15, 39, 88, 0.25);
  background: rgba(255, 255, 255, 0.9);
}

.step-title {
  font-weight: 600;
  color: #142048;
  margin-bottom: 0.6rem;
}

.step-desc {
  color: rgba(16, 34, 68, 0.7);
}

.cta {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 1.5rem;
}

.cta .primary {
  min-width: 180px;
  text-align: center;
}

@media (max-width: 640px) {
  .hero,
  .modules,
  .flow,
  .cta {
    border-radius: 1.5rem;
  }

  .hero-actions {
    flex-direction: column;
  }
}
</style>
