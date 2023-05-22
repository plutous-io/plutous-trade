from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from plutous.enums import Exchange
from plutous.trade.enums import Action, AssetType, PositionSide

from .base import Base, Enum
from .position import Position


class Trade(Base):
    identifier: Mapped[str]
    symbol: Mapped[str]
    exchange: Mapped[Exchange] = mapped_column(Enum(Exchange, schema="public"))
    asset_type: Mapped[AssetType] = mapped_column(Enum(AssetType))
    action: Mapped[Action] = mapped_column(Enum(Action))
    side: Mapped[PositionSide] = mapped_column(Enum(PositionSide))
    price: Mapped[float]
    quantity: Mapped[float]
    position_id: Mapped[int] = mapped_column(ForeignKey(Position.id))

    position: Mapped[Position] = relationship(Position, back_populates="trades")

    @property
    def bot(self):
        return self.position.bot
