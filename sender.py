import http.server
import socketserver
import socket

def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

def start_server(port, file_path):
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving file at http://{get_ip_address()}:{port}")
        httpd.serve_forever()

# Example usage
start_server(33455, "C:/Users/natha/OneDrive/Desktop/AB-332.docx")

