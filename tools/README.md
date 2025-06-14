# 🔧 Tools 目录

这个目录包含了开发和维护网站的各种工具和脚本。

## 📋 工具列表

```
tools/
├── simple_mcp_test.py      # 🧪 MCP简化测试程序
├── mcp_main.py            # 🚀 MCP完整客户端程序
├── website_env_setup.sh   # 🌐 Website环境快速设置
├── setup.sh              # ⚙️ 基础环境安装脚本
└── requirements.txt       # 📦 Python依赖包列表
```

## 🚀 快速开始

### 1. 环境设置

```bash
# 方法一：使用快速设置脚本
./tools/website_env_setup.sh

# 方法二：手动设置
conda create -n Website python=3.11 -y
conda activate Website
pip install -r tools/requirements.txt
```

### 2. MCP功能测试

```bash
# 激活环境
conda activate Website

# 运行简化测试程序（推荐）
python tools/simple_mcp_test.py

# 或运行完整程序
python tools/mcp_main.py
```

## 🔧 工具详细说明

### simple_mcp_test.py
**简化版MCP测试程序**

- ✅ **无复杂依赖**: 只需要Python标准库
- ✅ **交互式界面**: 友好的命令行交互
- ✅ **功能齐全**: 包含所有主要测试功能

**主要功能**:
- 加载并显示MCP配置
- 检查环境前置条件
- 模拟文件系统操作
- 模拟Git操作
- 模拟Context7查询

**使用示例**:
```bash
python tools/simple_mcp_test.py

# 交互命令示例
help                    # 显示帮助
config                  # 显示MCP配置  
check                   # 检查环境
fs                      # 测试文件系统
git                     # 测试Git功能
context7                # 模拟Context7
use context7 博客开发    # 模拟查询
quit                    # 退出
```

### mcp_main.py
**完整版MCP客户端程序**

- ⚠️ **需要MCP SDK**: 需要安装 `mcp` 包
- 🔌 **真实连接**: 可以连接真实的MCP服务器
- 🔄 **异步操作**: 支持并发操作

**使用场景**:
- 需要连接真实MCP服务器
- 进行高级MCP开发
- 性能测试和压力测试

### website_env_setup.sh
**Website环境快速设置脚本**

**功能**:
- 自动激活Website conda环境
- 显示环境信息和已安装包
- 检查MCP配置状态
- 提供使用建议

**使用方法**:
```bash
./tools/website_env_setup.sh
```

### setup.sh
**基础环境安装脚本**

**功能**:
- 检查Python和pip安装状态
- 安装requirements.txt中的依赖
- 检查Node.js和npm状态
- 设置执行权限

**使用方法**:
```bash
./tools/setup.sh
```

### requirements.txt
**Python依赖包列表**

**包含的包**:
- `requests` - HTTP请求处理
- `aiohttp` - 异步HTTP
- `flask` - Web框架
- `fastapi` - 现代API框架
- `beautifulsoup4` - HTML解析
- `markdown` - Markdown处理
- `jinja2` - 模板引擎

## 🎯 使用场景

### 网站开发

1. **本地开发环境**:
   ```bash
   ./tools/website_env_setup.sh
   cd website
   python -m http.server 8000
   ```

2. **内容创建辅助**:
   ```bash
   python tools/simple_mcp_test.py
   # 使用 "use context7 markdown教程" 获取最新语法
   ```

### MCP开发和测试

1. **快速功能验证**:
   ```bash
   python tools/simple_mcp_test.py
   ```

2. **高级开发**:
   ```bash
   python tools/mcp_main.py
   ```

### 环境维护

1. **检查环境状态**:
   ```bash
   ./tools/website_env_setup.sh
   ```

2. **重新安装依赖**:
   ```bash
   ./tools/setup.sh
   ```

## 🔍 故障排除

### 常见问题

1. **权限错误**:
   ```bash
   chmod +x tools/*.sh
   ```

2. **Python环境问题**:
   ```bash
   # 重新创建环境
   conda env remove -n Website
   conda create -n Website python=3.11 -y
   conda activate Website
   pip install -r tools/requirements.txt
   ```

3. **MCP配置问题**:
   - 检查 `~/.cursor/mcp.json` 是否存在
   - 验证JSON格式是否正确
   - 确保Cursor已重启

4. **Node.js相关问题**:
   ```bash
   # 通过conda安装
   conda install nodejs -c conda-forge -y
   
   # 或使用系统包管理器
   brew install node  # macOS
   ```

### 日志和调试

- **MCP测试日志**: 程序运行时会显示详细状态
- **环境检查**: 使用 `check` 命令查看环境状态
- **配置验证**: 使用 `config` 命令查看MCP配置

## 🔗 相关资源

- [MCP官方文档](https://modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Context7 GitHub](https://github.com/upstash/context7)
- [Conda环境管理](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

## 📞 获取帮助

如果遇到问题：
1. 查看程序输出的错误信息
2. 检查环境配置是否正确
3. 参考 `docs/MCP_README.md` 获取详细说明
4. 在GitHub仓库中提交Issue 