# Programação funcional

Programação funcional é o processo de **construir software através de composição de funções puras, evitando compartilhamento de estados, dados mutáveis e efeitos colaterais. É declarativa ao invés de Imperativa** Essa é uma definição do Eric Elliott que eu gosto muito.

Mas confesso que tem muita informação nesse parágrafo não é, então vamos começar do começo.

## De onde veio a ideia de programação funcional ?

A inspiração do paradigma funcional veio dos matemáticos teóricos que lidam com grandes abstrações

Eles costumam trabalhar com sistemas complexos e a maneira como eles encontraram para se manterem organizados e chegar no objetivo final foi através das funções. Se trouxermos para nosso mundo de desenvolvimento, existe uma certa analogias de que trabalhamos com sistemas complexos e com **abstrações**.

Então o paradigma funcional foi inspirado nesse modelo de trabalho onde as funções são utilizadas para lidar com abstrações e aplicou no desenvolvimento de sistemas.

Agora que já entendemos um pouco da história, vamos ver os **conceitos fundamentais começar a desenvolver de modo funcional**.

## Composição de função


**Composição de funções** é criar uma nova função através da composição de outras. Por exemplo, vamos criar uma função que vai **filtrar** um **array**, filtrando somente os números pares e multiplicando por dois:

```
const numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros.filter((numero) => numero % 2 === 0).map((numero) => numero * 2) 
// [ 4, 8, 12, 16, 20 ]
```


## Funções Puras

**Uma função é chamada pura quando invocada mais de uma vez produz exatamente o mesmo resultado**. Isto é, o retorno da função é sempre o mesmo se você passar os mesmos parâmetros, então ela não pode depender de valores mutáveis. Por outro lado, ela não pode causa efeitos colaterais externos, pois se ela imprime uma linha de saída, altera algo no banco, lança um foguete para o espaço, ao invocá-la a segunda vez ela vai causar um novo efeito.

```
const verfica_se_e_maior_que = (entrada1, entrada2) => entrada1 >= entrada2;
```

Se imprimirmos:

```
verfica_se_e_maior_que(13, 13) // true
```

A função ```verifica_se_e_maior_que()``` é pura porque atende todos os requisitos listados. Por não causar efeito colateral e por não usar valores mutáveis compartilhados, seus resultados podem ser cacheados e ela pode ser executada em paralelo sem maiores preocupações.

## Imutabilidade

**Imutabilidade** significa que uma vez que uma variável que recebeu um valor, vai possuir esse valor para sempre, ou quando criamos um objeto ele não pode ser modificado.

O objeto **string** do Javascript por exemplo é imutável:

```
const sobreNome = "Silveira"

sobreNome.replace("Silveira", "Souza") //'Souza'

sobreNome //'Silveira'
```

## Efeito Colateral

**Efeito colateral é toda interação da nossa função com o mundo externo** No nosso dia a dia fazemos coisas como:

- Acessar banco de dados;
- Realizar chamadas assíncronas,
- Alterar propriedades de objetos entre outras tarefas

E nem sempre podemos prever esse resultado.

Mas dissemos antes que funções puras não possuem efeito coleateral certo ? Mas programamos para um mundo onde dados mudam constantemente.

Então a programação funcional não elimina efeitos colaterais totalmente, mas tentam confiná-los. Como fazemos interface com o mundo real, algumas partes do programa vão ser impuras então o papel é minimizar essas partes e separá-las do resto do programa.

## Imperativo x Declarativo

É muito comum aprender a programar de forma **imperativa**, onde mandamos alguém fazer algo. Busque o usuário 15 no banco de dados. Valide essas informações do usuário.

Na programação funcional tentamos programar de forma **declarativa**, onde declaramos o que desejamos, sem explicitar como será feito. Qual o usuário 15? Quais os erros dessas informações?

## Estado Compartilhado

**Estado compartilhado** é qualquer valor que está acessível por mais de um ponto de uma aplicação. Por exemplo:

```
const idade = 31
const calculaIdadeDosIrmaos = ( idadeIrmao ) => idade + idadeIrmao 
```

Neste caso a função ```calculaIdadeDosIrmaos()``` utiliza uma variável externa que está fora do seu escopo e não depende apenas dos argumentos passados.