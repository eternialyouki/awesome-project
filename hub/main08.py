# 请求体_字段
#导入包annotated,FastAPI,BaseModel,Field
from fastapi import FastAPI,Body
from typing import Annotated
from pydantic import BaseModel,Field


#实例
app = FastAPI()


#数据模式
class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None,title="项目描述",max_length=300
    )
    price: Annotated[float,Field(gt=0,description="价格必须大于0")]
    tax: float | None = None


#装饰器
@app.put("/items/{item_id}")
async def update_items(
    item_id: int,
    item: Annotated[Item,Body(embed=True)],
):
    results= {"item_id": item_id,"item": item}
    return results