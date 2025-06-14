#!/bin/bash

echo "🚀 MCP主程序安装脚本"
echo "===================="

# 检查Python版本
python_version=$(python3 --version 2>&1)
if [[ $? -eq 0 ]]; then
    echo "✅ Python版本: $python_version"
else
    echo "❌ Python3未安装，请先安装Python3"
    exit 1
fi

# 检查pip
if command -v pip3 &> /dev/null; then
    echo "✅ pip3已安装"
else
    echo "❌ pip3未安装，请先安装pip3"
    exit 1
fi

# 安装依赖
echo "📦 安装Python依赖包..."
pip3 install -r requirements.txt

if [[ $? -eq 0 ]]; then
    echo "✅ 依赖安装成功"
else
    echo "❌ 依赖安装失败"
    echo "💡 尝试手动安装: pip3 install mcp"
fi

# 检查Node.js和npm（MCP服务器需要）
if command -v node &> /dev/null; then
    node_version=$(node --version)
    echo "✅ Node.js版本: $node_version"
else
    echo "⚠️  Node.js未安装，部分MCP服务器可能无法运行"
    echo "💡 请安装Node.js: https://nodejs.org/"
fi

if command -v npm &> /dev/null; then
    npm_version=$(npm --version)
    echo "✅ npm版本: $npm_version"
else
    echo "⚠️  npm未安装"
fi

# 设置执行权限
chmod +x mcp_main.py

echo ""
echo "🎉 安装完成！"
echo "📋 使用方法:"
echo "   python3 mcp_main.py"
echo ""
echo "🔧 如果遇到问题，请检查:"
echo "   1. Python3和pip3是否正确安装"
echo "   2. Node.js和npm是否安装（用于MCP服务器）"
echo "   3. MCP配置文件是否存在: ~/.cursor/mcp.json" 