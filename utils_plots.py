import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

## PLOT 1

def plot1(df):
    df['Year'] = pd.to_datetime(df['Year'])
    df['Tasa de Alfabetismo Rounded'] = df['Tasa de Alfabetismo'].round(2)
    df['Tasa de Alfabetismo Text'] = df['Tasa de Alfabetismo Rounded'].apply(lambda x: f"{x}%")

    fig1 = make_subplots(specs=[[{"secondary_y": True}]])
    fig1.add_trace(
        go.Bar(x=df['Year'], y=df['Tasa de Alfabetismo Rounded'], name='Tasa de Alfabetismo',
            text=df['Tasa de Alfabetismo Text'], textposition='auto', marker_color='rgb(255, 204, 153)'),
        secondary_y=False,
    )
    fig1.add_trace(
        go.Scatter(x=df['Year'], y=df['Cambio % Tasa de Alfabetismo'], name='Cambio % Tasa de Alfabetismo',
                mode='lines+markers', line=dict(color='rgb(176, 224, 230)', width=2)),
        secondary_y=True,
    )
    fig1.update_layout(
        title_text="Tasa de Alfabetismo y Cambio Porcentual",
        template='plotly_white',
        legend_title='Indicador'
    )
    fig1.update_yaxes(title_text="Tasa de Alfabetismo (%)", range=[70, 100], secondary_y=False)
    fig1.update_yaxes(title_text="Cambio Porcentual (%)", range=[0, 2.5], secondary_y=True)

    return fig1

## PLOT 2

def plot2(df):
    df['Años Promedio de Escolaridad Rounded'] = df['Años Promedio de Escolaridad'].round(2)
    df['Años Promedio de Escolaridad Text'] = df['Años Promedio de Escolaridad Rounded']
    df['Cambio % Años de Escolaridad Text'] = df['Cambio % Años de Escolaridad'].round(2).astype(str)

    fig2 = make_subplots(specs=[[{"secondary_y": True}]])
    fig2.add_trace(
        go.Bar(x=df['Year'], y=df['Años Promedio de Escolaridad Rounded'], name='Años Promedio de Escolaridad',
            text=df['Años Promedio de Escolaridad Text'], textposition='auto', marker_color='rgb(173, 216, 230)'),
        secondary_y=False,
    )
    fig2.add_trace(
        go.Scatter(x=df['Year'], y=df['Cambio % Años de Escolaridad'], name='Cambio % Años de Escolaridad',
                mode='lines+markers', text=df['Cambio % Años de Escolaridad Text'], 
                line=dict(color='rgb(100, 149, 237)', width=2)),
        secondary_y=True,
    )
    fig2.update_layout(
        title_text="Años Promedio de Escolaridad y Cambio Porcentual",
        template='plotly_white',
        legend_title='Indicador'
    )
    fig2.update_yaxes(title_text="Años Promedio de Escolaridad", secondary_y=False)
    fig2.update_yaxes(title_text="Cambio Porcentual (%)", range=[4, 10], secondary_y=True)

    return fig2

## PLOT 3

def plot3(df):
    df['Asistencia Escolar Rounded'] = (df['Asistencia Escolar'] / 1e6).round(1)
    df['Asistencia Escolar Text'] = df['Asistencia Escolar Rounded'].apply(lambda x: f"{x}M")
    df['Cambio % Asistencia Escolar Text'] = df['Cambio % Asistencia Escolar'].round(2).astype(str) + '%'

    fig3 = make_subplots(specs=[[{"secondary_y": True}]])
    fig3.add_trace(
        go.Bar(x=df['Year'], y=df['Asistencia Escolar Rounded'], name='Asistencia Escolar',
            text=df['Asistencia Escolar Text'], textposition='auto', marker_color='rgb(144, 238, 144)'),
        secondary_y=False,
    )
    fig3.add_trace(
        go.Scatter(x=df['Year'], y=df['Cambio % Asistencia Escolar'], name='Cambio % Asistencia Escolar',
                mode='lines+markers', text=df['Cambio % Asistencia Escolar Text'], 
                line=dict(color='rgb(60, 179, 113)', width=2)),
        secondary_y=True,
    )
    fig3.update_layout(
        title_text="Asistencia Escolar y Cambio Porcentual",
        template='plotly_white',
        legend_title='Indicador'
    )
    fig3.update_yaxes(title_text="Asistencia Escolar (Millones)", secondary_y=False)
    fig3.update_yaxes(title_text="Cambio Porcentual (%)", range=[-2, 10], secondary_y=True)

    return fig3

## PLOT 4

