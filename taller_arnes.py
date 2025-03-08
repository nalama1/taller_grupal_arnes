import streamlit as st
import joblib
import numpy as np 

model_filename = 'arnes.pkl'
loaded_model = joblib.load(model_filename) 

st.title('Compra de Arneses y Botas para perros')
st.header("Tienda Super Can 🐶 ")
st.subheader("Ingrese los datos de su perro")
st.write("""
             *******************************
             
             Autor:  Nalama1 
             
    **Repositorio:** [GitHub - grupo2](https://github.com/nalama1/taller_grupal_arnes)
    """)


with st.form(key='perritos-pred-form'):
    col1, col2 = st.columns(2)
    
    arnes = col1.slider(label='Tamaño del arnés:', min_value=0, max_value=100)
    botas = col2.text_input(label='Tamaño de la Bota:')
    submit = st.form_submit_button(label='Check')
    
    if submit:
        inputs = np.array(arnes).reshape(-1, 1)
        predicted_boot_size = int(loaded_model.predict(inputs)[0])
        st.write("El tamaño de bota recomendado es: ", predicted_boot_size)            
               
        try:
            botas = int(botas)  
        except ValueError:
            st.error("Ingrese un número válido para el tamaño de la bota.")            
        
        if botas == predicted_boot_size:
            st.success("¡Gran elección! 🐶🎉 Creemos que estas botas se adaptarán bien a su perro.", icon="✅")
        if botas > predicted_boot_size:
            st.error("⚠️ ¡Cuidado! 🐾 Las botas que has seleccionado podrían ser DEMASIADO GRANDES para un perro tan "\
                       f" pequeño como el suyo. Recomendamos unas botas de tamaño {predicted_boot_size}", icon="⚠️")
        elif botas < predicted_boot_size:
            st.warning("❌ Las botas que has seleccionado podrían ser DEMASIADO PEQUEÑAS para un perro tan "\
                       f" grande como el suyo. Recomendamos unas botas de tamaño {predicted_boot_size} 🐕🔍")
                
                
 
