# ⚡ 快速开始指南

> 5分钟快速了解和使用这个仓库！

## 🎯 我是什么角色？

### 👁️ 我只想看网站
**直接访问**: [tian-sports-sciences.me](https://tian-sports-sciences.me)

### 🔧 我想修改网站内容
1. **编辑主页**: 修改 `website/index.html`
2. **添加文章**: 复制 `website/acl-injury.html` 并修改
3. **更新样式**: 编辑 `website/css/styles.css`
4. **测试**: 在 `website/` 目录运行 `python -m http.server 8000`

### 🤖 我想使用AI工具
1. **设置环境**: 运行 `./tools/website_env_setup.sh`
2. **测试MCP**: 运行 `python tools/simple_mcp_test.py`
3. **在Cursor中使用**: 重启Cursor，使用 `use context7`

### 💻 我是开发者
1. **克隆仓库**: `git clone https://github.com/0TCUT/0TCUT.github.io.git`
2. **查看完整文档**: 阅读 `README.md`
3. **选择工具**: 查看 `tools/README.md`

## 📂 5秒了解目录结构

```
📁 website/     🌐 网站文件（HTML、CSS、JS）
📁 tools/       🔧 开发工具和MCP脚本  
📁 docs/        📚 详细文档和说明
📁 backup/      🗄️ 备份和临时文件
```

## 🚀 常用操作

### 快速预览网站
```bash
cd website && python -m http.server 8000
# 访问 http://localhost:8000
```

### 快速测试MCP
```bash
python tools/simple_mcp_test.py
```

### 快速部署更新
```bash
git add . && git commit -m "更新内容" && git push
```

## 📞 需要帮助？

- 📖 **详细说明**: 查看 `README.md`
- 🔧 **工具问题**: 查看 `tools/README.md`  
- 🤖 **MCP使用**: 查看 `docs/MCP_README.md`
- 🌐 **网站修改**: 查看 `website/README.md`

## ⭐ 推荐流程

### 新手第一次使用
1. 访问在线网站了解内容
2. 阅读本文档了解结构
3. 尝试修改 `website/index.html` 的一个小地方
4. 本地预览测试效果

### 进阶使用
1. 设置开发环境
2. 学习MCP工具使用
3. 创建新的文章页面
4. 优化网站性能和SEO

---

**💡 提示**: 每个目录都有自己的 `README.md`，遇到问题先查看对应目录的说明！ 