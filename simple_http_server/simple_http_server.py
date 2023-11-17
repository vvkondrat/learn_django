from http.server import HTTPServer, BaseHTTPRequestHandler

# указывает на каком хосту запускается наш веб-сервер
APP_HOST = 'localhost'
# указывает на каком порту будет работать на веб-сервер
APP_PORT = 8000

class SimpleGetHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf8")
        self.end_headers()

    def _html(self, message):
        content = (f"<html>"
                   f"<body>"
                   f"<h1>{message}</h1>"
                   f"</body>"
                   f"</html>")
        return content.encode("utf8")
    

    def do_GET(self):
        # указываем какие заголовки должны быть в нашем запросе
        self._set_headers()
        message = "Привет, мир!"
        # преобразуем message в html код, преобразуем в ответ и отправляем клиенту
        self.wfile.write(self._html(message))


# в аргументах указываем класс сервера и обработчик для наших GET запросов
def run_server(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = (APP_HOST, APP_PORT)
    # инициализируется сервер
    httpd = server_class(server_address, handler_class)
    # указываем, что сервер необходимо хранить вечно (пока не упадет из-за ошибки)
    httpd.serve_forever()

# запуск сервера
if __name__ == "__main__":
    run_server(handler_class=SimpleGetHandler)