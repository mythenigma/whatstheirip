#!/usr/bin/env python3
"""
为多个blog文章生成流程图
"""

def generate_how_ip_tracking_works(lang='en'):
    """生成IP追踪工作原理流程图"""
    
    if lang == 'en':
        title = "How IP Tracking Works"
        steps = [
            ("User Visits Website", "User's browser sends request"),
            ("Server Receives Request", "Server logs IP address"),
            ("IP Geolocation Lookup", "Database matches IP to location"),
            ("Data Collection", "Collect: IP, location, time, device"),
            ("Analytics Processing", "Analyze and store data"),
            ("Results Display", "Show tracking results")
        ]
    else:
        title = "IP追踪工作原理"
        steps = [
            ("用户访问网站", "浏览器发送请求"),
            ("服务器接收请求", "服务器记录IP地址"),
            ("IP地理位置查询", "数据库匹配IP到位置"),
            ("数据收集", "收集：IP、位置、时间、设备"),
            ("数据分析处理", "分析和存储数据"),
            ("结果显示", "显示追踪结果")
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
  
  <!-- Start -->
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

def generate_ip_tracker_vs_grabber(lang='en'):
    """生成IP Tracker vs IP Grabber对比图"""
    
    if lang == 'en':
        title = "IP Tracker vs IP Grabber"
        tracker_title = "IP Tracker"
        grabber_title = "IP Grabber"
        tracker_features = [
            "Real-time monitoring",
            "Analytics dashboard",
            "Geolocation data",
            "Multiple tracking methods",
            "Legal compliance"
        ]
        grabber_features = [
            "One-time capture",
            "Simple link sharing",
            "Basic IP logging",
            "Quick setup",
            "Lightweight tool"
        ]
    else:
        title = "IP追踪器 vs IP抓取器"
        tracker_title = "IP追踪器"
        grabber_title = "IP抓取器"
        tracker_features = [
            "实时监控",
            "分析仪表板",
            "地理位置数据",
            "多种追踪方法",
            "法律合规"
        ]
        grabber_features = [
            "一次性捕获",
            "简单链接分享",
            "基本IP记录",
            "快速设置",
            "轻量级工具"
        ]
    
    svg = f'''<svg viewBox="0 0 1000 650" xmlns="http://www.w3.org/2000/svg">
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
  
  <rect width="1000" height="650" fill="url(#bgGrad)"/>
  <text x="500" y="40" font-family="Inter, sans-serif" font-size="28" font-weight="700" text-anchor="middle" fill="#2d3748">{title}</text>
  
  <!-- IP Tracker -->
  <g id="tracker">
    <rect x="50" y="100" width="400" height="500" rx="20" fill="white" stroke="#667eea" stroke-width="4" opacity="0.95" filter="url(#shadow)"/>
    <text x="250" y="145" font-family="Inter, sans-serif" font-size="24" text-anchor="middle" fill="#667eea" font-weight="700">{tracker_title}</text>
    
    <line x1="70" x2="430" y1="170" y2="170" stroke="#667eea" stroke-width="2"/>
'''
    
    y_start = 210
    for i, feature in enumerate(tracker_features):
        y = y_start + i * 50
        svg += f'''    <circle cx="80" cy="{y}" r="6" fill="#667eea"/>
    <text x="100" y="{y+5}" font-family="Inter, sans-serif" font-size="14" fill="#2d3748">{feature}</text>
'''
    
    svg += '''  </g>
  
  <!-- VS -->
  <text x="500" y="350" font-family="Inter, sans-serif" font-size="36" font-weight="700" text-anchor="middle" fill="#764ba2">VS</text>
  
  <!-- IP Grabber -->
  <g id="grabber">
    <rect x="550" y="100" width="400" height="500" rx="20" fill="white" stroke="#f5576c" stroke-width="4" opacity="0.95" filter="url(#shadow)"/>
    <text x="750" y="145" font-family="Inter, sans-serif" font-size="24" text-anchor="middle" fill="#f5576c" font-weight="700">{grabber_title}</text>
    
    <line x1="570" x2="930" y1="170" y2="170" stroke="#f5576c" stroke-width="2"/>
'''
    
    for i, feature in enumerate(grabber_features):
        y = y_start + i * 50
        svg += f'''    <circle cx="580" cy="{y}" r="6" fill="#f5576c"/>
    <text x="600" y="{y+5}" font-family="Inter, sans-serif" font-size="14" fill="#2d3748">{feature}</text>
'''
    
    svg += '''  </g>
</svg>'''
    
    return svg

def generate_email_tracking_flow(lang='en'):
    """生成邮件追踪流程图"""
    
    if lang == 'en':
        title = "Email Tracking Process Flow"
        steps = [
            ("Send Email", "Email with tracking pixel sent"),
            ("Email Opened", "Recipient opens email"),
            ("Pixel Loaded", "Tracking pixel image loads"),
            ("IP Captured", "Server logs IP address"),
            ("Data Recorded", "Store: IP, time, location"),
            ("Analytics Updated", "Dashboard shows open rate")
        ]
    else:
        title = "邮件追踪流程图"
        steps = [
            ("发送邮件", "发送包含追踪像素的邮件"),
            ("邮件打开", "收件人打开邮件"),
            ("像素加载", "追踪像素图片加载"),
            ("IP捕获", "服务器记录IP地址"),
            ("数据记录", "存储：IP、时间、位置"),
            ("分析更新", "仪表板显示打开率")
        ]
    
    svg = f'''<svg viewBox="0 0 900 700" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#f8f9fa;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#e9ecef;stop-opacity:1" />
    </linearGradient>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#4A90E2"/>
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
  
  <!-- Start -->
  <ellipse cx="450" cy="90" rx="100" ry="45" fill="#4A90E2" stroke="#357ABD" stroke-width="2" opacity="0.9"/>
  <text x="450" y="100" font-family="Inter, sans-serif" font-size="16" text-anchor="middle" fill="white" font-weight="600">{'Start' if lang == 'en' else '开始'}</text>
  
'''
    
    y_positions = [180, 250, 320, 390, 460, 530]
    colors = ["#4A90E2", "#357ABD", "#2E5C8A", "#1E3A5F", "#0F1F2F", "#48bb78"]
    
    for i, (step_title, step_desc) in enumerate(steps):
        y = y_positions[i]
        color = colors[i]
        
        if i > 0:
            prev_y = y_positions[i-1]
            svg += f'  <path d="M 450 {prev_y + 50} L 450 {y - 25}" stroke="#4A90E2" stroke-width="3" fill="none" marker-end="url(#arrow)"/>\n'
        
        svg += f'''  <g>
    <rect x="300" y="{y-25}" width="300" height="70" rx="12" fill="white" stroke="{color}" stroke-width="3" opacity="0.95" filter="url(#shadow)"/>
    <text x="450" y="{y}" font-family="Inter, sans-serif" font-size="15" text-anchor="middle" fill="#2d3748" font-weight="700">{step_title}</text>
    <text x="450" y="{y+20}" font-family="Inter, sans-serif" font-size="12" text-anchor="middle" fill="#4a5568">{step_desc}</text>
  </g>
  
'''
    
    svg += f'''  <path d="M 450 580 L 450 620" stroke="#4A90E2" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
  <ellipse cx="450" cy="650" rx="100" ry="45" fill="#48bb78" stroke="#38a169" stroke-width="2" opacity="0.9"/>
  <text x="450" y="660" font-family="Inter, sans-serif" font-size="16" text-anchor="middle" fill="white" font-weight="600">{'Complete' if lang == 'en' else '完成'}</text>
</svg>'''
    
    return svg

def generate_ip_address_structure(lang='en'):
    """生成IP地址结构图解"""
    
    if lang == 'en':
        title = "IP Address Structure"
        ipv4_title = "IPv4 Address"
        ipv6_title = "IPv6 Address"
        ipv4_example = "192.168.1.1"
        ipv6_example = "2001:0db8:85a3::8a2e:0370:7334"
    else:
        title = "IP地址结构"
        ipv4_title = "IPv4地址"
        ipv6_title = "IPv6地址"
        ipv4_example = "192.168.1.1"
        ipv6_example = "2001:0db8:85a3::8a2e:0370:7334"
    
    svg = f'''<svg viewBox="0 0 1000 600" xmlns="http://www.w3.org/2000/svg">
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
  
  <rect width="1000" height="600" fill="url(#bgGrad)"/>
  <text x="500" y="40" font-family="Inter, sans-serif" font-size="28" font-weight="700" text-anchor="middle" fill="#2d3748">{title}</text>
  
  <!-- IPv4 -->
  <g id="ipv4">
    <rect x="50" y="100" width="420" height="450" rx="15" fill="white" stroke="#667eea" stroke-width="3" filter="url(#shadow)"/>
    <text x="260" y="140" font-family="Inter, sans-serif" font-size="22" text-anchor="middle" fill="#667eea" font-weight="700">{ipv4_title}</text>
    <text x="260" y="200" font-family="Monaco, monospace" font-size="32" text-anchor="middle" fill="#2d3748" font-weight="600">{ipv4_example}</text>
    
    <!-- IPv4 Structure -->
    <text x="80" y="260" font-family="Inter, sans-serif" font-size="14" fill="#4a5568" font-weight="600">Structure:</text>
    <text x="80" y="290" font-family="Inter, sans-serif" font-size="13" fill="#2d3748">• 32-bit address</text>
    <text x="80" y="315" font-family="Inter, sans-serif" font-size="13" fill="#2d3748">• 4 octets (8 bits each)</text>
    <text x="80" y="340" font-family="Inter, sans-serif" font-size="13" fill="#2d3748">• Dotted decimal notation</text>
    <text x="80" y="365" font-family="Inter, sans-serif" font-size="13" fill="#2d3748">• ~4.3 billion addresses</text>
    <text x="80" y="390" font-family="Inter, sans-serif" font-size="13" fill="#2d3748">• Widely supported</text>
  </g>
  
  <!-- IPv6 -->
  <g id="ipv6">
    <rect x="530" y="100" width="420" height="450" rx="15" fill="white" stroke="#f5576c" stroke-width="3" filter="url(#shadow)"/>
    <text x="740" y="140" font-family="Inter, sans-serif" font-size="22" text-anchor="middle" fill="#f5576c" font-weight="700">{ipv6_title}</text>
    <text x="740" y="200" font-family="Monaco, monospace" font-size="24" text-anchor="middle" fill="#2d3748" font-weight="600">{ipv6_example}</text>
    
    <!-- IPv6 Structure -->
    <text x="560" y="260" font-family="Inter, sans-serif" font-size="14" fill="#4a5568" font-weight="600">Structure:</text>
    <text x="560" y="290" font-family="Inter, sans-serif" font-size="13" fill="#2d3748">• 128-bit address</text>
    <text x="560" y="315" font-family="Inter, sans-serif" font-size="13" fill="#2d3748">• 8 groups of 16 bits</text>
    <text x="560" y="340" font-family="Inter, sans-serif" font-size="13" fill="#2d3748">• Hexadecimal notation</text>
    <text x="560" y="365" font-family="Inter, sans-serif" font-size="13" fill="#2d3748">• Nearly unlimited addresses</text>
    <text x="560" y="390" font-family="Inter, sans-serif" font-size="13" fill="#2d3748">• Built-in security (IPsec)</text>
  </g>
</svg>'''
    
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
    print('开始生成流程图...\n')
    
    # 1. IP追踪工作原理
    en1 = generate_how_ip_tracking_works('en')
    save_diagram(en1, 'how-ip-tracking-works.svg', 'en')
    zh1 = generate_how_ip_tracking_works('zh')
    save_diagram(zh1, 'how-ip-tracking-works.svg', 'zh')
    
    # 2. IP Tracker vs IP Grabber
    en2 = generate_ip_tracker_vs_grabber('en')
    save_diagram(en2, 'ip-tracker-vs-ip-grabber.svg', 'en')
    zh2 = generate_ip_tracker_vs_grabber('zh')
    save_diagram(zh2, 'ip-tracker-vs-ip-grabber.svg', 'zh')
    
    # 3. 邮件追踪流程
    en3 = generate_email_tracking_flow('en')
    save_diagram(en3, 'email-tracking-process-flow.svg', 'en')
    zh3 = generate_email_tracking_flow('zh')
    save_diagram(zh3, 'email-tracking-process-flow.svg', 'zh')
    
    # 4. IP地址结构
    en4 = generate_ip_address_structure('en')
    save_diagram(en4, 'ip-address-structure.svg', 'en')
    zh4 = generate_ip_address_structure('zh')
    save_diagram(zh4, 'ip-address-structure.svg', 'zh')
    
    print('\n完成! 已生成8个流程图（中英文各4个）')
