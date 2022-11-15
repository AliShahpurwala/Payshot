from fastapi import FastAPI

app = FastAPI()


@app.get(path='/', summary='Index page of our application',
         description='This is the function that will be called whenever '
                     'a user navigates to / url. As in, https://localhost:8000/,'
                     'they will be greeted with whatever this function returns.')
def index_page():
    return '<h1>Hello World</h1>'
