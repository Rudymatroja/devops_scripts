#!/usr/bin/python

"""
AUTHOR: Rudy Matroja
lang: python
version: 3.11
Usage: python script.py
Tested: YES
Reason: auto create branch protection rule for organization whenever new repo is created
updated Date: 22-Nov-2022 07:18:49 CST
"""

# Import required Packages
from flask import Flask
from flask import request
from flask import json 
import requests
import os

# Github authentication and default branch
TOKEN =os.environ['GITHUB_TOKEN']
headers = {'Authorization': 'Bearer '+TOKEN, 'Accept': 'application/vnd.github+json'}
default_branch_name="main"

# Set protection rule based on requirement
protection_rules=json.dumps({"required_status_checks":None,"enforce_admins":True,"required_pull_request_reviews":{"dismissal_restrictions":{},"dismiss_stale_reviews":True,"require_code_owner_reviews":True,"required_approving_review_count":5,"require_last_push_approval":True,"bypass_pull_request_allowances":{}},"restrictions":None,"required_linear_history":True,"allow_force_pushes":None,"allow_deletions":False,"block_creations":False,"required_conversation_resolution":False,"lock_branch":False,"allow_fork_syncing":False})

app = Flask(__name__)

# basic Health check of the flask service
@app.route('/')
def root():
  return 'HEALTH:OK'

# github webhook handler
@app. route('/githubwebhook', methods=['POST']) 
def hook_root():
    repo_data=request.json

    #verify the action, whether repo created or modified or deleted
    if repo_data['action'] != "created":
      return json.dumps({"status":"actiontype != created, ignored request"})
    repo_full_name=repo_data['repository']['full_name']
    fetch_branch_details = requests.get('https://api.github.com/repos/'+repo_full_name+'/branches', headers=headers )
    branch_details=fetch_branch_details.json()
    branch_list = [ sub['name'] for sub in branch_details ]

    # verify the branch is present or not, ( if not present return 404 error )
    if default_branch_name in branch_list:
      
      # GITHUB api for creating protection rule
      protection_rules_res = requests.put('https://api.github.com/repos/'+repo_full_name+'/branches/'+default_branch_name+'/protection', data =protection_rules, headers=headers )
      if protection_rules_res.status_code == 200:
         return json.dumps({"status":"ok"})
      else:
         return json.dumps({"status":"failure while creating protection rule"}), 404
    else:
      return json.dumps({"status":"default branch with name main not found"}), 404

if __name__ == '__main__':
  #change debug mode based on requirement
  app.run(debug=True)
