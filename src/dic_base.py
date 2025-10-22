import pandas as pd
from modulos import Modulo

class DicBase:
    """Classe responsável por interagir com o dicionário de variáveis.
    """
    def __init__(self, path="dicionario_tratado.csv"):
        self.df = pd.read_csv(path)
        self.colspecs = []
        self.names = []
        self._process_dic()

    def _process_dic(self):
        dic_vars = (
            self.df.groupby('Código da variável', as_index=False)
            .agg({'Posição inicial':'first', 'Tamanho':'first'})
            .rename(columns={'Código da variável':'var'})
        )

        dic_vars['Posição inicial'] = dic_vars['Posição inicial'].astype('Int64')
        dic_vars['Tamanho'] = dic_vars['Tamanho'].astype('Int64')
        dic_vars['start0'] = dic_vars['Posição inicial'] - 1
        dic_vars['end0']   = dic_vars['start0'] + dic_vars['Tamanho']

        self.colspecs = list(zip(dic_vars['start0'].astype(int), dic_vars['end0'].astype(int)))
        self.names = dic_vars['var'].tolist()
        self.dic_vars = dic_vars

    def get_vars_by_module(self, *modulos: Modulo):
        """Retorna as variáveis do dicionário de um determinado módulo.

        Args:
            *modulos (Modulo): Um ou mais módulos do Enum Modulo.

        Returns:
            list: Todas as variáveis que começam com o prefixo de  qualquer módulo informado.
        """
        if not modulos:
            raise ValueError("Informe pelo menos um módulo (ex: Modulo.S ou Modulo.S, Modulo.C).")
        
        prefixos = []
        for m in modulos:
            if hasattr(m, "prefixo"):
                prefixos.append(m.prefixo)
            elif isinstance(m, str):
                prefixos.append(m)
            else:
                prefixos.append(m.name)

        regex = "^(" + "|".join(prefixos) + ")"
        mask = self.dic_vars["var"].str.match(regex)
        return self.dic_vars.loc[mask, "var"].tolist()