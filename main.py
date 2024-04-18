import shutil
from openai import *
from bs4 import BeautifulSoup as Soup
import os
from git import *
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
    origin = repo.remote(name='origin')
    origin.push()

def create_new_blog(title, content, cover_image):
    cover_image = Path(cover_image)

    files = len(list(PATH_TO_CONTENT.glob('*.html')))
    new_title = f'{files+1}.html'
    path_to_new_content = PATH_TO_CONTENT/new_title
    shutil.copy(cover_image, PATH_TO_CONTENT)

    if not os.path.exists(path_to_new_content):
        #Write new file
        with open(path_to_new_content, 'w') as f:
            f.write('<!DOCTYPE html> \n')
            f.write('<html>\n')
            f.write('<head>\n')
            f.write(f'<title> {title} </title>\n')
            f.write('</head>\n')
            f.write('<body>\n')
            f.write("<img src = '{cover_image.name}' alt = 'Cover Image'> <br/> \n")
            f.write(f'<h1>{title}</h1>')
            f.write(content.replace('\n', '<br />\n'))
            f.write('</body>')
            f.write('</html>')
            print('Blog Created')
            return(path_to_new_content)
    else:
        raise FileExistsError('File already exists, ABORT!')
    
with open(PATH_TO_BLOG/'index.html') as index:
    soup = Soup(index.read())

print(soup)

path_to_new_content = create_new_blog('Test Title', 'pure gibberish and lots of it', 'c:\ecojohn.jpg')
    

random_text_string = '<h2> ANOTHER ONE </h2>'
with open(PATH_TO_BLOG/'index.html', 'w' ) as f:
    f.write(random_text_string)

update_blog()
