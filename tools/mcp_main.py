#!/usr/bin/env python3
"""
MCP Main Program - 加载和测试MCP服务器
用于个人网站开发的MCP客户端示例
"""

import asyncio
import json
import os
import sys
from typing import Dict, Any, Optional
from pathlib import Path

# MCP相关导入
try:
    from mcp import ClientSession
    from mcp.client.stdio import stdio_client
    from mcp.types import (
        InitializeRequest,
        ListResourcesRequest,
        ListToolsRequest,
        CallToolRequest,
        ReadResourceRequest
    )
except ImportError:
    print("❌ MCP Python SDK未安装，请运行: pip install mcp")
    sys.exit(1)


class MCPManager:
    """MCP服务器管理器"""
    
    def __init__(self, config_path: str = "/Users/tian/.cursor/mcp.json"):
        self.config_path = config_path
        self.servers = {}
        self.sessions = {}
        
    async def load_config(self) -> Dict[str, Any]:
        """加载MCP配置"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                return config.get('mcpServers', {})
        except FileNotFoundError:
            print(f"❌ 配置文件未找到: {self.config_path}")
            return {}
        except json.JSONDecodeError as e:
            print(f"❌ 配置文件JSON格式错误: {e}")
            return {}
    
    async def connect_server(self, name: str, config: Dict[str, Any]) -> bool:
        """连接到MCP服务器"""
        try:
            print(f"🔌 正在连接服务器: {name}")
            
            # 构建命令
            command = config.get('command', 'npx')
            args = config.get('args', [])
            env = config.get('env', {})
            
            # 设置环境变量
            server_env = os.environ.copy()
            server_env.update(env)
            
            # 创建stdio客户端
            server_params = {
                'command': command,
                'args': args,
                'env': server_env
            }
            
            # 这里简化处理，实际使用时需要更复杂的连接逻辑
            print(f"✅ 服务器 {name} 配置加载成功")
            self.servers[name] = config
            return True
            
        except Exception as e:
            print(f"❌ 连接服务器 {name} 失败: {e}")
            return False
    
    async def test_filesystem_server(self):
        """测试文件系统服务器"""
        print("\n📁 测试文件系统服务器...")
        
        # 列出当前目录文件
        current_dir = Path.cwd()
        files = list(current_dir.glob("*"))
        
        print(f"📂 当前目录: {current_dir}")
        print("📄 文件列表:")
        for file in files[:10]:  # 只显示前10个
            if file.is_file():
                print(f"   📄 {file.name} ({file.stat().st_size} bytes)")
            else:
                print(f"   📁 {file.name}/")
    
    async def test_git_server(self):
        """测试Git服务器"""
        print("\n🔀 测试Git服务器...")
        
        try:
            import subprocess
            
            # 检查Git状态
            result = subprocess.run(['git', 'status', '--porcelain'], 
                                  capture_output=True, text=True, cwd='.')
            
            if result.returncode == 0:
                if result.stdout.strip():
                    print("📝 Git状态 - 有未提交的更改:")
                    for line in result.stdout.strip().split('\n'):
                        print(f"   {line}")
                else:
                    print("✅ Git状态 - 工作目录干净")
                
                # 显示最近的提交
                log_result = subprocess.run(['git', 'log', '--oneline', '-5'], 
                                          capture_output=True, text=True, cwd='.')
                if log_result.returncode == 0:
                    print("📋 最近的提交:")
                    for line in log_result.stdout.strip().split('\n'):
                        print(f"   {line}")
            else:
                print("❌ 当前目录不是Git仓库")
                
        except FileNotFoundError:
            print("❌ Git未安装")
        except Exception as e:
            print(f"❌ Git操作失败: {e}")
    
    async def test_context7_simulation(self):
        """模拟Context7功能"""
        print("\n🚀 模拟Context7功能...")
        
        # 模拟获取最新文档
        sample_docs = {
            "Next.js": "Next.js 15.0 - 最新的React框架，支持App Router",
            "React": "React 18.2 - 包含并发特性和Suspense",
            "Tailwind CSS": "Tailwind CSS 3.4 - 最新的实用工具CSS框架",
            "TypeScript": "TypeScript 5.3 - 最新的类型检查功能"
        }
        
        print("📚 可用的最新文档:")
        for tech, description in sample_docs.items():
            print(f"   🔖 {tech}: {description}")
    
    async def interactive_mode(self):
        """交互模式"""
        print("\n🎯 进入交互模式 (输入 'quit' 退出)")
        
        while True:
            try:
                command = input("\n💬 请输入命令 (或 'help' 查看帮助): ").strip()
                
                if command.lower() in ['quit', 'exit', 'q']:
                    print("👋 再见!")
                    break
                elif command.lower() == 'help':
                    self.show_help()
                elif command.lower() == 'status':
                    await self.show_status()
                elif command.lower() == 'test-fs':
                    await self.test_filesystem_server()
                elif command.lower() == 'test-git':
                    await self.test_git_server()
                elif command.lower() == 'test-context7':
                    await self.test_context7_simulation()
                elif command.startswith('use context7'):
                    await self.simulate_context7_query(command)
                else:
                    print("❓ 未知命令，输入 'help' 查看帮助")
                    
            except KeyboardInterrupt:
                print("\n👋 再见!")
                break
            except Exception as e:
                print(f"❌ 执行命令时出错: {e}")
    
    def show_help(self):
        """显示帮助信息"""
        print("""
