# 🧑‍💻 Sistema de Cadastro de Pessoas

Projeto em Python feito para praticar lógica de programação e manipulação de arquivos.
O sistema roda no terminal e guarda os dados em um arquivo `.txt`.

## ✨ Funcionalidades

- Listar pessoas cadastradas
- Cadastrar novas pessoas
- Remover pessoas com confirmação
- Validar dados de entrada (nome só com letras, idade entre 0 e 120)
- Salvar os dados em arquivo, para não perdê-los ao fechar o programa

## 🛠️ Tecnologias

- Python 3

## ▶️ Como rodar

1. Instale o [Python](https://www.python.org/downloads/)
2. Clone este repositório:
```
   git clone https://github.com/lucasmiguel389/cadastro-pessoas.git
```
3. Entre na pasta do projeto:
```
   cd cadastro-pessoas
```
4. Execute o programa:
```
   python cadastro.py
```

## 📂 Como os dados são guardados

Cada pessoa fica em uma linha do arquivo `pessoas.txt`, com nome e idade separados por `;`:

```
Ana;20
Pedro;35
```

## 📚 O que aprendi

- Funções, listas e dicionários
- Laços `while` e `for`
- Validação de entrada do usuário
- Leitura e escrita de arquivos com `open()`
- Tratamento de erros com `try / except`

## 🚀 Próximas melhorias

- Buscar pessoa pelo nome
- Editar um cadastro existente