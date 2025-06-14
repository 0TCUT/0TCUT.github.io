# 🏥 Tian Sports Sciences - 运动科学与生物力学网站

> 专业的运动科学和生物力学知识分享平台，包含软件教程、研究文章和开发工具。

## 🌐 在线访问

- **主网站**: [tian-sports-sciences.me](https://tian-sports-sciences.me)
- **GitHub Pages**: [0TCUT.github.io](https://0tcut.github.io)

## 📋 仓库结构

```
0TCUT.github.io/
├── 📁 website/          # 🌐 主网站文件
│   ├── index.html       # 主页
│   ├── acl-injury.html  # ACL损伤专题页
│   ├── css/            # 样式文件
│   ├── js/             # JavaScript文件
│   ├── assets/         # 图片和静态资源
│   └── CNAME           # 自定义域名配置
├── 📁 tools/            # 🔧 开发工具
│   ├── simple_mcp_test.py      # MCP测试程序
│   ├── mcp_main.py             # MCP主程序
│   ├── website_env_setup.sh    # 环境设置脚本
│   ├── setup.sh               # 安装脚本
│   └── requirements.txt       # Python依赖
├── 📁 docs/             # 📚 文档
│   └── MCP_README.md    # MCP使用说明
├── 📁 backup/           # 🗄️ 备份文件
│   └── TEMP/           # 临时文件备份
└── README.md           # 📖 本说明文档
```

## 🚀 快速开始

### 对于访客（查看网站）

1. **在线访问**：直接访问 [tian-sports-sciences.me](https://tian-sports-sciences.me)
2. **本地预览**：打开 `website/index.html` 文件

### 对于开发者（修改网站）

1. **克隆仓库**：
   ```bash
   git clone https://github.com/0TCUT/0TCUT.github.io.git
   cd 0TCUT.github.io
   ```

2. **修改网站内容**：
   - 编辑 `website/index.html` 修改主页
   - 修改 `website/css/styles.css` 调整样式
   - 添加新页面到 `website/` 目录

3. **本地测试**：
   ```bash
   # 简单HTTP服务器
   cd website
   python -m http.server 8000
   # 访问 http://localhost:8000
   ```

4. **部署更新**：
   ```bash
   git add .
   git commit -m "更新网站内容"
   git push origin main
   ```

## 🔧 开发工具使用

### MCP (Model Context Protocol) 工具

这个仓库包含了强大的MCP工具，用于AI辅助开发：

1. **环境设置**：
   ```bash
   # 创建conda环境
   conda create -n Website python=3.11 -y
   conda activate Website
   
   # 或使用快速设置脚本
   ./tools/website_env_setup.sh
   ```

2. **安装依赖**：
   ```bash
   cd tools
   pip install -r requirements.txt
   ```

3. **运行MCP测试**：
   ```bash
   python tools/simple_mcp_test.py
   ```

### 可用功能

- ✅ **Context7**: 获取最新技术文档
- ✅ **文件系统操作**: 自动化文件管理
- ✅ **Git集成**: 版本控制辅助
- ✅ **网络搜索**: 实时信息获取

详细使用说明请查看 [`docs/MCP_README.md`](docs/MCP_README.md)

## 🎯 网站功能特性

### 主要内容

- **🧬 生物力学软件教程**
  - Matlab 数据分析
  - Visual 3D 建模
  - OpenSim 仿真

- **📄 研究文章**
  - ACL损伤机制研究
  - 运动损伤预防
  - 生物力学分析

- **🔗 社交媒体链接**
  - 知乎专栏
  - B站视频教程
  - 微信交流群

### 技术栈

- **前端**: HTML5, CSS3, JavaScript
- **框架**: Bootstrap 5
- **图标**: Font Awesome
- **分析**: Google Analytics
- **托管**: GitHub Pages

## 📝 内容更新指南

### 添加新文章

1. **创建HTML页面**：
   ```bash
   cp website/acl-injury.html website/new-article.html
   ```

2. **修改内容**：
   - 更新标题和内容
   - 调整样式和布局

3. **更新导航**：
   - 在 `website/index.html` 中添加链接
   - 更新文章列表

### 更新软件教程

1. **准备资源**：
   - 添加图片到 `website/assets/img/`
   - 更新软件图标

2. **修改主页**：
   - 编辑 `website/index.html` 中的软件部分
   - 更新描述和链接

## 🔧 维护指南

### 定期维护任务

1. **内容更新**：
   - 检查软件版本更新
   - 更新过时的链接
   - 添加新的研究内容

2. **技术维护**：
   - 更新依赖包版本
   - 检查网站性能
   - 优化SEO设置

3. **备份管理**：
   - 定期清理 `backup/` 目录
   - 保留重要的历史版本

### 故障排除

1. **网站无法访问**：
   - 检查 `website/CNAME` 文件
   - 验证DNS设置
   - 查看GitHub Pages状态

2. **MCP工具问题**：
   - 检查conda环境激活
   - 验证Node.js和Python安装
   - 查看错误日志

## 🤝 贡献指南

### 如何贡献

1. **Fork 仓库**
2. **创建功能分支**: `git checkout -b feature/new-feature`
3. **提交更改**: `git commit -m 'Add new feature'`
4. **推送分支**: `git push origin feature/new-feature`
5. **创建Pull Request**

### 贡献类型

- 🐛 **Bug修复**: 修复网站错误
- ✨ **新功能**: 添加新的内容或功能
- 📝 **文档改进**: 完善说明文档
- 🎨 **UI优化**: 改进用户界面

## 📞 联系方式

- **网站**: [tian-sports-sciences.me](https://tian-sports-sciences.me)
- **知乎**: [@UT_Biomechanics](https://www.zhihu.com/people/UT_Biomechanics)
- **B站**: [207216853](https://space.bilibili.com/207216853)
- **GitHub**: [@0TCUT](https://github.com/0TCUT)

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

感谢所有为运动科学和生物力学领域做出贡献的研究者和开发者。

---

**最后更新**: 2025年1月 | **维护者**: Tian Sports Sciences Team