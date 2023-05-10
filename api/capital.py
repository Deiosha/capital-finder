from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # url string
        url = self.path
        # taking in the url to split
        url_components = parse.urlsplit(url)
        # creating a list with the values representing the query string
        query_string_list = parse.parse_qsl(url_components.query)
        # creating a dict object, contents are taken from query_string_list
        dictionary = dict(query_string_list)


# creating response
        message = "Working"
#       passing the code
        self.send_response(200)
#       content type
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        # to write the message
        self.wfile.write(message.encode())

if __name__ == '__main__':
    server_address = ('localhost', 8000)  # use any available port
    httpd = HTTPServer(server_address, handler)  # httpd is a commonly used abbreviation for "HTTP Daemon"
    print(f'Starting httpd server on {server_address[0]}:{server_address[1]}')
    httpd.serve_forever()