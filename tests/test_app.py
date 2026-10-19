import os
import unittest
import json
from threading import Thread
from http.client import HTTPConnection
from unittest.mock import patch
from http.server import ThreadingHTTPServer
from app.main import Handler, student_info

class TestStudent(unittest.TestCase):
    def test_name(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(student_info()["name"], "Ramazan")

    def test_surname(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(student_info()["surname"], "Suleimanov")

    def test_group(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(student_info()["group"], "IT2-2308")

    def test_student_id(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(student_info()["student_id"], "37408")

    def test_environment(self):
        with patch.dict(os.environ, {"STUDENT_NAME": "TestUser"}):
            self.assertEqual(student_info()["name"], "TestUser")

    def test_health(self):
        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            port = server.server_address[1]
            conn = HTTPConnection("127.0.0.1", port, timeout=5)
            conn.request("GET", "/health")
            response = conn.getresponse()
            data = json.loads(response.read())
            self.assertEqual(response.status, 200)
            self.assertEqual(data["status"], "ok")
            conn.close()
        finally:
            server.shutdown()
            server.server_close()
            thread.join()

if __name__ == "__main__":
    unittest.main()
