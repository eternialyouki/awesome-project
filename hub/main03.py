# 请求体
#导入fastapi,BaseModel
from fastapi import FastAPI
from pydantic import BaseModel


#创建数据模型
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


#实例
app = FastAPI()


#路径装饰器
@app.post("/items")
#操作函数
async def update_item(
    item_id: int,
    item: Item,
    q: str| None = None
):
    #合并数据
    result = {"item_id":item_id,**item.model_dump()}

    #判断
    if q:
        result.update({"q":q})
    #输出
    return result