import unittest
from http import HTTPStatus

from flask_reverse_proxy_fix.middleware import ReverseProxyPrefixFix
from app import create_app_with_middleware, create_app_without_middleware


class FlaskReverseProxyMiddlewarePathPrefixTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        self.app_context.pop()

    def test_with_prefix(self):
        self.app = create_app_with_middleware()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        self.app.config['REVERSE_PROXY_PATH'] = '/foo'
        ReverseProxyPrefixFix(self.app)

        expected_url = 'http://localhost:9000/test/sample'

        response = self.client.get(
            '/sample',
            base_url='http://localhost:9000'
        )
        json_response = response.get_json()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn('links', json_response.keys())
        self.assertIn('self', json_response['links'].keys())
        self.assertEqual(expected_url, json_response['links']['self'])

    def test_without_prefix(self):
        self.app = create_app_without_middleware()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        expected_url = 'http://localhost:9000/sample'

        response = self.client.get(
            '/sample',
            base_url='http://localhost:9000'
        )
        json_response = response.get_json()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn('links', json_response.keys())
        self.assertIn('self', json_response['links'].keys())
        self.assertEqual(expected_url, json_response['links']['self'])
