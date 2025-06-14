#!/usr/bin/env python3
"""
简化版MCP测试程序
用于测试MCP配置和模拟功能
"""

import json
import os
import subprocess
import sys
from pathlib import Path


class SimpleMCPTester:
    """简化的MCP测试器"""
    
    def __init__(self, config_path: str = "/Users/tian/.cursor/mcp.json"):
        self.config_path = config_path
        self.config = {}
        
    def load_config(self):
        """加载MCP配置"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.config = data.get('mcpServers', {})
                return True
        except FileNotFoundError:
            print(f"❌ 配置文件未找到: {self.config_path}")
            return False
        except json.JSONDecodeError as e:
            print(f"❌ 配置文件JSON格式错误: {e}")
            return False
    
    def show_config(self):
        """显示配置信息"""
        print("\n📋 MCP服务器配置:")
        print("=" * 40)
        
        if not self.config:
            print("❌ 没有找到MCP服务器配置")
            return
        
        for name, config in self.config.items():
            disabled = config.get('disabled', False)
            status = "❌ 已禁用" if disabled else "✅ 已启用"
            command = config.get('command', 'unknown')
            args = config.get('args', [])
            
            print(f"\n🔧 服务器: {name}")
            print(f"   状态: {status}")
            print(f"   命令: {command}")
            print(f"   参数: {' '.join(args)}")
            
            # 检查环境变量
            env = config.get('env', {})
            if env:
                print(f"   环境变量:")
                for key, value in env.items():
                    if value:
                        print(f"     {key}: ✅ 已设置")
                    else:
                        print(f"     {key}: ❌ 未设置")
    
    def test_prerequisites(self):
        """测试前置条件"""
        print("\n🔍 检查前置条件:")
        print("=" * 30)
        
        # 检查Node.js
        try:
            result = subprocess.run(['node', '--version'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ Node.js: {result.stdout.strip()}")
            else:
                print("❌ Node.js未安装或有问题")
        except FileNotFoundError:
            print("❌ Node.js未安装")
        
        # 检查npm
        try:
            result = subprocess.run(['npm', '--version'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ npm: {result.stdout.strip()}")
            else:
                print("❌ npm未安装或有问题")
        except FileNotFoundError:
            print("❌ npm未安装")
        
        # 检查npx
        try:
            result = subprocess.run(['npx', '--version'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ npx: {result.stdout.strip()}")
            else:
                print("❌ npx未安装或有问题")
        except FileNotFoundError:
            print("❌ npx未安装")
    
    def test_filesystem_functions(self):
        """测试文件系统功能"""
        print("\n📁 文件系统功能测试:")
        print("=" * 35)
        
        current_dir = Path.cwd()
        print(f"📂 当前目录: {current_dir}")
        
        # 列出文件
        files = list(current_dir.glob("*"))
        print(f"📄 文件总数: {len(files)}")
        
        print("📋 文件列表 (前10个):")
        for i, file in enumerate(files[:10]):
            if file.is_file():
                size = file.stat().st_size
                print(f"   {i+1:2}. 📄 {file.name} ({size} bytes)")
            elif file.is_dir():
                print(f"   {i+1:2}. 📁 {file.name}/")
    
    def test_git_functions(self):
        """测试Git功能"""
        print("\n🔀 Git功能测试:")
        print("=" * 25)
        
        try:
            # 检查是否是Git仓库
            result = subprocess.run(['git', 'rev-parse', '--is-inside-work-tree'], 
                                  capture_output=True, text=True, cwd='.')
            
            if result.returncode != 0:
                print("❌ 当前目录不是Git仓库")
                return
            
            print("✅ 当前目录是Git仓库")
            
            # 检查Git状态
            result = subprocess.run(['git', 'status', '--porcelain'], 
                                  capture_output=True, text=True, cwd='.')
            
            if result.stdout.strip():
                print("📝 Git状态 - 有未提交的更改:")
                for line in result.stdout.strip().split('\n')[:5]:
                    print(f"     {line}")
            else:
                print("✅ Git状态 - 工作目录干净")
            
            # 显示最近的提交
            result = subprocess.run(['git', 'log', '--oneline', '-3'], 
                                  capture_output=True, text=True, cwd='.')
            if result.returncode == 0 and result.stdout.strip():
                print("📋 最近的提交:")
                for line in result.stdout.strip().split('\n'):
                    print(f"     {line}")
            
        except FileNotFoundError:
            print("❌ Git未安装")
        except Exception as e:
            print(f"❌ Git操作失败: {e}")
    
    def simulate_context7(self):
        """模拟Context7功能"""
        print("\n🚀 Context7功能模拟:")
        print("=" * 30)
        
        # 模拟技术栈检测
        tech_stack = []
        
        # 检查项目文件
        if Path('package.json').exists():
            tech_stack.append("Node.js/JavaScript")
        if Path('requirements.txt').exists():
            tech_stack.append("Python")
        if Path('index.html').exists():
            tech_stack.append("HTML/CSS")
        if Path('tailwind.config.js').exists():
            tech_stack.append("Tailwind CSS")
        if any(Path('.').glob('*.tsx')):
            tech_stack.append("TypeScript/React")
        
        if tech_stack:
            print("🔍 检测到的技术栈:")
            for tech in tech_stack:
                print(f"     ✅ {tech}")
        else:
            print("🔍 未检测到特定技术栈")
        
        # 模拟最新文档
        print("\n📚 模拟最新文档:")
        sample_docs = {
            "React": "React 18.2 - 并发特性、Suspense改进",
            "Next.js": "Next.js 15.0 - App Router、Turbopack",
            "Tailwind": "Tailwind CSS 3.4 - 容器查询、动态视口",
            "TypeScript": "TypeScript 5.3 - 导入属性、switch(true)"
        }
        
        for tech, desc in sample_docs.items():
            print(f"     📖 {tech}: {desc}")
    
    def interactive_demo(self):
        """交互式演示"""
        print("\n🎯 交互式演示模式")
        print("=" * 25)
        print("输入 'help' 查看可用命令，'quit' 退出")
        
        while True:
            try:
                command = input("\n💬 输入命令: ").strip().lower()
                
                if command in ['quit', 'exit', 'q']:
                    print("👋 再见!")
                    break
                elif command == 'help':
                    self.show_help()
                elif command == 'config':
                    self.show_config()
                elif command == 'check':
                    self.test_prerequisites()
                elif command == 'fs':
                    self.test_filesystem_functions()
                elif command == 'git':
                    self.test_git_functions()
                elif command == 'context7':
                    self.simulate_context7()
                elif command.startswith('use context7'):
                    query = command.replace('use context7', '').strip()
                    self.simulate_context7_query(query)
                else:
                    print("❓ 未知命令，输入 'help' 查看帮助")
                    
            except KeyboardInterrupt:
                print("\n👋 再见!")
                break
            except Exception as e:
                print(f"❌ 执行命令时出错: {e}")
    
    def show_help(self):
        """显示帮助"""
        print("""
