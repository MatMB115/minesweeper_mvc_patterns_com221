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

- [Minesweeper com designs pattern MVC e Strategy](#minesweeper-com-designs-pattern-mvc-e-strategy)
  - [Sobre](#sobre)
  - [Funcionalidades :gear:](#funcionalidades-gear)
  - [MVC:](#mvc)
  - [Strategy :thinking:](#strategy-thinking)
  - [Pré-requisitos e configuração :hammer\_and\_wrench:](#pré-requisitos-e-configuração-hammer_and_wrench)
    - [PyQt5](#pyqt5)
  - [Layout :art:](#layout-art)
  - [Tecnologias :technologist:](#tecnologias-technologist)
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
## MVC:

O núcleo da aplicação foi construída nas classes Model, View, Controller e Cell. 

- **Cell**: classe de suma importância, compõe as células que geram um campo minado e armazena os atributos e funções essenciais para validar a lógica do jogo;

- **Model**: classe que implementa a lógica do jogo, define a estrutura e as funcionalidades, desde a definição do que tem no jogo até as dificuldades, formas de salvar, implementação de regras e tudo o que for necessário para o funcionamento do jogo;

- **Controller**: A controller funciona como uma ponte entre a View e a Model, seria mais um nível de abstração, fazendo com que a View utilize das funções da Model sem conhecê-las. No caso desse projeto a controller faz a chamada das funções da model quando um evento ocorre na view, por exemplo, se um jogador clica em uma determinada dificuldade na interface da view, ela chama a função da controller que cria um novo jogo nessa dificuldade, todavia, essa função da controller não implementa a criação desse novo jogo na nova dificuldade, ela apenas chama as funções da model necessárias para realizar tal tarefa passando os parâmetros da view, como a nova dificuldade;

- **View**: A View é a parte estética do projeto, implementa a interface gráfica e processa os eventos e interações do usuário chamando a controller, que por sua vez chama as funções que estão implementadas na Model, no nosso projeto toda a implementação da interface gráfica com PyQT está nessa classe;


![MVCMinesweep](/class_diagram.png)

---
## Strategy :thinking:
Conforme o UML acima, foi necessário criar uma classe de contexto SaveGame, uma vez que python não reserva uma palavra chave para interfaces. Essa classe fica incumbida de conectar a model com a implementação do strategy pela classe (interface) TypeFile, permitindo que o usuário troque a implementação concreta do atributo TypeFile na model em tempo de execução. 

O jogo permite que o usuário exporte o histórico de vitórias com o tempo de jogo para os arquivos do tipo: JSON, CSV e TXT.
    
Export do save como JSON:

<p align="center">
  <img alt="export_json" title="#export_json" src="https://user-images.githubusercontent.com/84544053/205668163-7aaf6d81-5040-4708-a088-0ed29a36b87a.png" width="500px">
</p>

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
- Windows 11;
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

# Para linux
$ python3 main.py

# Para Windows
$ py main.py

# O jogo será iniciado corretamente

```

---
## Layout :art:
O jogo conta com uma tela principal que possui o campo minado usando assets inspirados no grandioso Minesweeper do Windows 95, um contador de bombas, um botão de status/start e um timer. Há também três botões na menubar para mudar o modo de jogo, exportar o histórico e sair da aplicação.

<p align="center">
  <img alt="RepiMe" title="#First" src="https://user-images.githubusercontent.com/84544053/205647262-0156348f-290f-4044-a404-4c28f3e5a49b.png" width="200px">

  <img alt="RepiMe" title="#HomeNoLogin" src="https://user-images.githubusercontent.com/84544053/205645834-4e1a015b-0001-4611-bcc8-b1cb1af386c3.png" width="200px">
  
  <img alt="RepiMe" title="#HomeLogin" src="https://user-images.githubusercontent.com/84544053/205646117-6d1b73e7-bff6-4f15-9b4e-031a7beffee4.png" width="200px">

  <img alt="RepiMe" title="#UserRegister" src="https://user-images.githubusercontent.com/84544053/205646550-20fb1d7a-4d39-4dc4-b3c9-aa44fdba7182.png" width="200px">

  <img alt="RepiMe" title="#UserRegister2" src="https://user-images.githubusercontent.com/84544053/205647466-ae247fe5-30fd-4a0b-869b-55559832508a.png" width="200px">
  
  <img alt="RepiMe" title="#VagaRegist" src="https://user-images.githubusercontent.com/84544053/205647878-fb04ab1c-3ae8-4a74-8571-26aa6a993742.png" width="200px">
</p>

<p align="center">
  <img alt="RepiMe" title="#UserRegister3" src="https://user-images.githubusercontent.com/84544053/205651917-a7d9d6bf-1376-4186-8661-1ab502b63bf3.png" width="385px">

  <img alt="RepiMe" title="#VagaRegist2" src="https://user-images.githubusercontent.com/84544053/205651671-26ba86c0-26b9-4531-9067-d37476a60d45.png" width="400px">
</p>

---
## Tecnologias :technologist:
    O ponto de início deste projeto foi um ambiente virtual python, as dependências utilizadas estão presentes abaixo.
---
Aplicação:

    -> Python 3.10.8
    - pyQt5
    - pip
    - pyInstaller
    - Virtual environment
    - csv
    - json
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

Repositório dedicado para o versionamento do campo minado desenvolvido usando os design patterns.
