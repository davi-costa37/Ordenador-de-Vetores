📊 Manipulador e Ordenador de Vetores (Python)
Este projeto consiste em uma aplicação interativa via console desenvolvida em Python para carregar, exibir e ordenar um vetor composto por 20 números inteiros. O sistema utiliza uma estrutura de menu em loop para guiar as ações do usuário.

⚙️ Funcionalidades
O algoritmo é dividido em funções modulares que gerenciam o fluxo de dados:

Menu Dinâmico: Um loop while mantém o programa ativo até que a opção de encerramento (9) seja acionada. O menu conta com tratamento de exceções (try/except) para evitar travamentos caso o usuário digite letras em vez de números.

Carga de Dados (fcarrega): Solicita ao usuário a digitação sequencial de 20 números inteiros, populando o vetor dinamicamente com a função append().

Ordenação Crescente (fclassifica): Organiza todos os números armazenados dentro do vetor em ordem crescente. O método utiliza uma implementação direta de comparação cruzada por índices (Select Sort/Bubble Sort simples) usando a sintaxe nativa de troca de variáveis do Python (swap): a, b = b, a.

Exibição Formatada (pmostrar): Varre a estrutura utilizando o método enumerate() para imprimir no console cada elemento acompanhado de seu respectivo índice.

🛠️ Tecnologias e Conceitos
Linguagem: Python 3

Estrutura de Dados: Listas (Vetores de tamanho fixo inicializado com 20 elementos).

Paradigmas: Programação Modular (divisão em funções) e Tratamento de Erros (ValueError).

📄 Licença
Este projeto está sob a licença MIT.
