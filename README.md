<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/MatMB115/minesweeper_mvc_patterns_com221?color=%2304D361">

<img alt="Repository size" src="https://img.shields.io/github/repo-size/MatMB115/minesweeper_mvc_patterns_com221">

<a href="https://github.com/MatMB115/minesweeper_mvc_patterns_com221/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/MatMB115/minesweeper_mvc_patterns_com221">
  </a>

<img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">
   <a href="https://github.com/MatMB115/minesweeper_mvc_patterns_com221/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/MatMB115/minesweeper_mvc_patterns_com221?style=social">
  </a>
</p>

<p align="center">
  <a href="https://github.com/MatMB115/minesweeper_mvc_patterns_com221">
    <img src="https://imgur.com/mLCTpqG.png" height="185" width="185" alt="MineSweep-logo" />
  </a>
</p>

<p align="center">
    <a href="https://www.python.org/">
        <img align="center" alt="RepiMe-Flutter" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg">
    </a>
</p>

# Minesweeper com designs pattern MVC e Strategy
Campo minado guiado pelos padrões de projeto MVC e Strategy. O jogo foi desenvolvido com Python 3 e a interface gráfica utiliza a biblioteca Qt5 da linguagem.

---
## Sobre

Conforme os conceitos abordados na disciplina de Programação Orientada Objetos II da Universidade Federal de Itajubá ministrada pelo professor [Phyllipe](https://github.com/phillima), a equipe desenvolveu um campo minado com a interface gráfica Qt5 aplicando os padrões de projeto MVC e Strategy. 



As orientações estão divididas nos seguintes tópicos:

- [Funcionalidades](#funcionalidades-gear)
- [MVC](#mvc)
- [Strategy](#strategy-thinking)
- [Pré-requisitos e configuração](#pré-requisitos-e-configuração-hammer_and_wrench)
- [Layout](#layout-art)
- [Tecnologias](#tecnologias-technologist)
- [Contribuidores](#contribuidores)

---
## Funcionalidades :gear:

 - [x] Easy mode com MVC;
 - [x] Mid mode com MVC;
 - [x] Hard mode com MVC;
 - [x] Random mode (usuário insere as dimensões) com MVC;
 - [x] Implantar um timer básico;
 - [x] Timer utilizando os assets;
 - [x] Strategy para saves;
 - [x] Exportar save para JSON;
 - [x] Exportar save para CSV;
 - [x] Exportar save para TXT.

---
## MVC :

O jogo conta com 4 classes principais além da main, a matriz do campo é composta pela classe cell...

![MVCMinesweep](/class_diagram.png)

---
## Strategy :thinking:
Para desenvolver o sistema responsável por salvar o histórico da sessão dos jogadores foi...

---
## Pré-requisitos e configuração :hammer_and_wrench:
No geral, para executar a aplicação é recomendado que o sistema já possua:
- [Python3](https://www.python.org/downloads/);
- Biblioteca Qt5;
- pyInstaller (se desejar gerar um executável para seu sistema);
- [Git](https://git-scm.com/downloads) (opcional caso deseje clonar o repositório);
- [Visual Studio Code](https://code.visualstudio.com/download) (se desejar executar o jogo pelo terminal).

Vale ressaltar que um executável para Windows será disponilibizado na path [Windows](/Windows). 

O campo minado foi testado nos seguintes sistemas operacionais (ambientes de desenvolvimento):
- Windows 10;
- Manjaro KDE;
- Ubuntu 18.04 LTS.

### PyQt5

Para instalar a biblioteca em ambos os ambientes supracitados será necessário abrir um terminal (tanto o bash no Visual Studio Code quanto PowerShell no Windows Terminal servirão). Execute o comando abaixo para instalar a biblioteca:
>pip install pyqt5

Para iniciar o jogo pelo terminal deve-se seguir as instruções abaixo.

```bash

# Clone este repositório com
$ git clone https://github.com/MatMB115/minesweeper_mvc_patterns_com221
# ou
$ git clone git@github.com:MatMB115/minesweeper_mvc_patterns_com221.git

# Acesse a pasta do projeto no seu terminal/cmd
$ cd minesweeper_mvc_patterns_com221

# Acesse a pasta do jogo
$ cd minesweeper

# Chame o interpretador do python 3 com o main.py
$ python3 main.py

# O jogo será iniciado corretamente

```

---
## Layout :art:
Imagens do jogo aqui

---
## Tecnologias :technologist:
    O ponto de início deste projeto foi um ambiente virtual python, as dependências utilizadas estão presentes abaixo.
---
Aplicação:

    -> Python 3.10.8
    - pyQt5
---
Utilitários:

    -> Dev
    - Visual Studio Code 1.73
    - PyCharm 2022.3
---  

## Contribuidores

<table>
  <tr>
    <td align="center"><a href="https://github.com/MatMB115"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/63670910?v=4" width="100px;" alt=""/><br /><sub><b>Matheus Martins</b></sub></a><br /><a href="https://github.com/MatMB115?tab=repositories" title="Minesweep">:technologist:</a></td>
    <td align="center"><a href="https://github.com/ODBreno"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/92598517?v=4" width="100px;" alt=""/><br /><sub><b>Breno Oliveira</b></sub></a><br /><a href="https://github.com/MatMB115/repime" title="RepiMe">:technologist:</a></td>
    <td align="center"><a href="https://github.com/thais-souza311"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/84544053?v=4" width="100px;" alt=""/><br /><sub><b>Thais Souza</b></sub></a><br /><a href="https://github.com/thais-souza311" title="RepiMe">:technologist:</a></td>
    <td align="center"><a href="https://github.com/omateusluz"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/78989307?v=4" width="100px;" alt=""/><br /><sub><b>Matheus Luz</b></sub></a><br /><a href="https://github.com/omateusluz" title="RepiMe">:technologist:</a></td>
  </tr>
</table>
