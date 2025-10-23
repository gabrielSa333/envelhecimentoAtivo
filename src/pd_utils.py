import pandas as pd
import operator

OPS = {
    "==": operator.eq,
    "!=": operator.ne,
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
}

def compare_numeric(df: pd.DataFrame, col: str, op: str, value: int) -> pd.Series:
    """
    Cria uma série booleana aplicando uma comparação numérica em determinada coluna.
    Exemplo: compare_numeric(df, "C008", ">=", 60)

    Args:
        df (pd.DataFrame): DataFrame base
        col (str): Nome da coluna
        op (str): Operador (==, !=, >, <, >=, <=)
        value (int): Valor numérico

    Raises:
        ValueError: Coluna não encontrada ou Operador inválido.

    Returns:
        pd.Series: Série booleana.
    """
    if col not in df.columns:
        raise ValueError(f"Coluna '{col}' não encontrada.")
    if op not in OPS:
        raise ValueError(f"Operador inválido: {op}")

    col_num = pd.to_numeric(df[col], errors="coerce")
    return OPS[op](col_num, value)

def between_numeric(df: pd.DataFrame, col: str, lower: int, upper: int, inclusive: str = "both") -> pd.Series:
    """
    Cria uma série booleana indicando se os valores da coluna estão entre lower e upper.

    Args:
        df (pd.DataFrame): DataFrame base.
        col (str): Nome da váriavel.
        lower (int | float): Limite inferior.
        upper (int | float): Limite superior.
        inclusive (str): Define se inclui os limites ('both', 'neither', 'left', 'right'). Default = both

    Returns:
        pd.Series: Série booleana.
    """
    if col not in df.columns:
        raise ValueError(f"Coluna '{col}' não encontrada no DataFrame.")

    col_num = pd.to_numeric(df[col], errors="coerce")
    return col_num.between(lower, upper, inclusive=inclusive)

def is_na(df, col: str) -> pd.Series:
    """
    Retorna uma série booleana indicando se a coluna tem valores NA/nulos.

    Args:
        df (pd.DataFrame): DataFrame base
        col (str): Nome da coluna

    Returns:
        pd.Series booleana
    """
    if col not in df.columns:
        raise ValueError(f"Coluna '{col}' não encontrada.")
    return df[col].isna()
