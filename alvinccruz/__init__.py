from flask import Flask

from . import home_page


BP_GROUPS = [
    home_page,
]


def create_app():
    app = Flask(__name__)
    for bp_group in BP_GROUPS:
        for module in dir(bp_group):
            obj = getattr(bp_group, module)
            if hasattr(obj, "bp"):
                bp = getattr(obj, "bp")
                app.register_blueprint(bp)

    return app


