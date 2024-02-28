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
   