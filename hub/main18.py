# 请求文件
# fastapi提供了bytes(适合极小文件)和UploadFile(所有文件)
#导入
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse  # 👈 单独从 responses 导入


#实例
app=FastAPI()


#装饰器
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    #读取
    await file.seek(0)
    contents = await file.read()
    #返回信息
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "file_size": len(contents),
        "message": "文件上传成功！"
    }
@app.get("/")
async def main():
    content = """
    <body>
    <form action="/uploadfile/" enctype="multipart/form-data" method="post">
    <input name="file" type="file">
    <input type="submit">
    </form>
    </body>
    """
    return HTMLResponse(content=content)
