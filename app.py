import os
import unittest

from flask import Flask, jsonify, url_for
from flask_reverse_proxy_fix.middleware import ReverseProxyPrefixFix


def create_app_with_middleware():
    app = Flask(__name__)

    # Configure and load Middleware
    app.config['REVERSE_PROXY_PATH'] = '/test'
    ReverseProxyPrefixFix(app)

    # Support running integration tests
    @app.cli.command()
    def test():
        """Run integration tests."""
        tests = unittest.TestLoader().discover(os.path.join(os.path.dirname(__file__), 'tests'))
        unittest.TextTestRunner(verbosity=2).run(tests)

    @app.route("/sample")
    def sample():
        payload = {
            'links': {
                'self': url_for('.sample', _external=True)
            }
        }

        return jsonify(payload)

    return app


def create_app_without_middleware():
    app = Flask(__name__)

    # Support running integration tests
    @app.cli.command()
    def test():
        """Run integration tests."""
        tests = unittest.TestLoader().discover(os.path.join(os.path.dirname(__file__), 'tests'))
        unittest.TextTestRunner(verbosity=2).run(tests)

    @app.route("/sample")
    def sample():
        payload = {
            'links': {
                'self': url_for('.sample', _external=True)
            }
        }

        return jsonify(payload)

    return app


if __name__ == "__main__":
    test_app = create_app_with_middleware()

    # Support PyCharm debugging
    if 'PYCHARM_HOSTED' in os.environ:
        # Exempting Bandit security issue (binding to all network interfaces)
        #
        # All interfaces option used because the network available within the container can vary across providers
        # This is only used when debugging with PyCharm. A standalone web server is used in production.
        test_app.run(host='0.0.0.0', port=9000, debug=True, use_debugger=False, use_reloader=False)  # nosec
