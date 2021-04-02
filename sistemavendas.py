
# Sistema de Vendas

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import time
import plotly.express as px
import colorsys
import plotly.offline as py
import plotly.graph_objs as go
import seaborn as sns

# Limpa os objetos do python
import gc

# função para carregar o dataset
@st.cache




def get_data():
    

    def totvendas(ano):
    
        #print(categ)
        datasetz=dataset.loc[dataset['ano']==ano]
    
        vlvenda=datasetz['ValorVenda'].sum()
        #somavalor=float(ab[0])
        #somavalor=float(ab[0])
        return vlvenda #somavalor

    
    dataset_original=pd.read_csv('Vendas.csv',sep=';',encoding='latin-1',decimal=",")
    dataset=dataset_original  #.copy()

    dataset['Data Venda']=pd.to_datetime(dataset['Data Venda'],format='%d/%m/%Y') #Converter o campo em data
    dataset['ano']=dataset['Data Venda'].dt.year
    dataset['mes']=dataset['Data Venda'].dt.month


    dataset_novo1=dataset.drop_duplicates(subset=['ano'])

                                              
    dataset_novo1['Totalvendas']=dataset_novo1['ano'].apply(totvendas)

    titulo='Total de Vendas por ANO '
    fig = go.Figure([go.Bar(x=dataset_novo1['ano'], y=dataset_novo1['Totalvendas'])])
    fig.update_layout(title='Total de vendas por ano',
    xaxis_title='Ano',
    yaxis_title='Total de Vendas')
    #fig.show()

    return fig
 
def get_data2():
    

    def totalvendas(categ):
        
        datasetz=dataset.loc[dataset['Categoria']==categ]
    
        ab=datasetz['ValorVenda'].sum()
        #somavalor=float(ab[0])
        #somavalor=float(ab[0])
        return ab #somavalor


    dataset=pd.read_csv('Vendas.csv',sep=';',encoding='latin-1',decimal=",")
    

    dataset['Data Venda']=pd.to_datetime(dataset['Data Venda'],format='%d/%m/%Y') #Converter o campo em data


    dataset['ano']=dataset['Data Venda'].dt.year
    dataset['mes']=dataset['Data Venda'].dt.month

    dataset_novo=dataset.drop_duplicates(subset=['Categoria'])

    dataset_novo['Totalvendas']=dataset_novo['Categoria'].apply(totalvendas)
    dataset_novo=dataset_novo.sort_values(['ano'],ascending=[False])

    layout = go.Layout(title='Total de Vendas por Categoria',
                    barmode='group',
                    xaxis=dict(title='Categoria'),yaxis=dict(title='Valor Total de Vendas'))

    fig = go.Figure(data=go.Bar(x=dataset_novo['Categoria'],y=dataset_novo['Totalvendas']), layout=layout)

    return fig


def get_data3():
    
    dataset_original=pd.read_csv('Vendas.csv',sep=';',encoding='latin-1',decimal=",") #decimal converte a virgula em ponto

    def somarx(unico):
        ab=0
        #print('somarx',vano,vcateg)
        datasetxx=dataset1.loc[dataset1['unico']==unico ]
        #datasetxx2=datasetxx.loc[datasetxx['Categoria']==vcateg]    
        ab=datasetxx['ValorVenda'].sum()
        #print(ab)
        #somavalor=float(ab[0])
        #somavalor=float(ab[0])
        return ab #somavalor


    dataset1=dataset_original.copy() # dataset geral

    dataset1['Data Venda']=pd.to_datetime(dataset1['Data Venda'],format='%d/%m/%Y') #Converter o campo em data


    #dataset1['ano']=dt.datetime.strptime(dataset1['Data Venda'],'%Y')
    dataset1['ano']=dataset1['Data Venda'].dt.year
    dataset1['mes']=dataset1['Data Venda'].dt.month


    dataset1 = dataset1.astype({'ano': str, 'mes': str})
    dataset1['unico']=dataset1['ano']+dataset1['Categoria']


    dataset_ano=dataset1.drop_duplicates(subset=['ano','Categoria'])

    #Retira os duplicados
    dataset_novo=dataset1.drop_duplicates(subset=['ano','Categoria'])


    #Criar total de vendas de ano por categoria
    dataset_novo['tot_vendas_ano_cat']=dataset_novo['unico'].apply(somarx)
    dataset_novo1=dataset_novo.sort_values(['ano'])


    ds_ano=dataset_novo1['ano'].unique().tolist()


    data=[]

    for vano in ds_ano:
        df_temp=dataset_novo1.loc[dataset_novo1['ano']==vano] 
        vtot = df_temp['tot_vendas_ano_cat']
        final_df = pd.DataFrame({'Categoria': df_temp['Categoria'],'Valor':vtot})
        trace1=go.Bar(x=final_df['Categoria'],y=final_df['Valor'],name=vano)
        data.append(trace1)
        #del df_temp
        
    layout = go.Layout(
        title='Relatório de Vendas por Categorias por Ano',
        barmode='group',
        xaxis=dict(title='Ano por Categoria'),yaxis=dict(title='Valor de Vendas'))

    fig = go.Figure(data=data, layout=layout)

    return fig


