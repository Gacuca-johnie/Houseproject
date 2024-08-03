import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth, firestore, storage

# Initialize Firebase if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate('path/to/your/serviceAccountKey.json')  # Replace with your path
    firebase_admin.initialize_app(cred)

db = firestore.client()

def app():
    # Check if user is logged in
    if 'user_id' not in st.session_state or not st.session_state.user_id:
        st.warning("You need to be logged in to access this page.")
        st.write("[Login here](#)")
        return

    st.title("Seller Page")

    st.subheader("Add Property for Sale")

    # Input fields for property details
    property_name = st.text_input("Property Name")
    property_description = st.text_area("Property Description")
    property_location = st.text_input("Location")
    property_size = st.selectbox("Property Size", ["Single Room", "Bedsitter", "1 Bedroom", "2 Bedroom", "3 Bedroom", "4 Bedroom", "5 Bedroom"])
    property_price = st.number_input("Price", min_value=0)

    # Upload images
    uploaded_files = st.file_uploader("Choose images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    # Submit button
    if st.button("Submit Property"):
        try:
            # Save property details to Firestore
            property_ref = db.collection('properties').add({
                "name": property_name,
                "description": property_description,
                "location": property_location,
                "size": property_size,
                "price": property_price,
                "seller_id": st.session_state.user_id
            })

            # Upload images to Firebase Storage
            for file in uploaded_files:
                upload_image(file, property_ref.id)

            st.success("Property submitted successfully!")
        except Exception as e:
            st.error(f"Error submitting property: {e}")

def upload_image(image_file, property_id):
    # Get the storage bucket
    bucket = storage.bucket()
    
    # Create a unique filename
    filename = f"{property_id}/{image_file.name}"
    
    # Upload the file to Firebase Storage
    blob = bucket.blob(filename)
    blob.upload_from_file(image_file)
    
    # Make the blob publicly accessible (optional)
    blob.make_public()
    
    st.write(f"Uploaded {image_file.name} to {blob.public_url}")

# Example to demonstrate the `app` function
if __name__ == '__main__':
    app()
