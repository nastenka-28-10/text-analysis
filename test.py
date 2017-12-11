from flask import Flask
import unittest
from datetime import datetime

from main import app
from io import BytesIO

class FlaskTest(unittest.TestCase):

    def setUp(self):
        """Set up test application client"""
        self.app = app.test_client() 
        self.app.testing = True

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_home_page_status_code(self):
        result = self.app.get('/home')
        self.assertEqual(result.status_code, 200)

    def test_contact_status_code(self):
        result = self.app.get('/contact')
        self.assertEqual(result.status_code, 200)

    def test_about_status_code(self):
        result = self.app.get('/about')
        self.assertEqual(result.status_code, 200)

    def test_post_upload_request(self):
        """Assert that user is redirected with status 302 after creating a todo item"""
        data = dict(
            file=(BytesIO(b'uploading .txt file'), "file.txt")
        )
        response = self.app.post('/uploader', content_type='multipart/form-data',data=data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
