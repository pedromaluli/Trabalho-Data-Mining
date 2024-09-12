import pandas as pd

df_original= pd.read_csv("base_dados_original.csv" ,sep=';', decimal='.', encoding='ISO-8859-1', low_memory=False)
df_preparada= pd.read_csv("base_dados_preparada.csv" ,sep=';', decimal='.', encoding='ISO-8859-1')

df_preparada.info()

# # Loop through all object columns
# for col in df_preparada.select_dtypes(include=['object']).columns:
#     # Convert the column to numeric (coerce non-numeric values to NaN)
#     df_preparada[col] = pd.to_numeric(df_preparada[col], errors='coerce')
    
#     # Convert to integers (after filling NaN with a default value, e.g., 0)
#     df_preparada[col] = df_preparada[col].fillna(0).astype(int)
# Loop through all object columns
# for col in df_preparada.select_dtypes(include=['object']).columns:
#     # Try converting the column to numeric
#     try:
#         # If the column can be converted entirely to numeric (ints), convert and fill NaN with 0
#         df_preparada[col] = pd.to_numeric(df_preparada[col], errors='raise').fillna(0).astype(int)
#     except ValueError:
#         # If conversion fails, leave it as object or convert it to string
#         df_preparada[col] = df_preparada[col].astype(str)



# Replace 'column_name' with the name of your column

# print(non_null_count)

int_columns = ["Emissao","Serie","Valor total encerrado da serie","Preco unitario","Quantidade total emitida da serie",
"Valor total emitido da serie","Quantidade total encerrada da serie","Prazo serie","Spread","Juros","Artigo da 12431"]

for col in int_columns:
    df_preparada[col] = pd.to_numeric(df_preparada[col], errors='coerce').fillna(0).astype(int)

    
df_preparada.info()