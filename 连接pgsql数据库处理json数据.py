import json
import pandas
import psycopg2
from pandas import DataFrame

# 数据库连接参数
conn = psycopg2.connect(database="qz_rule_test", user="apollo", password="apollo1234", host="119.254.97.11", port="3311")
conn = psycopg2.connect(database="qz_rule_test", user="apollo", password="apollo****", host="119.254.**.**", port="****")
cur = conn.cursor()
cur.execute("select trait_atom_res,applyno from model6_test_csc;")
rows = cur.fetchall()        # all rows in table

dict=[]
dict_2=[]
for w in rows:
    d=list(w)[0]
    f=list(w)[1]
   # print(d)
    dict.append(d)
    dict_2.append(f)
# rows_keys=rows[0][0].keys()
# with open('d://111.txt', 'w') as file:
#     for i in rows:
#         file.write('%s' % i[0][j])

#rows.to_csv(r"C:\Users\Administrator\Desktop\rows.csv")

from pandas import DataFrame
# data=DataFrame(country_name,population)
# print(data)
data=DataFrame(dict,dict_2)
data.to_csv(r"C:\Users\Administrator\Desktop\model6_test_csc.csv")
