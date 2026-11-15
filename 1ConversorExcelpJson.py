"""Converte a planilha histórica em registros JSON sem sobrescrever a base do site."""
import json
from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent
SAIDA = BASE / "outputs"

def converter():
    SAIDA.mkdir(exist_ok=True)
    df = pd.read_excel(BASE / "0.Informações_Extraídas.xlsx")
    registros = df.astype(object).where(df.notna(), None).to_dict(orient="records")
    destino = SAIDA / "eventos_extraidos.json"
    destino.write_text(json.dumps(registros, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    print(f"{len(registros)} registros exportados para {destino}")

if __name__ == "__main__":
    converter()
