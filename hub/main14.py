# 响应模型_返回类型
#导入fastapi,BaseModel
from fastapi import FastAPI
from pydantic import BaseModel


# 实例
app = FastAPI()


# 定义响应模型
class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str

#装饰器
@app.post("/user/", response_model=UserOut)
async def create_user(
    user: UserIn
):
    #内部可访问
    print(user.password)

    # 返回响应
    return user