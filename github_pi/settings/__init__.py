
try:
    from .local import *
except ImportError:
    pass


PACKAGES = {
    "tqdm": "tqdm/tqdm",
    "flask": "pallets/flask",
}
