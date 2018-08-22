from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os
from cowpy import cow
import json
from textwrap import dedent

# os.environ is like process.env


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        # set a status code
        # set any headers
        # set any body data on the response
        # end headers

        if parsed_path.path == '/':

            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            html = dedent('''
        <html>
        <head>
            <title> cowsay </title>
        </head>
        <body>
            <header>
                <nav>
                <ul>
                    <li><a href="/cow">cowsay</a></li>
                </ul>
                </nav>
            <header>
            <main>
            </main>
        </body>
        </html>''')
            self.wfile.write(html.encode())
            return

        elif parsed_path.path == '/cow':
            try:
                buttcow = cow.Stegosaurus()
                msg = buttcow.milk(parsed_qs['msg'][0])
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(msg.encode())
                return
            except KeyError:
                self.send400()
        else:
            self.send_response(404)
            self.end_headers()
            buttcow = cow.Ghostbusters()
            msg = buttcow.milk('404 ERROR!!! NOT FOUND!!!!')
            self.wfile.write(msg.encode())

    def do_POST(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/cow':

            try:
                buttcow = cow.Stegosaurus()
                msg = buttcow.milk(parsed_qs['msg'][0])
                msg_json = json.dumps({'content': msg})
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                print(msg_json)
                self.wfile.write(msg_json.encode())
                return

            except KeyError:
                self.send400()
        else:
            self.send_response(404)
            self.end_headers()
            buttcow = cow.Ghostbusters()
            msg = buttcow.milk('404 ERROR!!! NOT FOUND!!!!')
            self.wfile.write(msg.encode())

    def send400(self):
        self.send_response(400)
        self.end_headers()
        buttcow = cow.Sodomized()
        msg = buttcow.milk('400 ERROR!!! BAD REQUEST!!!')
        self.wfile.write(msg.encode())


def create_server():
    return HTTPServer(
        ('127.0.0.1', int(os.environ['PORT'])),
        SimpleHTTPRequestHandler
    )


def run_forever():
    server = create_server()

    try:
        print(f'Server running on {os.environ["PORT"]}')
        server.serve_forever()


    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    run_forever()
