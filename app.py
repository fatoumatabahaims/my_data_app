import streamlit as st
from dashboard import dashboard_page
from scraper import scrape_category, max_pages_available
from database import save_to_sql
from display_raw import display_raw_page
from evaluation import evaluation_page


# Barre latérale
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Aller à :",
    ["Dashboard", "Scraping", "Afficher CSV", "Évaluation"]
)

# Page Dashboard
if page == "Dashboard":
    dashboard_page()

# Page Scrap
elif page == "Scraping":

    st.header("Scraper les données CoinAfrique")

    category = st.selectbox(
        "Choisir une catégorie :",
        ["chiens", "moutons", "poules-lapins-et-pigeons", "autres-animaux"]
    )

    max_pages = st.number_input(
        "Nombre de pages à scraper :",
        1,
        max_pages_available[category],
        1
    )

    if st.button("Lancer le scraping"):
        df = scrape_category(category, max_pages)
        st.dataframe(df)

        # Enregistrements
        df.to_csv(f"data/{category}_scraped.csv", index=False)
        save_to_sql(df, category)

        st.success("Scraping terminé et données enregistrées.")

# Page CSV bruts
elif page == "Afficher CSV":
    display_raw_page()

# Formulaire Kobotoolbox
elif page == "Évaluation":
    evaluation_page()
