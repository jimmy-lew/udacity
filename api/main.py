from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bikeshare_2 import Router
from model_types import QueryBody, TimeResponse
import uvicorn

app = FastAPI()
router = Router()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(router.router)


@app.get('/ok')
def check_ok():
    return {
        'code': 200,
        'status': 'OK'
    }


@app.post('/calculate')
def calculate_stats(query: QueryBody) -> QueryBody:

    return query


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
    pass
