# coding=utf-8


from jqdatasdk import *


import datetime
now1 = datetime.datetime.now()

df = get_all_securities()
for code in df.index:
    df2 = get_price(code)
    print("%s len:%s" % (code, len(df2.index)))

now2 = datetime.datetime.now()
print("use %s" % (now2 - now1))