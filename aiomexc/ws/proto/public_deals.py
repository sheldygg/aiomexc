from dataclasses import dataclass, field
from typing import Annotated, List

from pure_protobuf.annotations import Field
from pure_protobuf.message import BaseMessage


@dataclass
class PublicDealsMessageItem(BaseMessage):
    price: Annotated[str, Field(1)] = ""
    quantity: Annotated[str, Field(2)] = ""
    trade_type: Annotated[int, Field(3)] = 0
    time: Annotated[int, Field(4)] = 0


@dataclass
class PublicDealsMessage(BaseMessage):
    deals: Annotated[List[PublicDealsMessageItem], Field(1)] = field(
        default_factory=list
    )
    event_type: Annotated[str, Field(2)] = ""
