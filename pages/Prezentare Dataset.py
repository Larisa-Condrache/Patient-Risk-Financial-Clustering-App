import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Diabetes Dataset")

df = pd.read_csv("CSVs/diabetes.csv")

st.header("Dataset Overview")
st.subheader("Primele 5 rânduri din dataset")
st.dataframe(df.head())

st.header("Informatie coloane")
st.header("Explicația coloanelor din dataset")

st.markdown("""
### 📊 Coloanele datasetului *Diabetes*

**1. Pregnancies (Număr de sarcini)**  
Reprezintă numărul total de sarcini pe care le-a avut pacienta.

**2. Glucose (Nivelul glucozei)**  
Concentrația glucozei din sânge. Valori ridicate pot indica diabet.

**3. BloodPressure (Tensiunea arterială)**  
Tensiunea arterială diastolică (valoarea mică), măsurată în mm Hg.

**4. SkinThickness (Grosimea pliului cutanat)**  
Grosimea pliului cutanat tricipital, utilizată pentru estimarea grăsimii corporale.

**5. Insulin (Nivelul de insulină)**  
Cantitatea de insulină din sânge măsurată după 2 ore.

**6. BMI (Indicele de masă corporală)**  
Indice calculat ca raport între greutate și înălțime (kg/m²). Un BMI mare crește riscul de diabet.

**7. DiabetesPedigreeFunction (Predispoziție genetică)**  
Scor care indică probabilitatea de diabet pe baza istoricului familial.

**8. Age (Vârsta)**  
Vârsta pacientei, exprimată în ani.

**9. Outcome (Diagnostic)**  
Variabilă țintă:  
- `0` – persoana **nu are diabet**  
- `1` – persoana **are diabet**
""")

df_cc = pd.read_csv("CSVs/CC GENERAL.csv")
st.header("Dataset Credit Card Clients")
st.subheader("Primele 5 rânduri din dataset")
st.dataframe(df_cc.head())

st.header("Informatie coloane - Credit Card Clients")
st.markdown("""
### 📊 Coloanele datasetului *Credit Card Clients*

**1. CUST_ID (ID client)**  
ID unic pentru fiecare client. Folosit doar pentru identificare.

**2. BALANCE (Sold curent)**  
Soldul curent al cardului de credit. Valoarea datorată de client.

**3. BALANCE_FREQUENCY (Frecvența menținerii soldului)**  
Cât de frecvent clientul își menține soldul lunar (0 = niciodată, 1 = constant).

**4. PURCHASES (Total cumpărături)**  
Totalul tuturor cumpărăturilor efectuate cu cardul.

**5. ONEOFF_PURCHASES (Cumpărături într-o singură plată)**  
Cumpărături efectuate într-o singură tranzacție.

**6. INSTALLMENTS_PURCHASES (Cumpărături în rate)**  
Totalul cumpărăturilor efectuate în rate.

**7. CASH_ADVANCE (Retrageri numerar)**  
Sumele retrase în numerar cu cardul de credit.

**8. PURCHASES_FREQUENCY (Frecvența cumpărăturilor)**  
Frecvența totală a tranzacțiilor de cumpărături.

**9. ONEOFF_PURCHASES_FREQUENCY (Frecvența cumpărăturilor one-off)**  
Frecvența plăților unice efectuate cu cardul.

**10. PURCHASES_INSTALLMENTS_FREQUENCY (Frecvența cumpărăturilor în rate)**  
Cât de frecvent clientul face cumpărături în rate.

**11. CASH_ADVANCE_FREQUENCY (Frecvența retragerilor numerar)**  
Cât de des clientul retrage numerar cu cardul.

**12. CASH_ADVANCE_TRX (Număr tranzacții numerar)**  
Numărul total de retrageri de numerar.

**13. PURCHASES_TRX (Număr tranzacții cumpărături)**  
Numărul total de tranzacții de cumpărături (one-off + rate).

**14. CREDIT_LIMIT (Limită card)**  
Limita maximă disponibilă pe cardul de credit.

**15. PAYMENTS (Plăți efectuate)**  
Suma totală plătită pentru reducerea datoriei.

**16. MINIMUM_PAYMENTS (Plată minimă lunară)**  
Suma minimă datorată lunar de client.

**17. PRC_FULL_PAYMENT (Procent plăți integrale)**  
Procentul lunilor în care clientul a plătit integral soldul de pe card.

**18. TENURE (Vechimea contului)**  
Numărul de luni în care clientul a avut cardul de credit.
""")

