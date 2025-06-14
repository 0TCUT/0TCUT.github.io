# MCP 测试程序使用指南

## 🚀 概述

这个项目包含了用于测试和使用MCP（Model Context Protocol）的程序，专为个人网站开发优化。

## 📋 文件说明

- `simple_mcp_test.py` - 简化版MCP测试程序（推荐）
- `mcp_main.py` - 完整版MCP客户端程序（需要更多依赖）
- `requirements.txt` - Python依赖包
- `setup.sh` - 自动安装脚本

## 🔧 已配置的MCP服务器

根据 `/Users/tian/.cursor/mcp.json` 配置：

1. **Context7** 🚀
   - 获取最新技术文档
   - 用法：`use context7`

2. **Filesystem** 📁
   - 文件系统操作
   - 读取、列出文件

3. **Git** 🔀
   - Git版本控制
   - 状态检查、日志查看

4. **Brave Search** 🔍
   - 网络搜索（需要API密钥）

## 🚀 快速开始

### 方法一：直接运行简化版程序

```bash
# 运行测试程序
python3 simple_mcp_test.py
```

### 方法二：完整安装

```bash
# 运行安装脚本
./setup.sh

# 或手动安装
pip3 install -r requirements.txt
python3 mcp_main.py
```

## 💡 使用示例

### 基本测试
程序启动后会自动执行：
- 加载MCP配置
- 检查前置条件（Node.js、npm、Git）
- 测试文件系统功能
- 测试Git功能
- 模拟Context7功能

### 交互式命令

进入交互模式后，可以使用以下命令：

```bash
help                    # 显示帮助
config                  # 显示MCP配置
check                   # 检查前置条件
fs                      # 测试文件系统
git                     # 测试Git功能
context7                # 模拟Context7
use context7 博客网站    # 模拟Context7查询
quit                    # 退出程序
```

### Context7 查询示例

```bash
use context7 创建个人博客
use context7 Next.js 最新特性
use context7 Tailwind CSS 配置
```

## 🎯 适用场景

### 个人网站开发
- **博客系统**：MDX、Markdown处理
- **项目展示**：GitHub集成
- **技术分享**：代码高亮、语法支持

### 技术栈支持
- **前端**：React、Next.js、Vue、HTML/CSS
- **样式**：Tailwind CSS、CSS Modules
- **内容**：Markdown、MDX
- **部署**：Vercel、Netlify、GitHub Pages

## 🔍 故障排除

### 常见问题

1. **Node.js未安装**
   ```bash
   # macOS
   brew install node
   
   # 或访问 https://nodejs.org/
   ```

2. **MCP配置文件未找到**
   - 确保文件存在：`~/.cursor/mcp.json`
   - 或在Cursor中重新配置MCP

3. **Git功能测试失败**
   - 确保当前目录是Git仓库
   - 运行 `git init` 初始化仓库

4. **权限问题**
   ```bash
   chmod +x simple_mcp_test.py
   chmod +x setup.sh
   ```

### 环境要求

- **Python 3.7+**
- **Node.js 16+**（MCP服务器需要）
- **Git**（版本控制功能）
- **npm/npx**（安装MCP服务器）

## 📚 进阶使用

### 添加新的MCP服务器

编辑 `~/.cursor/mcp.json`：

```json
{
  "mcpServers": {
    "your-server": {
      "command": "npx",
      "args": ["-y", "@your/mcp-server"],
      "disabled": false
    }
  }
}
```

### 自定义查询

修改 `simple_mcp_test.py` 中的 `simulate_context7_query` 方法，添加你的查询逻辑。

## 🎉 下一步

1. **在Cursor中使用**：重启Cursor，开始使用配置好的MCP
2. **创建博客项目**：使用Context7获取最新的Next.js模板
3. **文件管理**：使用Filesystem MCP管理项目文件
4. **版本控制**：使用Git MCP管理代码版本

## 📞 支持

如果遇到问题：
1. 检查前置条件是否满足
2. 查看程序输出的错误信息
3. 确保MCP配置文件格式正确

---

**作者**: Tian Sports Sciences  
**用途**: 个人网站开发的MCP测试和使用  
**版本**: 1.0.0 