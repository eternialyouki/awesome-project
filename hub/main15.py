# 更多模型
#导入fastapi,BaseModel
from fastapi import FastAPI
from pydantic import BaseModel,EmailStr


#实例
app = FastAPI()


#基类
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

#输入
class UserIn(UserBase):
    password: str


#输出
class UserOut(UserBase):
    pass


#数据库
class UserInDB(UserBase):
    hashed_password: str

#加密
def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password

def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    #解包+追加哈希
    user_in_db = UserInDB(**user_in.model_dump(),hashed_password  = hashed_password)
    print(f"用户{user_in.username}已保存!(模拟)")
    return user_in_db

#装饰器
@app.post("/user/",response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved