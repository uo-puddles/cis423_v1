import pandas as pd
import numpy as np
import subprocess
import importlib
import sys


user = 'uo-puddles'  #change to your github name
repo = 'cis423_starter'  #change to your own repo name
repo = 'cis423_v1'   #**************************************** remove this before class
sub = 'setup'        #change to your file name

#bring a fresh copy of the repo in and import.
#get rid of cached version first.
def reload_repo(user:str, repo_name:str, sub:str=''):
  my_github_repo = repo_name if not sub else f'{repo_name}.{sub}'
  clone_url = f'https://github.com/{user}/{repo_name}.git'
  subprocess.run(["rm", "-r", repo_name])  #get rid of old version
  subprocess.run(['git', 'clone', clone_url])   #get latest from github
  if my_github_repo in sys.modules:
    print('Removing cached version ...')
    sys.modules.pop(my_github_repo)  #uncache so force to look on path
  return importlib.import_module(my_github_repo)

up = reload_repo(user, repo, sub)  #same as import w22_repo.setup as up
