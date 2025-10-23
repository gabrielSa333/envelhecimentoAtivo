import os, pandas as pd
from dic_base import DicBase
from modulos import Modulo
from pathlib import Path
import numpy as np

def parse_dicionario():
    print("=> Parse dicionário.")
    df = pd.read_excel("dicionario_PNS_microdados_2019.xls", skiprows=1, header=0)
    df.columns = df.columns.str.replace('\n', ' ').str.strip()
    df = df.rename(columns={
        'Unnamed: 4': 'Descrição quesito',
        'Categorias': 'Tipo categoria',
        'Unnamed: 6': 'Descrição categoria'
    })
    df = df[~df['Posição inicial'].astype(str).str.contains('Parte|Módulo', case=False, na=False)]
    df = df.dropna(how='all')
    df = df.drop(index=0)
    df.to_csv("dicionario_tratado.csv", index=False, encoding="utf-8")
    cols_to_ffill = ['Posição inicial', 'Tamanho', 'Código da variável', 'Quesito', 'Descrição quesito']
    df[cols_to_ffill] = df[cols_to_ffill].ffill()
    print(df.iloc[2])
    print("Fim parse dicionário.")

def parse_data(chunksize):
    print("=> Inicializando leitura e persistência dos dados em chunks.")
    dic = DicBase()

    reader = pd.read_fwf(
        "PNS_2019.txt",
        colspecs=dic.colspecs,
        names=dic.names,
        dtype=str,
        encoding="utf-8",
        chunksize=chunksize
    )

    for i, chunk in enumerate(pd.read_fwf("PNS_2019.txt",
                                      colspecs=dic.colspecs, names=dic.names,
                                      dtype=str, encoding="utf-8",
                                      chunksize=50_000)):
        print(f"- Chunk: {i}")
        chunk.to_parquet(f"out_parquet/part-{i:04d}.parquet",
                        engine="pyarrow", compression="snappy", index=False)
        print(f"- Fim chunk: {i}")

    print("Fim da persistência de dados.")

if __name__ == "__main__":
    parse_dicionario()
    os.makedirs("out_parquet", exist_ok=True)
    parse_data(50_000) # ALTERE O chunksize de acordo com o que seu computador suporta

