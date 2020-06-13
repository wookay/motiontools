import pkg_resources
__version__ = pkg_resources.require("motiontools")[0].version

from .motiontools import *
from .base import *
