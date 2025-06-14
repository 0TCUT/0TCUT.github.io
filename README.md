# 🌐 Website 目录

这个目录包含了Tian Sports Sciences网站的所有前端文件。

## 📋 文件结构

```
website/
├── index.html          # 🏠 主页 - 网站首页
├── acl-injury.html     # 📄 ACL损伤专题页面
├── CNAME              # 🔗 自定义域名配置
├── css/               # 🎨 样式文件
│   └── styles.css     # 主要样式表
├── js/                # ⚡ JavaScript文件
│   └── scripts.js     # 主要脚本
└── assets/            # 📦 静态资源
    ├── favicon.ico    # 网站图标
    └── img/           # 图片资源
```

## 🔧 开发说明

### 本地预览

1. **简单HTTP服务器**：
   ```bash
   cd website
   python -m http.server 8000
   # 访问 http://localhost:8000
   ```

2. **Live Server** (VS Code扩展)：
   - 安装Live Server扩展
   - 右键点击 `index.html` → "Open with Live Server"

### 文件修改指南

#### 修改主页内容
- **文件**: `index.html`
- **主要部分**:
  - 导航栏: `<nav>` 部分
  - 软件介绍: `#softwares` 部分
  - 文章展示: `#portfolio` 部分
  - 联系信息: `#team` 部分

#### 添加新页面
1. 复制 `acl-injury.html` 作为模板
2. 修改内容和标题
3. 在 `index.html` 中添加链接

#### 样式修改
- **文件**: `css/styles.css`
- **包含**: Bootstrap主题 + 自定义样式
- **注意**: 文件较大，建议使用搜索功能定位

#### 添加图片
- **位置**: `assets/img/`
- **用途**: 软件图标、文章配图、背景图等
- **格式**: 支持 PNG、JPG、SVG

## 🎯 部署说明

### GitHub Pages部署

文件修改后自动部署：
1. 提交更改到main分支
2. GitHub Actions自动部署
3. 约5分钟后生效

### 自定义域名

- **配置文件**: `CNAME`
- **当前域名**: `tian-sports-sciences.me`
- **修改方法**: 直接编辑CNAME文件内容

## ⚠️ 注意事项

1. **路径引用**: 修改文件位置时注意更新路径
2. **图片优化**: 上传前压缩图片以提高加载速度  
3. **响应式设计**: 确保在不同设备上正常显示
4. **SEO优化**: 更新页面标题和meta标签

## 🔗 相关链接

- [在线网站](https://tian-sports-sciences.me)
- [GitHub Pages文档](https://docs.github.com/pages)
- [Bootstrap 5文档](https://getbootstrap.com/docs/5.0/)
- [Font Awesome图标](https://fontawesome.com/) 