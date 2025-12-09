import streamlit as st

def evaluation_page():
    st.title("Application Evaluation")

    st.write(
        "Choose the type of evaluation form you want to complete. "
        "You can either fill out the KoboToolbox form or the Google Form."
    )

    # User chooses between KoboToolbox or Google Form
    choice = st.radio(
        "Select a form to complete:",
        ("KoboToolbox Form", "Google Form")
    )

    # --- KOBO TOOLBOX FORM FIRST ---
    if choice == "KoboToolbox Form":
        st.subheader("KoboToolbox Evaluation Form")

        st.write("Please complete the form below:")

        st.markdown(
            """
            <iframe 
                src="https://ee.kobotoolbox.org/x/kdYYIz9t"
                width="100%" 
                height="900" 
                frameborder="0">
            </iframe>
            """,
            unsafe_allow_html=True
        )

    # --- GOOGLE FORM SECOND ---
    else:
        st.subheader("Google Evaluation Form")

        st.write("Please complete the Google Form below:")

        st.markdown(
            """
            <iframe 
                src="https://docs.google.com/forms/d/e/1FAIpQLSc3mzq2HMA4vPRENbNSGkAL-uHSbqgzJkw_sLtiv7CWDeAOMg/viewform"
                width="100%" 
                height="900" 
                frameborder="0" 
                marginheight="0" 
                marginwidth="0">
            </iframe>
            """,
            unsafe_allow_html=True
        )
