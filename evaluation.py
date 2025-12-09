import streamlit as st

def evaluation_page():
    st.title("Application Evaluation")

    st.write(
        "Please choose which evaluation form you want to fill out. "
        "You can select either the KoboToolbox form or the Google Form."
    )

    choice = st.radio(
        "Select a form to open:",
        ("KoboToolbox Form", "Google Form")
    )

    # KOBO FORM OPTION
    if choice == "KoboToolbox Form":
        st.subheader("KoboToolbox Evaluation Form")

        st.info(
            "KoboToolbox does not allow embedded viewing inside Streamlit. "
            "Click the button below to open the form in a new tab."
        )

        kobo_url = "https://ee.kobotoolbox.org/x/kdYYIz9t"

        st.markdown(
            f"""
            <a href="{kobo_url}" target="_blank">
                <button style="
                    padding:12px 25px;
                    background-color:#4CAF50;
                    color:white;
                    border:none;
                    border-radius:5px;
                    font-size:16px;
                    cursor:pointer;">
                    Open Kobo Form
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )

    
    #  GOOGLE FORM OPTION
    
    else:
        st.subheader("Google Form Evaluation")

        google_form_url = "YOUR_GOOGLE_FORM_LINK_HERE"

        st.info(
            "Click the button below to open the Google Form in a new tab."
        )

        st.markdown(
            f"""
            <a href="{google_form_url}" target="_blank">
                <button style="
                    padding:12px 25px;
                    background-color:#2196F3;
                    color:white;
                    border:none;
                    border-radius:5px;
                    font-size:16px;
                    cursor:pointer;">
                    Open Google Form
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )
