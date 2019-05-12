#include <iostream>
#include <sstream>
#include <string>
#include <iomanip>

using namespace std;

int main()
{
    string letra;
    string texto;
    int qtdPalavras = 0;
    int total = 0;
    getline(cin, letra);
    getline(cin, texto);
    bool mesmaPalavra = false;

    for(int i=0; i<texto.length();i++)
    {
        if(texto[i] == letra[0] && !mesmaPalavra)
        {
            qtdPalavras++;
            mesmaPalavra = true;
        }
        else if(texto[i] == ' ')
        {
            total++;
            mesmaPalavra = false;
        }
    }
    total++;
    float porcentagem = qtdPalavras;
    porcentagem = porcentagem/total;
    porcentagem = porcentagem * 100;
    stringstream stream;
    stream << fixed << setprecision(1) << porcentagem;
    cout << stream.str();

}
