from flask import Flask, request, redirect, url_for
from flask_login import LoginManager
from http import HTTPStatus

from . import home_page
from . import book_shelf

BP_GROUPS = [
    home_page,
    book_shelf
]


def create_app():
    app = Flask(__name__)
    for bp_group in BP_GROUPS:
        for module in dir(bp_group):
            obj = getattr(bp_group, module)
            if hasattr(obj, "bp"):
                bp = getattr(obj, "bp")
                app.register_blueprint(bp)

    login_manager = LoginManager(app)

    @login_manager.user_loader
    def load_user(user_id):
        return user_id

    @login_manager.unauthorized_handler
    def unauthorized():
        if request.blueprint == 'api':
            abort(HTTPStatus.UNAUTHORIZED)
        return redirect(url_for('landing_page.home'))

    return app


