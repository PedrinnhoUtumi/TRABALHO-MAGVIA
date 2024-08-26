#include <iostream>
#include <string>
#include <list>
#include <algorithm>
using namespace std;

/*1.
Verificar se um número é primo

bool is_primo()
{
    int n;
    cout << "Enter a number: ";
    cin >> n;
    if (n == 1 && n == 2 && n % 2 == 0)
    {
        return false;
    }
    for (int i = 3; i * i <= n; i += 2)
    {
        if (n % i == 0)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    cout << "O numero eh primo?: " << (is_primo() ? "Sim" : "Nao") << endl;
    return 0;
}
*/

/*2.
Escreva um programa em Python que leia as notas da primeira prova dos N alunos
de Algoritmos, descubra e imprima a maior nota. O valor N deve ser informado pelo
usuário.

int main()
{
    int qntdeNotas = 0;
    cout << "Quantas notas?: ";
    cin >> qntdeNotas;
    list<double> listaNotas;
    for (int i = 0; i < qntdeNotas; i++)
    {
        double nota = 0;
        cout << "Nota " << i + 1 << ": ";
        cin >> nota;

        listaNotas.insert(listaNotas.begin(), nota);
    }
    double maiorValor = *max_element(listaNotas.begin(), listaNotas.end());
    cout << "maior nota: " << maiorValor << endl;
    return 0;
}
*/

/*3.
Fatorial de um número
int fatorial = 1;

int main()
{
    int numero;
    cout << "Digite um numero: ";
    cin >> numero;
    for (int i = 1; i <= numero; i++)
    {
        fatorial *= i;
    }
    cout << "Fatorial do numero " << numero << " eh: " << fatorial << endl;
    return fatorial;
}
*/

/*4.
Escreva um programa em C++ que leia um número inteiro e imprima o seu sucessor

int main() {
    int numero;
    cout << "Digite um numero: ";
    cin >> numero;
    cout << "Sucessor do numero " << numero << " eh: " << numero + 1;
    return 0;
}
*/

/*5.
Faça uma calculadora simples

char trocaOp(double num1, double num2)
{
    char op;
    cout << "Digite a operacao (+, -, *, /): ";
    cin >> op;
    switch (op)
    {
    case '+':
        cout << "Soma: " << num1 + num2 << endl;
        break;
    case '-':
        cout << "Subtracao: " << num1 - num2 << endl;
        break;
    case '*':
        cout << "Multiplicacao: " << num1 * num2 << endl;
        break;
    case '/':
        cout << "Divisao: " << num1 / num2 << endl;
        break;
    default:
        cout << "Operacao invalida " << endl;
        break;
    }
    return op;
}

int main()
{
    double num1, num2;
    cout << "entre com o num1: ";
    cin >> num1;

    cout << "entre com o num2: ";
    cin >> num2;
    trocaOp(num1, num2);
}
*/