def plot4(df):
    df.rename(columns={
        'Hogares con computadora como proporción del total de hogares - Porcentaje de hogares - Estados Unidos Mexicanos': 'Proporción de Hogares con Computadora',
        'Hogares con conexión a Internet como proporción del total de hogares - Porcentaje de hogares - Estados Unidos Mexicanos': 'Proporción de Hogares con Internet',
        'Unnamed: 0': 'Año'
    }, inplace=True)

    df['Proporción de Hogares con Computadora'] = df['Proporción de Hogares con Computadora'].round(2)
    df['Proporción de Hogares con Internet'] = df['Proporción de Hogares con Internet'].round(2)

    fig4 = go.Figure()

    fig4.add_trace(
        go.Bar(
            x=df['Año'], 
            y=df['Proporción de Hogares con Computadora'], 
            name='Hogares con Computadora',
            marker_color='rgb(255, 192, 203)', 
            text=df['Proporción de Hogares con Computadora'],
            textposition='auto'
        )
    )
    fig4.add_trace(
        go.Bar(
            x=df['Año'], 
            y=df['Proporción de Hogares con Internet'], 
            name='Hogares con Internet',
            marker_color='rgb(173, 216, 230)', 
            text=df['Proporción de Hogares con Internet'],
            textposition='auto'
        )
    )
    fig4.update_layout(
        title_text="Proporción de Hogares con Computadora e Internet",
        xaxis_title="Año",
        yaxis_title="Porcentaje de Hogares",
        template='plotly_white',
        barmode='group',
        legend_title='Indicador'
    )

    return fig4

## PLOT 5

def plot5(df):
    df.rename(columns={
    'Usuarios de Internet como proporción de la población de seis años o más de edad - Porcentaje de usuarios - Estados Unidos Mexicanos': 'Proporción de Usuarios de Internet',
    'Usuarios de computadora como proporción de la población de seis años o más de edad - Porcentaje de usuarios - Estados Unidos Mexicanos': 'Proporción de Usuarios de Computadora',
    'Unnamed: 0': 'Año'
    }, inplace=True)

    
    df['Proporción de Usuarios de Internet'] = df['Proporción de Usuarios de Internet'].round(2)
    df['Proporción de Usuarios de Computadora'] = df['Proporción de Usuarios de Computadora'].round(2)

    fig5 = go.Figure()

    fig5.add_trace(
        go.Bar(
            x=df['Año'], 
            y=df['Proporción de Usuarios de Internet'], 
            name='Usuarios de Internet',
            marker_color='rgb(255, 223, 186)',  # Color naranja pastel
            text=df['Proporción de Usuarios de Internet'],
            textposition='auto'
        )
    )
    fig5.add_trace(
        go.Bar(
            x=df['Año'], 
            y=df['Proporción de Usuarios de Computadora'], 
            name='Usuarios de Computadora',
            marker_color='rgb(255, 250, 205)', 
            text=df['Proporción de Usuarios de Computadora'],
            textposition='auto'
        )
    )
    fig5.update_layout(
        title_text="Proporción de Usuarios de Internet y Computadora",
        xaxis_title="Año",
        yaxis_title="Porcentaje de la Población",
        template='plotly_white',
        barmode='group',  
        legend_title='Indicador'
    )

    return fig5

## PLOT 6   

def plot6(df):
    df.rename(columns={
    'Usuarios de computadora que la usan como herramienta de apoyo escolar como proporción del total de usuarios de computadora - Porcentaje de usuarios - Estados Unidos Mexicanos': 'Usuarios de Computadora en Apoyo Escolar',
    'Usuarios de teléfono celular como proporción de la población de seis años o más de edad - Porcentaje de usuarios - Estados Unidos Mexicanos': 'Usuarios de Teléfono Celular',
    'Unnamed: 0': 'Año'
    }, inplace=True)

    df['Usuarios de Computadora en Apoyo Escolar'] = df['Usuarios de Computadora en Apoyo Escolar'].round(2)
    df['Usuarios de Teléfono Celular'] = df['Usuarios de Teléfono Celular'].round(2)

    fig6 = go.Figure()

    fig6.add_trace(
        go.Bar(
            x=df['Año'], 
            y=df['Usuarios de Computadora en Apoyo Escolar'], 
            name='Usuarios de Computadora en Apoyo Escolar',
            marker_color='rgb(216, 191, 216)', 
            text=df['Usuarios de Computadora en Apoyo Escolar'],
            textposition='auto'
        )
    )

    fig6.add_trace(
        go.Bar(
            x=df['Año'], 
            y=df['Usuarios de Teléfono Celular'], 
            name='Usuarios de Teléfono Celular',
            marker_color='rgb(144, 238, 144)', 
            text=df['Usuarios de Teléfono Celular'],
            textposition='auto'
        )
    )

    fig6.update_layout(
        title_text="Proporción de Usuarios de Computadora en Apoyo Escolar y Teléfono Celular",
        xaxis_title="Año",
        yaxis_title="Porcentaje de Usuarios",
        template='plotly_white',
        barmode='group', 
        legend_title='Indicador'
    )

    return fig6

