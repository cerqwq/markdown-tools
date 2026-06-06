"""
Markdown Tools - AI Markdown工具集
支持Markdown生成、转换、分析
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class MarkdownTools:
    """
    AI Markdown工具集
    支持：生成、转换、分析、优化
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_from_outline(self, outline: str, style: str = "professional") -> str:
        """从大纲生成Markdown"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请根据以下大纲生成完整的Markdown文档：

大纲：
{outline}

风格：{style}

要求：
1. 结构清晰
2. 内容充实
3. 使用Markdown格式"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def convert_to_html(self, markdown: str) -> str:
        """转换为HTML"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请将以下Markdown转换为HTML：

{markdown}

只返回HTML代码："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_toc(self, markdown: str) -> str:
        """生成目录"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为以下Markdown生成目录：

{markdown}

只返回目录的Markdown代码："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def analyze_structure(self, markdown: str) -> Dict:
        """分析文档结构"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请分析以下Markdown文档的结构：

{markdown}

请返回JSON格式：
{{
    "title": "标题",
    "headings": [{{"level": 1, "text": "标题"}}],
    "word_count": 字数,
    "sections": 数量,
    "has_code": true/false,
    "has_tables": true/false,
    "has_images": true/false,
    "suggestions": ["建议1", "建议2"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}

    def optimize_markdown(self, markdown: str) -> str:
        """优化Markdown"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请优化以下Markdown文档：

{markdown}

要求：
1. 改善结构
2. 增强可读性
3. 修正格式问题
4. 保持内容完整"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_changelog(self, changes: List[Dict]) -> str:
        """生成变更日志"""
        if not self.client:
            return "LLM客户端未配置"

        changes_text = json.dumps(changes, ensure_ascii=False, indent=2)

        prompt = f"""请根据以下变更生成CHANGELOG.md：

{changes_text}

使用Keep a Changelog格式："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_badges(self, project_info: Dict) -> str:
        """生成徽章"""
        badges = []
        if "python" in str(project_info.get("tech", [])).lower():
            badges.append("![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)")
        if "license" in project_info:
            badges.append(f"![License](https://img.shields.io/badge/License-{project_info['license']}-yellow)")
        return "\n".join(badges)


def create_tools(**kwargs) -> MarkdownTools:
    """创建Markdown工具"""
    return MarkdownTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("Markdown Tools")
    print()

    # 测试
    outline = """
    # 项目名称
    ## 简介
    ## 特性
    ## 安装
    ## 使用
    ## 贡献
    ## 许可证
    """

    result = tools.generate_from_outline(outline, "professional")
    print(result[:300] + "...")
