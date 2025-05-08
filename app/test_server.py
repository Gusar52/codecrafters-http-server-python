import unittest
import requests
import os
import threading
import time
from app.main import main

class TestHTTPServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_thread = threading.Thread(target=main)
        cls.server_thread.daemon = True
        cls.server_thread.start()
        time.sleep(0.5)

    def test_root_path(self):
        response = requests.get("http://localhost:4221/")
        self.assertEqual(response.status_code, 200)

    def test_echo_endpoint(self):
        test_string = "hello-world"
        response = requests.get(f"http://localhost:4221/echo/{test_string}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text.strip(), test_string)

    def test_user_agent(self):
        test_agent = "MyTestAgent/1.0"
        response = requests.get(
            "http://localhost:4221/user-agent",
            headers={"User-Agent": test_agent}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, test_agent)

    def test_file_operations(self):
        test_content = "Test file content"
        response = requests.post(
            "http://localhost:4221/files/testfile.txt",
            data=test_content
        )
        self.assertEqual(response.status_code, 201)
    
        response = requests.get("http://localhost:4221/files/testfile.txt")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, test_content)

        if os.path.exists("./testfile.txt"):
            os.remove("./testfile.txt")

if __name__ == "__main__":
    unittest.main()