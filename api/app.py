import celery.states as states
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from worker import celery

app = FastAPI()


@app.get("/add/{param1}/{param2}", response_class=HTMLResponse)
async def add(param1: int, param2: int) -> str:
    task = celery.send_task('tasks.add', args=[param1, param2], kwargs={})
    response = f"<a href='{app.url_path_for('check_task', task_id=task.id)}'>check status of {task.id} </a>"
    return response


@app.get("/check/{task_id}", response_class=HTMLResponse)
async def check_task(task_id: str) -> str:
    res = celery.AsyncResult(task_id)
    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)


@app.get("/health_check")
async def health_check():
    return {"Status": "Ok"}
