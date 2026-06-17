Álbum da Copa - Parte 2
Sobre o projeto

Este projeto faz parte da construção de uma API para gerenciamento de figurinhas de um álbum da Copa.

Na Parte 1, os dados eram armazenados em um arquivo JSON.

Nesta Parte 2, o projeto está passando do armazenamento em JSON para PostgreSQL, iniciando a migração para um banco de dados relacional e preparando a aplicação para trabalhar com consultas mais avançadas.

Fluxo atual:

figurinhas.json
        ↓
importar_figurinhas.py
        ↓
PostgreSQL

O objetivo é que, nas próximas etapas, a API deixe de consumir diretamente o JSON e passe a consultar os dados diretamente no banco.

Tecnologias utilizadas
Python
Flask
PostgreSQL
JSON
psycopg2
Git/GitHub

Estrutura do projeto
ALBUM-COPA/
│
├── api.py
├── album.py
├── database.py
├── importar_figurinhas.py
├── figurinhas.json
├── main.py
└── README.md