🔧 可用命令:
   help     - 显示此帮助
   config   - 显示MCP配置
   check    - 检查前置条件
   fs       - 测试文件系统功能
   git      - 测试Git功能
   context7 - 模拟Context7功能
   use context7 [query] - 模拟Context7查询
   quit/exit/q - 退出程序
        """)
    
    def simulate_context7_query(self, query: str):
        """模拟Context7查询"""
        if not query:
            query = "通用查询"
        
        print(f"\n🔍 Context7查询: {query}")
        print("📝 模拟响应:")
        
        # 根据查询提供模拟响应
        if any(keyword in query.lower() for keyword in ['blog', '博客', 'website', '网站']):
            print("""
✨ 个人博客网站建议:
- 使用Next.js 15 + App Router
- 集成MDX用于文章编写
- 使用Tailwind CSS进行样式设计
- 添加语法高亮支持
- 实现标签和搜索功能

示例文件结构:
```
blog/
├── app/
│   ├── blog/
│   │   └── [slug]/
│   └── page.tsx
├── content/
│   └── posts/
└── components/
    └── MDXComponents.tsx
```
            """)
        elif any(keyword in query.lower() for keyword in ['next.js', 'nextjs']):
            print("""
✨ Next.js 15.0 最新特性:
- 改进的App Router性能
- Turbopack支持
- 更好的服务端组件
- 优化的图像处理

创建项目:
```bash
npx create-next-app@latest my-blog --typescript --tailwind --app
```
            """)
        else:
            print(f"📚 为查询 '{query}' 提供相关的最新技术文档...")


def main():
    """主函数"""
    print("🎯 简化版MCP测试程序")
    print("作者: Tian Sports Sciences")
    print("用途: 测试MCP配置和模拟功能")
    print("=" * 50)
    
    # 创建测试器
    tester = SimpleMCPTester()
    
    # 加载配置
    print("📋 加载MCP配置...")
    if not tester.load_config():
        print("⚠️  无法加载配置，但可以继续测试其他功能")
    else:
        print(f"✅ 成功加载 {len(tester.config)} 个MCP服务器配置")
    
    # 显示配置
    tester.show_config()
    
    # 测试前置条件
    tester.test_prerequisites()
    
    # 测试基本功能
    tester.test_filesystem_functions()
    tester.test_git_functions()
    tester.simulate_context7()
    
    # 进入交互模式
    tester.interactive_demo()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 程序被用户中断")
    except Exception as e:
        print(f"\n❌ 程序运行出错: {e}")
        sys.exit(1) 