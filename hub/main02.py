# 查询参数
#导入包
from fastapi import FastAPI
#创建实例
app = FastAPI()


#定义装饰器
@app.get("/items/{item_id}/foo/{foo_id}")
#异步函数
async def read_items(
    foo_id:str,
    item_id:int,
    q:str | None = None,
    short:bool = False
    ):
    #字典
    item = {foo_id: foo_id, item_id:item_id}
    #判断
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {"description":"这是一段详细描述"}
        )
    #输出
    return item