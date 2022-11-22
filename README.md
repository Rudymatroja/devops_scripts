# devops_scripts
author: Rudymatroja </br>
change: 22-11-2022 </br>
Reason: auto create branch protection rule for default branch whenever new repo is created

## Script: repo_protectionrule
Name: repo_protectionrule.py

### Prerequistes
Python Version : 3.11 </br>
pip Version : 22.3

### Installation of python packages
`pip install flask` </br>
`pip install requests`

### Setting environment variables 
windows `set GITHUB_TOKEN=<Personal_access_token>` </br>
Linux `export GITHUB_TOKEN=<Personal_access_token>`

### starting python code
`python ./repo_protectionrule.py`

### Setting up github webhook
visit github_organization  -> settings -> webhooks -> click on create webhook </br>
URL: http://<public_ip|dnsname|ngrok>/githubwebhook </br>
request type: application/json </br>
Tick only repository action -> create webhook </br>

### Healthcheck of python code
send get request to only "/" path, it will return 200 code </br>
`curl <localhost|publicip>/ -I` </br>

