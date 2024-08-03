# firebase_utils.py
import firebase_admin
from firebase_admin import credentials, firestore, auth

# Initialize Firebase Admin SDK
cred = credentials.Certificate('pondering-tutorial-1a5ce-979794598388.json')
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

def create_user(email, password):
    user = auth.create_user(email=email, password=password)
    return user.uid

def get_user_by_email(email):
    user = auth.get_user_by_email(email)
    return user

def add_property(description, amount, location, size, pictures):
    properties_ref = db.collection('properties')
    properties_ref.add({
        'description': description,
        'amount': amount,
        'location': location,
        'size': size,
        'pictures': pictures
    })

def get_properties(min_price, max_price, location):
    properties_ref = db.collection('properties')
    query = properties_ref.where('amount', '>=', min_price).where('amount', '<=', max_price).where('location', '==', location)
    results = query.stream()
    properties = [doc.to_dict() for doc in results]
    return properties
