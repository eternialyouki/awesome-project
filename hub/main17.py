# 表单数据
# From
# application/x-www-form-urlencoded
#导入
from fastapi import FastAPI,Form
from typing import Annotated

#实例
app=FastAPI()

#装饰器
@app.post("/login/")
async def login(

    username: Annotated[str, Form()],
    password: Annotated[str, Form()]

):
    return {"username": username,"password":password}