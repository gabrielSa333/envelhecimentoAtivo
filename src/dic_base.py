import pandas as pd
from modulos import Modulo

class DicBase:
    """Classe responsável por interagir com o dicionário de variáveis.
    """
    def __init__(self, path="dicionario_tratado.csv"):
        self.df = pd.read_csv(path)
        self.colspecs = []
        self.names = []
        self.code_maps = {}
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

        self.df['Tipo categoria'] = self.df['Tipo categoria'].astype('string')
        self.df['Descrição categoria'] = self.df['Descrição categoria'].astype('string')

        for var, g in self.df.groupby('Código da variável'):
            if not g.empty:
                codigos = g['Tipo categoria'].astype(str).str.strip()
                descricoes = g['Descrição categoria'].astype(str).str.strip()
                self.code_maps[var] = dict(zip(codigos, descricoes))

    def get_vars_by_module(self, *modulos: Modulo):
        """Retorna as variáveis do dicionário de um determinado módulo. Pode ser utilizado para extrair colunas específicas do dataframe

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
    
    def describe_var(self, codigo: str):
        """Exibe informações descritivas da variável

        Args:
            codigo (str): Código da variável. (ex: 'V0001', 'V0024', 'C008')
        """

        if codigo not in self.df['Código da variável'].unique():
            print(f"Variável '{codigo}' não encontrada no dicionário.")
            return
        
        var_info = self.df[self.df['Código da variável'] == codigo]
        descricao = var_info['Descrição quesito'].dropna().unique()
        descricao = descricao[0].strip() if len(descricao) > 0 else "(sem descrição)"

        print(f"\n {codigo} — {descricao}")
        g = var_info[['Tipo categoria', 'Descrição categoria']].dropna(how='all')
        if not g.empty:
            print("Valores possíveis:")
            for _, row in g.iterrows():
                tipo = str(row['Tipo categoria']).strip()
                desc = str(row['Descrição categoria']).strip()
                if tipo == "nan" or desc == "nan":
                    continue
                print(f"  {tipo:>3} → {desc}")
        else:
            print("(sem categorias associadas)")