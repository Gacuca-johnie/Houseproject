import streamlit as st
from streamlit_option_menu import option_menu
from account import app as account_app
from home import app as home_app
from rent import app as rent_app
from buy import app as buy_app
from lessor import app as lessor_app
from seller import app as seller_app

st.set_page_config(page_title="KenyaPropertyHub")

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='KenyaPropertyHub',
                options=['Home', 'Rent', 'Buy', 'Lessor', 'Seller', 'Account'],
                icons=['house-fill', 'search', 'shop', 'person-fill', 'tag-fill', 'person-circle'],
                menu_icon='house-door-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px"},
                    "nav-link-selected": {"background-color": "#02ab21"}
                }
            )

        if app == 'Home':
            st.write(' HOME')
            home_app()
        elif app == 'Rent':
            st.write(' RENT')
            rent_app()
        elif app == 'Buy':
            st.write(' BUY')
            buy_app()
        elif app == 'Lessor':
            st.write(' LESSOR')
            lessor_app()
        elif app == 'Seller':
            st.write(' SELLER')
            seller_app()
        elif app == 'Account':
            st.write(' ACCOUNT')
            account_app()

# Create an instance of the MultiApp class
app = MultiApp()
app.add_app("Home", home_app)
app.add_app("Rent", rent_app)
app.add_app("Buy", buy_app)
app.add_app("Lessor", lessor_app)
app.add_app("Seller", seller_app)
app.add_app("Account", account_app)

# Run the app
app.run()
