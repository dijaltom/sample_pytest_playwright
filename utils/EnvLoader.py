from pathlib import Path
import csv
import os
from constants.constants import *
class EnvLoader:
    def __init__(self,path,column_name,testcase_id):
        self.path=path
        self.testcase_id=testcase_id
        self.column_name=column_name

    def load_csv(self):
        root=Path(__file__).resolve().parent.parent
        path=root/"resources"/"testdata"/self.path
        with open(path,"r+") as p:
            reader=csv.reader(p)
            headers=next(reader)
            if not self.column_name in headers:
                raise ValueError(f"File doesnt have column name with value {self.column_name} ")
            data=[dict(zip(headers,row)) for row in reader]
            filtered_data=[{self.testcase_id:j} for j in [r for r in data if r[self.column_name]==self.testcase_id]]
            CSV_VAR.extend(filtered_data)

    @staticmethod
    def var(testcase_id,item_name):
        val=""
        for iw in CSV_VAR:
            val = iw.get(testcase_id, {}).get(item_name, item_name)
        return val


#
# if __name__=="__main__":
#     dg = CsvLoader("inputdata.csv","testcaseId","test1")
#     dg.load_csv()
#     dg.var("test1","email")