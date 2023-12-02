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

@app.get("/games")
def games():
    return "Тут будет все связанное с играми"


@app.get("/about/")
def about():
    return "Тут будет \"О проекте\""
