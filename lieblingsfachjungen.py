import streamlit as st
import pandas as pd
import altair as alt

st.header("Lieblingsfach Jungen")
st.subheader("Was ist Dein Lieblingsfach in der Schule?")

source = pd.DataFrame({
        'Anteil(%)': [41.2, 17.9, 7.2, 4, 3.7, 3.7, 3.5, 3.2, 0.6, 0],
        'Fach': ['Sport', 'Mathematik', 'Deutsch', 'Kunst', 'Sachkunde', 'Erdkunde', 'Biologie', 'Englisch', 'Religion, Ethik', 'Musik']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Fach:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis n=681; 6-12 Jahre; Deutschland
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: iconkids & youth")