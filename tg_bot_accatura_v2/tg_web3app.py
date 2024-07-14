# tg_web3app.py

from http.server import HTTPServer, BaseHTTPRequestHandler

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print('self')

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(("html_content + add_html_content").encode('utf-8'))
        # return 're'

if __name__ == '__main__':
    print('Второй файл запущен')
    server_address = ('', 8080)
    server = HTTPServer(server_address, requestHandler)
    server.serve_forever()