# SSH
SSH = Secure Shell/ Secure Socket Shell
### What is it?
- Network Protocol that allows secure way to access a computer
- Provides strong password AUTH and Public key AUTH 
- Encrypted data comms between 2 computers over open network
- Used to manage systems and apps remotely

### HTTPS VS SSH
1. https is used more commonly due to its easier config 
2. SSH provides more security with its use of a public key cryptography


### Creating SSH key pair

- ON Terminal
  - ```ssh-keygen -C```


### Best practices
1. Disable password AUTH:
   - key-pair AUTH is more secure
2. Dont share Key Pairs
   - keep to yourself in safe space eg Azure Vaults


### Steps to making key pair
1. go to .ssh folder
2. create key pair
   - ```ssh-keygen -t rsa -b 4096 -C <email>```
3. Will say to enter file = Create keypair name
   - name.pub = public key **ONLY THING THAT CAN BE SHOWN**
   - will show picture = has been created

### How to see Public key and what to do with it
1. cat <keypair.**pub**
2. copy all except for any white space
3. go to github repo and then settings
4. Deploy Keys
5. add a key with title and paste key 

### Creating ssh-agent and adding ssh key
Needs to be done as without this step cannot clone
1. ```eval `ssh-agent` ```
   - will give agent pid
2. ```ssh-add ~/.ssh/<keypair(priv)>```
3. ```ssh -T git@github.com```
   - authenticate github 

### git clone 'ssh clone code'

## ALERT: DONT EXPOSE PRIVATE KEY
