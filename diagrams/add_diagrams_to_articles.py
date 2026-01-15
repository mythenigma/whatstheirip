#!/usr/bin/env python3
"""
批量在blog文章中添加流程图（SVG + Mermaid）
"""

import re
from pathlib import Path

blog_dir = Path(__file__).parent.parent / 'blog'

# 文章和对应的流程图映射
diagram_mapping = {
    'how-ip-tracking-works.html': {
        'diagram': 'how-ip-tracking-works.svg',
        'mermaid': '''flowchart TD
    A[User Visits Website] --> B[Browser Sends Request]
    B --> C[Server Receives Request]
    C --> D[Server Logs IP Address]
    D --> E[IP Geolocation Lookup]
    E --> F[Data Collection]
    F --> G[Analytics Processing]
    G --> H[Results Display]
    
    style A fill:#667eea,stroke:#764ba2,stroke-width:2px,color:#fff
    style H fill:#48bb78,stroke:#38a169,stroke-width:2px,color:#fff''',
        'position': 'how-tracking-works',
        'title': 'IP Tracking Process Flow'
    },
    'ip-tracker-vs-ip-grabber-guide.html': {
        'diagram': 'ip-tracker-vs-ip-grabber.svg',
        'mermaid': '''graph LR
    A[IP Tracker] --> A1[Real-time monitoring]
    A --> A2[Analytics dashboard]
    A --> A3[Geolocation data]
    A --> A4[Multiple tracking methods]
    A --> A5[Legal compliance]
    
    B[IP Grabber] --> B1[One-time capture]
    B --> B2[Simple link sharing]
    B --> B3[Basic IP logging]
    B --> B4[Quick setup]
    B --> B5[Lightweight tool]
    
    style A fill:#667eea,stroke:#764ba2,stroke-width:3px,color:#fff
    style B fill:#f5576c,stroke:#d32f2f,stroke-width:3px,color:#fff''',
        'position': 'comparison',
        'title': 'IP Tracker vs IP Grabber Comparison'
    },
    'email-tracking-best-practices.html': {
        'diagram': 'email-tracking-process-flow.svg',
        'mermaid': '''flowchart TD
    A[Send Email] --> B[Email Opened]
    B --> C[Pixel Loaded]
    C --> D[IP Captured]
    D --> E[Data Recorded]
    E --> F[Analytics Updated]
    
    style A fill:#4A90E2,stroke:#357ABD,stroke-width:2px,color:#fff
    style F fill:#48bb78,stroke:#38a169,stroke-width:2px,color:#fff''',
        'position': 'introduction',
        'title': 'Email Tracking Process Flow'
    },
    'ip-address-basics.html': {
        'diagram': 'ip-address-structure.svg',
        'mermaid': '''graph TB
    A[IP Address] --> B[IPv4]
    A --> C[IPv6]
    B --> B1[32-bit address]
    B --> B2[4 octets]
    B --> B3[Dotted decimal]
    C --> C1[128-bit address]
    C --> C2[8 groups]
    C --> C3[Hexadecimal]
    
    style B fill:#667eea,stroke:#764ba2,stroke-width:2px,color:#fff
    style C fill:#f5576c,stroke:#d32f2f,stroke-width:2px,color:#fff''',
        'position': 'ipv4-vs-ipv6',
        'title': 'IP Address Structure'
    },
    'track-ip-from-a-link.html': {
        'diagram': 'link-tracking-process-flow.svg',
        'mermaid': '''flowchart TD
    A[Create Tracking Link] --> B[Share Link]
    B --> C[User Clicks Link]
    C --> D[Redirect & Capture]
    D --> E[Store Data]
    E --> F[View Analytics]
    
    style A fill:#667eea,stroke:#764ba2,stroke-width:2px,color:#fff
    style F fill:#48bb78,stroke:#38a169,stroke-width:2px,color:#fff''',
        'position': 'introduction',
        'title': 'Link IP Tracking Process'
    },
    'ip-tracking-gdpr-compliance.html': {
        'diagram': 'gdpr-compliance-checklist.svg',
        'mermaid': '''flowchart TD
    A[GDPR Compliance] --> B[Legal Basis]
    A --> C[Privacy Policy]
    A --> D[Data Minimization]
    A --> E[User Rights]
    A --> F[Security Measures]
    A --> G[Data Retention]
    A --> H[Breach Notification]
    
    style A fill:#4A90E2,stroke:#357ABD,stroke-width:3px,color:#fff''',
        'position': 'checklist',
        'title': 'GDPR Compliance Checklist'
    },
    'how-to-find-someones-ip-address.html': {
        'diagram': 'find-ip-methods.svg',
        'mermaid': '''graph LR
    A[Find IP Methods] --> B[URL Tracking]
    A --> C[Email Tracking]
    A --> D[Social Media]
    A --> E[Gaming Platforms]
    A --> F[Chat Apps]
    
    style A fill:#667eea,stroke:#764ba2,stroke-width:3px,color:#fff''',
        'position': 'introduction',
        'title': 'Methods to Find IP Address'
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
        
        # 在</head>之前插入
        if '</head>' in content:
            content = content.replace('</head>', mermaid_script + '\n  </head>')
    
    return content

def add_diagram_to_article(filepath, config, lang='en'):
    """在文章中添加流程图"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 添加Mermaid脚本
    content = add_mermaid_script(content)
    
    # 构建流程图HTML
    diagram_path = f'../diagrams/{lang}/{config["diagram"]}'
    diagram_html = f'''
            <!-- {config["title"]} Diagram -->
            <div class="diagram-container" style="margin: 3rem 0; text-align: center;">
              <h4 style="margin-bottom: 1.5rem; color: #2d3748;">{config["title"]}</h4>
              
              <!-- SVG Diagram -->
              <figure style="margin-bottom: 2rem;">
                <img src="{diagram_path}" 
                     alt="{config["title"]} Diagram"
                     loading="lazy"
                     style="max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                <figcaption style="margin-top: 1rem; color: #4a5568; font-size: 0.9rem;">Visual representation of {config["title"].lower()}</figcaption>
              </figure>
              
              <!-- Mermaid Diagram -->
              <div class="mermaid-diagram" style="background: #f8f9fa; padding: 2rem; border-radius: 10px; margin-top: 2rem;">
                <h5 style="margin-bottom: 1rem; color: #2d3748;">Interactive Flow Diagram</h5>
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
        f'#{position}'
    ]
    
    inserted = False
    for pattern in patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            # 在匹配位置之后插入
            insert_pos = match.end()
            # 找到下一个段落或标题
            next_p = content.find('<p>', insert_pos)
            next_h = content.find('<h', insert_pos)
            next_pos = min([p for p in [next_p, next_h] if p > 0] or [len(content)])
            
            # 在段落之前插入
            if next_p > 0 and next_p < next_pos:
                content = content[:next_p] + diagram_html + '\n          ' + content[next_p:]
                inserted = True
                break
    
    # 如果没找到，尝试在第一个h2之后插入
    if not inserted:
        first_h2 = re.search(r'<h2[^>]*>', content)
        if first_h2:
            insert_pos = content.find('</h2>', first_h2.end())
            if insert_pos > 0:
                # 找到下一个段落
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
    print('开始为文章添加流程图...\n')
    
    for filename, config in diagram_mapping.items():
        filepath = blog_dir / filename
        if filepath.exists():
            if add_diagram_to_article(filepath, config, 'en'):
                print(f'✓ 已添加流程图到: {filename}')
            else:
                print(f'✗ 无法添加流程图到: {filename} (未找到插入位置)')
        else:
            print(f'✗ 文件不存在: {filename}')
    
    print('\n完成!')
