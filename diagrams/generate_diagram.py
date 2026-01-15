#!/usr/bin/env python3
"""
SVG流程图生成工具
用于为博客文章生成流程图和图表
"""

import os
from pathlib import Path

def generate_ip_tracking_flow(lang='en'):
    """生成IP追踪流程图"""
    
    if lang == 'en':
        title = "IP Tracking Process Flow"
        steps = [
            ("Create Tracking Link", "Generate a unique tracking URL"),
            ("Share Link", "Send link via email, social media, or message"),
            ("User Clicks", "Target user clicks on the tracking link"),
            ("Capture IP", "Server logs the visitor's IP address"),
            ("View Results", "Access IP data and geolocation info")
        ]
    else:
        title = "IP追踪流程图"
        steps = [
            ("创建追踪链接", "生成唯一的追踪URL"),
            ("分享链接", "通过邮件、社交媒体或消息发送链接"),
            ("用户点击", "目标用户点击追踪链接"),
            ("捕获IP", "服务器记录访问者的IP地址"),
            ("查看结果", "访问IP数据和地理位置信息")
        ]
    
    svg_content = f'''<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <!-- 背景渐变 -->
  <defs>
    <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#f8f9fa;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#e9ecef;stop-opacity:1" />
    </linearGradient>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#667eea"/>
    </marker>
  </defs>
  
  <rect width="800" height="600" fill="url(#bgGradient)"/>
  
  <!-- 标题 -->
  <text x="400" y="40" font-family="Inter, sans-serif" font-size="24" font-weight="600" text-anchor="middle" fill="#2d3748">
    {title}
  </text>
  
  <!-- 开始节点 -->
  <g id="start">
    <ellipse cx="400" cy="100" rx="90" ry="45" fill="#667eea" stroke="#764ba2" stroke-width="2" opacity="0.9"/>
    <text x="400" y="110" font-family="Inter, sans-serif" font-size="16" text-anchor="middle" fill="white" font-weight="600">
      {'Start' if lang == 'en' else '开始'}
    </text>
  </g>
  
  <!-- 步骤 -->
'''
    
    y_positions = [180, 260, 340, 420, 500]
    colors = ["#667eea", "#764ba2", "#f093fb", "#f5576c", "#4facfe"]
    
    for i, (step_title, step_desc) in enumerate(steps):
        y = y_positions[i]
        color = colors[i]
        
        # 箭头
        if i > 0:
            prev_y = y_positions[i-1]
            svg_content += f'  <path d="M 400 {prev_y + 60} L 400 {y - 20}" stroke="#667eea" stroke-width="3" fill="none" marker-end="url(#arrowhead)"/>\n'
        
        # 步骤框
        svg_content += f'''  <g id="step{i+1}">
    <rect x="250" y="{y-20}" width="300" height="80" rx="12" fill="white" stroke="{color}" stroke-width="3" opacity="0.95" filter="url(#shadow)"/>
    <text x="400" y="{y+5}" font-family="Inter, sans-serif" font-size="16" text-anchor="middle" fill="#2d3748" font-weight="700">
      {step_title}
    </text>
    <text x="400" y="{y+25}" font-family="Inter, sans-serif" font-size="13" text-anchor="middle" fill="#4a5568">
      {step_desc}
    </text>
  </g>
  
'''
    
    # 结束节点
    svg_content += f'''  <!-- 结束节点 -->
  <path d="M 400 540 L 400 555" stroke="#667eea" stroke-width="3" fill="none" marker-end="url(#arrowhead)"/>
  <g id="end">
    <ellipse cx="400" cy="570" rx="90" ry="45" fill="#48bb78" stroke="#38a169" stroke-width="2" opacity="0.9"/>
    <text x="400" y="580" font-family="Inter, sans-serif" font-size="16" text-anchor="middle" fill="white" font-weight="600">
      {'Complete' if lang == 'en' else '完成'}
    </text>
  </g>
  
  <!-- 阴影效果 -->
  <defs>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="3"/>
      <feOffset dx="2" dy="2" result="offsetblur"/>
      <feComponentTransfer>
        <feFuncA type="linear" slope="0.3"/>
      </feComponentTransfer>
      <feMerge>
        <feMergeNode/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
</svg>'''
    
    return svg_content

def save_diagram(content, filename, lang='en'):
    """保存SVG文件"""
    output_dir = Path(__file__).parent / lang
    output_dir.mkdir(exist_ok=True)
    
    output_path = output_dir / filename
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✓ 已生成: {output_path}')

if __name__ == '__main__':
    # 生成英文版IP追踪流程图
    en_content = generate_ip_tracking_flow('en')
    save_diagram(en_content, 'ip-tracking-process-flow.svg', 'en')
    
    # 生成中文版IP追踪流程图
    zh_content = generate_ip_tracking_flow('zh')
    save_diagram(zh_content, 'ip-tracking-process-flow.svg', 'zh')
    
    print('\n完成! 流程图已生成。')
