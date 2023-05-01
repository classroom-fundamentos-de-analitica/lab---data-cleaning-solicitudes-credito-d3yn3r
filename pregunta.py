"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    
    df.monto_del_credito = df.monto_del_credito.str.replace(',','') 
    df.monto_del_credito = df.monto_del_credito.str.strip('$')
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.monto_del_credito = df.monto_del_credito.astype(int)

    df.dropna(axis=0, inplace=True)

    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, dayfirst=True)  

    colString = df.select_dtypes(include=['object']).columns.tolist()
    
    for i in colString:
        df[i] = df[i].str.lower()
        df[i] = df[i].replace('-',' ')
        df[i] = df[i].replace('_',' ')
    
    df.drop_duplicates(inplace=True)

    return df