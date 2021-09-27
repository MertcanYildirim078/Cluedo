print('Cluedo Spel') #Kolonel van geelen en  Professor Pimpel
Man = input('Bent u een man of een vrouw? ')
Leeftijd = int(input('Hoe oud bent u? '))
Leeftijdk = Leeftijd >= 18
Haar = input('Welke kleur haar heeft u? ')
Haarz = Haar == 'zwart'
Haarg = Haar == 'grijs'
Wapens = input('Heeft u ervaring met wapens en/of tactische komplotten? j/n ')
Wapensj = Wapens == 'j'
Militaire = input('Heeft u ooit in de militaire geweest? j/n ')
Militairej = Militaire == 'j'
Bril = input('Heeft u een bril? j/n ' )
Brilj = Bril == 'j'
archeoloog = input('Heeft u wetenschap over archeoloog of bent u een archeoloog? j/n ')
archeoloogj = archeoloog == 'j'
if Man == 'man':
    pass
elif Man == 'vrouw':
    print('Helaas bent u niet de persoon die wij zoeken. Helaas!')
if Leeftijdk == False:
    print('Helaas bent u niet de persoon die wij zoeken. Helaas!')
if Haarz and Wapensj and Militairej == True:
    print('Je bent aangenomen voor de sollicatatie gesprek van Kolonel van geelen!')
if Haarg and Brilj and archeoloogj == True:
    print('Je bent aangenomen voor de sollicatatie gesprek van  Professor Pimpel!')
