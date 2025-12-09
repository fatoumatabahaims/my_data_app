import streamlit as st

def dashboard_page():

    # Title
    
    st.title("My Data App")

    st.markdown("""
    This application helps you work with animal listings from the CoinAfrique website.
    It provides a simple interface to scrape data, view the raw CSV files, explore cleaned data,
    and evaluate the application.
    """)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Overview of main features
    
    st.header("What you can do with this app")

    st.markdown("""
    The application is organized into four main sections, available in the left-hand navigation menu:
    """)

    # 1. Scraping
    st.subheader("1. Scrape data")
    st.markdown("""
    **Purpose:**  
    Collect animal listings from CoinAfrique over several pages.

    **How it works:**  
    - Go to the **“Scraping”** page in the left menu.  
    - Choose a category (dogs, sheep, poultry/rabbits/pigeons, or other animals).  
    - Select how many pages you want to scrape.  
    - Click on **“Lancer le scraping”**.  

    The app will then:
    - scrape the selected pages,  
    - display the scraped data in a table,  
    - and save the results both as a CSV file and into the SQLite database.
    """)

    # 2. View raw CSV
    st.subheader("2. View raw scraped data (CSV)")
    st.markdown("""
    **Purpose:**  
    Inspect the original data exactly as it was scraped, without any cleaning.

    **How it works:**  
    - Go to the **“Afficher CSV”** page.  
    - Choose one of the available files (for example: dogs, sheep, etc.).  
    - The app displays the full CSV content in a table.  

    This section is useful to check what was collected before any cleaning or analysis.
    """)

    # 3. Cleaned data and analysis
    st.subheader("3. Work with cleaned data")
    st.markdown("""
    **Purpose:**  
    Use cleaned versions of the scraped data for simple analysis and visualisation.

    **How it works (conceptually):**  
    - During scraping, the data is stored in the SQLite database.  
    - Another part of the app can load these tables, clean columns such as the price,
      remove missing records, and create simple charts (for example: price distribution).  

    This functionality makes the data easier to interpret than the raw CSV files.
    """)

    # 4. Evaluation form
    st.subheader("4. Evaluate the application")
    st.markdown("""
    **Purpose:**  
    Collect feedback from users about the application.

    **How it works:**  
    - Go to the **“Évaluation”** page.  
    - A KoboToolbox form is embedded inside the app.  
    - Fill in your name, give a rating, and write any comments you have.  

    The responses are stored directly in KoboToolbox and can be reviewed later.
    """)

    st.markdown("<hr>", unsafe_allow_html=True)

    
    # Closing sentence
    st.markdown("""
    Use the navigation menu on the left to access each feature and test the full workflow:
    scraping → raw CSV → cleaned data → evaluation.
    """)
