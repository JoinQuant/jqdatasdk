# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_MANUFACTURING_PMI(Base):
    """
    制造业采购经理指数
    """

    __tablename__ = "MAC_MANUFACTURING_PMI"

    id = Column(Integer, primary_key=True)
    stat_month = Column(String(20), nullable=False)
    pmi = Column(DECIMAL(10, 4))
    produce_idx = Column(DECIMAL(10, 4))
    new_orders_idx = Column(DECIMAL(10, 4))
    new_export_orders_idx = Column(DECIMAL(10, 4))
    order_in_hand_idx = Column(DECIMAL(10, 4))
    finished_produce_idx = Column(DECIMAL(10, 4))
    purchase_quantity_idx = Column(DECIMAL(10, 4))
    import_idx = Column(DECIMAL(10, 4))
    exfactory_idx = Column(DECIMAL(10, 4))
    purchases_idx = Column(DECIMAL(10, 4))
    raw_material_idx = Column(DECIMAL(10, 4))
    employ_idx = Column(DECIMAL(10, 4))
    delivery_time_idx = Column(DECIMAL(10, 4))
    production_expected_idx = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)