import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

# Citim datele
df = pd.read_csv("CSVs/diabetes.csv")

st.header("Model de Clasificare - Decision Tree")

# Setăm variabilele
X = df.drop("Outcome", axis=1)  # caracteristici
y = df["Outcome"]               # țintă

# Împărțim în date de antrenament și test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Cream modelul
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Prezicem
y_pred = clf.predict(X_test)

# Evaluare
accuracy = accuracy_score(y_test, y_pred)
st.write(f"Accuracy: {accuracy*100:.2f}%")

# Matrice de confuzie
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=["No Diabetes","Diabetes"], yticklabels=["No Diabetes","Diabetes"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

# Raport de clasificare
print(classification_report(y_test, y_pred))

st.header("Model de Clasificare - K-Nearest Neighbors (KNN)")

# Radio buttons pentru alegere
option = st.radio(
    "Alege metoda de afișare:",
    ('Predicție KNN pentru un pacient', 'K-Means Clustering clienți')
)

# Funcții KNN
if option == 'Predicție KNN pentru un pacient':
    st.subheader("Exemplu simplu de predicție folosind KNN")

    # Citim datele
    df = pd.read_csv("CSVs/diabetes.csv")

    # Funcție KNN
    def euclidean_distance(point1, point2):
        return np.sqrt(np.sum((np.array(point1) - np.array(point2))**2))

    def knn_predict(training_data, training_labels, test_point, k):
        distances = []
        for i in range(len(training_data)):
            dist = euclidean_distance(test_point, training_data[i])
            distances.append((dist, training_labels[i]))
        distances.sort(key=lambda x: x[0])
        k_nearest_labels = [label for _, label in distances[:k]]
        return Counter(k_nearest_labels).most_common(1)[0][0]

    X_values = df.drop('Outcome', axis=1).values
    Y_values = df['Outcome'].values

    test_patient_data = [1, 148, 72, 35, 0, 33.6, 0.627, 1]  # pacientul de test
    k = 5

    st.write(f"Nr {len(X_values)} pacienți.")
    st.write(f"Punct de test: {test_patient_data}")
    st.write(f"Valoarea k: {k}")

    prediction = knn_predict(X_values, Y_values, test_patient_data, k)

    st.write(f"KNN este: {prediction}")
    if prediction == 1:
        st.error("Pacientul este în risc")
    else:
        st.success("Pacientul nu este în risc")

# functie k-means
elif option == 'K-Means Clustering clienți':
    st.header("Metoda de Clasificare - K-Means Clustering pentru analiza clienților")

    # Citim fișierul corect
    df_cc = pd.read_csv("CSVs/CC GENERAL.csv")

    # Eliminăm coloana ID și completăm valorile lipsă
    df_cc = df_cc.drop("CUST_ID", axis=1)
    df_cc = df_cc.fillna(df_cc.mean())

    features = [
        'BALANCE', 'BALANCE_FREQUENCY', 'PURCHASES', 'ONEOFF_PURCHASES',
        'INSTALLMENTS_PURCHASES', 'CASH_ADVANCE', 'PURCHASES_FREQUENCY',
        'ONEOFF_PURCHASES_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY',
        'CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_TRX', 'PURCHASES_TRX',
        'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT',
        'TENURE'
    ]
    X_cc = df_cc[features]

    # Normalizare
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_cc)

    # Determinarea nr optim de clustere (metoda Elbow)
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, random_state=42)
        kmeans.fit(X_scaled)
        wcss.append(kmeans.inertia_)

    st.subheader("Grafic metoda Elbow")
    fig1, ax1 = plt.subplots()
    ax1.plot(range(1, 11), wcss, marker='o')
    ax1.set_xlabel("Număr de clustere")
    ax1.set_ylabel("WCSS")
    ax1.set_title("Elbow Method")
    st.pyplot(fig1)

    # Aplicare KMeans cu 4 clustere
    kmeans = KMeans(n_clusters=4, random_state=42)
    df_cc['Cluster'] = kmeans.fit_predict(X_scaled)

    st.subheader("Sumar clustere")
    st.dataframe(df_cc.groupby('Cluster')[features].mean())

    # Vizualizare PCA 2D
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    fig2, ax2 = plt.subplots(figsize=(8,6))
    scatter = ax2.scatter(X_pca[:,0], X_pca[:,1], c=df_cc['Cluster'], cmap='rainbow')
    ax2.set_xlabel("PCA 1")
    ax2.set_ylabel("PCA 2")
    ax2.set_title("Distribuția clienților (PCA)")
    st.pyplot(fig2)

# Modele de clasificare SVM
st.header("Model de Clasificare - Support Vector Machine (SVM)")

svm_clf = SVC(kernel='linear', random_state=42)
svm_clf.fit(X_train, y_train)
y_pred_svm = svm_clf.predict(X_test)

accuracy_svm = accuracy_score(y_test, y_pred_svm)
st.write(f"Accuracy SVM: {accuracy_svm*100:.2f}%")

cm_svm = confusion_matrix(y_test, y_pred_svm)
fig1, ax1 = plt.subplots()
sns.heatmap(cm_svm, annot=True, fmt='d', cmap='Blues', xticklabels=["No Diabetes","Diabetes"],
            yticklabels=["No Diabetes","Diabetes"], ax=ax1)
ax1.set_xlabel("Predicted")
ax1.set_ylabel("Actual")
ax1.set_title("Confusion Matrix - SVM")
st.pyplot(fig1)

st.text("Classification Report - SVM")
st.text(classification_report(y_test, y_pred_svm))


# Model random forest
st.header("Model de Clasificare - Random Forest Classifier")

rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
rf_clf.fit(X_train, y_train)
y_pred_rf = rf_clf.predict(X_test)

accuracy_rf = accuracy_score(y_test, y_pred_rf)
st.write(f"Accuracy Random Forest: {accuracy_rf*100:.2f}%")

cm_rf = confusion_matrix(y_test, y_pred_rf)
fig2, ax2 = plt.subplots()
sns.heatmap(cm_rf, annot=True, fmt='d', cmap='Greens', xticklabels=["No Diabetes","Diabetes"],
            yticklabels=["No Diabetes","Diabetes"], ax=ax2)
ax2.set_xlabel("Predicted")
ax2.set_ylabel("Actual")
ax2.set_title("Confusion Matrix - Random Forest")
st.pyplot(fig2)

st.text("Classification Report - Random Forest")
st.text(classification_report(y_test, y_pred_rf))
