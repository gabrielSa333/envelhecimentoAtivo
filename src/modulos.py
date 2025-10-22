from enum import Enum

class Modulo(Enum):
    """Enum com o prefixo e descrição dos módulos descritos no dicionário."""
    # Parte 1 - Identificação e controle
    VD = ("VD", "VARIÁVEIS DE AMOSTRAGEM")
    # Parte 2 - Domicílio						
    A = ("A", "Informações do Domicílio")
    B = ("B", "Visitas domiciliares de Equipe de Saúde da Família e Agentes de Endemias")
    # Parte 3 - Questionário do Morador
    C = ("C", "Características gerais dos moradores")
    D = ("D", "Características de educação dos moradores")
    E = ("E", "Características de trabalho das pessoas de 14 anos ou mais de idade")
    F = ("F", "Rendimentos de outras fontes")
    G = ("G", "Pessoas com deficiências (Para pessoas de 2 anos ou mais de idade)")
    I = ("I", "Cobertura de Plano de Saúde")
    J = ("J", "Utilização de serviços de saúde ")
    K = ("K", "Saúde dos indivíduos com 60 anos ou mais")
    L = ("L", "Crianças com menos de dois anos de idade")
    # Parte 4  - Questionário do Morador Selecionado (Para pessoas de 15 anos ou mais de idade)
    M = ("M", "Características do trabalho e apoio social")
    N = ("N", "Percepção do estado de saúde")
    O = ("O", "Acidentes")
    P = ("P", "Estilos de vida")
    Q = ("Q", "Doenças crônicas")
    R = ("R", "Saúde da Mulher (Para mulheres de 15 anos ou mais de idade)")
    S = ("S", "Atendimento Pré-Natal  (Para mulheres de 15 anos ou mais de idade)")
    U = ("U", "Saúde Bucal")
    Z = ("Z", "Paternidade e Pré-natal do parceiro (Para homens de 15 anos ou mais)")
    V = ("V", "Violência (Para pessoas de 18 anos ou mais de idade)")
    T = ("T", "Doenças transmissíveis")
    Y = ("Y", "Atividade sexual (Para pessoas de 18 anos ou mais de idade)")
    H = ("H", "Atendimento médico (Para pessoas de 18 anos ou mais de idade)")
    W = ("W", "ANTROPOMETRIA")
    X = ("X", "")

    def __init__(self, prefixo, descricao):
        self.prefixo = prefixo
        self.descricao = descricao

    def __str__(self):
        return f"{self.prefixo - self.descricao}"