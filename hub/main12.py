# Cookie 参数
# Cookie 参数用于在客户端和服务器之间传递信息。它们通常用于会话管理、用户身份验证和个性化设置。
# Swagger UI 无法测试 Cookie 参数（由于浏览器安全限制)
# 三个兄弟：Query、Path、Cookie 的用法完全一样，都可以写 max_length、description 等校验参数
# 通常用于做“登录状态保持”、“用户偏好设置”（比如 language=zh-CN）
# 导入
from fastapi import FastAPI,Cookie
from typing import Annotated


#实例
app = FastAPI()


#装饰器
@app.get("/items/")
#定义函数
async def read_items(
    ads_id: Annotated[str | None, Cookie()] = None
):
    return {"ads_id": ads_id}