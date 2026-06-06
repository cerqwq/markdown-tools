# 📝 Markdown Tools

AI Markdown工具集，支持Markdown生成、转换、分析。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📝 从大纲生成Markdown
- 🔄 Markdown转HTML
- 📋 目录生成
- 📊 文档结构分析
- ⚡ Markdown优化
- 📊 变更日志生成
- 🏷️ 徽章生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from markdown_tools import create_tools

tools = create_tools()

# 从大纲生成
md = tools.generate_from_outline("# 项目\n## 介绍\n## 安装")

# 转HTML
html = tools.convert_to_html(md)

# 生成目录
toc = tools.generate_toc(md)

# 分析结构
analysis = tools.analyze_structure(md)

# 优化
optimized = tools.optimize_markdown(md)

# 生成徽章
badges = tools.generate_badges({"tech": ["Python"], "license": "MIT"})
```

## 📁 项目结构

```
markdown-tools/
├── tools.py       # Markdown工具核心
└── README.md
```

## 📄 许可证

MIT License
