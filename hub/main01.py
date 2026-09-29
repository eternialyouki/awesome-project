# 路径参数
#导入fasstapi模块
from fastapi import FastAPI
#创建实例
app = FastAPI()
#定义装饰器
@app.get("/items/{item_id}")
#定义异步函数
async def read_items(item_id: int):
    #返回内容
    return {"item_id": item_id}
