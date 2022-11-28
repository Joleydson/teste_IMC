t="Teste de IMC"
print(t)
i='Atenção! Use ponto, no caso de números decimais, não virgula ao preencher os campos solicitados.'
print(i)
peso=eval(input('Digite o seu peso: '))
altura=eval(input('Digite sua altura: '))
imc=(peso)/(altura**2)
round(imc,2)#a função -round- irá arredondar o número na quantidade de casas decimais especificadas após a vírgula
#'{:.2f}'.format(imc) essa função só funciona dentro da função print, para comandos de execulção de cálculos o aconselhável é o comando -round-
if(imc>=18.5<=24.9):
 resultado=('Parabéns! Você está com o peso ideal.')
 p1=(altura**2)*18.5
 p2=(altura**2)*24.9
if(imc>=25<=29.9):
 resultado=(' Você está com sobrepeso.')
if(imc>=30<=39.9):
 resultado=('Você está com obesidade.')
print(f'Seu IMC é:{imc:.2f},{resultado}')#ao colocar, imc:.2f, foi limitado o numero de casas decimáis de pois da vírgula para 2 algarismos
print(f'o seu peso ideal está entre {p1:.2f}kg e {p2:.2f}kg')