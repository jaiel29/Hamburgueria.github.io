# Sistema de Hamburgueria

## Escopo

- **Objetivo:**

Desenvolver um sistema de gestão para uma hamburgueria, visando otimizar seus processos de atendimento e eliminar o uso do papel. A meta é criar uma plataforma intuitiva e eficiente que facilite o gerenciamento das operações do estabelecimento, aumentando sua produtividade e satisfação do cliente.

- **Requisitos funcionais:**
- **Requisitos não funcionais:**

## Equipe Responsável

- [Alberto Ziurkelis de Araujo](https://github.com/AlbertZiurk) --> Back-End
- [Alex Abel Costa Silva](https://github.com/AllexAbel) --> Front-End
- [Beatriz Kelly Lopes Rocha](https://github.com/beatrizklr) --> DBA/QA
- [Bianca Vieira Santos](https://github.com/bincst18) --> Web Designer
- [Cauê Alves Barreto]() --> DBA
- [Jaiel Johabe Macedo Barboza](https://github.com/jaiel29)  --> QA
- [João Vitor Alves de Alencar](https://github.com/alzolansk) --> Backend
- [Kauhã Conceição de Moura](https://github.com/Kauhacdm) --> Front-End
- [Lucas Rocha Santos](https://github.com/1lsantos) --> QA
- [Raquel Santos Vieira](https://github.com/Raquel0612) --> Web Designer/DBA
- [Samuel Boldieri Monteiro](https://github.com/destru345) --> Front-End
- [Túlio Custódio Nassif](https://github.com/tuliocns) --> Gerente

## Estrutura de Pastas utilizando o plano de arquitetura MVC (Model-View-Controller)
- .gitignore
- .gitattributes
- .env
- Model
    - config.py
- View
    - css
    - images
    - pages
- Controller
    - app.py

## Stack utilizada





| **Front-end** | **Back-end** | **SGBD** | **Web Designer** | **Modelagem de Dados** | 
|-----------|----------| ---------- | --- | --- |
|[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ||[![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)|[![MySQL](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)|[![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?&style=for-the-badge&logo=Canva&logoColor=white)](https://img.shields.io/badge/Canva-%2300C4CC.svg?&style=for-the-badge&logo=Canva&logoColor=white)|[Draw.io](https://app.diagrams.net/)
|[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)||[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
|[![JS](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)|

## Paleta de cores e formato de texto
| Cor Primária     | Código Hexadecimal |
| --------------- || ------------------ |
| Amarelo Dourado  | #E1A83A            |
| Cinza Escuro     | #B4ADAD            |
| Vermelho Escuro  | #880016            |

| Cor Secundária      | Código Hexadecimal|
| ------------------ || ----------------- |
| Branco              | #000000           |
| Preto               | #FFFFFF           |
| Azul Marinho        | #004AAD           |
| Vermelho Escarlate  | #FF3131           |
| Verde Limão         | #29D825           |

- Fonte padrão de texto: Sans-Serif

## Instalação de dependências do projeto
- [pip](https://pip.pypa.io/en/stable/installation/)
- [pip install mysql-connector-python](https://www.geeksforgeeks.org/how-to-install-mysql-connector-package-in-python/)
- [pip install Flask](https://flask.palletsprojects.com/en/2.3.x/installation/)
- [pip install python-dotenv](https://pypi.org/project/python-dotenv/)

## Variáveis de Ambiente
_Certifique-se de definir os campos de chave e valor, em seu repositório local, com base nos parâmetros definidos no banco de dados utilizado._

- HOST_NAME --> host do banco
- USER_NAME --> nome do usuário de SGBD
- PWD_NAME --> senha do SGBD
- DB_NAME --> nome do banco


## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/AlbyOrganization/Hamburgueria.github.io.git
```

Entre no diretório do projeto

```bash
  cd my-project
```

Instale as dependências (certifique-se de ter o python instalado)

```bash
  pip install mysql-connector-python
  pip install Flask
  pip innstall python-dotenv
```
Crie um arquivo .env.local no Model e defina as variáveis locais

```bash
  HOST_NAME= 'nome da conexão de host'
  USER_NAME= 'nome do usuário'
  PWD_NAME='senha do banco'
  DB_NAME='nome do banco'
```