# 查询参数模型
#导入Annotated,Literal,Fastapi,Query,BaseMidel,field
from fastapi import FastAPI,Query
from typing import Annotated,Literal
from pydantic import BaseModel,Field


#实例
app = FastAPI()


#模式
class FiulterParams(BaseModel):
    limit: int = Field(100,gt=0,le=100)
    offset: int = Field(0,ge=0)
    order_by: Literal["created_at","updated_at"]="created_at"
    tags:list[str]=[]


#装饰器
@app.get("/items")
async def read_items(
    filter_query:Annotated[FiulterParams,Query()]
):
    return filter_query