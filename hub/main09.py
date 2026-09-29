# 请求体_嵌套模型
# list——数组，Set——去重，HttpUrl，请求体可多层嵌套包括List[请求体]，
# 列表要加内部类型，去重用 set
# 任意字典（dict[int, float]）
#导入Annotated,FastAPI,Body,BaseModel,HttpUrl,Field
from fastapi import FastAPI,Body
from typing import Annotated
from pydantic import BaseModel,HttpUrl,Field


#实例
app = FastAPI()


#模式
class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    price: Annotated[float,Field(gt=0)]
    tags: set[str] = set ()
    images: list[Image] | None = None

class Offer(BaseModel):
    name: str
    items: list[Item]


#装饰器
@app.post("/sffers")
async def update_sffers(
    offer: Offer
):
    return offer