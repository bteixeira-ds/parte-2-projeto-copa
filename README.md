# Álbum da Copa - Parte 2

## Sobre o projeto

Este projeto faz parte da construção de uma API para gerenciamento de figurinhas de um álbum da Copa.

Na **Parte 1**, os dados eram armazenados em um arquivo **JSON**.

Na **Parte 2**, iniciou-se a migração do projeto para **PostgreSQL**, permitindo que os dados sejam armazenados em um banco de dados relacional e preparando a aplicação para consultas mais avançadas.

---

## Fluxo atual

```text
figurinhas.json
        ↓
importar_figurinhas.py
        ↓
PostgreSQL
```

Objetivo das próximas etapas:

```text
PostgreSQL
        ↓
API Flask
        ↓
JavaScript
        ↓
Interface Web
```

---

## Tecnologias utilizadas

- Python
- Flask
- PostgreSQL
- JSON
- psycopg2
- Git/GitHub

---

## Estrutura do projeto

```text
ALBUM-COPA/
│
├── api.py
├── album.py
├── database.py
├── importar_figurinhas.py
├── figurinhas.json
├── main.py
└── README.md
