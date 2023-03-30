from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import Router
import uvicorn

app = FastAPI()
router = Router()

app.include_router(router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)


if __name__ == '__main__':
    uvicorn.run('main:app', port=8080, reload=True)
