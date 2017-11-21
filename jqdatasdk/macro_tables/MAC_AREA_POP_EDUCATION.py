# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_POP_EDUCATION(Base):
    """
    各地区按性别和受教育程度分人口情况表
    """
    __tablename__ = "MAC_AREA_POP_EDUCATION"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    age_over_6 = Column(DECIMAL(20, 4))
    male_age_over_6 = Column(DECIMAL(20, 4))
    female_age_over_6 = Column(DECIMAL(20, 4))
    no_schooling = Column(DECIMAL(20, 4))
    male_no_schooling = Column(DECIMAL(20, 4))
    female_no_schooling = Column(DECIMAL(20, 4))
    primary_school = Column(DECIMAL(20, 4))
    male_primary_school = Column(DECIMAL(20, 4))
    female_primary_school = Column(DECIMAL(20, 4))
    junior_secondary_school = Column(DECIMAL(20, 4))
    male_junior_secondary_school = Column(DECIMAL(20, 4))
    female_junior_secondary_school = Column(DECIMAL(20, 4))
    senior_secondary_school = Column(DECIMAL(20, 4))
    male_senior_secondary_school = Column(DECIMAL(20, 4))
    female_senior_secondary_school = Column(DECIMAL(20, 4))
    college = Column(DECIMAL(20, 4))
    male_college = Column(DECIMAL(20, 4))
    female_college = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)