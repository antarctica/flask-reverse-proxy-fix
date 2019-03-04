from flask import Flask, jsonify, url_for
from flask_reverse_proxy_fix.middleware import ReverseProxyPrefixFix


def create_app_with_middleware():
    app = Flask(__name__)

    # Configure and load Middleware
    app.config['REVERSE_PROXY_PATH'] = '/test'
    ReverseProxyPrefixFix(app)

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

    @app.route("/sample")
    def sample():
        payload = {
            'links': {
                'self': url_for('.sample', _external=True)
            }
        }

        return jsonify(payload)

    return app
