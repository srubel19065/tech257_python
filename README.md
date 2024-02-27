# Python and Markdown

## Markdown basics

### Marking code 

This prints something to the screen: `print("Hello World!")`

```
# print message to the screen
print("Hello World!")
```

### Highlighting text 

This is how you do italics: _italics_ or *italics* <br>
This is how you do bold: **this is in bold**

### Bullet points vs numbered lists

* item 1 
* item 2
  * item 2.1
* item 3

Steps
1. Step 1
2. Step 2
    * point about this step

# Git

### VCS

- Version Control
  - saving snapshots (committing) changes/versions of a file/folder
  - only staged/tracked/indexed
- create repos
- branches
- .git file = has everything - tracked
- .gitignore = if don't want tracked

### Centralised VCS

- repo on server
- anyone wanting to use need to download copy
  - usually is locked
- close it(updates) + unlocks

### Distributed VCS

- repo on server
  - usually online like github
- download copy repo to local machine
  - pulling = from server to local
  - pushing = local to server
- freely make changes on file (local)

#### Anything with a . at beginning is hidden