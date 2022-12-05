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
Para desenvolver o sistema responsável por salvar o histórico da sessão dos jogadores vamos exemplicar sucintamente demonstrando a implementação de um exemplo do histórico e, em seguida, as chamadas das funções...

---
Implementação:

    -> Classe para o arquivo JSON
    
    class To_json(TypeFile):
    def create_file(self, model):
        json_dict = {}
        if len(model.playersEasy) != 0:
            easy_dict = {"NamePlayer": "PlayTime"}
            for player in model.playersEasy:
                easy_dict[player.get_nome()] = player.get_time()
            json_dict["Easy"] = easy_dict

        if len(model.playersMid) != 0:
            mid_dict = {"NamePlayer": "PlayTime"}
            for player in model.playersMid:
                mid_dict[player.get_nome()] = player.get_time()
            json_dict["Mid"] = mid_dict

        if len(model.playersHard) != 0:
            hard_dict = {"NamePlayer": "PlayTime"}
            for player in model.playersHard:
                hard_dict[player.get_nome()] = player.get_time()
            json_dict["Hard"] = hard_dict

        if len(model.playersRandom) != 0:
            rand_dict = {"NamePlayer": "PlayTime"}
            for player in model.playersRandom:
                rand_dict[player.get_nome()] = player.get_time()
            json_dict["Random"] = rand_dict

        json_obj = json.dumps(json_dict, indent=4)
        with open("historico.json", "w") as outfile:
            outfile.write(json_obj)
        outfile.close()
        
        
        -> Classe para Salvar o Jogo
        
        class SaveGame:
    strategy: TypeFile

    def __init__(self, strategy: TypeFile = None):
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = To_json()

    def start_save(self, model):
        self.strategy.create_file(model)
        
    
---
Imagem do Resultado:
 
 
![image](https://user-images.githubusercontent.com/84544053/205668163-7aaf6d81-5040-4708-a088-0ed29a36b87a.png)


---
Funções:

    -> Salvar no formato JSON
        def save_as_json(self):
        self.model.save.strategy = To_json()
        self.model.save_state()
        
     -> Salvar no formato CSV
        def save_as_csv(self):
        self.model.save.strategy = To_csv()
        self.model.save_state()
        
      -> Salvar no formato TXT
        def save_as_txt(self):
        self.model.save.strategy = To_txt()
        self.model.save_state()

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

# Para linux
$ python3 main.py

# Para Windows
$ py main.py

# O jogo será iniciado corretamente

```

---
## Layout :art:
![image](https://user-images.githubusercontent.com/84544053/205647262-0156348f-290f-4044-a404-4c28f3e5a49b.png)
![image](https://user-images.githubusercontent.com/84544053/205645834-4e1a015b-0001-4611-bcc8-b1cb1af386c3.png)
![image](https://user-images.githubusercontent.com/84544053/205646117-6d1b73e7-bff6-4f15-9b4e-031a7beffee4.png)
![image](https://user-images.githubusercontent.com/84544053/205646550-20fb1d7a-4d39-4dc4-b3c9-aa44fdba7182.png)
![image](https://user-images.githubusercontent.com/84544053/205647466-ae247fe5-30fd-4a0b-869b-55559832508a.png)
![image](https://user-images.githubusercontent.com/84544053/205651917-a7d9d6bf-1376-4186-8661-1ab502b63bf3.png)
![image](https://user-images.githubusercontent.com/84544053/205646782-f06088b4-2209-4bb8-bc54-2bb9b31cc0c7.png)
![image](https://user-images.githubusercontent.com/84544053/205647878-fb04ab1c-3ae8-4a74-8571-26aa6a993742.png)
![image](https://user-images.githubusercontent.com/84544053/205651671-26ba86c0-26b9-4531-9067-d37476a60d45.png)




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
