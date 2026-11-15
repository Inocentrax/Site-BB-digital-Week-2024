# Agenda web — BB Digital Week 2024

Agenda histórica com 173 registros de eventos em JSON, busca, filtros e ordenação, desenvolvida em HTML, CSS e JavaScript.

**Status:** Aplicação de estudo · dados históricos de 2024.

[← Catálogo de projetos e estudos](https://github.com/Inocentrax/portfolio-dados)

---

Interface para consultar a programação organizada do BB Digital Week 2024. A base atual contém **173 registros** no JSON versionado. O fluxo de extração original está no [projeto PDF → Excel](https://github.com/Inocentrax/Cronograma-BB-Digital-Week-2024).

## Executar localmente

A aplicação usa `fetch` para carregar o JSON: abra por um servidor HTTP, não diretamente por `file://`. Com Python disponível:

```bash
python -m http.server 8000
```

Acesse `http://localhost:8000`. A página oferece busca, filtros por data/local/palestrante/trilha e ordenação.

## Estrutura

| Arquivo | Responsabilidade |
|---|---|
| [index.html](index.html) | Interface e filtros |
| [script.js](script.js) | Carregamento, filtro, ordenação e cartões |
| [3.Eventos_Organizados.json](3.Eventos_Organizados.json) | Base consumida pelo site |
| [1ConversorExcelpJson.py](1ConversorExcelpJson.py) | Conversão da planilha em registros JSON |
| [2.padronizacao_python_json.py](2.padronizacao_python_json.py) | Normalização de datas e horários |

## Preparar novos dados

```bash
python -m pip install -r requirements.txt
python 1ConversorExcelpJson.py
python 2.padronizacao_python_json.py
```

Os scripts leem `0.Informações_Extraídas.xlsx` e geram intermediários em `outputs/`. Revise o resultado antes de substituir o JSON usado pelo site.

## Próximos passos

- [ ] Separar título da palestra e lista de palestrantes no esquema dos dados.
- [ ] Gerar opções dos filtros a partir do JSON em vez de manter listas manuais.
- [ ] Conferir se os 173 registros correspondem a eventos únicos ou a partes de eventos.
- [ ] Acrescentar mensagem visível para falha de carregamento e resultado vazio.

Projeto pessoal de organização de uma programação histórica; não é um canal oficial do evento.
