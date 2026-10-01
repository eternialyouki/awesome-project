# 额外数据类型
#导入fastapi,Body,Annotated,datetime,time,timedelta,UUID
from fastapi import FastAPI, Body
from typing import Annotated
from datetime import datetime, time, timedelta
from uuid import UUID


#实例
app = FastAPI()


#装饰器
@app.put("/items/{item_id}")
#定义函数
async def update_item(
    
    item_id: UUID,
    start_datetime: Annotated[datetime,Body()],
    end_datetime: Annotated[datetime,Body()],
    process_after: Annotated[timedelta,Body()],
    repeat_at: Annotated[time | None,Body()]=None
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_datetime
    return {
        "item_id": item_id,             # 项目ID
        "start_datetime": start_datetime, # 开始时间
        "end_datetime": end_datetime,   # 结束时间
        "process_after": process_after, # 延迟时间
        "repeat_at": repeat_at,         # 重复时间
        "start_process": start_process, # 真正开始处理的时间
        "duration": duration,           # 任务持续时长
    }
# item = 项目、物品；id = 身份证号/编号
# start = 开始；datetime = 日期时间
# end = 结束
# process = 处理；after = 在...之后 
# repeat = 重复；at = 在...时刻
# duration = 持续时长（duration 是电影/视频里的“时长”）