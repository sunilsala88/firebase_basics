

ref_url='url'


import firebase_admin
from firebase_admin import credentials, db

# Path to your Firebase service account key JSON file
cred = credentials.Certificate(
 "dictionary from json file"
)

# Initialize the Firebase app
firebase_admin.initialize_app(cred, {
    'databaseURL': ref_url
})

ref = db.reference('main_users')

# Get a reference to the users
users_ref = ref.get()

# Print all users
# print(users_ref)

n=input('enter user name')
p=input('password')
validity=0
for u,u_data in users_ref.items():
    # print(u_data)
    if u_data['name']==n and u_data['password']==p:
        print('login successful')
        validity=u_data['validity']
        break

print(f"user {n} has validity till",validity)
import datetime as dt
import sys
import pandas as pd
validity=pd.to_datetime(validity).date()
print(validity)

#check if validity exist:
if validity<dt.date.today():
    print('validity expired')
    sys.exit()
else:
    print('starting strategy')



#python code to print first 100 fibonacci numbers
n=100
a,b=0,1
for i in range(n):
    print(a,end=' ')
    a,b=b,a+b
