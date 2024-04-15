# C++

## Bibliotecas
#Include inclui bibliotecas, como por exemplo:
```C++
#include <iostream>
```

## Main Function
Todo programa c++ precisa de uma função main 
```C++
#include <iostream>
int main(){
    //Código
    return 0;
}
```

## Input/Output
std : : cin >> é onde você dá o input desejado

std : : cout << é onde fica o output(saída)
```c++
#include <iostream>
int main() {
    int number;
    std::cout << "Enter an integer: ";
    std::cin >> number;
    std::cout << "You entered: " << number << std::endl;
    return 0;
}

```

## Data Types
- Int: números inteiros
- Float: números com 1 casa após a vírgula, como 6.9
- Double: números com 2 casas após a vírgula, como 6.96
- Char: Caracteres (String)

## Estruturas

### Condicional
```c++
if (condicao){
    //Se a condição for verdade
} else {
    //Se a condição for falsa
}
```

### Loop
```c++
while (condicao){
    //Enquanto a condição for verdade
}

for (inicio; condicao; atualizacao){
    //Enquanto a condição for verdade
}
```

### Switch 
```c++
switch (variavel){
    case valor1:
        //Executará se a variavel for igual ao valor1
        break;
    case valor2:
        //Executará se a variavel for igual ao valor2
        break;
    default: 
        //Se a variável não for igual à nenhum valor
} 
```

### Função 
São blocos de comando reusáveis, ou seja, podemos criar a função e usar ela pelo resto do código
```c++
TipoQueaFuncaoVaiRetornar NomeDaFuncao(TipoDoParametro parametro){
    //Código
    return Valor;
}
```