# 请求体——多个参数
from typing import Annotated

from fastapi import FastAPI, Path,Body,Query
from pydantic import BaseModel

app = FastAPI()


#请求体
class Item(BaseModel):
    name: str | None =None

class User(BaseModel):
    name: int | None =None

#装饰器1 路径+查询+请求体
# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: Annotated[int ,Path(title="...",ge=0,le=1000)],
#     q:str | None = None,
#     item: Item | None = None
# ):
#     result={"item_id":item_id}

#     if q:
#         result.update({"q": q})
#     if item:
#         result.update({"item": item})
#     return result

#装饰器2 多个请求体
# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: int, 
#     item: Item,
#     user: User
# ):
#     reaults={"item_id":item_id}
#     if item:
#         reaults.update({"item": item})
#     if user:
#         reaults.update({"user": user})
#     return reaults

#装饰器3 引入Body
# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: Annotated[int, Path(title="商品",ge=1)],
#     item: Item,
#     user: User,
#     importance: Annotated[int, Body(ge=5)]
# ):
#     results={"item_id": item_id,"importance": importance}

#     if item:
#         results.update({"item": item})
#     if user:
#         results.update({"user": user})
#     return results


#装饰器4 请求体+查询参数
# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: Annotated[int, Path(title="商品",ge=1)],
#     item: Item,
#     user: User,
#     importance: Annotated[int, Body(ge=5)],
#     q: str
# ):
#     results={"item_id": item_id,"q": q,"importance": importance}

#     if item:
#         results.update({"item": item})
#     if user:
#         results.update({"user": user})
#     return results

#装饰器5 （Body(embed=True)）
@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: Annotated[int, Path(title="商品",ge=1)],
    item: Annotated[Item,Body(embed=True)],
    user: User,
    importance: Annotated[int, Body(ge=5)],
    q: str
):
    results={"item_id": item_id,"q": q,"importance": importance}

    if item:
        results.update({"item": item})
    if user:
        results.update({"user": user})
    return results