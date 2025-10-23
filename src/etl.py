import os, pandas as pd
from dic_base import DicBase
from modulos import Modulo

if __name__ == "__main__":
    print("=> Inicializa dicionário.")
    dic = DicBase()
    print("Fim dicionário.")

    print("=> mkdir")
    os.makedirs("out_parquet", exist_ok=True)

    # ALTERE O chunksize de acordo com o que seu computador suporta
    print("=> Inicializando leitura e persistência dos dados em chunks.")
    reader = pd.read_fwf(
        "PNS_2019.txt",
        colspecs=dic.colspecs,
        names=dic.names,
        dtype=str,
        encoding="utf-8",
        chunksize=50_000
        # usecols=dic.get_vars_by_module(Modulo.S, Modulo.V)  # opcional: especificar os módulos
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
