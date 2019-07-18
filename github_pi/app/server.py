from pathlib import Path

from bottle import route, TEMPLATE_PATH, view, abort

from .utils import normalize

from .. import settings
from ..github_storage.assets import get_assets

TEMPLATE_PATH.append(Path(__file__) / ".." / "views")


@route("/")
@view("index.tpl")
def index():
    return {'packages': list(map(normalize, settings.PACKAGES))}


@route("/<package_name>/")
@view("package.tpl")
def package(package_name):
    try:
        repo_name = settings.PACKAGES[package_name]
    except KeyError:
        abort(404)
    assets = dict(get_assets(repo_name))
    return {"assets": assets, 'package_name': package_name}


def package_redirect():
    # todo
    pass
