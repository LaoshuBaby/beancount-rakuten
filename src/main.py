import re
import json

FILE_PATH=input("输入或粘贴文件路径：\n")

with open(FILE_PATH,"r",encoding="utf-8") as f:
    file_data=f.read()

method = "datasortbody"
stmt_payment_list_data=[json.loads(line.replace("data-sort='","")[0:-1]) for line in re.findall(pattern=r'data-sort=\'{.*?}\'',string=file_data)]

print(stmt_payment_list_data)

import pandas as pd
stmt_payment_list=pd.DataFrame(data=[ [item["date"],item["date"],item["date"],item["date"],item["date"],item["date"] ] for item in stmt_payment_list_data],columns=["date","name","type","payment","amount","index_of_contract"])
print(len(stmt_payment_list))