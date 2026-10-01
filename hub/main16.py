# 响应状态码
# 200 成功
# 201 已创建
# 404 未找到
# 422 数据校验失败
# 500 服务器错误
# 装饰器参数

#导入
from fastapi import FastAPI,status
from pydantic import BaseModel,EmailStr

#实例
app=FastAPI()


#基类
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    pass

class UserInDB(UserBase):
    hashed_password: str


#加密
def fake_password_hasher(raw_password: str):
    return "nihao" + raw_password

def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    #解包+数据库字典追加哈希
    user_in_db = UserInDB(**user_in.model_dump(),hashed_password = hashed_password)
    print("已保存")
    return user_in_db

#装饰器
@app.post(
        "/User/",
          response_model=UserOut,
          status_code = status.HTTP_201_CREATED
          )
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved