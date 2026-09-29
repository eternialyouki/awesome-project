# 查询参数和字符串校验
#导入fastapi,Query,Annotated
from fastapi import FastAPI,Query
from typing import Annotated


#实例
app = FastAPI()


#装饰器
@app.get("/items")
#操作函数
async def read_items(
    q: Annotated[
        str|None,
        Query(
            min_length=2,
            max_length=50,
            pattern="^梁智$"
        )
    ] = None
):
    results = {"items":[{"item_id":"FOO"},{"item_id":"Bar"}]}
    #判断
    if q:
        results.update({"q":q})
    #输出
    return results
