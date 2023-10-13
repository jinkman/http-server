from http.server import HTTPServer, BaseHTTPRequestHandler


# 处理实例
class Request(BaseHTTPRequestHandler):

    # get
    def do_GET(self):
        self.send_response(200)
        self.end_headers() 
        
        msg = 'get success!' # 返回信息
        if self.path == '/hi':
            msg = 'hi'

        msg = str(msg).encode() #转为str再转为byte格式
        self.wfile.write(msg) # 返回客户端

    def do_POST(self):
        data = self.rfile.read(int(self.headers['content-length'])) #获取从客户端传入的参数（byte格式）
        data =  data.decode() #将byte格式转为str格式

        self.send_response(200)
        self.end_headers()

        msg = f'post success! data: {data}'
        msg = str(msg).encode()
        self.wfile.write(msg) # 返回给客户端


if __name__=='__main__':
    host = ('localhost',8080)
    server = HTTPServer(host, Request)
    server.serve_forever() #开启服务