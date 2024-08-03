import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate('path/to/your/serviceAccountKey.json')  # Replace with your path
    firebase_admin.initialize_app(cred)

def app():
    st.title("User Account Management")

    # Ensure session state is initialized
    if 'user_id' not in st.session_state:
        st.session_state.user_id = None

    if st.session_state.user_id:
        st.write(f"Logged in as user ID: {st.session_state.user_id}")
        if st.button("Logout"):
            # Clear session state for logout
            st.session_state.user_id = None
            st.success("Logged out successfully!")
            st.experimental_rerun()  # Refresh the page to reflect the logout status
        return

    # Show login/signup options
    option = st.selectbox("Choose an option", ["Login", "Sign Up"])

    if option == "Sign Up":
        st.subheader("Sign Up")
        email = st.text_input("Email", key='sign_up_email')
        password = st.text_input("Password", type="password", key='sign_up_password')

        if st.button("Sign Up"):
            try:
                user = auth.create_user(
                    email=email,
                    password=password,
                )
                st.success(f"Account created successfully! User ID: {user.uid}")
                st.session_state.user_id = user.uid
                st.experimental_rerun()  # Refresh to reflect the logged-in status
            except Exception as e:
                st.error(f"Error creating account: {e}")

    elif option == "Login":
        st.subheader("Login")
        email = st.text_input("Email", key='login_email')
        password = st.text_input("Password", type="password", key='login_password')

        if st.button("Login"):
            try:
                user = auth.get_user_by_email(email)
                # To simulate a login process in Firebase Admin SDK:
                # We can't directly authenticate users using email/password in Firebase Admin SDK
                # You should implement client-side login via Firebase Client SDK for actual authentication.
                st.success(f"Logged in successfully! User ID: {user.uid}")
                st.session_state.user_id = user.uid
                st.experimental_rerun()  # Refresh to reflect the logged-in status
            except Exception as e:
                st.error(f"Error logging in: {e}")

# Example to demonstrate the `app` function
if __name__ == '__main__':
    app()
