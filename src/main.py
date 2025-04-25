import re

FILE_PATH=input("输入或粘贴文件路径：\n")

with open(FILE_PATH,"r",encoding="utf-8") as f:
    file_data=f.read()

method = "datasortbody"
stmt_payment_list=re.findall(pattern=r'data-sort=\'{.*?}\'',string=file_data)

# print(stmt_payment_list)

for line in stmt_payment_list:
    print(line.replace("data-sort='","")[0:-1])