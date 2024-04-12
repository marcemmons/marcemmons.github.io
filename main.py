from openai import *
import os
from git import Repo
from pathlib import Path

PATH_TO_REPO = Path('c:\\github\\marcemmons.github.io\\.git')
PATH_TO_BLOG = PATH_TO_REPO.parent
PATH_TO_CONTENT = PATH_TO_BLOG/"content"

PATH_TO_CONTENT.mkdir(exist_ok=True, parents=True)


ai = OpenAI()
ai.api_key = os.getenv("OPENAI_API_KEY")

def update_blog(commit_message ='updates blog'):
    repo = Repo(PATH_TO_REPO)
    repo.git.add(all=True)
    repo.index.commit(commit_message)
    origin = Repo.remote(name='origin')
    origin.push

random_text_string = '<h2> Very Hopeful text </h2>'

with open(PATH_TO_BLOG/'index.html', 'w' ) as f:
    f.write(random_text_string)

update_blog()