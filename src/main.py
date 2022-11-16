"""
This file contains the main application object for fastapi.
"""
from fastapi import FastAPI
from starlette.responses import HTMLResponse

app = FastAPI()


@app.get(path='/', summary='Index page of our application',
         description='This is the function that will be called whenever '
                     'a user navigates to / url. As in, https://localhost:8000/,'
                     'they will be greeted with whatever this function returns.')
def index_page():
    """
    Args:
         None
    Returns:
         HTMLResponse
    """
    return HTMLResponse(content='<html><body><h1>Hello, world!</h1></body></html>',
                        media_type='text/html')
