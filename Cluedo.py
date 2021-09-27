print('Cluedo Spel') #Kolonel van geelen en  Professor Pimpel (Rosa Roodhart)
Man = input('Bent u een man of een vrouw? ')
Manv = Man == 'vrouw'
if Manv == True:
    actrice = input('Bent u een actrice of filmster? Of geweest? j/n ')
    actricej = actrice == 'j'
    if actricej == True:
        actriceogen = input('Heeft u donkere kringen onder uw ogen? j/n ')
        actriceogenj = actriceogen == 'j'
        if actriceogenj == True:
            rouwbeklag = input('Heeft u een fraai gespeelde rouwbeklag? j/n ')
            rouwbeklagj = rouwbeklag == 'j'
            if rouwbeklagj == True:
                print('Je bent aangenomen voor de sollicatatie gesprek van Rosa Roodhart!')
            else:
                print('Helaas bent u niet de persoon die wij zoeken. Helaas!')
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
    print('Je bent aangenomen voor de sollicatatie gesprek van Kolonel van Geelen!')
if Haarg and Brilj and archeoloogj == True:
    print('Je bent aangenomen voor de sollicatatie gesprek van  Professor Pimpel!')
if Haarz and Haarg == False:
    print('Je bent u niet de persoon die wij zoeken. Helaas!')
if Wapensj and Militairej and Brilj and archeoloogj == False:
    print('Je bent u niet de persoon die wij zoeken. Helaas!')

