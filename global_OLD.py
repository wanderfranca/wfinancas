import pandas as pd
import os

if ("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()):
    df_despesas = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=True)
    df_receitas = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=True)

else:
    data_structure = {
        'Valor':[],
        'Efetuado':[],
        'Fixo':[],
        'Data':[],
        'Categoria':[],
        'Descricao':[],
    }
    df_receitas = pd.DataFrame(data_structure)
    df_despesas = pd.DataFrame(data_structure)
    df_despesas.to_csv("df_despesas.csv")
    df_receitas.to_csv("df_receitas.csv")

if ("df_cat_receita.csv" in os.listdir()) and ("df_cat_despesa.csv" in os.listdir()):
    df_cat_receita = pd.read_csv("df_cat_receita.csv", index_col=0, parse_dates=True)
    df_cat_despesa = pd.read_csv("df_cat_despesa.csv", index_col=0, parse_dates=True)
    cat_receita = df_cat_receita.values.tolist()

else:
    cat_receita = {'Categoria': ["Salario", "Investimento", "Comissão", "Serviço Extra", "Bônus"]}
    cat_despesa = {'Categoria': ["Alimentação", "Aluguel", "Internet", "Combustível", "Saúde", "Lazer"]}

    df_cat_receita = pd.DataFrame(cat_receita)
    df_cat_despesa = pd.DataFrame(cat_despesa)
    df_cat_receita.to_csv("df_cat_receita.csv")
    df_cat_despesa.to_csv("df_cat_despesa.csv")