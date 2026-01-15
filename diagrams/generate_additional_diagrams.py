#!/usr/bin/env python3
"""
生成更多流程图
"""

def generate_link_tracking_flow(lang='en'):
    """生成链接追踪流程图"""
    
    if lang == 'en':
        title = "Link IP Tracking Process"
        steps = [
            ("Create Tracking Link", "Generate unique tracking URL"),
            ("Share Link", "Send via message, email, or social media"),
            ("User Clicks Link", "Target clicks on tracking link"),
            ("Redirect & Capture", "Redirect to destination, log IP"),
            ("Store Data", "Save: IP, timestamp, location, device"),
            ("View Analytics", "Access tracking dashboard")
        ]
    else:
        title = "链接IP追踪流程"
        steps = [
            ("创建追踪链接", "生成唯一的追踪URL"),
            ("分享链接", "通过消息、邮件或社交媒体发送"),
            ("用户点击链接", "目标点击追踪链接"),
            ("重定向并捕获", "重定向到目标，记录IP"),
            ("存储数据", "保存：IP、时间戳、位置、设备"),
            ("查看分析", "访问追踪仪表板")
        ]
    
    svg = f'''<svg viewBox="0 0 900 700" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#f8f9fa;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#e9ecef;stop-opacity:1" />
    </linearGradient>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#667eea"/>
    </marker>
    <filter id="shadow">
      <feGaussianBlur in="SourceAlpha" stdDeviation="3"/>
      <feOffset dx="2" dy="2" result="offsetblur"/>
      <feComponentTransfer><feFuncA type="linear" slope="0.3"/></feComponentTransfer>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  
  <rect width="900" height="700" fill="url(#bgGrad)"/>
  <text x="450" y="35" font-family="Inter, sans-serif" font-size="26" font-weight="700" text-anchor="middle" fill="#2d3748">{title}</text>
  
  <ellipse cx="450" cy="90" rx="100" ry="45" fill="#667eea" stroke="#764ba2" stroke-width="2" opacity="0.9"/>
  <text x="450" y="100" font-family="Inter, sans-serif" font-size="16" text-anchor="middle" fill="white" font-weight="600">{'Start' if lang == 'en' else '开始'}</text>
  
'''
    
    y_positions = [180, 250, 320, 390, 460, 530]
    colors = ["#667eea", "#764ba2", "#f093fb", "#f5576c", "#4facfe", "#48bb78"]
    
    for i, (step_title, step_desc) in enumerate(steps):
        y = y_positions[i]
        color = colors[i]
        
        if i > 0:
            prev_y = y_positions[i-1]
            svg += f'  <path d="M 450 {prev_y + 50} L 450 {y - 25}" stroke="#667eea" stroke-width="3" fill="none" marker-end="url(#arrow)"/>\n'
        
        svg += f'''  <g>
    <rect x="300" y="{y-25}" width="300" height="70" rx="12" fill="white" stroke="{color}" stroke-width="3" opacity="0.95" filter="url(#shadow)"/>
    <text x="450" y="{y}" font-family="Inter, sans-serif" font-size="15" text-anchor="middle" fill="#2d3748" font-weight="700">{step_title}</text>
    <text x="450" y="{y+20}" font-family="Inter, sans-serif" font-size="12" text-anchor="middle" fill="#4a5568">{step_desc}</text>
  </g>
  
'''
    
    svg += f'''  <path d="M 450 580 L 450 620" stroke="#667eea" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
  <ellipse cx="450" cy="650" rx="100" ry="45" fill="#48bb78" stroke="#38a169" stroke-width="2" opacity="0.9"/>
  <text x="450" y="660" font-family="Inter, sans-serif" font-size="16" text-anchor="middle" fill="white" font-weight="600">{'Complete' if lang == 'en' else '完成'}</text>
</svg>'''
    
    return svg

def generate_gdpr_compliance_checklist(lang='en'):
    """生成GDPR合规检查清单图"""
    
    if lang == 'en':
        title = "GDPR Compliance Checklist for IP Tracking"
        items = [
            ("Legal Basis", "Obtain consent or legitimate interest"),
            ("Privacy Policy", "Clear disclosure of data collection"),
            ("Data Minimization", "Collect only necessary data"),
            ("User Rights", "Right to access, delete, port data"),
            ("Security Measures", "Encrypt and protect data"),
            ("Data Retention", "Define retention periods"),
            ("Breach Notification", "Report within 72 hours")
        ]
    else:
        title = "IP追踪GDPR合规检查清单"
        items = [
            ("法律依据", "获得同意或合法利益"),
            ("隐私政策", "明确披露数据收集"),
            ("数据最小化", "仅收集必要数据"),
            ("用户权利", "访问、删除、导出数据权"),
            ("安全措施", "加密和保护数据"),
            ("数据保留", "定义保留期限"),
            ("违规通知", "72小时内报告")
        ]
    
    svg = f'''<svg viewBox="0 0 800 700" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#f8f9fa;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#e9ecef;stop-opacity:1" />
    </linearGradient>
    <filter id="shadow">
      <feGaussianBlur in="SourceAlpha" stdDeviation="3"/>
      <feOffset dx="2" dy="2" result="offsetblur"/>
      <feComponentTransfer><feFuncA type="linear" slope="0.3"/></feComponentTransfer>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  
  <rect width="800" height="700" fill="url(#bgGrad)"/>
  <text x="400" y="40" font-family="Inter, sans-serif" font-size="24" font-weight="700" text-anchor="middle" fill="#2d3748">{title}</text>
  
  <rect x="50" y="80" width="700" height="580" rx="20" fill="white" stroke="#4A90E2" stroke-width="3" filter="url(#shadow)"/>
  
'''
    
    y_start = 130
    for i, (item_title, item_desc) in enumerate(items):
        y = y_start + i * 75
        svg += f'''  <g>
    <rect x="80" y="{y-20}" width="640" height="60" rx="10" fill="#f8f9fa" stroke="#4A90E2" stroke-width="2"/>
    <circle cx="110" cy="{y+10}" r="12" fill="#4A90E2"/>
    <text x="110" y="{y+15}" font-family="Inter, sans-serif" font-size="14" text-anchor="middle" fill="white" font-weight="700">{i+1}</text>
    <text x="140" y="{y}" font-family="Inter, sans-serif" font-size="16" fill="#2d3748" font-weight="700">{item_title}</text>
    <text x="140" y="{y+20}" font-family="Inter, sans-serif" font-size="13" fill="#4a5568">{item_desc}</text>
  </g>
  
'''
    
    svg += '</svg>'
    return svg

