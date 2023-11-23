from fastapi import FastAPI

app = FastAPI(
    title='НК Кабачок'
)


@app.get("/")
def index():
    return "Привет Кабачанцы!"


@app.get("/news/")
def news():
    return "Тут будут новости"


@app.get("/about/")
def about():
    return "Тут будут \"О нас\""
