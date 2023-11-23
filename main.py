from fastapi import FastAPI

app = FastAPI(
    title='НК Кабачок'
)

@app.get("/")
def index():
    return "Привет Кабачанцы!"