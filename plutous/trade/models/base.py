from sqlalchemy.orm import DeclarativeBase

from plutous.models import BaseMixin


class Base(DeclarativeBase, BaseMixin):
    __table_args__ = ({"schema": "trade"},)
