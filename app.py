import streamlit as st
import pandas as pd
from utils_plots import *
from streamlit_folium import st_folium
import folium


st.set_page_config(page_title='UP Data Visualization',page_icon="assets/logo2.png",layout='wide')


nav = st.sidebar.selectbox("Menu",['Presentación',"Panel 1", "Panel 2", "Panel 3", "Panel 4"])

if nav == "Presentación":
    col1 , col2= st.columns([1,8])
    with col1:
        st.image("assets/logo1.jpeg",width=180)
    with col2:
        st.title("")
        st.title("")
        st.title("")
        st.write("")
        st.write("")
        st.title("Mejorando la Educación en México con IA y Conectividad Satelital")
        st.write("Maestría en Ciencia de Datos")
        st.write("Alumno: Iván Alberto Serrano Zapata")
        st.write("Profesores: Edgar Avalos Gauna y Bernardo Flores Heymann")
        st.write("Materia: Visualización de Datos y Narración de historias")

        st.markdown("""
        ## **Descripción del Proyecto**

        Este proyecto está enfocado en el **rezago educativo en México**, utilizando un enfoque descriptivo para analizar la condición actual de la educación en el país. Posteriormente, se propone una solución para mejorar la educación en comunidades marginadas a través de centros comunitarios que utilicen internet satelital y tutores especializados basados en **IA generativa**.

        ### **Objetivos del Proyecto**
        - **Describir la situación actual** del rezago educativo en México.
        - **Proponer una solución** para mejorar la educación en comunidades marginadas.
        - **Implementar tecnologías avanzadas**, como la IA generativa, para servir de tutores especializados.

        ### **Metodología**
        El proyecto se desarrolló utilizando **Streamlit** y **Plotly** para la creación de visualizaciones interactivas y atractivas. Las fuentes de datos utilizadas incluyen:
        - **INEGI** (Instituto Nacional de Estadística y Geografía)
        - **CONEVAL** (Consejo Nacional de Evaluación de la Política de Desarrollo Social)
        - **Prueba PISA** (Programme for International Student Assessment)

        ### **Tecnologías Utilizadas**
        - **Streamlit**: Una plataforma poderosa y fácil de usar para la creación de aplicaciones web interactivas en Python.
            - Permite desarrollar y desplegar aplicaciones de forma rápida y sencilla.
            - Ofrece soporte para integración con múltiples bibliotecas de visualización como Plotly.
        - **Plotly**: Biblioteca de visualización de datos interactiva que facilita la creación de gráficos y dashboards.

        ### **Enlace al Proyecto**
        Puedes encontrar el código fuente y más detalles sobre el proyecto en mi [GitHub](https://github.com/iserranoz/data_viz_UP).

        """)
        
    
if nav == "Panel 1":
    st.title("Evolución del rezago educativo en México")
    st.title("")

    with st.expander("¿Cómo ha cambiado la tasa de alfabetismo en México en los últimos 20 años?"):
        st.write("""La gráfica muestra la evolución de la tasa de alfabetismo en México desde el año 2000 hasta el 2020. 
                 Se observa un aumento constante en la tasa de alfabetismo, pasando del 90.45% en el año 2000 al 95.04% en el 2020. 
                 Además, se destaca el cambio porcentual en cada periodo,indicando mejoras continuas en los niveles de alfabetización.""")
        st.plotly_chart(plot1(pd.read_csv('data/educacion_clean.csv')),use_container_width=True)

    with st.expander("¿Cómo han evolucionado los años promedio de escolaridad en México en las últimas dos décadas?"):
        st.write("""La gráfica muestra la evolución de los años promedio de escolaridad en México desde el año 2000 hasta el 2020. 
                 Se observa un incremento constante en los años promedio de escolaridad, pasando de 7.5 años en el 2000 a 9.74 años en el 2020. 
                 También se destaca el cambio porcentual en cada periodo quinquenal, reflejando una tendencia de mejora en la educación formal recibida por la población.""")
        st.plotly_chart(plot2(pd.read_csv('data/educacion_clean.csv')),use_container_width=True)

    with st.expander("¿Cuál ha sido la tendencia en la asistencia escolar en México en los últimos 20 años?"):
        st.write("""La gráfica muestra la evolución de la asistencia escolar en México desde el año 2000 hasta el 2020. 
                 Se observa un aumento en la cantidad de estudiantes asistiendo a la escuela, pasando de 27 millones en el 2000 a 
                 31.7 millones en el 2020. Sin embargo, el cambio porcentual de la asistencia escolar muestra una tendencia fluctuante, 
                 con un pico de crecimiento entre 2005 y 2010 y una desaceleración en los años posteriores.""")
        st.plotly_chart(plot3(pd.read_csv('data/educacion_clean.csv')),use_container_width=True)

