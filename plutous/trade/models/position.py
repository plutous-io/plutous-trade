from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from plutous.trade.enums import AssetType, Exchange, PositionSide

from .base import Base, Enum
from .bot import Bot

if TYPE_CHECKING:
    from .trade import Trade


class Position(Base):
    asset_type: Mapped[AssetType] = mapped_column(Enum(AssetType))
    exchange: Mapped[Exchange] = mapped_column(Enum(Exchange))
    symbol: Mapped[str]
    side: Mapped[PositionSide] = mapped_column(Enum(PositionSide))
    quantity: Mapped[float]
    opened_at: Mapped[datetime]
    closed_at: Mapped[datetime]
    bot_id: Mapped[int] = mapped_column(ForeignKey(Bot.id))

    bot: Mapped[Bot] = relationship(Bot, back_populates="positions")
    trades: Mapped[list["Trade"]] = relationship("Trade", back_populates="position")
