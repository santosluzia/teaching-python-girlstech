# Guia: Pip e Ambiente Virtual no Python

## 1. O que é um ambiente virtual?

Um ambiente virtual é um espaço separado para instalar as bibliotecas de um projeto Python.

Isso ajuda a evitar conflitos entre projetos.

Por exemplo:

```text
Projeto A
└── .venv
    ├── pandas
    └── requests

Projeto B
└── .venv
    ├── numpy
    └── flask
```

Cada projeto pode ter suas próprias bibliotecas e versões.

---

## 2. Criando um ambiente virtual

Primeiro, entre na pasta do projeto:

```bash
cd ~/Desktop/teaching-python-girlstech
```

Depois, crie o ambiente virtual:

```bash
python -m venv .venv
```

Isso criará uma pasta chamada `.venv`.

---

## 3. Ativando o ambiente virtual

No Git Bash, no Windows:

```bash
source .venv/Scripts/activate
```

Quando o ambiente estiver ativado, aparecerá algo parecido com:

```text
(teaching-python-girlstech)
```

Isso significa que estamos trabalhando dentro do ambiente virtual.

---

## 4. O que é o pip?

O `pip` é o gerenciador de pacotes do Python.

Ele permite instalar bibliotecas que não fazem parte do Python básico.

Por exemplo:

```bash
python -m pip install requests
```

Nesse caso, estamos instalando a biblioteca `requests`.

---

## 5. Verificando se o pip está instalado

Use:

```bash
python -m pip --version
```

Exemplo:

```text
pip 26.x.x from .../.venv/Lib/site-packages/pip
```

Se aparecer a versão, o `pip` está instalado.

### Importante

O comando:

```bash
python pip --version
```

está errado.

O Python entende `pip` como se fosse um arquivo Python que ele precisa executar.

O correto é:

```bash
python -m pip --version
```

---

## 6. Caso o pip não esteja instalado

Dentro do ambiente virtual, podemos tentar:

```bash
python -m ensurepip --upgrade
```

Depois verifique novamente:

```bash
python -m pip --version
```

---

## 7. Instalando uma biblioteca

Para instalar uma biblioteca:

```bash
python -m pip install requests
```

Outro exemplo:

```bash
python -m pip install pandas
```

Podemos instalar várias de uma vez:

```bash
python -m pip install pandas numpy requests
```

---

## 8. Por que usar `python -m pip`?

Em alguns computadores, principalmente usando Git Bash no Windows, pode acontecer de:

```bash
pip --version
```

retornar:

```text
bash: pip: command not found
```

Mesmo assim, o pip pode estar instalado.

Por isso, uma forma mais segura é:

```bash
python -m pip --version
```

E para instalar:

```bash
python -m pip install requests
```

---

## 9. Listando os pacotes instalados

Para visualizar os pacotes instalados no ambiente virtual:

```bash
python -m pip list
```

Isso mostrará algo parecido com:

```text
Package    Version
---------- -------
pip        26.x
requests   2.x
```

---

## 10. Criando o requirements.txt

O arquivo `requirements.txt` serve para registrar as bibliotecas utilizadas pelo projeto.

Para criar:

```bash
python -m pip freeze > requirements.txt
```

Será criado:

```text
requirements.txt
```

Esse arquivo pode ser enviado junto com o projeto.

---

## 11. Para que serve o requirements.txt?

Imagine que outra pessoa recebeu seu projeto.

Ela pode criar um ambiente virtual e instalar todas as bibliotecas necessárias usando:

```bash
python -m pip install -r requirements.txt
```

Assim, não é necessário instalar cada biblioteca manualmente.

---

## 12. Fluxo completo

### Primeira vez no projeto:

```bash
cd ~/Desktop/teaching-python-girlstech
```

Criar o ambiente:

```bash
python -m venv .venv
```

Ativar:

```bash
source .venv/Scripts/activate
```

Verificar o pip:

```bash
python -m pip --version
```

Instalar uma biblioteca:

```bash
python -m pip install requests
```

Gerar o arquivo de dependências:

```bash
python -m pip freeze > requirements.txt
```

---

## 13. Quando voltar ao projeto

Não é necessário criar o ambiente novamente.

Basta ativá-lo:

```bash
source .venv/Scripts/activate
```

Depois você pode instalar ou utilizar as bibliotecas normalmente.

---

## 14. Desativando o ambiente virtual

Quando terminar de trabalhar:

```bash
deactivate
```

O nome do ambiente:

```text
(teaching-python-girlstech)
```

deixará de aparecer no terminal.

---

# Resumo dos principais comandos

### Criar ambiente virtual

```bash
python -m venv .venv
```

### Ativar no Git Bash

```bash
source .venv/Scripts/activate
```

### Verificar Python

```bash
python --version
```

### Verificar pip

```bash
python -m pip --version
```

### Instalar pacote

```bash
python -m pip install nome-do-pacote
```

### Listar pacotes

```bash
python -m pip list
```

### Gerar requirements.txt

```bash
python -m pip freeze > requirements.txt
```

### Instalar requirements.txt

```bash
python -m pip install -r requirements.txt
```

### Desativar ambiente

```bash
deactivate
```

## Em poucas palavras

```text
venv
↓
cria um ambiente isolado

pip
↓
instala e gerencia bibliotecas

requirements.txt
↓
registra as bibliotecas do projeto
```

O fluxo mais importante para memorizar é:

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install requests
python -m pip freeze > requirements.txt
deactivate
```
