from flask import Blueprint,render_template, url_for, g

from alvinccruz.nav_object import Navigation


bp = Blueprint("basic_python", __name__, template_folder="pages", url_prefix="/basicpython")

CONTEXT = {
        "shelf": "basic_python",
    }


@bp.route("/")
def home():
    return render_template("basic_python/home.html", **CONTEXT)


@bp.route("/history")
def history():
    return render_template("basic_python/history.html", **CONTEXT)


@bp.before_app_request
def navigation():
    if "nav" not in g:
        g.nav = {}

    if "book_shelf" not in g.nav:
        g.nav["book_shelf"] = {}

    g.nav["book_shelf"]["basic_python"] = navs()


def navs():
    nav = Navigation(
        label="Python",
        route=url_for("basic_python.home")
    )

    nav.sub_nav.append(
        Navigation(
            label="History",
            route=url_for("basic_python.history")
        )
    )

    return nav
