"""init

Revision ID: 3e037c0f4152
Revises: 
Create Date: 2023-05-23 03:57:18.342515

"""

import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "f5b96a26834a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    exchange_enum = sa.Enum(
        "BINANCE",
        "BINANCE_COINM",
        "BINANCE_USDM",
        "BITGET",
        "BYBIT",
        "GATEIO",
        "HUOBI",
        "HYPERLIQUID",
        "KUCOIN",
        "KUCOIN_FUTURES",
        "OKX",
        "PHEMEX",
        "WOO",
        "MEXC",
        "LBANK",
        name="exchange",
        schema="public",
    )
    op.create_table(
        "api_key",
        sa.Column("exchange", exchange_enum, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("key", sa.String(), nullable=False),
        sa.Column(
            "secret",
            sqlalchemy_utils.types.encrypted.encrypted_type.EncryptedType(),
            nullable=False,
        ),
        sa.Column(
            "passphrase",
            sqlalchemy_utils.types.encrypted.encrypted_type.EncryptedType(),
            nullable=True,
        ),
        sa.Column(
            "user_token",
            sqlalchemy_utils.types.encrypted.encrypted_type.EncryptedType(),
            nullable=True,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        schema="trade",
    )
    op.create_index(
        "ix_api_key_created_at", "api_key", ["created_at"], unique=False, schema="trade"
    )
    op.create_index(
        "ix_api_key_exchange_name",
        "api_key",
        ["exchange", "name"],
        unique=True,
        schema="trade",
    )
    op.create_index(
        "ix_api_key_updated_at", "api_key", ["updated_at"], unique=False, schema="trade"
    )
    op.create_table(
        "strategy",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column(
            "type",
            sa.Enum(
                "MOMENTUM",
                "MEAN_REVERSION",
                "ARBITRAGE",
                "MARKET_MAKING",
                "TREND_FOLLOWING",
                "SCALPING",
                name="strategytype",
                schema="trade",
            ),
            nullable=False,
        ),
        sa.Column(
            "asset_type",
            sa.Enum(
                "CASH",
                "STOCK",
                "CRYPTO",
                "ETF",
                "FUND",
                "PROPERTY",
                "COMMODITY",
                "NFT",
                "STOCK_FUTURES",
                "STOCK_OPTION",
                "COMMODITY_FUTURES",
                "COMMODITY_OPTION",
                "CRYPTO_FUTURES",
                "CRYPTO_INVERSE_FUTURES",
                "CRYPTO_OPTION",
                "CRYPTO_PERP",
                "CRYPTO_INVERSE_PERP",
                name="assettype",
                schema="trade",
            ),
            nullable=False,
        ),
        sa.Column(
            "direction",
            sa.Enum("LONG", "SHORT", "BOTH", name="strategydirection", schema="trade"),
            nullable=False,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
        schema="trade",
    )
    op.create_index(
        "ix_strategy_created_at",
        "strategy",
        ["created_at"],
        unique=False,
        schema="trade",
    )
    op.create_index(
        "ix_strategy_updated_at",
        "strategy",
        ["updated_at"],
        unique=False,
        schema="trade",
    )
    op.create_table(
        "bot",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column(
            "type",
            sa.Enum("CUSTOM", "WEBHOOK", name="bottype", schema="trade"),
            nullable=False,
        ),
        sa.Column("strategy_id", sa.Integer(), nullable=False),
        sa.Column("api_key_id", sa.Integer(), nullable=False),
        sa.Column("allocated_capital", sa.DECIMAL(20, 8), nullable=False),
        sa.Column("max_position", sa.Integer(), nullable=False),
        sa.Column("accumulate", sa.Boolean(), nullable=False),
        sa.Column("alert", sa.Boolean(), nullable=False),
        sa.Column("sentry_dsn", sa.String(), nullable=True),
        sa.Column("discord_webhooks", sa.ARRAY(sa.String()), nullable=False),
        sa.Column("config", postgresql.JSONB(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=False),
        sa.ForeignKeyConstraint(
            ["api_key_id"],
            ["trade.api_key.id"],
        ),
        sa.ForeignKeyConstraint(
            ["strategy_id"],
            ["trade.strategy.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
        schema="trade",
    )
    op.create_index(
        "ix_bot_created_at", "bot", ["created_at"], unique=False, schema="trade"
    )
    op.create_index(
        "ix_bot_updated_at", "bot", ["updated_at"], unique=False, schema="trade"
    )
    op.create_table(
        "position",
        sa.Column(
            "asset_type",
            sa.Enum(
                "CASH",
                "STOCK",
                "CRYPTO",
                "ETF",
                "FUND",
                "PROPERTY",
                "COMMODITY",
                "NFT",
                "STOCK_FUTURES",
                "STOCK_OPTION",
                "COMMODITY_FUTURES",
                "COMMODITY_OPTION",
                "CRYPTO_FUTURES",
                "CRYPTO_INVERSE_FUTURES",
                "CRYPTO_OPTION",
                "CRYPTO_PERP",
                "CRYPTO_INVERSE_PERP",
                name="assettype",
                schema="trade",
            ),
            nullable=False,
        ),
        sa.Column("exchange", exchange_enum, nullable=False),
        sa.Column("symbol", sa.String(), nullable=False),
        sa.Column(
            "side",
            sa.Enum("LONG", "SHORT", "FLAT", name="positionside", schema="trade"),
            nullable=False,
        ),
        sa.Column("price", sa.DECIMAL(20, 8), nullable=False),
        sa.Column("quantity", sa.DECIMAL(20, 8), nullable=False),
        sa.Column("realized_pnl", sa.DECIMAL(20, 8), nullable=False),
        sa.Column("opened_at", sa.DateTime(), nullable=False),
        sa.Column("closed_at", sa.DateTime(), nullable=True),
        sa.Column("bot_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=False),
        sa.ForeignKeyConstraint(
            ["bot_id"],
            ["trade.bot.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        schema="trade",
    )
    op.create_index(
        "ix_position_created_at",
        "position",
        ["created_at"],
        unique=False,
        schema="trade",
    )
    op.create_index(
        "ix_position_updated_at",
        "position",
        ["updated_at"],
        unique=False,
        schema="trade",
    )
    op.create_table(
        "trade",
        sa.Column("position_id", sa.Integer(), nullable=False),
        sa.Column("identifier", sa.String(), nullable=False),
        sa.Column("symbol", sa.String(), nullable=False),
        sa.Column("exchange", exchange_enum, nullable=False),
        sa.Column(
            "asset_type",
            sa.Enum(
                "CASH",
                "STOCK",
                "CRYPTO",
                "ETF",
                "FUND",
                "PROPERTY",
                "COMMODITY",
                "NFT",
                "STOCK_FUTURES",
                "STOCK_OPTION",
                "COMMODITY_FUTURES",
                "COMMODITY_OPTION",
                "CRYPTO_FUTURES",
                "CRYPTO_INVERSE_FUTURES",
                "CRYPTO_OPTION",
                "CRYPTO_PERP",
                "CRYPTO_INVERSE_PERP",
                name="assettype",
                schema="trade",
            ),
            nullable=False,
        ),
        sa.Column(
            "action",
            sa.Enum("BUY", "SELL", name="action", schema="trade"),
            nullable=False,
        ),
        sa.Column(
            "side",
            sa.Enum("LONG", "SHORT", "FLAT", name="positionside", schema="trade"),
            nullable=False,
        ),
        sa.Column("price", sa.DECIMAL(20, 8), nullable=False),
        sa.Column("quantity", sa.DECIMAL(20, 8), nullable=False),
        sa.Column("realized_pnl", sa.DECIMAL(20, 8), nullable=False),
        sa.Column("datetime", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=False),
        sa.ForeignKeyConstraint(
            ["position_id"],
            ["trade.position.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        schema="trade",
    )
    op.create_index(
        "ix_trade_created_at", "trade", ["created_at"], unique=False, schema="trade"
    )
    op.create_index(
        "ix_trade_updated_at", "trade", ["updated_at"], unique=False, schema="trade"
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_trade_updated_at", table_name="trade", schema="trade")
    op.drop_index("ix_trade_created_at", table_name="trade", schema="trade")
    op.drop_table("trade", schema="trade")
    op.drop_index("ix_position_updated_at", table_name="position", schema="trade")
    op.drop_index("ix_position_created_at", table_name="position", schema="trade")
    op.drop_table("position", schema="trade")
    op.drop_index("ix_bot_updated_at", table_name="bot", schema="trade")
    op.drop_index("ix_bot_created_at", table_name="bot", schema="trade")
    op.drop_table("bot", schema="trade")
    op.drop_index("ix_strategy_updated_at", table_name="strategy", schema="trade")
    op.drop_index("ix_strategy_created_at", table_name="strategy", schema="trade")
    op.drop_table("strategy", schema="trade")
    op.drop_index("ix_api_key_updated_at", table_name="api_key", schema="trade")
    op.drop_index("ix_api_key_exchange_name", table_name="api_key", schema="trade")
    op.drop_index("ix_api_key_created_at", table_name="api_key", schema="trade")
    op.drop_table("api_key", schema="trade")
    # ### end Alembic commands ###
