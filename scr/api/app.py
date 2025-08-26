"""
This file contains all the stuff for api with flask.
"""

from flask import Flask
from scr.api.routes.math_routes import bp as math_routes
from scr.mathlib import MathError

def create_app():
    app = Flask(__name__)

    # Register all blueprints (routes)
    app.register_blueprint(math_routes, url_prefix="/math")

    @app.errorhandler(MathError)
    def handle_math_error(error):
        return {
            "error": str(error),
            "code": error.__class__.__name__.upper()
        }, 400

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

