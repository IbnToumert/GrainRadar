import streamlit as st
import pandas as pd
import datetime

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="GrainRadar | Veille Céréalière", layout="wide", page_icon="🌾")

# --- DONNÉES SIMULÉES (À remplacer par vos API : Refinitiv, OpenWeather, Reuters, etc.) ---
date_jour = datetime.datetime.now().strftime("%d/%m/%Y")

# --- EN-TÊTE ---
st.title("🌾 GrainRadar : Tableau de Bord Stratégique Céréalier")
st.markdown(f"**Date de mise à jour :** {date_jour} | **Focus :** Blé Tendre, Blé Dur, Maïs")
st.divider()

# --- 1. SYNTHÈSE JOURNALIÈRE ---
st.header("📝 Synthèse du Marché Mondial")
st.info("""
**Tendance du jour :** Pression haussière sur le blé tendre suite aux révisions de rendements en Europe de l'Est. 
Le marché du maïs reste stable grâce aux bonnes conditions de semis en Amérique du Sud. Le blé dur maintient des primes élevées en raison des inquiétudes sur la qualité au Canada.
""")

# --- 2. BOURSES MONDIALES (MATIF & CBOT) ---
st.header("📈 Cotations des Grandes Bourses")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Blé Tendre (Euronext/MATIF)")
    st.metric(label="Contrat Rapproché (EUR/t)", value="234.50", delta="+2.50 (1.1%)")
    st.metric(label="CBOT Soft Red Winter (USD/bu)", value="580.25", delta="+4.00")

with col2:
    st.subheader("Blé Dur")
    st.metric(label="FOB Prix indicatif (EUR/t)", value="385.00", delta="-1.50")
    st.metric(label="Bourse de Bologne (EUR/t)", value="390.00", delta="0.00")

with col3:
    st.subheader("Maïs")
    st.metric(label="Euronext (EUR/t)", value="212.00", delta="-0.75")
    st.metric(label="CBOT Corn (USD/bu)", value="452.50", delta="-2.25")

st.divider()

# --- 3. MÉTÉO DES GRANDS PRODUCTEURS ---
st.header("🌤️ Météo & Conditions Agronomiques")
meteo_data = {
    "Région/Pays": ["Russie (Sud)", "États-Unis (Plaines)", "France (Beauce)", "Canada (Prairies)", "Brésil (Mato Grosso)"],
    "Culture Impactée": ["Blé Tendre", "Blé Dur / Maïs", "Blé Tendre", "Blé Dur", "Maïs (Safrinha)"],
    "Condition": ["Déficit hydrique sévère", "Températures optimales", "Excès d'eau", "Sécheresse modérée", "Pluies bénéfiques"],
    "Impact Prix": ["Haussier ↗", "Neutre ➔", "Haussier (Qualité) ↗", "Haussier ↗", "Baissier ↘"]
}
st.dataframe(pd.DataFrame(meteo_data), use_container_width=True, hide_index=True)

col_meteo, col_geopol = st.columns(2)

with col_meteo:
    # --- 4. SITUATION DES PORTS CÉRÉALIERS ---
    st.header("⚓ Trafic et Logistique Portuaire")
    ports_data = {
        "Port": ["Rouen (France)", "Novorossiysk (Russie)", "Odessa (Ukraine)", "Santos (Brésil)", "Vancouver (Canada)"],
        "Statut": ["🟢 Fluide", "🟠 Congestionné", "🔴 Restreint", "🟢 Fluide", "🟠 Retards ferroviaires"],
        "Temps d'attente": ["1-2 jours", "5-7 jours", "Variable", "2-3 jours", "4-6 jours"]
    }
    st.table(pd.DataFrame(ports_data))

with col_geopol:
    # --- 5. GÉOPOLITIQUE ET MACROÉCONOMIE ---
    st.header("🌍 Veille Géopolitique & Réglementaire")
    st.markdown("""
    *   **🔴 Mer Noire :** Nouvelles frappes signalées près des infrastructures portuaires du sud d'Odessa. Les primes de risque d'assurance maritime augmentent de 0.5%.
    *   **🇪🇺 Union Européenne :** La Commission étudie de nouvelles restrictions sur les importations de céréales d'Europe de l'Est pour apaiser les syndicats agricoles.
    *   **🇨🇳 Chine :** Annonce d'un nouveau plan d'achat stratégique de maïs brésilien pour le trimestre prochain, contournant partiellement le marché américain.
    *   **🚢 Canal de Panama :** Les niveaux d'eau s'améliorent, réduisant les restrictions de tirant d'eau pour les vraquiers.
    """)

st.divider()
st.caption("Propulsé par GrainRadar Analytics | Les données affichées sont simulées à des fins de démonstration.")