from .base_settings import *

try:
    from .local_settings import *
except ModuleNotFoundError:
    pass
