# 🔐 Gerador de Senhas Seguro

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/Tkinter-GUI-blueviolet?style=for-the-badge" alt="Tkinter">
  <img src="https://img.shields.io/badge/Segurança-100%25%20Local-success?style=for-the-badge" alt="Segurança Local">
</p>

Um gerador de senhas moderno, minimalista e **extremamente seguro**, desenvolvido em Python. O projeto conta com duas formas de uso: uma interface de linha de comando (CLI) rápida e uma interface gráfica (GUI) elegante e intuitiva em modo escuro.

---

## 📖 Sobre o Projeto

A geração de senhas seguras é essencial para proteger suas contas digitais. Este projeto foi construído sob uma **arquitetura unificada**, onde a inteligência matemática de criptografia e aleatoriedade fica centralizada no backend (`main.py`) e pode ser consumida tanto pelo terminal quanto pelo aplicativo visual de mesa (`gui.py`).

Diferente de geradores web comuns, este aplicativo roda **100% localmente no seu computador**. Suas senhas nunca viajam pela internet, garantindo imunidade total contra interceptações de rede.

---

## ⚡ Recursos Principais

- **Garantia de Requisitos:** Ao marcar critérios como Letras Maiúsculas, Minúsculas, Números ou Símbolos, a lógica garante que **pelo menos um** caractere de cada categoria escolhida estará presente na senha final.
- **Embaralhamento Seguro:** Utiliza a biblioteca padrão `random` para misturar a posição dos caracteres garantidos, evitando padrões previsíveis.
- **Medidor de Força em Tempo Real (Exclusivo GUI):** Um algoritmo calcula a entropia da senha com base no tamanho e variedade de caracteres, exibindo um status visual dinâmico:
  - 🔴 **Fraca**
  - 🟠 **Média**
  - 🟢 **Forte**
  - 🔵 **Muito Forte**
- **Cópia Instantânea:** Copie a senha gerada para a área de transferência com um único clique.
- **Design Premium Dark:** Interface gráfica construída no Tkinter com foco em contraste moderno (paleta Slate-900 com destaque em verde esmeralda).

---

## 🛠️ Como Executar

### 1. Interface Gráfica (Recomendado)
Para abrir a janela interativa com slider, caixas de seleção e medidor de força visual:

```bash
python3 gui.py
```

### 2. Interface de Linha de Comando (Terminal)
Caso prefira gerar senhas de forma extremamente rápida diretamente pelo terminal:

```bash
python3 main.py
```

---

## 📂 Estrutura de Arquivos

```text
├── main.py          # O backend de geração de senhas e a versão de terminal (CLI)
├── gui.py           # O frontend visual desktop construído com o Tkinter (GUI)
├── .gitignore       # Arquivo de proteção do Git para ignorar caches temporários
└── README.md        # Documentação do projeto (este arquivo!)
```

---

## 🚀 Tecnologias Utilizadas

- **[Python](https://www.python.org/):** Linguagem principal do projeto.
- **[Tkinter](https://docs.python.org/3/library/tkinter.html):** Toolkit gráfico nativo do Python para a criação da interface do usuário.
- **[Random & String](https://docs.python.org/3/library/index.html):** Módulos nativos de tratamento de caracteres e aleatoriedade matemática.
