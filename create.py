import sys
import os
from dotenv import load_dotenv
from github import Github

load_dotenv()

path = os.getenv('FILEPATH')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

github_link = "https://github.com"

def create ():
    print("Creating...")
    foldername = str(sys.argv[1])
    user = Github(username, password).get_user()
    user.login
    repo = user.create_repo(foldername) 
    commands = ["git init", 
                f"echo #{foldername} > README.md",
                f"git remote add origin {github_link}/{user.login}/{foldername}.git",
                "git add .",
                'git commit -m "Initial commit" ',
                'git push -u origin master']
    
    try: 
        os.makedirs(path+str(foldername))
        os.chdir(path+str(foldername))
        for command in commands:
            os.system(command)
        os.system('code .')

    except :
        print("Repo already exists")

if __name__ == "__main__":
    create()