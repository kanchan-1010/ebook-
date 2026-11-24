import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    os.chdir(DIRECTORY)
    # Check if port is already open or find next available port
    port = PORT
    httpd = None
    while port < 8010:
        try:
            httpd = socketserver.TCPServer(("", port), Handler)
            break
        except OSError:
            port += 1
            
    if not httpd:
        print("Could not bind to ports 8000-8010.")
        sys.exit(1)
        
    url = f"http://localhost:{port}/index.html"
    print("=" * 60)
    print(f"  DEAR 2027, I'M READY - LOCAL PREVIEW SERVER")
    print(f"  Live URL: {url}")
    print("  Serving workspace: " + DIRECTORY)
    print("  Press Ctrl+C to stop the server.")
    print("=" * 60)
    
    webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()

if __name__ == "__main__":
    start_server()
