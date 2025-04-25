import json


import pandas as pd

FILE_PATH = input("输入或粘贴文件路径：\n")

with open(FILE_PATH, "r", encoding="utf-8") as f:
    file_data = f.read()

method = "html.datasortbody"

if method == "html.datasortbody":

    import re

    stmt_payment_list = pd.DataFrame(
        data=[
            [
                item["date"],
                item["name"],
                item["type"],
                item["payment"],
                item["amount"],
                item["index_of_contract"],
            ]
            for item in [
                json.loads(line.replace("data-sort='", "")[0:-1])
                for line in re.findall(
                    pattern=r"data-sort=\'{.*?}\'", string=file_data
                )
            ]
        ],
        columns=[
            "date",
            "name",
            "type",
            "payment",
            "amount",
            "index_of_contract",
        ],
    )
    # print(stmt_payment_list)

elif method == "html.document":
    from bs4 import BeautifulSoup
    soup=BeautifulSoup(file_data,features="lxml")
    stmt_payment_list_data=[str(i).replace("\n","") for i in soup.find_all("div",attrs="stmt-payment-lists__i js-payment-accordion-ctrl js-payment-sort-item")]
    print(type(stmt_payment_list_data[0]))
    # print(stmt_payment_list[0])
    # print(len(stmt_payment_list))
    for i in stmt_payment_list_data:
        soup_lint=BeautifulSoup(i,features="lxml")
        soup_data=soup_lint("div",attrs="stmt-payment-lists__data")
        print(soup_data)

elif method == "csv":
    pass
elif method == "pdf" :
    pass
else:
    exit(0)