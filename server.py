# 光伏遮阳系统控制端 服务器启动文件
import http.server
import socketserver

# 定义服务器端口（8888可以改成其他数字，比如9999）
PORT = 8888

# 配置服务器，让它能访问我们的网页
Handler = http.server.SimpleHTTPRequestHandler

# 启动服务器
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("✅ 服务器启动成功！")
    print(f"🌐 请在浏览器输入：http://127.0.0.1:{PORT}")
    print("🛑 按 Ctrl+C 可以停止服务器")
    httpd.serve_forever()