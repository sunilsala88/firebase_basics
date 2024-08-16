

ref_url='url '


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

# Add a new user
ref.child('user_1').set({
    'name': 'sunil',
    'account': 'XGBOP',
    'validity': '2024-08-01'
})

# Update an existing user
ref.child('user_1').update({
    'age': 31
})


# Delete a specific user
ref.child('user_1').delete()


# Get a reference to the users
users_ref = ref.get()

# Print all users
print(users_ref)



