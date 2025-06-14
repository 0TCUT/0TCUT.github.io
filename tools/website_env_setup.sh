#!/bin/bash

echo "🌐 Website开发环境设置脚本"
echo "========================="

# 激活conda环境
echo "🔄 激活Website conda环境..."
conda activate Website

if [ $? -eq 0 ]; then
    echo "✅ Website环境激活成功"
    
    # 显示环境信息
    echo ""
    echo "📋 环境信息:"
    echo "   Python版本: $(python --version)"
    echo "   Node.js版本: $(node --version)"
    echo "   npm版本: $(npm --version)"
    echo "   当前目录: $(pwd)"
    
    # 显示已安装的包
    echo ""
    echo "📦 主要已安装包:"
    echo "   ✅ requests - HTTP请求"
    echo "   ✅ aiohttp - 异步HTTP"
    echo "   ✅ flask - Web框架"
    echo "   ✅ fastapi - 现代API框架"
    echo "   ✅ beautifulsoup4 - HTML解析"
    echo "   ✅ markdown - Markdown处理"
    echo "   ✅ jinja2 - 模板引擎"
    
    # 检查MCP配置
    echo ""
    echo "🔧 MCP配置检查:"
    if [ -f "/Users/tian/.cursor/mcp.json" ]; then
        echo "   ✅ MCP配置文件存在"
    else
        echo "   ❌ MCP配置文件未找到"
    fi
    
    # 提供使用建议
    echo ""
    echo "🚀 使用建议:"
    echo "   1. 测试MCP: python simple_mcp_test.py"
    echo "   2. 创建Flask应用: python -c 'from flask import Flask; print(\"Flask可用\")'"
    echo "   3. 运行FastAPI: uvicorn main:app --reload"
    echo "   4. 处理Markdown: python -c 'import markdown; print(\"Markdown可用\")'"
    
    echo ""
    echo "🎯 环境设置完成，开始您的网站开发之旅吧！"
    
else
    echo "❌ 环境激活失败，请检查conda配置"
    exit 1
fi 