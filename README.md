# devops_scripts
author: Rudymatroja

change: 22-11-2022

## Script: repo_protectionrule
Name: repo_protectionrule.py

### Prerequistes
Python Version : 3.11

pip Version : 22.3

### Installation of python packages
`pip install flask`

`pip install requests`

### Setting environment variables 
windows `set GITHUB_TOKEN=<Personal_access_token>`

Linux `export GITHUB_TOKEN=<Personal_access_token>`

### starting python code

`python ./repo_protectionrule.py`

### Setting up github webhook

visit github_organization  -> settings -> webhooks -> click on create webhook
URL: http://<public_ip|dnsname|ngrok>/githubwebhook
request type: application/json
Tick only repository action -> create webhook

### Healthcheck of python code
send get request to only "/" path, it will return 200 code
`curl <localhost|publicip>/ -I`

