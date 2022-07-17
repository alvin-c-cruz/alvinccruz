from flask import Blueprint, render_template, g, url_for
from flask_login import login_required

from alvinccruz.nav_object import Navigation


bp = Blueprint("index", __name__, template_folder="pages", url_prefix="/home")


@bp.route("/")
@login_required
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
