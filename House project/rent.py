import streamlit as st
from firebase_utils import get_properties

def app():
    st.title("Find Properties for Rent")

    st.subheader("Search for Properties")

    min_price = st.number_input("Minimum Rent Amount", min_value=0)
    max_price = st.number_input("Maximum Rent Amount", min_value=0)
    location = st.text_input("Location")
    description_query = st.text_input("Description (partial match)")

    if st.button("Search"):
        try:
            # Ensure location and description_query are not empty
            if not location:
                st.error("Please provide a location.")
                return
            if not description_query:
                st.error("Please provide a description query.")
                return

            # Fetch properties
            results = get_properties(min_price, max_price, location.lower(), description_query.lower())
            
            if results:
                st.subheader("Search Results")
                for prop in results:
                    st.write(f"Description: {prop['description']}")
                    st.write(f"Amount: Ksh {prop['amount']}")
                    st.write(f"Location: {prop['location']}")
                    st.write(f"Size: {prop['size']}")
                    for picture in prop['pictures']:
                        st.image(picture)  # Display images from URLs
            else:
                st.write("No properties found matching your criteria.")
        
        except Exception as e:
            st.error(f"Error searching for properties: {e}")
