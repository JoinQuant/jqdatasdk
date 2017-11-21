# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_SALE_RETAIL_MONTH(Base):
    """
    社会消费品销售总额
    """
    __tablename__ = "MAC_SALE_RETAIL_MONTH"

    id = Column(Integer, primary_key=True)
    stat_month = Column(String(20), nullable=False)
    retail_sin = Column(DECIMAL(20, 4))
    retail_acc = Column(DECIMAL(20, 4))
    retail_sin_yoy = Column(DECIMAL(10, 4))
    retail_acc_yoy = Column(DECIMAL(10, 4))
    scale_retail_sin = Column(DECIMAL(20, 4))
    scale_retail_acc = Column(DECIMAL(20, 4))
    scale_retail_sin_yoy = Column(DECIMAL(10, 4))
    scale_retail_acc_yoy = Column(DECIMAL(10, 4))
    city_retail_sin = Column(DECIMAL(20, 4))
    city_retail_acc = Column(DECIMAL(20, 4))
    city_retail_sin_yoy = Column(DECIMAL(10, 4))
    city_retail_acc_yoy = Column(DECIMAL(10, 4))
    rural_retail_sin = Column(DECIMAL(20, 4))
    rural_retail_acc = Column(DECIMAL(20, 4))
    rural_retail_sin_yoy = Column(DECIMAL(10, 4))
    rural_retail_acc_yoy = Column(DECIMAL(10, 4))
    hotel_retail_sin = Column(DECIMAL(20, 4))
    hotel_retail_acc = Column(DECIMAL(20, 4))
    hotel_retail_sin_yoy = Column(DECIMAL(10, 4))
    hotel_retail_acc_yoy = Column(DECIMAL(10, 4))
    hotel_scale_retail_sin = Column(DECIMAL(20, 4))
    hotel_scale_retail_acc = Column(DECIMAL(20, 4))
    hotel_scale_retail_sin_yoy = Column(DECIMAL(10, 4))
    hotel_scale_retail_acc_yoy = Column(DECIMAL(10, 4))
    sale_retail_sin = Column(DECIMAL(20, 4))
    sale_retail_acc = Column(DECIMAL(20, 4))
    sale_retail_sin_yoy = Column(DECIMAL(10, 4))
    sale_retail_acc_yoy = Column(DECIMAL(10, 4))
    sale_scale_retail_sin = Column(DECIMAL(20, 4))
    sale_scale_retail_acc = Column(DECIMAL(20, 4))
    sale_scale_retail_sin_yoy = Column(DECIMAL(10, 4))
    sale_scale_retail_acc_yoy = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)
