from dataclasses import dataclass
from http import HTTPMethod

from aiomexc.types import UID
from .base import MexcMethod


@dataclass(kw_only=True)
class GetUID(MexcMethod):
    __returning__ = UID
    __api_http_method__ = HTTPMethod.GET
    __api_method__ = "uid"
    __requires_auth__ = True
