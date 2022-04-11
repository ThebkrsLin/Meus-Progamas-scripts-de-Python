s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
 print('Estes segmentos formam um triangulo', end=' ')
 if s1 == s2 ==s3:
   print('Equilatero!')
 elif  s1 != s2 != s3 != s1:
     print('Escaleno!')
 else:
    print('Isoceslis!')
else:
    print('Nao tem como formar um triangulo com esse segmentos!')
