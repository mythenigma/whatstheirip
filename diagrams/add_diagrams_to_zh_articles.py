#!/usr/bin/env python3
"""
为中文blog文章添加流程图（SVG + Mermaid）
"""

import re
from pathlib import Path

blog_dir = Path(__file__).parent.parent / 'blog' / 'zh'

# 中文文章和对应的流程图映射
zh_diagram_mapping = {
    'how-to-find-someones-ip-address-social-media.html': {
        'diagram': 'find-ip-methods.svg',
        'mermaid': '''graph LR
    A[查找IP方法] --> B[URL追踪]
    A --> C[邮件追踪]
    A --> D[社交媒体]
    A --> E[游戏平台]
    A --> F[聊天应用]
    
    style A fill:#667eea,stroke:#764ba2,stroke-width:3px,color:#fff''',
        'position': 'introduction',
        'title': '查找IP地址的方法'
    }
}

def add_mermaid_script(content):
    """添加Mermaid.js脚本（如果还没有）"""
    if 'mermaid.esm.min.mjs' not in content:
        mermaid_script = '''
  <!-- Mermaid.js for diagrams -->
  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize({ startOnLoad: true, theme: 'default' });
  </script>'''
        
        if '</head>' in content:
            content = content.replace('</head>', mermaid_script + '\n  </head>')
    
    return content

def add_diagram_to_article(filepath, config, lang='zh'):
    """在文章中添加流程图"""
    if not filepath.exists():
        return False
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 添加Mermaid脚本
    content = add_mermaid_script(content)
    
    # 构建流程图HTML
    diagram_path = f'../../diagrams/{lang}/{config["diagram"]}'
    diagram_html = f'''
            <!-- {config["title"]} 流程图 -->
            <div class="diagram-container" style="margin: 3rem 0; text-align: center;">
              <h4 style="margin-bottom: 1.5rem; color: #2d3748;">{config["title"]}</h4>
              
              <!-- SVG流程图 -->
              <figure style="margin-bottom: 2rem;">
                <img src="{diagram_path}" 
                     alt="{config["title"]} 流程图"
                     loading="lazy"
                     style="max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                <figcaption style="margin-top: 1rem; color: #4a5568; font-size: 0.9rem;">{config["title"]}可视化图表</figcaption>
              </figure>
              
              <!-- Mermaid交互式流程图 -->
              <div class="mermaid-diagram" style="background: #f8f9fa; padding: 2rem; border-radius: 10px; margin-top: 2rem;">
                <h5 style="margin-bottom: 1rem; color: #2d3748;">交互式流程图</h5>
                <div class="mermaid">
{config["mermaid"]}
                </div>
              </div>
            </div>
'''
    
    # 查找插入位置
    position = config['position']
    
    # 尝试多种匹配模式
    patterns = [
        f'<h2[^>]*id="{position}"[^>]*>',
        f'<h2[^>]*>{position}',
        f'id="{position}"',
        f'#{position}',
        f'<h2[^>]*>.*介绍',
        f'<h2[^>]*>.*引言'
    ]
    
    inserted = False
    for pattern in patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            insert_pos = match.end()
            next_p = content.find('<p>', insert_pos)
            next_h = content.find('<h', insert_pos)
            next_pos = min([p for p in [next_p, next_h] if p > 0] or [len(content)])
            
            if next_p > 0 and next_p < next_pos:
                content = content[:next_p] + diagram_html + '\n          ' + content[next_p:]
                inserted = True
                break
    
    # 如果没找到，在第一个h2之后插入
    if not inserted:
        first_h2 = re.search(r'<h2[^>]*>', content)
        if first_h2:
            insert_pos = content.find('</h2>', first_h2.end())
            if insert_pos > 0:
                next_p = content.find('<p>', insert_pos)
                if next_p > 0:
                    content = content[:next_p] + diagram_html + '\n          ' + content[next_p:]
                    inserted = True
    
    if inserted:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

if __name__ == '__main__':
    print('开始为中文文章添加流程图...\n')
    
    for filename, config in zh_diagram_mapping.items():
        filepath = blog_dir / filename
        if add_diagram_to_article(filepath, config, 'zh'):
            print(f'✓ 已添加流程图到: {filename}')
        else:
            print(f'✗ 无法添加流程图到: {filename}')
    
    print('\n完成!')
