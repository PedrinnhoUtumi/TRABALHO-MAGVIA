#include <iostream>
#include <string>
#include <list>
#include <algorithm>
#include <HtmlHelp.h>
using namespace std;

/*1.
Verificar se um número é primo

bool is_primo()
{
    int n;
    cout << "Enter a number: ";
    cin >> n;
    if (n % 2 == 0 || n == 1 || n == 2)
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
    int qntdeNotas;
    cout << "Quantas notas?: ";
    cin >> qntdeNotas;
    list<double> listaNotas;
    for (int i = 0; i < qntdeNotas; i++)
    {
        double nota;
        cout << "Nota " << i + 1 << ": ";
        cin >> nota;

        listaNotas.insert(listaNotas.begin(), nota);
    }
    double maiorValor = *max_element(listaNotas.begin(), listaNotas.end());
    cout << "maior nota: " << maiorValor << endl;
    cout << "maior nota: " << *max_element(listaNotas.begin(), listaNotas.end()) << endl;
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
// int main() {
//     int num = 10;
//     cout << num << endl;
//     int* ponteiro = &num;
//     *ponteiro = 37;
//     cout << ponteiro << endl;
//     cout << &num << endl;
//     cout << num << endl;
//     return 0;
// }




// #include <Arduino.h>
// #include <UnicViewAD.h>

// #define contaGiro 2

// LCM Lcm(Serial2);

// int girosNum;

// int quantosGiros() {
//   pinMode(contaGiro, INPUT_PULLDOWN);
//   int giros = digitalRead(contaGiro);
//   if(giros == HIGH) {
//     girosNum += 1;    
//   }
//   return girosNum;
// }

// int direcao() {
//   int asciiCode = Lcm.readVP(100);
//   if(asciiCode == 26879) {
//     Serial.print("Vp 100: Horario\n");

//   } else if (asciiCode == 25087) {
//     Serial.print("Vp 100: Anti Horario\n");
  
//   } else {
//     Serial.print("Vp 100: Escolha apenas uma das opcoes\n");
  
//   }
//   return asciiCode;
// }

// void setup() {
//   Lcm.begin();
//   Serial.begin(115200);
//   Serial2.begin(115200, SERIAL_8N1, 42, 41, false, 100);
// }

// void loop() {
//   Serial.print("Vp 80: ");
//   Serial.println(Lcm.readVP(80));

//   Serial.print("Vp 69: ");
//   Lcm.writeVP(69, quantosGiros());
//   Serial.println(Lcm.readVP(69));

//   direcao();
  
//   delay(1000);

// }















/*Palindromo*/

// string contrario(string palindromo) {
//     string contrario = palindromo;
//     reverse(contrario.begin(), contrario.end());
//     return contrario;
// }
//
// bool isPalindromo() {
//     string palindromo;
//     cout << "Entre com uma palavra: ";
//     cin >> palindromo;
//     if (contrario(palindromo) == palindromo) {
//         cout << "eh palindromo" << endl;
//     } else {
//         cout << "nao eh palindromo" << endl;
//     }
// }
//
// int main() {
//     isPalindromo();
//     return 0;
// }
//
// string lowCase(string Palindromo){
//     string lowTipe = Palindromo;
//     transform(lowTipe.begin(), lowTipe.end(), lowTipe.begin(), 
//                 [](unsigned char c) { return tolower(c); });
//     return lowTipe;
// }
//
// bool reverser(string Palindromo){
//     string contrario;
//     contrario = Palindromo;
//     reverse(contrario.begin(), contrario.end() );
//     return contrario == Palindromo;
// }
//
// bool isPalindromo(){
//     string Palindromo;
//     cout << "Entre com uma palavra: ";
//     cin >> Palindromo;
//     if (reverser(lowCase(Palindromo))) {
//         cout << "Eh palindromo";
//     } else {
//         cout << "nao eh palindromo";
//     }
// }
//
// int main(){
//     isPalindromo();
//     return 0;
// }