## PLOT 7

def plot7(df):
    fig7 = go.Figure()

    fig7.add_trace(
        go.Bar(
            x=df['Entidad'],
            y=df['Porcentaje 2018'],
            name='2018',
            marker_color='rgb(173, 216, 230)',
            text=df['Porcentaje 2018'],
            textposition='auto'
        )
    )
    fig7.add_trace(
        go.Bar(
            x=df['Entidad'],
            y=df['Porcentaje 2020'],
            name='2020',
            marker_color='rgb(100, 149, 237)', 
            text=df['Porcentaje 2020'],
            textposition='auto'
        )
    )
    fig7.update_layout(
        title_text="Porcentaje de Rezago Educativo por Estado: 2018 vs 2020",
        xaxis_title="Entidad",
        yaxis_title="Porcentaje de Rezago Educativo",
        template='plotly_white',
        barmode='group',
        legend_title='Año'
    )

    return fig7

## PLOT 8

def plot8(df):
    df_grouped = df.groupby('Zona').agg({
    'Porcentaje 2018': 'mean',
    'Porcentaje 2020': 'mean'
    }).reset_index()

    fig8 = go.Figure()

    fig8.add_trace(
        go.Bar(
            x=df_grouped['Zona'],
            y=df_grouped['Porcentaje 2018'],
            name='2018',
            marker_color='rgb(255, 182, 193)', 
            text=df_grouped['Porcentaje 2018'].round(2).astype(str) + '%',
            textposition='auto'
        )
    )
    fig8.add_trace(
        go.Bar(
            x=df_grouped['Zona'],
            y=df_grouped['Porcentaje 2020'],
            name='2020',
            marker_color='rgb(240, 128, 128)', 
            text=df_grouped['Porcentaje 2020'].round(2).astype(str) + '%',
            textposition='auto'
        )
    )
    fig8.update_layout(
        title_text="Promedio de Rezago Educativo por Zona: 2018 vs 2020",
        xaxis_title="Zona",
        yaxis_title="Porcentaje Promedio de Rezago Educativo",
        template='plotly_white',
        barmode='group',
        legend_title='Año',
        width=1200,
        height=500
    )

    return fig8

## PLOT 9

def plot9(df):
    # Configurar el tema de Plotly para colores suaves y agradables
    colors = {
        'Mexico': 'rgba(31, 119, 180, 0.8)',  # Azul suave
        'OCDE': 'rgba(255, 191, 0, 0.8)'     # Amarillo suave
    }

    fig9 = make_subplots(rows=1, cols=3, subplot_titles=("Lectura", "Matemáticas", "Ciencias"))

    fig9.add_trace(
        go.Scatter(x=df['Año'], y=df['Lectura'], mode='lines+markers', name='Mexico', 
                   line=dict(color=colors['Mexico']), marker=dict(color=colors['Mexico']),showlegend=True),
        row=1, col=1
    )
    fig9.add_trace(
        go.Scatter(x=df['Año'], y=df['Promedio OCDE Lectura'], mode='lines+markers', name='Promedio OCDE',
                   line=dict(color=colors['OCDE']), marker=dict(color=colors['OCDE']),showlegend=True),
        row=1, col=1
    )

    fig9.add_trace(
        go.Scatter(x=df['Año'], y=df['Matemáticas'], mode='lines+markers', name='Mexico Matemáticas',
                   line=dict(color=colors['Mexico']), marker=dict(color=colors['Mexico']),showlegend=False),
        row=1, col=2
    )
    fig9.add_trace(
        go.Scatter(x=df['Año'], y=df['Promedio OCDE Matemáticas'], mode='lines+markers', name='OCDE Matemáticas',
                   line=dict(color=colors['OCDE']), marker=dict(color=colors['OCDE']),showlegend=False),
        row=1, col=2
    )

    fig9.add_trace(
        go.Scatter(x=df['Año'], y=df['Ciencias'], mode='lines+markers', name='Mexico Ciencias',
                   line=dict(color=colors['Mexico']), marker=dict(color=colors['Mexico']),showlegend=False),
        row=1, col=3
    )
    fig9.add_trace(
        go.Scatter(x=df['Año'], y=df['Promedio OCDE Ciencias'], mode='lines+markers', name='OCDE Ciencias',
                   line=dict(color=colors['OCDE']), marker=dict(color=colors['OCDE']),showlegend=False),
        row=1, col=3
    )

    fig9.update_layout(
        title_text='Comparación de Puntajes Prueba PISA: México vs OCDE',
        template='plotly_white',
        height=600,
        showlegend=True
    )

    fig9.update_xaxes(title_text='Año')
    fig9.update_yaxes(title_text='Puntaje')

    return fig9