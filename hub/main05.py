# 路径参数和数据校验
#导入fastapi,Query,Path,Annotated
from fastapi import FastAPI,Query,Path
from typing import Annotated


#实例
app = FastAPI()


#装饰器
@app.get("/items/{item_id}")
#操作函数
async def read_items(
    item_id:Annotated[int,Path(title="获取项目ID",ge=1,le=100)],
    q: Annotated[str | None,Query(alias="item-query")]=None
):
    results={"item_id":item_id}
    if q:
        results.update({"q":q})
    return results
