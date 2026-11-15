"""Normaliza registros intermediários; revisar antes de atualizar o JSON público."""
import json
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent / "outputs"

def formatar_data(valor):
    if not isinstance(valor, str):
        return valor
    for formato in ("%d/%m/%Y", "%Y-%m-%d", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(valor, formato).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return valor

def formatar_horario(valor):
    if not isinstance(valor, str):
        return valor
    partes = valor.replace(" às ", " - ").split(" - ")
    if len(partes) != 2:
        return valor
    try:
        return " - ".join(datetime.strptime(p.strip(), "%Hh%M").strftime("%H:%M") for p in partes)
    except ValueError:
        return valor

def padronizar():
    entrada = BASE / "eventos_extraidos.json"
    dados = json.loads(entrada.read_text(encoding="utf-8"))
    registros = dados if isinstance(dados, list) else dados["Sheet1"]
    for evento in registros:
        evento["Data"] = formatar_data(evento.get("Data"))
        evento["Horário"] = formatar_horario(evento.get("Horário"))
    destino = BASE / "eventos_organizados.json"
    destino.write_text(json.dumps(registros, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{len(registros)} registros padronizados em {destino}; revisar antes de publicar.")

if __name__ == "__main__":
    padronizar()
