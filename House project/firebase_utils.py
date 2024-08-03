
import firebase_admin
from firebase_admin import credentials, auth, firestore

# Initialize Firebase app
cred = credentials.Certificate('pondering-tutorial-1a5ce-979794598388.json')
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Initialize Firestore DB
db = firestore.client()

def create_user(email, password):
    """Create a new user with email and password."""
    user = auth.create_user(email=email, password=password)
    return user.uid

def login_user(email, password):
    """Login a user and return their UID."""
    # Firebase Authentication doesn't have a login function for the client side, only server-side SDK
    # Use Firebase Client SDK in your web app for login
    raise NotImplementedError("Client-side login is not implemented. Use Firebase Client SDK for authentication.")

def logout_user():
    """Logout the current user."""
    # Firebase Authentication doesn't support logout server-side, it needs to be handled on the client side
    raise NotImplementedError("Client-side logout is not implemented. Use Firebase Client SDK for authentication.")

def add_property(description, amount, location, size, pictures, user_uid):
    """Add a property to Firestore."""
    properties_ref = db.collection('properties')
    properties_ref.add({
        'description': description,
        'amount': amount,
        'location': location,
        'size': size,
        'pictures': pictures,
        'user_uid': user_uid
    })

def get_properties(description=None, min_amount=None, max_amount=None, location=None):
    """Get properties from Firestore based on search criteria."""
    properties_ref = db.collection('properties')
    query = properties_ref

    if description:
        query = query.where('description', '>=', description)
    if min_amount is not None:
        query = query.where('amount', '>=', min_amount)
    if max_amount is not None:
        query = query.where('amount', '<=', max_amount)
    if location:
        query = query.where('location', '==', location)

    results = query.stream()
    properties = []
    for doc in results:
        properties.append(doc.to_dict())

    return properties

def get_user_properties(user_uid):
    """Get properties listed by a specific user."""
    properties_ref = db.collection('properties')
    query = properties_ref.where('user_uid', '==', user_uid)
    results = query.stream()
    properties = []
    for doc in results:
        properties.append(doc.to_dict())

    return properties
