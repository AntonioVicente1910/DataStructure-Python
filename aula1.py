#from unidecode import unidecode
#def disascentuados(texto):
#    texto = unidecode(texto)
#    return texto
#cidade = input('Qual cidade você nasceu? \n')
#cidade = cidade.casefold()
#disascentuados(cidade)
#if (cidade == 'camboriu'):
#    print('Você é Camboriuense')
#elif (cidade == 'balneario camboriu'):
#    print('Você é Balneário Camboriuense')
#elif (cidade == 'itajai'):
#    print('Você é itajaiense')
#else:
#    print('Você não nasceu no vale do Itajaí')



valeItajaí = {'Balneário Camboriú':'Balneário Camboriuense', 'Camboriú': 'Camboriuense', 'Itajaí': 'Itajaienese'}

for m in valeItajaí:
    print('Quem nasce em', m, 'é', valeItajaí[m])