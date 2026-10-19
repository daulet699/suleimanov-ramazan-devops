import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

def student_info():
    return {
        "name": os.getenv("STUDENT_NAME", "Ramazan"),
        "surname": os.getenv("STUDENT_SURNAME", "Suleimanov"),
        "group": os.getenv("STUDENT_GROUP", "IT2-2308"),
        "student_id": os.getenv("STUDENT_ID", "37408"),
        "course": "DevOps"
    }

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/student"):
            data = student_info()
            status = 200
        elif self.path == "/health":
            data = {"status": "ok"}
            status = 200
        else:
            data = {"error": "Not found"}
            status = 404

        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8086"))
    print("DevOps Student Application", flush=True)
    print(student_info(), flush=True)
    print(f"Server running on port {port}", flush=True)
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()