if nav == "Panel 2":
    st.title("El rezago educativo y la tecnología en México")
    st.title("")
    with st.expander("¿Cómo ha evolucionado el acceso a computadoras e internet en los hogares mexicanos en los últimos años?"):
        st.write("""La gráfica muestra la proporción de hogares con computadora e internet en México desde el año 2015 hasta el 2022. 
                 Se observa un incremento en la disponibilidad de internet en los hogares, que pasó de 39.09% en 2015 a 68.5% en 2022. 
                 En contraste, la proporción de hogares con computadoras ha tenido una ligera fluctuación, manteniéndose relativamente estable en torno al 44-45% durante el mismo periodo.""")
        
        st.plotly_chart(plot4(pd.read_csv('data/tic_com.csv')),use_container_width=True)

    with st.expander("¿Cómo ha cambiado el uso de internet y computadoras entre la población mexicana en los últimos años?"):
        st.write("""La gráfica muestra la proporción de usuarios de internet y computadoras en México desde el año 2015 hasta el 2022. Se observa un notable incremento en el uso de internet, que pasó del 57.35% en 2015 al 78.63% en 2022. 
                 En contraste, el uso de computadoras ha disminuido ligeramente, de un 51.21% en 2015 a un 36.99% en 2022, 
                 reflejando una posible preferencia por otros dispositivos para acceder a internet.""")
        st.plotly_chart(plot5(pd.read_csv('data/tic_com.csv')),use_container_width=True)

    with st.expander("¿Cómo han cambiado los usos de computadoras y teléfonos celulares para apoyo escolar en México en los últimos años?"):
        st.write("""La gráfica muestra la proporción de usuarios que utilizan computadoras para apoyo escolar y aquellos que usan teléfonos celulares en México desde el año 2015 hasta el 2022. 
                 Se observa un aumento continuo en el uso de teléfonos celulares, que pasó del 71.38% en 2015 al 79.24% en 2022. 
                 En contraste, el uso de computadoras para apoyo escolar ha mostrado una ligera fluctuación, manteniéndose alrededor del 46-52% durante el mismo periodo.""")
        st.write("")
        st.plotly_chart(plot6(pd.read_csv('data/tic_com.csv')),use_container_width=True)

if nav == "Panel 3":
    st.title("Otras perspectivas sobre el rezago y la educación en México")
    st.title("")
    
    
    with st.expander("¿Cómo varía el rezago educativo entre los diferentes estados de México y qué cambios se han observado entre 2018 y 2020?"):
        st.write("""La gráfica muestra el porcentaje de rezago educativo por estado en México para los años 2018 y 2020. Se observa una variación significativa entre los estados, 
                 con Chiapas, Oaxaca y Michoacán mostrando los niveles más altos de rezago educativo en ambos años. 
                 Aunque en algunos estados se han visto ligeras mejoras, en otros, el porcentaje de rezago educativo se ha mantenido relativamente constante o incluso ha aumentado.""")
        st.write("")
        st.plotly_chart(plot7(pd.read_csv('data/rezago_educativo_entidad.csv')),use_container_width=True)

    with st.expander("¿Cómo se comparan los puntajes de México en la prueba PISA con el promedio de la OCDE en las áreas de lectura, matemáticas y ciencias?"):
        st.write("""La gráfica compara los puntajes de México en la prueba PISA con el promedio de la OCDE en las áreas de lectura, matemáticas y ciencias desde el año 2005 hasta el 2020. En todas las áreas, se observa que México se encuentra consistentemente por debajo del promedio de la OCDE. 
                 Los puntajes de México muestran una tendencia a la baja, especialmente notable en matemáticas y ciencias, mientras que el promedio de la OCDE también ha mostrado una disminución.""")
        st.plotly_chart(plot9(pd.read_csv('data/data_pisa.csv')),use_container_width=True)

if nav == "Panel 4":
    st.title("Tecnología: Una Solución Prometedora para combatir el Rezago Educativo")
    st.title("")
    st.markdown("""
    ### **Olintla, Puebla**

    Olintla es un pequeño pueblo situado en la Sierra Norte de Puebla, México. Con una población predominantemente indígena, enfrenta desafíos significativos en términos de rezago social y educativo. El acceso limitado a recursos educativos y tecnológicos ha contribuido a altas tasas de analfabetismo y bajos niveles de escolaridad. A pesar de estos obstáculos, la comunidad muestra un fuerte sentido de resiliencia y un deseo creciente de mejorar sus condiciones de vida.
    """)
    col1 , col2= st.columns([2,2])
    location = [20.103276, -97.682447]
    m = folium.Map(location=location, zoom_start=14)
    folium.Marker(location, popup='Olintla Puebla').add_to(m)
    
    with col1:
        col1.title("")
        col1.write("")
        col1.write("")
        st_folium(m, width=700, height=500)

    with col2:
        col2.title("")
        col2.write("")
        col2.write("")
        col2.image("assets/olintla1.jpeg", width=650)

    st.title("")
    st.title("")
    st.markdown("### **Propuesta de Centros Comunitarios con Internet Satelital e Inteligencia Artificial**")
    st.title("")
    col1 , col2= st.columns([2,2])
    with col1:
        col1.image("assets/internet2.jpeg", width=500)

    with col2:
        col2.image("assets/IA2.jpeg", width=650)
    
    st.title("")

    st.markdown("""
    Para abordar el rezago educativo en las comunidades más marginadas de México, proponemos la creación de centros comunitarios equipados con acceso a internet satelital y tutores basados en inteligencia artificial (IA). Estos centros ofrecerán recursos educativos avanzados y personalizados, facilitando el aprendizaje y el desarrollo de habilidades cruciales para los estudiantes.

    #### Beneficios de la Propuesta:
    - **Acceso a Internet Satelital**: Proporciona conectividad en áreas remotas y rurales donde las infraestructuras tradicionales son insuficientes.
    - **Tutores de IA Generativa**: Ofrecen apoyo educativo personalizado, adaptándose a las necesidades individuales de cada estudiante.
    - **Recursos Educativos Modernos**: Facilitan el acceso a contenidos educativos actualizados y de alta calidad.

    Esta iniciativa tiene el potencial de transformar significativamente la educación en comunidades marginadas, reduciendo la brecha educativa y brindando nuevas oportunidades para el desarrollo personal y profesional de los estudiantes.

    """)
        
