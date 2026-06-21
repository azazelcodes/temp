from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import json
import mimetypes
from webbrowser import open

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = Path(self.translate_path(self.path))

        if path.is_dir():
            if Path(path).resolve() == Path(".").resolve():
                return super().do_GET()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            contents = [
                {
                    "name": p.name,
                    "type": "directory" if p.is_dir() else mimetypes.guess_type(p.name)[0] or "application/octet-stream"
                }
                for p in path.iterdir()
            ]

            self.wfile.write(json.dumps(contents).encode())
            return

        if path.is_file():
            return super().do_GET()

        self.send_error(404, "Not found")

    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

mimetypes.add_type("application/wasm", ".wasm")
open("http://localhost:8000")
HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
