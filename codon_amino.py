#!/usr/bin/env python3
#dicionario dos codons e seus respectivos aminoacidos
codons = {
    'GCU' : 'Alanina',
    'UGU' : 'Cisteína',
    'AUG' : 'Metionina',
    'UGA' : 'Stop',
    'UAA' : 'Stop'
}

#parte do script que imprime as opções de codons ao usuario
print(list(codons.keys()))

#parte do script que o usuario escolhe qual codon quer obter o aminoacido correspondente
codon = input('Coloque sua sequência de códons: ' )
codon2 = input('Coloque sua sequência de códons: ' )

#parte do script que é imprimido as duas opções escolhidas pelo usuario anteriormente
print("Sua sequência de aminoácidos é: ", codons[codon], codons[codon2])
