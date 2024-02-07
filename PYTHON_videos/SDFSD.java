carro c1 = new Carro();

c1.nome = "UNO";
c1.marca = "Fiat";
c1.ano = 2015;
c1.vel = 0;

int x;
System.out.printf("Digite o valor que deseja acelerar o carro")
x = ler.nextInt();


c1.acerelar(x); //pegando o metodo acelerar da classe carro para o objeto e mandando acelerar 

System.out.printf("A velocidade agora será %d ")