def generate_find_ip_methods(lang='en'):
    """生成查找IP地址方法对比图"""
    
    if lang == 'en':
        title = "Methods to Find Someone's IP Address"
        methods = [
            ("URL Tracking", "Create tracking link", "#667eea"),
            ("Email Tracking", "Embed tracking pixel", "#764ba2"),
            ("Social Media", "Share tracking link", "#f093fb"),
            ("Gaming Platforms", "Use game server logs", "#f5576c"),
            ("Chat Apps", "Send tracking link", "#4facfe")
        ]
    else:
        title = "查找他人IP地址的方法"
        methods = [
            ("URL追踪", "创建追踪链接", "#667eea"),
            ("邮件追踪", "嵌入追踪像素", "#764ba2"),
            ("社交媒体", "分享追踪链接", "#f093fb"),
            ("游戏平台", "使用游戏服务器日志", "#f5576c"),
            ("聊天应用", "发送追踪链接", "#4facfe")
        ]
    
    svg = f'''<svg viewBox="0 0 1000 600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#f8f9fa;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#e9ecef;stop-opacity:1" />
    </linearGradient>
    <filter id="shadow">
      <feGaussianBlur in="SourceAlpha" stdDeviation="4"/>
      <feOffset dx="3" dy="3" result="offsetblur"/>
      <feComponentTransfer><feFuncA type="linear" slope="0.3"/></feComponentTransfer>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  
  <rect width="1000" height="600" fill="url(#bgGrad)"/>
  <text x="500" y="40" font-family="Inter, sans-serif" font-size="26" font-weight="700" text-anchor="middle" fill="#2d3748">{title}</text>
  
'''
    
    x_positions = [100, 300, 500, 700, 900]
    for i, (method_title, method_desc, color) in enumerate(methods):
        x = x_positions[i]
        svg += f'''  <g>
    <rect x="{x-80}" y="100" width="160" height="450" rx="15" fill="white" stroke="{color}" stroke-width="3" filter="url(#shadow)"/>
    <text x="{x}" y="150" font-family="Inter, sans-serif" font-size="16" text-anchor="middle" fill="{color}" font-weight="700">{method_title}</text>
    <text x="{x}" y="180" font-family="Inter, sans-serif" font-size="12" text-anchor="middle" fill="#4a5568">{method_desc}</text>
    
    <!-- Icon placeholder -->
    <circle cx="{x}" cy="250" r="40" fill="{color}" opacity="0.2"/>
    <text x="{x}" y="260" font-family="Inter, sans-serif" font-size="24" text-anchor="middle" fill="{color}">{i+1}</text>
    
    <!-- Features -->
    <text x="{x}" y="320" font-family="Inter, sans-serif" font-size="11" text-anchor="middle" fill="#2d3748">• Easy setup</text>
    <text x="{x}" y="345" font-family="Inter, sans-serif" font-size="11" text-anchor="middle" fill="#2d3748">• Real-time data</text>
    <text x="{x}" y="370" font-family="Inter, sans-serif" font-size="11" text-anchor="middle" fill="#2d3748">• Accurate results</text>
  </g>
  
'''
    
    svg += '</svg>'
    return svg

def save_diagram(content, filename, lang='en'):
    """保存SVG文件"""
    from pathlib import Path
    output_dir = Path(__file__).parent / lang
    output_dir.mkdir(exist_ok=True)
    
    output_path = output_dir / filename
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✓ 已生成: {output_path}')

if __name__ == '__main__':
    print('开始生成更多流程图...\n')
    
    # 1. 链接追踪流程
    en1 = generate_link_tracking_flow('en')
    save_diagram(en1, 'link-tracking-process-flow.svg', 'en')
    zh1 = generate_link_tracking_flow('zh')
    save_diagram(zh1, 'link-tracking-process-flow.svg', 'zh')
    
    # 2. GDPR合规检查清单
    en2 = generate_gdpr_compliance_checklist('en')
    save_diagram(en2, 'gdpr-compliance-checklist.svg', 'en')
    zh2 = generate_gdpr_compliance_checklist('zh')
    save_diagram(zh2, 'gdpr-compliance-checklist.svg', 'zh')
    
    # 3. 查找IP方法
    en3 = generate_find_ip_methods('en')
    save_diagram(en3, 'find-ip-methods.svg', 'en')
    zh3 = generate_find_ip_methods('zh')
    save_diagram(zh3, 'find-ip-methods.svg', 'zh')
    
    print('\n完成! 已生成6个新流程图（中英文各3个）')
