# 已添加流程图的文章列表

## ✅ 已完成

### 英文文章 (已添加SVG + Mermaid双重流程图)

1. **how-ip-tracking-works.html**
   - SVG: `diagrams/en/how-ip-tracking-works.svg`
   - Mermaid: IP追踪工作流程图
   - 位置: "How IP Tracking Works" 章节

2. **ip-tracker-vs-ip-grabber-guide.html**
   - SVG: `diagrams/en/ip-tracker-vs-ip-grabber.svg`
   - Mermaid: IP Tracker vs IP Grabber 对比图
   - 位置: "IP Tracker vs IP Grabber: Key Differences" 章节

3. **email-tracking-best-practices.html**
   - SVG: `diagrams/en/email-tracking-process-flow.svg`
   - Mermaid: 邮件追踪流程图
   - 位置: 文章介绍部分

4. **ip-address-basics.html**
   - SVG: `diagrams/en/ip-address-structure.svg`
   - Mermaid: IP地址结构图
   - 位置: "IPv4 vs IPv6" 章节

5. **track-ip-from-a-link.html**
   - SVG: `diagrams/en/link-tracking-process-flow.svg`
   - Mermaid: 链接追踪流程图
   - 位置: 文章介绍部分

6. **ip-tracking-gdpr-compliance.html**
   - SVG: `diagrams/en/gdpr-compliance-checklist.svg`
   - Mermaid: GDPR合规检查清单
   - 位置: "Compliance Checklist" 章节

7. **how-to-find-someones-ip-address.html**
   - SVG: `diagrams/en/find-ip-methods.svg`
   - Mermaid: 查找IP方法对比图
   - 位置: 文章介绍部分

### 中文文章 (已添加SVG + Mermaid双重流程图)

1. **zh/how-to-find-someones-ip-address-social-media.html**
   - SVG: `diagrams/zh/find-ip-methods.svg`
   - Mermaid: 查找IP方法对比图
   - 位置: 文章介绍部分

## 📋 流程图特性

### 双重展示方式
每篇文章都包含两种流程图：

1. **SVG静态图**
   - 高质量矢量图
   - 快速加载
   - 适合打印和分享

2. **Mermaid交互式图**
   - 可交互的流程图
   - 支持缩放和查看
   - 代码形式，易于维护

### Mermaid.js集成
所有文章都已添加Mermaid.js库：
```html
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true, theme: 'default' });
</script>
```

## 🎨 流程图样式

### 容器样式
```css
.diagram-container {
  margin: 3rem 0;
  text-align: center;
}
```

### SVG图片样式
- 最大宽度: 100%
- 圆角: 10px
- 阴影: 0 4px 15px rgba(0,0,0,0.1)
- 响应式设计

### Mermaid容器样式
- 背景: #f8f9fa
- 内边距: 2rem
- 圆角: 10px
- 顶部边距: 2rem

## 📊 统计信息

- **已添加流程图的文章数**: 8篇
  - 英文: 7篇
  - 中文: 1篇
- **流程图总数**: 16个（每篇文章2个：SVG + Mermaid）
- **Mermaid脚本**: 已集成到所有相关文章

## 🔄 待添加流程图的文章

### 高优先级
- [ ] `ip-tracker-how-to-find-someones-ip-complete-guide.html` - IP追踪完整指南
- [ ] `ip-tracking-customer-journey.html` - 客户旅程地图
- [ ] `ip-tracking-analytics.html` - 数据分析流程

### 中优先级
- [ ] `track-pdf-readers-without-them-knowing.html` - PDF追踪流程
- [ ] `ip-geolocation-technology-explained.html` - 地理位置定位过程
- [ ] `ip-tracking-cybersecurity.html` - 安全威胁检测流程

## 🛠️ 使用方法

### 查看流程图
1. 打开文章页面
2. 滚动到相应的章节
3. 查看SVG静态图和Mermaid交互式图

### 编辑流程图
1. **SVG**: 编辑 `diagrams/en/` 或 `diagrams/zh/` 中的SVG文件
2. **Mermaid**: 在文章HTML中直接编辑Mermaid代码块

### 添加新流程图
1. 生成SVG文件并保存到 `diagrams/en/` 或 `diagrams/zh/`
2. 在文章中添加流程图HTML代码
3. 添加对应的Mermaid代码

---

*最后更新：2025-01-15*