def get_data4():
    
    dataset_original=pd.read_csv('Vendas.csv',sep=';',encoding='latin-1',decimal=",") #decimal converte a virgula em ponto

    def somarx(unico):
        ab=0
        #print('somarx',vano,vcateg)
        datasetxx=dataset1.loc[dataset1['unico']==unico ]
        #datasetxx2=datasetxx.loc[datasetxx['Categoria']==vcateg]    
        ab=datasetxx['ValorVenda'].sum()
        #print(ab)
        #somavalor=float(ab[0])
        #somavalor=float(ab[0])
        return ab #somavalor


    dataset1=dataset_original.copy() # dataset geral

    dataset1['Data Venda']=pd.to_datetime(dataset1['Data Venda'],format='%d/%m/%Y') #Converter o campo em data


    #dataset1['ano']=dt.datetime.strptime(dataset1['Data Venda'],'%Y')
    dataset1['ano']=dataset1['Data Venda'].dt.year
    dataset1['mes']=dataset1['Data Venda'].dt.month


    dataset1 = dataset1.astype({'ano': str, 'mes': str})
    dataset1['unico']=dataset1['ano']+dataset1['Categoria']


    dataset_ano=dataset1.drop_duplicates(subset=['ano','Categoria'])

    #Retira os duplicados
    dataset_novo=dataset1.drop_duplicates(subset=['ano','Categoria'])


    #Criar total de vendas de ano por categoria
    dataset_novo['tot_vendas_ano_cat']=dataset_novo['unico'].apply(somarx)
    dataset_novo1=dataset_novo.sort_values(['ano'])



    ds_categ=dataset_novo1['Categoria'].unique().tolist()



    data=[]

    for vcateg in ds_categ:
        df_temp=dataset_novo1.loc[dataset_novo1['Categoria']==vcateg]
        vtot = df_temp['tot_vendas_ano_cat']
        final_df = pd.DataFrame({'ano': df_temp['ano'],'Valor':vtot})
        trace1=go.Bar(x=final_df['ano'],y=final_df['Valor'],name=vcateg)#,text=status)
        data.append(trace1)   
        #del df_temp
        

    layout = go.Layout(
        title='Relatório de ano por Categoria',
        barmode='group',
        xaxis=dict(title='Ano por Categoria'),yaxis=dict(title='Valor de Vendas'))

    fig = go.Figure(data=data, layout=layout)

    return fig

######################################
# Inicio do programa
######################################

st.image('img1.png')
#col1, col2, col3 = st.beta_columns(3)
#foto = Image.open('foto.png')
#inserindo na coluna 2
#col2.image(foto, use_column_width=True)



# título
st.title("Análise das vendas da redeX")

# subtítulo
st.markdown("Relatórios gerencias para apoio a tomada de decisão")

st.sidebar.subheader("Aperte o botão para gerar os relatórios")
#data_hoje = datetime.date.today()
#ontem = datetime.timedelta(days=1)
#data_selecionada = st.sidebar.date_input('Data', data_hoje)

# inserindo um botão na tela
btn_predict = st.sidebar.button("Mostrar Relatórios")

# verifica se o botão foi acionado
if btn_predict:
    
    data = get_data()
    st.plotly_chart(data)

    data2=get_data2()
    st.plotly_chart(data2)
    
    data3=get_data3()
    st.plotly_chart(data3)
    
    data4=get_data4()
    st.plotly_chart(data4)

