# 导入FastAPI模块
# 1导入FastAPI
from fastapi import FastAPI

# 2创建一个FastAPI实例
app = FastAPI()

# 3定义一个路径装饰器
@app.get("/")
# 4定义异步一个路径操作函数
async def root():
    #返回内容
    return {"message": "Hello World"}