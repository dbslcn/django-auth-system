# App User - Projeto de Gerenciamento e Integração

Este projeto consiste em uma estrutura baseada em Django com o intuito de gerenciar usuários e integrar dados com o Supabase utilizando uma arquitetura modularizada.

## Estrutura do Projeto

O projeto é baseado no framework web Django e está dividido em algumas aplicações principais e módulos utilitários:

- **Apps Django**: `home`, `accounts`, `logim` e `singup` formam a base em desenvolvimento das funcionalidades da interface e gerenciamento dentro do framework.
- **Configurações (`setup/`)**: Contém as diretrizes e regras centrais do projeto (gerado pelo `django-admin startproject`), roteamento e conexão com o banco local (SQLite).
- **Módulo `utils/`**: Utilitários auxiliares para regras de negócio isoladas das views e models:
  - `SupabaseClient.py`: Cliente HTTP isolado focado em comunicação com a API REST do Supabase via biblioteca `httpx` com configurações baseadas em variáveis de ambiente `.env`.
  - `security.py`: Wrapper para gerenciar facilmente o hash e validação de senhas com segurança, usando `make_password` e `check_password` do Django (com Argon2).
  - `EmailValidator.py`: Validador técnico de e-mails usando serviços de validação de `core` nativos do Django com registro de logs automatizado.
- **`main .py`**: Script de teste e execução primária que simula o fluxo completo de negócio em Python puro usando os utilitários: recebe um e-mail válido, converte uma senha em hash forte e introduz os dados em uma tabela (`profiles`) hospedada no Supabase.

## Dependências e Requisitos

Para funcionamento correto, o ambiente requer certas variáveis preenchidas no arquivo `.env` localizado na raiz do projeto:

- `SUPABASE_URL`
- `SUPABASE_KEY`

As principais dependências do projeto envolvem bibliotecas base como `Django`, abstração de variáveis de ambiente do `python-dotenv` e o cliente de requisições `httpx`.

## Execução

**Para rodar como um projeto Django:**
```bash
python manage.py runserver
```

**Para execução do fluxo de testes em Supabase de forma rápida:**
```bash
python "main .py"
```
