# Gerador de Diagramas de Autômatos

Este projeto é uma aplicação web feita com **Python** e **Streamlit** que permite criar **diagramas de autômatos** a partir da definição de estados, símbolos de entrada e uma tabela de transições.

A ferramenta é ótima para estudantes e profissionais que trabalham com **Autômatos Finitos Determinísticos (AFD)**, **Autômatos Finitos Não Determinísticos (AFN)** e desejam visualizar seus modelos de forma prática.

---

## 🚀 Funcionalidades

- Definir estados e símbolos de entrada manualmente
- Montar a tabela de transições de forma interativa
- Selecionar o estado inicial e estados de aceitação
- Gerar automaticamente o diagrama do autômato
- Salvar o diagrama como imagem `.png` no ambiente local

---

## 🛠️ Tecnologias utilizadas

- Python
- Streamlit
- Graphviz
- Pandas

---

## 📆 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/G0dof/diagram-generator
cd diagram-generator
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

Linux/macOS:
```bash
python -m venv venv
source venv/bin/activate
```

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências Python usando PDM

```bash
pdm install
```

> **Obs**: Certifique-se de que o `pdm` esteja instalado. Caso não esteja, instale com:
>
> ```bash
> pipx install pdm
> ```

### 4. Instale o Graphviz (necessário para gerar o .png)

**Windows:**
- Baixe e instale o Graphviz pelo site oficial: https://graphviz.gitlab.io/_pages/Download/Download_windows.html
- Durante a instalação, selecione a opção para adicionar o Graphviz ao PATH.

**Linux (Ubuntu):**
```bash
sudo apt-get install graphviz
```

**macOS:**
```bash
brew install graphviz
```

---

## ▶️ Como rodar o aplicativo

Depois de instalar tudo:

```bash
pdm run streamlit run src/diagram-generator/main.py
```

---

## 📂 Estrutura do projeto

```
src/
    app.py        # Código principal do Streamlit
README.md
pdm.lock
pyproject.toml
```
