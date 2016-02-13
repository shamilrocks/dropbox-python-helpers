#Create an alias/environment variable in your .bash_profile
#Similar to https://natelandau.com/my-mac-osx-bash_profile/
#for your token to access Dropbox API programmatically
#example DROPBOX_TOKEN = Unique token

#Import Dropbox Python sdk
import dropbox
#Import OS Environment Variables
import os
#gets the environment variable from the OS for DROPBOX_TOKEN
YOUR_TOKEN = os.getenv("DROPBOX_TOKEN")
#set dbx variable to authenticate with Dropbox using environment variable
dbx = dropbox.Dropbox(YOUR_TOKEN)
#get current account info for user, tests to see if Dropbox connection is working
useraccountinfo = dbx.users_get_current_account()
print (useraccountinfo)
