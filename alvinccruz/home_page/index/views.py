from flask import Blueprint, render_template, g, url_for

from alvinccruz.nav_object import Navigation


bp = Blueprint("index", __name__, template_folder="pages", url_prefix="/home")


@bp.route("/")
def home():
    return render_template("index/home.html")


@bp.before_app_request
def navigation():
    if "nav" not in g:
        g.nav = {}

    g.nav["index"] = Navigation(
        label="Home",
        route=url_for("index.home")
    )
