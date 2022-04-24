import pandas as pd
df = pd.read_excel("drug_order_detai_1.xls", sheet_name="drug_order_detail2")

df["销售额"] = df["销量"] * df['价格']
sum = df['销售额'].sum()
print("所有分店总销售额是：%d"%(sum))
df2 = df['销售额'].groupby(df['分店']).describe()
print("各分店销售额的最小值、最大值、平均值如下：")
print("人大分店 %d %d %.2f"%(int(df2.loc['人大分店']['min']), int(df2.loc['人大分店']['max']), df2.loc['人大分店']['mean']))
print("四季青分店 %d %d %.2f"%(df2.loc['四季青分店']['min'], df2.loc['四季青分店']['max'], df2.loc['四季青分店']['mean']))
print("花园桥分店 %d %d %.2f"%(df2.loc['花园桥分店']['min'], df2.loc['花园桥分店']['max'], df2.loc['花园桥分店']['mean']))
print("金源分店 %d %d %.2f"%(df2.loc['金源分店']['min'], df2.loc['金源分店']['max'], df2.loc['金源分店']['mean']))