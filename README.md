# Lista de Exercício - Algoritmos Recursivo

# Fundamentos Matemáticos II

Este repositório contém os exercícios da disciplina **Fundamentos Matemáticos II**, com foco em **algoritmos recursivos** implementados em Python.

## 📚 Lista de Exercícios

### 1. Fatorial Recursivo

Implemente um algoritmo recursivo para o cálculo do fatorial `n!`, com `n` sendo um número inteiro.Fatoriais de números negativos são considerados nulos.

- **Entrada:** Um número inteiro `n`
- **Saída:** O valor do fatorial `n!`
- **Exceções:** Para `n < 0`, retorne `n! = 0`

---

### 2. Exponencial Recursiva

Implemente um algoritmo recursivo para o cálculo da exponencial `aⁿ`, com:

- `a` sendo um número qualquer (positivo, negativo ou zero)
- `n` um número inteiro **≥ 0**

**Atenção:** o caso `0⁰` não pode ser calculado.

- **Entrada:**
  - Uma base `a` (pode ser qualquer número, inclusive negativo)
  - Um expoente inteiro `n ≥ 0`
- **Saída:** O valor da exponencial `aⁿ`
- **Exceções:** Para o caso `0⁰`, informe que é “**impossível calcular**”.

---

### 3. Exponencial Modular Recursiva

Implemente um algoritmo recursivo para o cálculo da exponencial modular `aⁿ mod m`, com:

- `a` sendo um número inteiro qualquer (positivo, negativo ou zero)
- `n` um expoente inteiro **≥ 0**
- `m` um módulo inteiro **≥ 2**

**Atenção:** os casos `0⁰ mod m` e `m ≤ 1` não podem ser calculados.

- **Entrada:**

  - Uma base `a` (inteiro, inclusive negativo)
  - Um expoente `n ≥ 0`
  - Um módulo `m ≥ 2`
- **Saída:** O valor de `aⁿ mod m`
- **Exceções:**

  - Para o caso `0⁰ mod m`, informe que é “**impossível calcular**”
  - Para `m ≤ 1`, informe que é “**impossível calcular**”
- **Sugestão:** Pesquise por “exponencial modular recursiva” ou “recursive modular exponentiation”

---

### 4. Máximo Divisor Comum (MDC) Recursivo

Implemente um algoritmo recursivo para o cálculo do **mdc** de dois números inteiros `a` e `b`.

- **Entrada:** Dois números inteiros `a` e `b`
- **Saída:** O valor de `mdc(a, b)`
- **Exceções:** Para o caso em que `a = 0` e `b = 0`, informe que o mdc é “**indeterminado**”
- **Sugestão:** Pesquise por “mdc recursivo” ou “recursive greatest common divisor”

---

## 🧠 Objetivo

Praticar conceitos de recursão utilizando problemas clássicos da matemática e da computação.
