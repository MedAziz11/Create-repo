create-repo 

    shell command that can automate the steps of creating a github repo and the initial commit 🚀

    Install :
        # VSCODE and python should be installed #
        - git clone https://github.com/MedAziz11/Create-repo.git
        - cd Create-repo
        - pip install -r Requirements.txt
        - code .env
              --> Store in the .env file your Github username ,password and the path to where you want to save this project in your local machine
         Add Create-repo directory to your PATH in the Environment Variables
         
    After doing all the installation steps run:
            create-repo <YourRepoName>
            
    .env file content example:
        USERNAME:"YourUsername"
        PASSWORD:"YourPassword"
        FILEPATH:"C:\your\repo\path"
