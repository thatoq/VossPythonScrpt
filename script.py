import requests
from requests.exceptions import HTTPError
import os
from glob import glob
import shutil

client = 'https://reqres.in/api'
path ="./users"

def getUserInformation():
    try:
        response = requests.get('{}{}'.format(client,'/users?page=2'))
        return response
    except HTTPError as http_err:
      return ('HTTP error occurred')
    except Exception as err:
        return('Other error occurred')

def folderExists(yourPath):
    if(os.path.exists(yourPath)): 
        return True
    else:
        return False

def createUserFolders():
    try:
        data = getUserInformation().json()['data']
        for users in data:
            str_path= './users/'+str(users['id'])+"_"+users['first_name']+"_"+users['last_name']
            if(folderExists(str_path)==False):
                        os.mkdir(str_path)
    except OSError as error:
            print (error)
 
def downloadAvators(): 
    data = getUserInformation().json()['data']
    for users in data:
        str_path= './users/'+str(users['id'])+"_"+users['first_name']+"_"+users['last_name']
        if(folderExists(str_path)==True):
             image = requests.get(users['avatar']).content
             with open(str_path+"/"+str(users['id'])+'.jpg', 'wb') as handler:
                 handler.write(image)
    
createUserFolders()
downloadAvators()
