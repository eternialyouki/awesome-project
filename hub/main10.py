# 声明请求示例数据
# examples=[]得用列表
#导入
from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing  import Annotated


#实例
app = FastAPI()


#模式
class Item(BaseModel):
    name: Annotated[str, Field(examples=["苹果手机"])]
    description: Annotated[str, Field(examples=["最新款"])]
    price: Annotated[float, Field(gt=0,title="大于0")]

    #示例
    model_config = {
        "json_schema_extra":{
            "examples":[
                {
                "name": "苹果手机",
                "description": "最新款",
                "price":6999.0
                }
            ]
        }
    }

#装饰器
@app.put("/items/{item_id}")
async def update_items(
    item_id: int,
    item: Item
):
    results={
        "item_id":item_id,
        "item": item
    }

    return results