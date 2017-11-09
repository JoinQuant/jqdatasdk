# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INDUSTRY_AGR_PRODUCT_IDX_QUARTER(Base):
    """
    全国农产品生产价格指数表(季度)
    """
    __tablename__ = "MAC_INDUSTRY_AGR_PRODUCT_IDX_QUARTER"

    id = Column(Integer, primary_key=True)
    stat_quarter = Column(String(20), nullable=False)
    agricultural_products = Column(DECIMAL(20, 4))
    crop_products = Column(DECIMAL(20, 4))
    food = Column(DECIMAL(20, 4))
    grain = Column(DECIMAL(20, 4))
    wheat = Column(DECIMAL(20, 4))
    rice = Column(DECIMAL(20, 4))
    corn = Column(DECIMAL(20, 4))
    bean = Column(DECIMAL(20, 4))
    soybean = Column(DECIMAL(20, 4))
    potato = Column(DECIMAL(20, 4))
    oil_plants = Column(DECIMAL(20, 4))
    cotton = Column(DECIMAL(20, 4))
    sugar = Column(DECIMAL(20, 4))
    tobacco = Column(DECIMAL(20, 4))
    vegetable = Column(DECIMAL(20, 4))
    fruit = Column(DECIMAL(20, 4))
    tea = Column(DECIMAL(20, 4))
    forestry_products = Column(DECIMAL(20, 4))
    wood = Column(DECIMAL(20, 4))
    bamboo = Column(DECIMAL(20, 4))
    pectin = Column(DECIMAL(20, 4))
    animal_husbandry_products = Column(DECIMAL(20, 4))
    pig = Column(DECIMAL(20, 4))
    cow = Column(DECIMAL(20, 4))
    sheep = Column(DECIMAL(20, 4))
    poultry = Column(DECIMAL(20, 4))
    egg = Column(DECIMAL(20, 4))
    milk = Column(DECIMAL(20, 4))
    wool = Column(DECIMAL(20, 4))
    fishery = Column(DECIMAL(20, 4))
    marine_fishery_products = Column(DECIMAL(20, 4))
    marine_farm_products = Column(DECIMAL(20, 4))
    fresh_fishery_products = Column(DECIMAL(20, 4))
    fresh_farm_products = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)

    @property
    def update_keys(self):
        return ["agricultural_products",
                "crop_products",
                "food",
                "grain",
                "wheat",
                "rice",
                "corn",
                "bean",
                "soybean",
                "potato",
                "oil_plants",
                "cotton",
                "sugar",
                "tobacco",
                "vegetable",
                "fruit",
                "tea",
                "forestry_products",
                "wood",
                "bamboo",
                "pectin",
                "animal_husbandry_products",
                "pig",
                "cow",
                "sheep",
                "poultry",
                "egg",
                "milk",
                "wool",
                "fishery",
                "marine_fishery_products",
                "marine_farm_products",
                "fresh_fishery_products",
                "fresh_farm_products"]

    @property
    def filter_keys(self):
        return ["stat_quarter"]