

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

import pandas as pd
df=pd.read_csv('master.csv',index_col='users')
print(df)
d_users=df.to_dict('index')

print(d_users)
for i,j in d_users.items():
    ref.child(i).set(j)
