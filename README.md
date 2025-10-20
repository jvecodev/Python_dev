# Python_dev

Coleção de Estudos

## Estrutura do Repositório

O repositório está organizado nas seguintes pastas principais:

1.  [fundamentos](#fundamentos)
2.  [POO (Programação Orientada a Objetos)](#poo)
3.  [Modulos](#modulos)
4.  [LLM (Large Language Models)](#llm)
5.  [RedesNeurais](#redesneurais)

---

### fundamentos

Esta pasta contém exemplos de conceitos básicos e essenciais do Python.

* `ListComprehension.py`: Demonstração do uso de *list comprehensions*.
* `lambda.py`: Exemplo de uso de funções anônimas (lambda).
* `kwargs_args.py`: Exemplos de uso de `*args` (argumentos posicionais) e `**kwargs` (argumentos nomeados).
* `Slice.py`: Exemplos de fatiamento (*slicing*) de strings.
* `String.py`: Demonstração de vários métodos úteis para manipulação de strings (`upper`, `lower`, `replace`, `split`, etc.).

### POO

Esta pasta explora os conceitos de Programação Orientada a Objetos em Python.

* `aula1classe.py`: Definição de uma superclasse `Game`, demonstrando atributos, construtor (`__init__`) e métodos de instância.
* `aula1objetos.py`: Criação de instâncias (objetos) da classe `Game` e da subclasse `SinglePlayerGame`.
* `instancia.py`: Exemplo de utilização de métodos de instância para avaliar e calcular médias.
* `herença.py`: Exemplo de herança, com a subclasse `SinglePlayerGame` herdando da classe `Game` e sobrescrevendo métodos.

**Subpastas de POO:**

* **`abstract/`**:
    * `Animal.py`: Define uma classe abstrata `Animal` usando `ABC` e `@abstractmethod`.
    * `Cachorro.py`: Implementa as subclasses `Cachorro` e `Gato` que herdam de `Animal`.
    * `Objeto.py`: Instancia e utiliza as classes `Cachorro` e `Gato`.
* **`property/`**:
    * `Conta.py`: Demonstra o uso de `@property` (getter) e `@saldo.setter` (setter) para encapsulamento e controle de acesso a atributos privados (`__saldo`).
    * `Objeto.py`: Exemplo de uso da classe `Conta`, acessando o getter e o setter.
* **`iterator/`**:
    * `Contador.py`: Implementa um iterador customizado (métodos `__iter__` e `__next__`).
    * `Objeto.py`: Utiliza o iterador `Contador` em um loop `for`.
* **`Enumarate/`**:
    * `Enumarate.py`: Exemplos de uso da função `enumerate` para iterar sobre sequências obtendo índice e valor.
* **`Map/`**:
    * `Map.py`: Exemplo de uso da função `map` com lambda para aplicar uma função a todos os itens de uma lista.
    * `Filter.py`: Exemplo de uso da função `filter` com lambda para filtrar elementos de uma lista.
* **`Walrus/`**:
    * `walrus.py`: Demonstração do operador Walrus (`:=`) para atribuição e teste em uma única expressão.

### Modulos

Exemplos de criação e importação de módulos em Python.

* `ModulosBuiltIn.py`: Define uma função `soma` simples.
* `chamando.py`: Importa e utiliza a função `soma` do módulo `ModulosBuiltIn`.

### LLM

Esta pasta contém exemplos de interação com Grandes Modelos de Linguagem (LLMs) usando as bibliotecas `google-generativeai` (Gemini) e `transformers` (Hugging Face).

* `google_gemini.py`: Script para gerar conteúdo usando o modelo "gemini-1.5-flash-latest" da API do Google Gemini.
* `check_model.py`: Script para listar os modelos disponíveis na API do Google Gemini que suportam `generateContent`.
* `summary.py`: Exemplo de sumarização de texto usando um `pipeline` da biblioteca Transformers.
* `text_generation.py`: Exemplo de geração de texto em português usando um `pipeline` da Transformers.
* `mask.py`: Demonstração da tarefa "fill-mask" (preenchimento de máscara) com um modelo BERT em português.

### RedesNeurais

Contém material de estudo sobre Redes Neurais.

* `3.1.Redes Neurais.pdf`: Apresentação em PDF sobre os conceitos de Redes Neurais, incluindo topologia (camadas de entrada, ocultas, saída) e arquitetura (Feed Forward, Recorrente).

---


Para executar os exemplos, certifique-se de ter o Python instalado. Para os exemplos na pasta `LLM`, você precisará instalar as bibliotecas necessárias:

```bash
pip install google-generativeai transformers torch
