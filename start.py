# 本機啟動：在這個資料夾開靜態伺服器（只綁 127.0.0.1，不連外），並用預設瀏覽器開啟 index.html
import http.server, socketserver, webbrowser, os, threading

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


socketserver.TCPServer.allow_reuse_address = True
srv = None
for port in range(8080, 8100):
    try:
        srv = socketserver.TCPServer(("127.0.0.1", port), Handler)
        break
    except OSError:
        continue
if srv is None:
    raise SystemExit("8080-8099 埠都被占用，請關掉其他程式後再試")

url = "http://127.0.0.1:%d/index.html" % port
print("G-EIGHT 2026 展場地圖（加強版）：" + url)
print("關閉這個視窗即停止。")
threading.Timer(0.6, lambda: webbrowser.open(url)).start()
try:
    srv.serve_forever()
except KeyboardInterrupt:
    pass
