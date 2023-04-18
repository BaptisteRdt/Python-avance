from fastapi import FastAPI
import uvicorn
from website.router import configuration_route

app = FastAPI()

app = configuration_route(app)

if __name__ == '__main__':
    uvicorn.run(app)