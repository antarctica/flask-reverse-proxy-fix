import os
import unittest

from flask import Flask, jsonify, url_for
# noinspection PyPackageRequirements
from werkzeug.contrib.fixers import ProxyFix
from flask_reverse_proxy_fix.middleware import ReverseProxyPrefixFix


def create_app_with_middleware():
    _app = Flask(__name__)

    # Configure and load Middleware
    _app.config['REVERSE_PROXY_PATH'] = '/test'
    _app.wsgi_app = ProxyFix(_app.wsgi_app)
    _app.wsgi_app = ReverseProxyPrefixFix(_app.wsgi_app, _app.config['REVERSE_PROXY_PATH'])

    @_app.route("/sample")
    def sample():
        payload = {
            'links': {
                'self': url_for('.sample', _external=True)
            }
        }

        return jsonify(payload)

    return _app


def create_app_without_middleware():
    _app = Flask(__name__)

    @_app.route("/sample")
    def sample():
        payload = {
            'links': {
                'self': url_for('.sample', _external=True)
            }
        }

        return jsonify(payload)

    return _app


app = create_app_with_middleware()


# Support PyCharm debugging
if 'PYCHARM_HOSTED' in os.environ:
    # Exempting Bandit security issue (binding to all network interfaces)
    #
    # All interfaces option used because the network available within the container can vary across providers
    # This is only used when debugging with PyCharm. A standalone web server is used in production.
    app.run(host='0.0.0.0', port=9000, debug=True, use_debugger=False, use_reloader=False)  # nosec


# Support running integration tests
@app.cli.command()
def test():
    """Run integration tests."""
    tests = unittest.TestLoader().discover(os.path.join(os.path.dirname(__file__), 'tests'))
    unittest.TextTestRunner(verbosity=2).run(tests)