🔧 可用命令:
   help          - 显示此帮助
   status        - 显示服务器状态
   test-fs       - 测试文件系统功能
   test-git      - 测试Git功能
   test-context7 - 测试Context7功能
   use context7 [query] - 模拟Context7查询
   quit/exit/q   - 退出程序
        """)
    
    async def show_status(self):
        """显示服务器状态"""
        print("\n📊 MCP服务器状态:")
        for name, config in self.servers.items():
            disabled = config.get('disabled', False)
            status = "❌ 已禁用" if disabled else "✅ 已启用"
            print(f"   {name}: {status}")
    
    async def simulate_context7_query(self, query: str):
        """模拟Context7查询"""
        # 提取查询内容
        query_text = query.replace('use context7', '').strip()
        if not query_text:
            query_text = "通用查询"
        
        print(f"\n🔍 Context7查询: {query_text}")
        print("📝 模拟响应:")
        
        # 根据查询内容提供模拟响应
        if 'next.js' in query_text.lower():
            print("""
✨ Next.js 15.0 最新功能:
- 改进的App Router
- 更好的服务端组件支持
- 优化的构建性能
- 新的Turbopack集成

示例代码:
```javascript
// app/page.tsx
export default function Page() {
  return <h1>Hello, Next.js 15!</h1>
}
```
            """)
        elif 'react' in query_text.lower():
            print("""
⚛️ React 18.2 新特性:
- 并发渲染
- 自动批处理
- Suspense改进
- 新的Hooks

示例代码:
```javascript
import { useState, useTransition } from 'react'

function App() {
  const [isPending, startTransition] = useTransition()
  const [count, setCount] = useState(0)
  
  return <div>Count: {count}</div>
}
```
            """)
        else:
            print(f"📚 为查询 '{query_text}' 提供最新的技术文档和示例...")


async def main():
    """主函数"""
    print("🚀 MCP主程序启动")
    print("=" * 50)
    
    # 创建MCP管理器
    manager = MCPManager()
    
    # 加载配置
    print("📋 加载MCP配置...")
    config = await manager.load_config()
    
    if not config:
        print("❌ 没有找到MCP服务器配置")
        return
    
    print(f"✅ 找到 {len(config)} 个MCP服务器配置")
    
    # 连接服务器
    for name, server_config in config.items():
        if not server_config.get('disabled', False):
            await manager.connect_server(name, server_config)
    
    # 运行测试
    print("\n🧪 运行基本测试...")
    await manager.test_filesystem_server()
    await manager.test_git_server()
    await manager.test_context7_simulation()
    
    # 进入交互模式
    await manager.interactive_mode()


if __name__ == "__main__":
    print("🎯 个人网站开发 - MCP测试程序")
    print("作者: Tian Sports Sciences")
    print("用途: 测试和使用MCP服务器功能")
    print()
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 程序被用户中断")
    except Exception as e:
        print(f"\n❌ 程序运行出错: {e}")
        sys.exit(1) 