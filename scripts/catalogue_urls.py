"""Generate repository URLs for catalogue model assets."""
from urllib.parse import quote

RAW_BASE = "https://raw.githubusercontent.com/leomrocha/cad-models/master/"
FOLDER_BASE = "https://github.com/leomrocha/cad-models/tree/master/"


def repository_path(path):
    return quote(f"data/packages/{path.as_posix()}", safe="/")
