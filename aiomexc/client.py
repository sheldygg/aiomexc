from decimal import Decimal

from aiomexc.methods import (
    GetTickerPrice,
    GetAccountInformation,
    QueryOrder,
    MexcMethod,
    CreateListenKey,
    GetListenKeys,
    ExtendListenKey,
    DeleteListenKey,
    GetOpenOrders,
    CreateOrder,
    CancelOrder,
    GetUID,
)
from aiomexc.enums import OrderSide, OrderType
from aiomexc.types import (
    TickerPrice,
    AccountInformation,
    Order,
    MexcType,
    ListenKey,
    ListenKeys,
    CreatedOrder,
    CanceledOrder,
    UID,
)

from .session.base import BaseSession, Credentials
from .session.aiohttp import AiohttpSession


class MexcClient:
    def __init__(
        self, credentials: Credentials | None = None, session: BaseSession | None = None
    ):
        if session is None:
            session = AiohttpSession()

        self.session = session
        self.credentials = credentials

    async def __call__(
        self,
        method: MexcMethod[MexcType],
        credentials: Credentials | None = None,
        timeout: float | None = None,
    ) -> MexcType:
        return await self.session.request(
            method, credentials or self.credentials, timeout=timeout
        )

    async def get_ticker_price(self, symbol: str) -> TickerPrice:
        return await self(GetTickerPrice(symbol=symbol))

    async def get_account_information(
        self, credentials: Credentials | None = None, timeout: float | None = None
    ) -> AccountInformation:
        return await self(
            GetAccountInformation(), credentials=credentials, timeout=timeout
        )

    async def query_order(
        self,
        symbol: str,
        order_id: str | None = None,
        orig_client_order_id: str | None = None,
        credentials: Credentials | None = None,
        timeout: float | None = None,
    ) -> Order:
        return await self(
            QueryOrder(
                symbol=symbol,
                order_id=order_id,
                orig_client_order_id=orig_client_order_id,
            ),
            credentials=credentials,
            timeout=timeout,
        )

    async def create_listen_key(
        self, credentials: Credentials | None = None, timeout: float | None = None
    ) -> ListenKey:
        return await self(CreateListenKey(), credentials=credentials, timeout=timeout)

    async def get_listen_keys(
        self, credentials: Credentials | None = None, timeout: float | None = None
    ) -> ListenKeys:
        return await self(GetListenKeys(), credentials=credentials, timeout=timeout)

    async def extend_listen_key(
        self,
        listen_key: str,
        credentials: Credentials | None = None,
        timeout: float | None = None,
    ) -> ListenKey:
        return await self(
            ExtendListenKey(listen_key=listen_key),
            credentials=credentials,
            timeout=timeout,
        )

    async def delete_listen_key(
        self,
        listen_key: str,
        credentials: Credentials | None = None,
        timeout: float | None = None,
    ) -> ListenKey:
        return await self(
            DeleteListenKey(listen_key=listen_key),
            credentials=credentials,
            timeout=timeout,
        )

    async def get_open_orders(
        self,
        symbol: str,
        credentials: Credentials | None = None,
        timeout: float | None = None,
    ) -> list[Order]:
        return await self(
            GetOpenOrders(symbol=symbol), credentials=credentials, timeout=timeout
        )

    async def create_order(
        self,
        symbol: str,
        side: OrderSide,
        type: OrderType,
        quantity: Decimal | None = None,
        quote_order_qty: Decimal | None = None,
        price: Decimal | None = None,
        new_client_order_id: str | None = None,
        credentials: Credentials | None = None,
        timeout: float | None = None,
    ) -> CreatedOrder:
        return await self(
            CreateOrder(
                symbol=symbol,
                side=side,
                type=type,
                quantity=quantity,
                quote_order_qty=quote_order_qty,
                price=price,
                new_client_order_id=new_client_order_id,
            ),
            credentials=credentials,
            timeout=timeout,
        )

    async def cancel_order(
        self,
        symbol: str,
        order_id: str | None = None,
        orig_client_order_id: str | None = None,
        new_client_order_id: str | None = None,
        credentials: Credentials | None = None,
        timeout: float | None = None,
    ) -> CanceledOrder:
        return await self(
            CancelOrder(
                symbol=symbol,
                order_id=order_id,
                orig_client_order_id=orig_client_order_id,
                new_client_order_id=new_client_order_id,
            ),
            credentials=credentials,
            timeout=timeout,
        )

    async def get_uid(
        self, credentials: Credentials | None = None, timeout: float | None = None
    ) -> UID:
        return await self(GetUID(), credentials=credentials, timeout=timeout)
