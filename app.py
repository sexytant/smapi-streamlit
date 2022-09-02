import streamlit as st
import matching
from auth0_component import login_button


def main():
    # Using "with" notation
    with st.sidebar:
        clientId = "...."
        domain = "...."

        user_info = login_button(clientId, domain=domain)
        st.write(user_info)

        # Using object notation
        add_selectbox = st.sidebar.selectbox(
            "How would you like to be contacted?", ("Email", "Home phone", "Mobile phone")
        )
        st.write(add_selectbox)


if __name__ == "__main__":
    main()
