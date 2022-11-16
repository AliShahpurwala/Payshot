# Payshot
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)

_Start of something awesome!_
### Using the main app

So for this project, we're going to be using [FastAPI](https://fastapi.tiangolo.com/).
FastAPI is a framework used to create web servers. It's a python package which you'll need to download.

So before we begin, you're going to need to use a virtual environment to write and run the web server.

#### Virtual Environment
If you're using command prompt (Windows terminal), run this command inside of the Payshot folder.
```
python -m venv env
```
Now if you see the folders in Payshot, there should be a folder called `env`. If you don't have venv installed, check out [this article](https://python.land/virtual-environments/virtualenv).

Now, we never use git to track our virtual environment folder. It's very large because it has all of our dependency packages stored in it. But then, how do I tell you what packages you need ? That's where the file `requirements.txt` comes in to play. You can see I've added this file in the Payshot directory.

Now that we have `env`, we need to start up this environment. If you're on command prompt, run this command in Payshot folder.
```
env\Scripts\activate.bat
```
Now you're command line should look something like this:
```
(env) C:\Path\To\Payshot>
```
This is how you know, your environment has been activated. Next, we need to install our required dependencies. This only needs to be done once, next time you activate your environment, these dependencies will already be ready to use.

In command prompt, run this command in the payshot folder:
```
pip install -r requirements.txt
```
This will download all the dependencies needed. Now, you're ready to start developing.
To deactivate the virtual environment, just type `deactivate` in your command prompt.
#### Running the server
Once you have the virtual environment set up and running, to run the server, run this command in the Payshot directory with your virtual environment activated.
```
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```
### Resources
* [Official Git Online Book](https://git-scm.com/book/en/v2) -- Read the first 3 chapters, that should give you more than enough knowledge to help get us started. I used this book to learn it when I learnt Git in first year. It's very beginner friendly and it'll get you up and running quick :)
* [Python Virtual Environments](https://python.land/virtual-environments/virtualenv) -- Decent article about what a virutal environment is, why we need one and how to get up and running with one.
* [Web Service Gateway Interface](https://www.youtube.com/watch?v=WqrCnVAkLIo) -- I know that's a mouthful and sounds super complicated but do you ever wonder how exactly does an HTTP request become something that python can process and understand? This video is amazing and I love it. Maybe hold on till we start writing web server code before you watch it. It's very very very beginner accessible.
