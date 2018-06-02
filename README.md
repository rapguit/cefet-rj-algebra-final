# Trabalho Final de Algebra Linear Computacional
##### Enviroment: Python 3.6

Implementar métodos de redução de banda de matrizes com base nas heurísticas apresentadas em
http://www.sbmac.org.br/arquivos/notas/livro_75.pdf.

* Implementar uma das Heurísticas apresentadas no livro;
* Implementar o Gradiente Conjugado com Técnica de Armazenamento de Linha (**CSR**);
* Comparar a Heurística escolhida e o Gradiente Conjugado com relação ao tempo de processamento.

_OBS.: Usar matrizes grandes com aqueles esquemas de compactação. Para maiores detalhes, acesse este catálogo de matrizes https://sparse.tamu.edu._


## Como utilizar

Primeiramente, baixe o repostiório para a sua máquina.
Após baixá-lo, o repositório **raiz** (_cefet-rj-algebra-final_) terá a seguinte estrutura:

* Arquivos:
    * README.md
    * application.py
* Diretórios: 
    * datasets
    * modules
    * tests

Em seguida, acesse o diretório **_datasets_** na sua máquina e verifique os arquivos de matrizes do tipo *.mtx. Esses arquivos serão carregados na etapa de execução.

Um outro diretório importante a ser verificado é o **_modules_**, mais precisamente o arquivo contido neste diretório chamado _heuristic_cuthillmckee_. Esse arquivo será utilizado para rodar a heuristica utilizada neste trabalho para fins de comparação. Para executá-la:

* **python** _**heuristic_cuthillmckee.py**_ [**symetric_mode**] [**filename**]

#### Exemplo
* **python** _**modules/heuristic_cuthillmckee.py**_ **True**    **datasets/bcsstk18.mtx**

Para conhecer os parâmetros, execute **python** _**heuristic_cuthillmckee.py**_ **-h**

**OBS.: É necessário ter o Python (3.6) instalado em sua máquina.**

Por fim, para executar o **Gradiente Conjugado**, basta executar o arquivo _application.py_ da seguinte forma:

* **python** _**application.py**_ **--maxit INT** **--err FLOAT** **FILENAME.mtx**

#### Exemplo
* **python** _**application.py**_ **--maxit 100** **--err 0.01** **datasets/input11948x11948.mtx**

Para conhecer os parâmetros, execute **python** _**application.py**_ **-h**.

Então "mãos à obra" e bons resultados.

Abs =D