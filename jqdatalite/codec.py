# coding=utf-8
from utils import *
import pandas as pd
import numpy as np
import cPickle as pickle


class Codec(object):

    @classmethod
    def load(cls, data):
         return pickle.loads(data)

    # @classmethod
    # def load(cls, data):
    #     type, content = data["type"], data["data"]
    #     if type == "Panel":
    #         return cls.convert_panel(content)
    #     elif type == "DataFrame":
    #         return cls.convert_dataframe(content)
    #     elif type == "Series":
    #         return cls.convert_series(content)
    #     return cls.pandaize(content)

    @classmethod
    def pandaize(cls, data):
        if type(data) is float and np.isnan(data):
            return float("nan")
        elif is_str(data) and data.find("-") > 0:
            if data.find(":") > 0:
                return datetime.datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
            else:
                return datetime.datetime.strptime(data, "%Y-%m-%d").date()
        return data

    @classmethod
    def convert_panel(cls, data):
        return pd.Panel({k: cls.convert_dataframe(v) for k, v in data.items()})

    @classmethod
    def convert_dataframe(cls, data):
        lst = []
        for k, v in data.items():
            series = cls.convert_series(v)
            series.name = cls.pandaize(k)
            lst.append(series)
        return pd.DataFrame(lst)

    @classmethod
    def convert_series(cls, data):
        dct = {cls.pandaize(k): cls.pandaize(v) for k, v in data.items()}
        return pd.Series(dct)




