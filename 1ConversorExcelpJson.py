import pandas as pd

excel_path = "3.Informações_Extraídas.xlsx"  
df = pd.read_excel(excel_path)

json_data = df.to_dict(orient="records")

with open("events_data.json", "w", encoding="utf-8") as json_file:
    import json
    json.dump(json_data, json_file, ensure_ascii=False, indent=4)

print("Arquivo JSON gerado com sucesso!")
