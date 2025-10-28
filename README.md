# Classificação de Triângulos — Teste de Mutação

Este repositório foi desenvolvido com **fins acadêmicos**, para a disciplina **Testes de Software**.

O objetivo é demonstrar:
- a criação de um programa simples em Python que classifica triângulos (equilátero, isósceles, escaleno);
- a aplicação de **testes unitários** com `unittest`;
- e a **análise de mutação** utilizando a ferramenta `MutPy`.

---

## 📂 Estrutura do Projeto

```

triangulo-mutacao/
│
├── triangulo.py          # código principal
├── test_triangulo.py     # testes unitários
├── requirements.txt      # dependências
└── README.md             # este arquivo

```
---

## ▶️ Como executar

1. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
    ```

2. **Rodar testes unitários:**

   ```bash
   python -m unittest test_triangulo.py
   ```

3. **Executar o teste de mutação:**

   ```bash
   mut.py --target triangulo --unit-test test_triangulo -m
   ```

O comando acima gera os mutantes, executa os testes sobre eles e exibe o **escore de mutação** obtido.

