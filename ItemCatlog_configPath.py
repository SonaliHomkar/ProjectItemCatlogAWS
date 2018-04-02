import os

# This file is used to store configuration path

# This is used to store database path
DBPATH = os.path.abspath(os.path.join(os.path.dirname(__file__) ,'..','ItemCatlogData/ItemCatlog.db'))

# This is used to store client_secrets.json file path 
CLIENT_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','ItemCatlogData/client_secrets.json'))



