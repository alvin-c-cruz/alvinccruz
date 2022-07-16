from flask import Blueprint, render_template, url_for, g

from alvinccruz.nav_object import Navigation

bp = Blueprint("home_page", __name__, template_folder="pages")


@bp.route("/")
def home():
    return render_template("landing_page/home.html")


@bp.before_app_request
def navigation():
    if "nav" not in g:
        g.nav = {}

    g.nav["landing_page"] = Navigation(
        label="",
        route=url_for("home_page.home")
    )


