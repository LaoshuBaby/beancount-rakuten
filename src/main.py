import json
import re

import pandas as pd

FILE_PATH = input("输入或粘贴文件路径：\n")

with open(FILE_PATH, "r", encoding="utf-8") as f:
    file_data = f.read()

method = "html.datasortbody"

if method == "html.datasortbody":

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
    pass
elif method == "csv":
    pass
elif method == "pdf" :
    pass
else:
    exit(0)