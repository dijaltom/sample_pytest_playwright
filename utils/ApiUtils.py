
import httpx
from constants.constants import VAR
from pathlib import Path
import json

class ApiUtils:
    def __init__(self):
        pass
    @staticmethod
    async def load_payload(path=None,var_name=None):
        root=Path(__file__).parent.parent
        file_path=root/path
        if not Path(file_path).exists():
            raise ValueError(f"File path {path} not exists")
        with open(file_path,"r",encoding="utf8") as file:
            data=json.load(file)
            VAR[var_name]=data
            print("efe")

    @staticmethod
    async def  post(url=None,header=None,payload=None,timeout=5):
        async with httpx.AsyncClient(verify=False) as p:
            return await p.post(url=url,headers=header,data=payload,timeout=timeout)

    @staticmethod
    async def put(url=None, header=None, payload=None, timeout=5):
        async with httpx.AsyncClient(verify=False) as p:
            return await p.put(url=url, headers=header, data=payload, timeout=timeout)

    @staticmethod
    async def get(url=None, header=None, timeout=5):
        async with httpx.AsyncClient(verify=False) as p:
            return await p.get(url=url, headers=header, timeout=timeout)


# if __name__=="__main__":
#     import asyncio
#     asyncio.run(ApiUtils.load_payload("resources/payload/payload.json","payload"))
#     response=asyncio.run(ApiUtils.post(url="https://jsonplaceholder.typicode.com/posts",payload=VAR.get("payload")))
