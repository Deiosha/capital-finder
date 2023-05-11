from http.server import BaseHTTPRequestHandler, HTTPServer
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

        if 'country' in dictionary:
            country = dictionary['country']
            dictionary_api_url = f"https://restcountries.com/v3.1/name/{country}"
            response = requests.get(dictionary_api_url)
            data = response.json()
            capital = data[0]['capital'][0]
            message = f"The capital of {country} is {capital}"
        elif 'capital' in dictionary:
            capital = dictionary['capital']
            dictionary_api_url = f"https://restcountries.com/v3.1/capital/{capital}"
            response = requests.get(dictionary_api_url)
            data = response.json()
            country = data[0]['name']['common']
            message = f"{capital} is the capital of {country}"
        else:
            message = "Please enter a country OR capital. Thank you!"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

if __name__ == '__main__':
    server_address = ('localhost', 8000)  # use any available port
    httpd = HTTPServer(server_address, handler)  # httpd is a commonly used abbreviation for "HTTP Daemon"
    print(f'Starting httpd server on {server_address[0]}:{server_address[1]}')
    httpd.serve_forever()
