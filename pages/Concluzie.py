import streamlit as st

st.markdown("""
##Concluzie asupra modelelor și analizei realizate

### 1. Decision Tree (Arbore de decizie)
- Clasifică pacienții cu diabet pe baza caracteristicilor medicale.
- Acuratețe bună (raportată în aplicație).
- **Avantaje:** ușor de interpretat, reguli clare pentru diagnostic.
- **Limitări:** poate suferi de overfitting dacă datele sunt zgomotoase sau mici.

### 2. K-Nearest Neighbors (KNN)
- Exemplu de predicție aplicat unui pacient de test.
- Determină riscul pacientului prin comparație cu cei mai apropiați vecini.
- Rezultat pentru pacientul de test: `0` (nu este în risc) sau `1` (este în risc).
- **Avantaje:** simplu de implementat și intuitiv.
- **Limitări:** nu este scalabil pentru seturi mari de date; nu oferă explicații pentru decizie.

### 3. K-Means Clustering (analiza clienților)
- Aplicat pe datele clienților de credit pentru a identifica grupuri similare.
- Metoda **Elbow** a ajutat la alegerea unui număr optim de clustere (în exemplu: 4).
- Vizualizarea PCA 2D arată distribuția clienților și diferențele între clustere.
- **Avantaje:** oferă o privire de ansamblu asupra grupurilor de clienți.
- **Limitări:** nu este un model de clasificare; interpretarea depinde de domeniul de aplicare.

### 4. Support Vector Machine (SVM)
- Model liniar SVM utilizat pentru clasificarea pacienților.
- Rezultate: acuratețe comparabilă cu Decision Tree, robust la granițele între clase.
- **Avantaje:** robust la margini și date multidimensionale.
- **Limitări:** mai greu de interpretat; performanța depinde de kernel și parametri.

### 5. Random Forest Classifier
- Combină mai mulți arbori de decizie pentru a reduce overfitting și a crește acuratețea.
- Rezultate: cel mai bun model din aplicație ca performanță pe setul de test.
- **Avantaje:** robust, performant, mai puțin susceptibil la erori pe datele zgomotoase.
- **Limitări:** mai greu de interpretat decât un singur arbore.

### Observații generale
- Modelele de clasificare (`Decision Tree`, `KNN`, `SVM`, `Random Forest`) au fost aplicate pe **setul de date `diabetes.csv`**.
- Modelul de clustering (`K-Means PCA`) a fost aplicat pe **setul de date `CC GENERAL.csv`** pentru analiza clienților.
- Vizualizările (matrice de confuzie și PCA 2D) permit o interpretare mai intuitivă a rezultatelor.
- Pentru decizii clinice reale sau decizii financiare, aceste modele necesită validare suplimentară și ajustare a hiperparametrilor.
""")
