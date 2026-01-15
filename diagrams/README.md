# 流程图和图表目录

这个文件夹包含所有文章的SVG流程图和图表，帮助用户更好地理解内容。

## 文件夹结构

```
diagrams/
├── en/          # 英文文章的流程图
├── zh/          # 中文文章的流程图
└── templates/   # SVG模板和工具
```

## 使用说明

### 1. 命名规范
- 文件名应与对应的文章文件名一致（去掉.html后缀）
- 例如：`ip-tracker-how-to-find-someones-ip-complete-guide.svg`

### 2. SVG文件要求
- 使用标准SVG格式
- 确保响应式设计（使用viewBox）
- 添加适当的aria-label用于无障碍访问
- 文件大小尽量控制在50KB以内

### 3. 在文章中使用
```html
<figure class="diagram-container">
  <img src="../diagrams/en/ip-tracker-how-to-find-someones-ip-complete-guide.svg" 
       alt="IP Tracking Process Flow Diagram"
       loading="lazy">
  <figcaption>IP追踪流程图：从创建追踪链接到获取IP地址的完整过程</figcaption>
</figure>
```

## 流程图类型

### 1. 流程类（Process Flow）
- IP追踪流程
- 邮件追踪流程
- PDF追踪流程

### 2. 对比类（Comparison）
- IP Tracker vs IP Grabber
- 不同追踪方法对比

### 3. 架构类（Architecture）
- 系统架构图
- 技术栈图

### 4. 决策树（Decision Tree）
- 如何选择追踪方法
- 合规性检查流程

## 工具和资源

- 推荐使用工具：Draw.io, Figma, Inkscape
- 在线SVG编辑器：https://boxy-svg.com/
- SVG优化工具：SVGO
