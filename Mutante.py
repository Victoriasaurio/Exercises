x = int(input("Ingrese el tamaño del array --> "))
adn = input("Ingresar la secuencia del ADN --> ")

_array = []
_adn_array = []

# STRING-ARRAY
for a in adn:
    _array.append(a)
    
c = 0
i = 0
h = x
# MATRIZ
while c < x: 
    _adn_array.append(_array[i:h])
    i += x
    h += x
    c +=1

#HORIZONTAL
eje_y = 0
eje_x = 0
contador_A = 0
contador_C = 0
contador_G = 0
contador_T = 0
_igual = 0
_general = 0

while eje_x < x: 
    while eje_y < x:   
        if _adn_array[eje_x][eje_y] == 'A':
            contador_A += 1
        elif _adn_array[eje_x][eje_y] == 'C':
            contador_C += 1
        elif _adn_array[eje_x][eje_y] == 'G':
            contador_G += 1
        elif _adn_array[eje_x][eje_y] == 'T':
            contador_T += 1 
        eje_y += 1
    if contador_A >= 4 or contador_C >= 4 or contador_G >= 4 or contador_T >= 4:
        _general += 1
    contador_A = 0
    contador_C = 0
    contador_G = 0
    contador_T = 0
    eje_y = 0
    eje_x += 1

#VERTICAL
eje_y = 0
eje_x = 0
contador_A = 0
contador_C = 0
contador_G = 0
contador_T = 0

while eje_x < x: 
    while eje_y < x:  
        if _adn_array[eje_y][eje_x] == 'A':
            contador_A += 1
        elif _adn_array[eje_y][eje_x] == 'C':
            contador_C += 1
        elif _adn_array[eje_y][eje_x] == 'G':
            contador_G += 1
        elif _adn_array[eje_y][eje_x] == 'T':
            contador_T += 1 
        eje_y += 1
    if contador_A >= 4 or contador_C >= 4 or contador_G >= 4 or contador_T >= 4:
        _general += 1
    contador_A = 0
    contador_C = 0
    contador_G = 0
    contador_T = 0
    eje_y = 0
    eje_x += 1

#DIAGONAL
eje_x = 0
diagonal = 0
letra = ''

while eje_x < x:
    if letra != _adn_array[eje_x][eje_x]:
        letra = _adn_array[eje_x][eje_x]
        diagonal = 1
    else:
        diagonal += 1
        if diagonal >= 4:
            _general += 1
            diagonal = 1
    eje_x += 1
            
if _general > 1:
    print('Es mutante')

# AAAAAAGGGGACCCCATTTTACGTAATGGCAC
# TAAAAATGGGACTCCATTATACGTTATGGCAC

#['A', 'A', 'A', 'A', 'A']
#['G', 'G', 'G', 'G', 'G']
#['C', 'C', 'C', 'C', 'C']
#['T', 'T', 'T', 'T', 'T']
#['A', 'C', 'G', 'T', 'A']

# [
    # ['T', 'A', 'A', 'A', 'A'], 
    # ['A', 'T', 'G', 'G', 'G'], 
    # ['A', 'C', 'T', 'C', 'C'], 
    # ['A', 'T', 'T', 'T', 'T'], 
    # ['A', 'C', 'G', 'T', 'T']]
