# Git

### VCS

- Version Control
  - saving snapshots (committing) changes/versions of a file/folder
  - only staged/tracked/indexed
- create repos (files/directories)
- .git file = has everything that is tracked
- .gitignore = everything that we don't want tracked

### Centralised VCS

- a repo on server
- anyone wanting to use need to download copy
  - usually is locked
- close it(updates) + unlocks

### Distributed VCS

- repo on server
  - usually online like github
- download a copy of repo to local machine
  - pulling = from server to local
  - pushing = local to server
- freely make changes on file (local)

Anything with a . at beginning is hidden

## Stages of Git

1. Untracked
2. Tracked/Staged
3. Committed

#### Order of git commands
1. git init
   - convert normal repo to git repo
2. git status 
   - gives current status
3. git add .
   - adds all unstaged to staged
4. git commit -m "..."
   - commits all staged changes
   - -m " " = labelling with relevant message
   

## Git commands - History

- **git log** 
  - provides history of commits
  - latest from top to bottom
- **git diff <old-commit-id> <new-commit-id>**
  - This allows comparisons of commits
  - uses commmit IDs and provides changes that were made
- **git checkout <commit-id>**
  - view a previous commit's version of files/folders
  - swithces to the ID given
  - may seem like all other work has disappeared
  - 'detached Head from Master'
  - SAFE OPTION
- **git reset --hard <commit-id>**
  - hard reset to the ID provided
  - every work after that point is removed
  - DANGEROUS OPTION


## GitHub VS Git

![](C:\Users\rubel\Downloads\github_git.jpeg)
 - Git can be used without Github but Github cannot be used without Git
 - Git can be local
 - Github is an online service that can be used to store Git repos (publicly & privately)
 - 

## Methods to Pushing to Github

![](C:\Users\rubel\Downloads\methods_of_github.jpeg)
Method 1:
1. create empty repo
2. config where to put
3. push

Method 2:
1. create repo
2. git clone (clone remote repo to local so you have latest repo)
3. push

**Basic sync from REMOTE to Local Repo**
1. git remote add origin
   - adds the destination repo
2. git branch -M main 
   - switches to main (master if yours is called master)
   - only needed if not in master branch
3. git push (-u origin main)
   - push to repo

**Removing Folder/File from remote repo**
- removing means to remove from cached
- to remove a folder means it needs to recursively remove 
  - recursive = repeat and delete all things inside folder not just folder in one go
1. **command to remove**
- git rm --cached -r <folder>
  - The -r = recursively so only use this when wanting to remove whole folder
    - if removing file itself then -r not needed

### Using a .gitignore folder

- Everything with . in front means hidden
- .gitignore folder is used to put all things we dont want committed

#### **.gitignore**
- < .folder/file/ > 
  - format of how to place each folder/file inside
- This will specify that it wants to be not included
  - If a folder inserted, once pushed, it will still show up on Repo
    - Will need to remove from cache entirely for it to not show up