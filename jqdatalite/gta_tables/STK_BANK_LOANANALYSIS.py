

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_BANK_LOANANALYSIS(Base):
    __tablename__ = "STK_BANK_LOANANALYSIS"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    INSTITUTIONNAME = Column(String(100, u'utf8_bin'))
    SYMBOL = Column(String(400, u'utf8_bin'))
    ENDDATE = Column(DateTime, primary_key=True, nullable=False)
    NONPERFORMINGLOANRATIO = Column(Numeric(20, 4))
    PROVISIONCOVERAGE = Column(Numeric(20, 4))
    LOANPROVISIONSRATIO = Column(Numeric(20, 4))
    RMBLIQUIDITYRATIO = Column(Numeric(20, 4))
    EXCHANGELIQUIDITYRATIO = Column(Numeric(20, 4))
    RMBLOANTODEPOSITRATIO = Column(Numeric(20, 4))
    EXCHANGELOANTODEPOSITRATIO = Column(Numeric(20, 4))
    TOP1CUSTOMERSLOANRATIO = Column(Numeric(20, 4))
    TOP10CUSTOMERSLOANRATIO = Column(Numeric(20, 4))
    BORROWINGFUNDSRATIO = Column(Numeric(20, 4))
    LENDINGFUNDSRATIO = Column(Numeric(20, 4))
    RMBLONGTERMLOANSRATIO = Column(Numeric(20, 4))
    EXCHANGELONGTERMLOANSRATIO = Column(Numeric(20, 4))
    INTERNATIONALLOANSRATIO = Column(Numeric(20, 4))
    INTERESTRECOVERIES = Column(Numeric(20, 4))
    NORMALLOANMIGRATIONRATIO = Column(Numeric(20, 4))
    SMLSMIGRATIONRATIO = Column(Numeric(20, 4))
    SUBLOANMIGRATORYRATIO = Column(Numeric(20, 4))
    DOUBTFULLOANSMIGRATIONRATIO = Column(Numeric(20, 4))
    NORMALLOAN = Column(Numeric(20, 2))
    SPECIALMENTIONLOANS = Column(Numeric(20, 2))
    SUBPRIMELOANS = Column(Numeric(20, 2))
    DOUBTFULLOANS = Column(Numeric(20, 2))
    LOSSLOANS = Column(Numeric(20, 2))
    LOANLOSSRESERVEADEQUACYRATIO = Column(Numeric(20, 4))
    LOANSDEBTSREADYEARLYVALUE = Column(Numeric(20, 2))
    LOANSDEBTSREADYEXTRACTED = Column(Numeric(20, 2))
    LOANINTERESTWRITEDOWNS = Column(Numeric(20, 2))
    RECOVERBADLOANS = Column(Numeric(20, 2))
    TURNOUTBADLOANS = Column(Numeric(20, 2))
    WRITEOFFSOFBADLOANS = Column(Numeric(20, 2))
    LOANSDEBTSREADYENDVALUE = Column(Numeric(20, 2))
