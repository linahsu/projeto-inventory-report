# Boas-vindas ao repositório do projeto Inventory Report!

🧑‍💻 Neste projeto, foi desenvolvido um **gerador de relatórios**. O objetivo foi receber arquivos contendo informações sobre um estoque específico e, em seguida, produzir um relatório abrangente com base nesses dados. Esses dados de estoque podem ser obtidos de duas fontes:

* Através da importação de um arquivo `CSV`;

* Através da importação de um arquivo `JSON`;

Além disso, o relatório final possuirá duas versões: **simples** e **completa**.

## Detalhes

<details>
  <summary><strong> 📝 Habilidades trabalhadas </strong></summary>
  <br />

* Aplicar conceitos de Programação Orientada a Objetos em Python;

* Implementar leitura e escrita de arquivos `CSV` e `JSON` em Python;

</details>

<details>
  <summary><strong>🗃️ Arquivos com os dados de entrada</strong></summary><br />

#### Confira o exemplo de formato dos arquivos:

<strong>Arquivos CSV</strong>
Os arquivos **CSV** são separados por vírgula, como no exemplo abaixo:

```CSV
id,product_name,company_name,manufacturing_date,expiration_date,serial_number,storage_instructions
1,cadeira,Target Corporation,2021-02-18,2025-09-17,CR25,empilhadas
2,mesa,"Galena Madeira, Inc.",2022-12-06,2026-12-25,FR29,desmontadas
3,abajur,Keen Iluminação,2019-12-22,2025-11-07,CZ09,em caixas
```

<strong>Arquivos JSON</strong>
Os arquivos JSON seguem o seguinte modelo:

```json
[
    {
        "id": "1",
        "product_name": "Borracha",
        "company_name": "Papelaria Solar",
        "manufacturing_date": "2021-07-04",
        "expiration_date": "2029-02-09",
        "serial_number": "FR48",
        "storage_instructions": "Ao abrigo de luz solar"
    }
]
```

</details>

## Orientações 😉

<details>
<summary><strong>🛼 Como executar o projeto</strong></summary>
  <br />

1. Clone o repositório

-   Use o comando: `git clone git@github.com:linahsu/projeto-inventory-report.git`
-   Entre na pasta do repositório que você acabou de clonar:
    -   `cd projeto-inventory-report`

2. Crie o ambiente virtual para o projeto

```bash
python3 -m venv .venv && source .venv/bin/activate
```

3. Instale as dependências

```bash
python3 -m pip install -r dev-requirements.txt
```

4. O programa deverá ser executável <strong>via linha de comando</strong>.

O comando a ser executado será `ir`. Para que ele funcione em seu ambiente é preciso antes instalar o próprio código como um pacote pip:
<code>pip install .</code>

Agora você poderá chamar o comando `ir` passando seus argumentos:

<code>ir - p `argumento1` -t `argumento2`</code>

-   **argumento1** deve receber o caminho de um diretório com os arquivos de estoque à serem importados. Os arquivos dentro do diretório podem ser `csv`s ou `json`s.

-   **argumento2** pode receber duas strings: `simple` ou `complete`, cada uma gerando o respectivo tipo de relatório.

</details>

<details>
<summary><strong>🎛 Linter</strong></summary>
  <br />

Para garantir a qualidade do código, foi utilizado nesse projeto o linter `Flake8`, sendo alinhado com as boas práticas de desenvolvimento, sendo mais legível e de fácil manutenção! Para poder executar o `Flake8`, certifique-se de que o ambiente virtual foi criado e está ativo dentro do repositório.

Para rodá-lo localmente no repositório, execute o comando a seguir:

```bash
python3 -m flake8
```

Se a análise do `Flake8` encontrar problemas no código, tais problemas serão mostrados no terminal. Se não houver problema no código, nada será impresso no terminal.

</details>

<details>
  <summary><strong>🛠 Testes</strong></summary>
  <br />

Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

<strong>Executar os testes</strong>

```bash
python3 -m pytest
```

O arquivo `pyproject.toml` já configura corretamente o `pytest`. Entretanto, caso você queira que os testes gerem uma saída mais verbosa completa, o comando é:

```bash
python3 -m pytest -s -vv
```

O `pytest` possui diversos parâmetros que podem ser utilizados para executar os testes de diferentes formas. Alguns exemplos são:

```bash
python3 -m pytest tests/test_nome_do_arquivo.py  # Executa todos os testes do arquivo de testes especificado
python3 -m pytest tests/test_nome_do_arquivo.py::test_nome_do_teste  # Executa apenas o teste especificado
python3 -m pytest -k expressao  # Executa apenas os testes que contém a expressão informada como substring
python3 -m pytest -x  # Executa os testes até encontrar o primeiro erro
```

</details>

<details>
  <summary><strong>🐳 Docker</strong></summary>
  <br />
  Caso queria executar os testes do projeto via `docker-compose`, ao invés de no ambiente virtual, execute o comando:

```bash
docker-compose run --rm inventory pytest
```

</details>