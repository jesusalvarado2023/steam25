import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Función para simular el lanzamiento de dos dados
def lanzar_dados(n_lanzamientos):
    resultados = []
    for _ in range(n_lanzamientos):
        dado1 = np.random.randint(1, 7)
        dado2 = np.random.randint(1, 7)
        suma = dado1 + dado2
        resultados.append(suma)
    return resultados

# Configuración de la aplicación Streamlit
st.title("Generador de Gráficas de Frecuencia de Lanzamientos de Dos Dados")

# Entrada de número de lanzamientos
n_lanzamientos = st.number_input("Selecciona el número de lanzamientos", min_value=1, max_value=10000, value=1000)

# Botón para generar gráfico
if st.button("Generar Gráfico"):
    # Lanzamos los dados y obtenemos los resultados
    resultados = lanzar_dados(n_lanzamientos)

    # Creamos el gráfico de frecuencias
    fig, ax = plt.subplots()
    sns.histplot(resultados, bins=np.arange(2, 14) - 0.5, kde=False, ax=ax, color='skyblue')
    
    ax.set_title(f"Frecuencia de Sumas de {n_lanzamientos} Lanzamientos de Dos Dados")
    ax.set_xlabel("Suma de los Dados")
    ax.set_ylabel("Frecuencia")
    
    # Mostramos el gráfico en la aplicación
    st.pyplot(fig)

    # Mostrar estadísticas
    suma_mas_probable = max(set(resultados), key=resultados.count)
    st.write(f"La suma más probable en los lanzamientos es: {suma_mas_probable}")
