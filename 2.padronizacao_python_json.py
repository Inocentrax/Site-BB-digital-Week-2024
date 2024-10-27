import json
from datetime import datetime

with open('3.Informações_Extraídas.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

def formatar_data(data):
    try:
        return datetime.strptime(data, '%d/%m/%Y').strftime('%Y-%m-%d')
    except ValueError:
        return data  

def formatar_horario(horario):
    try:
        partes = horario.split(' - ')
        inicio = datetime.strptime(partes[0], '%Hh%M').strftime('%H:%M')
        fim = datetime.strptime(partes[1], '%Hh%M').strftime('%H:%M')
        return f"{inicio} - {fim}"
    except (ValueError, IndexError):
        return horario  

for evento in data['Sheet1']:
    evento['Data'] = formatar_data(evento['Data'])
    evento['Horário'] = formatar_horario(evento['Horário'])

with open('3.Informações_Extraídas_padronizado.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("JSON padronizado e salvo como '3.Informações_Extraídas_padronizado.json'")
