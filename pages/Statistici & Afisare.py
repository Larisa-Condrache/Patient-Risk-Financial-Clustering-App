import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv("CSVs/diabetes.csv")

st.header("Statistici generale ale datasetului")

st.write("Statistici descriptive pentru coloanele numerice:")
st.dataframe(df.describe())

st.header("Distribuția pacienților în funcție de Outcome")

chart_type = st.radio(
    "Alege tipul de grafic:",
    ("Grafic bar", "Grafic procentual (pie)")
)

outcome_counts = df["Outcome"].value_counts()

if chart_type == "Grafic bar":
    fig, ax = plt.subplots()
    sns.barplot(
        x=outcome_counts.index,
        y=outcome_counts.values,
        ax=ax
    )
    ax.set_xlabel("Outcome (0 = Fără diabet, 1 = Diabet)")
    ax.set_ylabel("Număr de pacienți")
    ax.set_title("Distribuția pacienților în funcție de diabet")
    st.pyplot(fig)

elif chart_type == "Grafic procentual (pie)":
    fig2, ax2 = plt.subplots()
    ax2.pie(
        outcome_counts.values,
        labels=["Fără diabet (0)", "Cu diabet (1)"],
        autopct="%1.1f%%",
        startangle=90
    )
    ax2.set_title("Procentaj pacienți după Outcome")
    st.pyplot(fig2)

# Distribuția numărului de sarcini (Pregnancies)

st.header("Distribuția numărului de sarcini (Pregnancies)")

fig1, ax1 = plt.subplots()
sns.countplot(x='Pregnancies', data=df, ax=ax1)
ax1.set_xlabel("Număr de sarcini")
ax1.set_ylabel("Număr de pacienți")
ax1.set_title("Distribuția numărului de sarcini")

st.pyplot(fig1)

# Numărul de sarcini pentru pacienții cu diabet

st.header("Numărul de sarcini pentru pacienții cu diabet")

# filtrăm pacienții cu diabet
diabetic_patients_df = df[df['Outcome'] == 1]

# numărăm sarcinile
pregnancies_count_diabetic = (
    diabetic_patients_df['Pregnancies']
    .value_counts()
    .sort_index()
)

fig2, ax2 = plt.subplots(figsize=(12, 6))
pregnancies_count_diabetic.plot(kind='bar', ax=ax2)

ax2.set_title("Numărul de sarcini pentru pacienții cu diabet")
ax2.set_xlabel("Număr de sarcini")
ax2.set_ylabel("Număr de pacienți cu diabet")
ax2.tick_params(axis='x', rotation=0)

st.pyplot(fig2)

# Relația dintre vârstă și nivelul glucozei

st.header("Relația dintre vârstă și nivelul glucozei")

fig3, ax3 = plt.subplots()

ax3.scatter(
    x=df.Age[df.Outcome == 1],
    y=df.Glucose[df.Outcome == 1],
    c="red",
    label="Cu diabet"
)

ax3.scatter(
    x=df.Age[df.Outcome == 0],
    y=df.Glucose[df.Outcome == 0],
    c="blue",
    label="Fără diabet"
)

ax3.set_xlabel("Vârstă")
ax3.set_ylabel("Nivelul glucozei")
ax3.set_title("Age vs Glucose în funcție de Outcome")
ax3.legend()

st.pyplot(fig3)
# Filtrare pacienți după vârstă
st.header("Filtrare pacienți după vârstă")
age_slider = st.slider("Selectează interval vârstă", int(df.Age.min()), int(df.Age.max()), (20, 60))
filtered_df = df[(df.Age >= age_slider[0]) & (df.Age <= age_slider[1])]
st.dataframe(filtered_df)

# Pairplot variabile cheie
st.header("Pairplot variabile cheie")

selected_features = ['Glucose', 'BMI', 'Age', 'BloodPressure', 'Insulin']
fig_pair = sns.pairplot(df[selected_features + ['Outcome']], hue='Outcome', palette='coolwarm')
st.pyplot(fig_pair)

# Boxplot Glucoză vs Outcome
st.header("Distribuția Glucozei în funcție de Outcome")

fig_glu, ax_glu = plt.subplots()
sns.boxplot(x='Outcome', y='Glucose', data=df, ax=ax_glu)
ax_glu.set_xticklabels(["Fără diabet (0)", "Cu diabet (1)"])
ax_glu.set_title("Boxplot Glucoză vs Outcome")
st.pyplot(fig_glu)

# Distribuția BMI-ului
st.header("Distribuția BMI-ului pacienților")

fig_bmi, ax_bmi = plt.subplots()
sns.histplot(df.BMI, bins=20, kde=True, color="purple", ax=ax_bmi)
ax_bmi.set_xlabel("BMI")
ax_bmi.set_ylabel("Număr de pacienți")
ax_bmi.set_title("Distribuția BMI-ului")
st.pyplot(fig_bmi)

# Histogramă pentru o variabilă aleasă
feature = st.selectbox("Alege variabila pentru histogramă", df.columns.drop('Outcome'))
fig, ax = plt.subplots()
sns.histplot(df[feature], bins=20, kde=True, ax=ax)
st.pyplot(fig)

