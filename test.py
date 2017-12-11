from flask import Flask
import unittest
from datetime import datetime

from main import app

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

    def test_uploader_status_code(self):
        result = self.app.get('/uploader')
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
