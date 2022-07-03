## Start Machine Learning Project.

### Software and account Requirement:

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT CLI](https://git.scm.com/downloads)

Ceating conda environment
```
conda create -p myVenv python==3.7 -y 
(-p used for conda environment working as project directory)

```
```
### to activate the conda environment
type: conda activate  myVenv/
or 
type conda activate  myVenv/
(here / is nessary for accessing current directory environment)
```

```
pip install -r requirements.txt
```

```
### To Add files to git

git add . 
or 
git add file_name1, file_name2, ... ...

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
-------
git status

To check all version maintained by git
--------------------------------------
git log


To create version/commit all changes by git
------------------------------------------------------
git commit -m "any messages"

To send version/changes to github
--------------------------------------
git push origin main


To check remote url
------------------------------------
git remote  -v
```

```
BUILD DOCKER IMAGES
------------------------------
docker build -t <image_name>:<tagname> .

To list docker images
-------------------------------------
docker images


Run docker image
------------------------
docker run -p 5000:5000 -e PORT=5000 a2d35ded190e

To check running container in docker
----------------------------------------------
docker ps

Docker STOP Command
-----------------------
docker stop container_id
```

```
python setup.py install
```