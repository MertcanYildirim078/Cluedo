print('Cluedo Spel') #Kolonel van geelen en  Professor Pimpel
Man = input('Bent u een man of een vrouw? ')
Leeftijd = input('Hoe oud bent u? ')
Leeftijdk = Leeftijd >= 18
Haar = input('Welke kleur haar heeft u? ')
Haarz = Haar == 'zwart'
Wapens = input('Heeft u ervaring met wapens en/of tactische komplotten? j/n ')
Bril = input('Heeft u een bril? j/n ' )
archeoloog = input('Heeft u wetenschap over archeoloog of bent u een archeoloog? j/n ')
if Man == 'man':
    pass
elif Man == 'vrouw':
    print('Helaas bent u niet de persoon die wij zoeken. Helaas!')
if Leeftijdk == False:
    print('Helaas bent u niet de persoon die wij zoeken. Helaas!')