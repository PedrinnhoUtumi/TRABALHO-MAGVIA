# Linguagem de Programação C

## Introdução

A linguagem de programação C é uma das linguagens de programação mais antigas e influentes. Desenvolvida por Dennis Ritchie na década de 1970 na Bell Labs, C foi projetada para ser uma linguagem de programação de propósito geral e de alto nível que também oferecia um controle próximo ao hardware do computador.

## Características Principais

- **Simplicidade**: C é conhecida por sua simplicidade e poder expressivo. Ela fornece um conjunto de construções primitivas que podem ser combinadas para criar programas complexos.
  
- **Portabilidade**: Os programas escritos em C podem ser compilados para muitas arquiteturas diferentes com pouca ou nenhuma modificação. Isso a torna ideal para sistemas que precisam ser executados em diferentes plataformas.

- **Eficiência**: C permite aos programadores escrever código que se aproxima do nível do hardware, resultando em programas rápidos e eficientes. Isso a tornou uma escolha popular para desenvolvimento de sistemas e aplicativos que requerem desempenho.

- **Acesso a Memória**: C oferece aos programadores controle direto sobre a memória do sistema, permitindo alocações e desalocações de memória sob demanda. Essa característica é útil para aplicativos que precisam gerenciar recursos com eficiência.

## Sintaxe Básica

Um programa C típico consiste em funções que contêm declarações de variáveis, instruções e chamadas de outras funções. Aqui está um exemplo simples de um programa C que imprime "Hello, World!":

```c
#include <stdio.h>

void main() {
    printf("Hello, World!\n");
}
```

### Declaração de variáveis
Deve colocar o tipo da variável, logo em seguida o nome dela e o valor correspondente ao tipo da variável

Variáveis devem ter nomes únicos dentro do escopo que estão. Ou seja, não podemos declarar duas variáveis chamadas numerosecreto.

Se fizermos isso, por algum engano, o compilador reclamará e não nos gerará o executável do programa. 