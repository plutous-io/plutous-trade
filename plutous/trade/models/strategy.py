from sqlalchemy.orm import Mapped

from plutous.trade.enums import StrategyType

from .base import Base


class Strategy(Base):
    name: Mapped[str]
    description: Mapped[str]
    type: Mapped[StrategyType]
    allocated_capital: Mapped[float]
