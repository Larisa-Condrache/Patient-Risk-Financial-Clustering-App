import streamlit as st

# Configurarea paginii
st.set_page_config(
    page_title="Proiect Diabet",
    page_icon="🩺",
    layout="centered",
)

# Titlu și subtitlu
st.title("Proiect SIIA")
st.markdown(
    """
    ### Bine ați venit în aplicația noastră de analiză a modelelor de clasificare!
    Această aplicație vă permite să explorați datele, să testați modele de clasificare și să înțelegeți riscurile pentru pacienți.
    """
)

# Secțiune interactivă: descriere pagini
st.markdown("### Navigare")
st.markdown("""
Folosește **meniul din stânga** pentru a naviga între pagini:

- 📊 **Prezentare Dataset** – Explorează coloanele și valorile datasetului.
- 📈 **Statistici & Afișare** – Vizualizări grafice și analize descriptive.
- 🧠 **Modele de Clasificare** – Aplică și testează modele ML (Decision Tree, KNN, SVM, Random Forest).
- 📌 **Concluzii** – Rezumatul rezultatelor și interpretarea modelelor.
- ❓ **Quiz** – Mini test interactiv pentru evaluarea cunoștințelor despre diabet.
""")
