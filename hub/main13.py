# Header 参数
# 与定义 Header 参数的方式与定义 Query、Path、Cookie 参数相同
# 功能：字符转换和接受重复请求头
#导入fastapi,header,Annotated
from fastapi import FastAPI, Header
from typing import Annotated


#实例
app = FastAPI()


#装饰器
@app.get("/items")
#定义函数
async def read_items(

    user_agent: Annotated[str | None, Header()]=None,
    x_token: Annotated[list[str] | None, Header()]=None
):
    return{"user_Agent": user_agent, "x_Token values": x_token}