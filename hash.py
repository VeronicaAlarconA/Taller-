from turtle import st


def modulo(num):
    return num%11
mod=82
print('el hash para: '+str(mod)+' es: '+str(modulo(mod)))

def plegado(num):
    x = [int(a) for a in str(num)]
    a=0
    sum=0
    while a< len(x):
        sum+=x[a]
        a+=1
    return modulo(sum)
ple=520
print('plegado ')
print('el hash para: '+str(ple)+' es: '+str(plegado(ple)))

def strToweightNum(s):
    sum=0
    for i in range(len(s)):
        sum += (i+1) * ord(s[i])
    return sum
def h_str(s):  
    return strToweightNum(s)%11
a='juli'
print('cadena de caracteres ponderado')
print('el hash para: '+str(a)+' es: '+str(h_str(a)))

def strToNum(s):
    sum=0
    for c in s:
        sum += ord(c)
    return sum
b='juli'
print('cadena de caracteres')
print('el hash para: '+str(b)+' es: '+str(h_str(b)))

def cuadrado(num):
    cuadrado=0
    num=num**2
    print(num)
    x = [int(a) for a in str(num)]
    #print(x)
    if len(x)%2==0:       
        cuadrado=str(x[int((len(x)/2)-1)])
        cuadrado+=str(x[int(len(x)/2)])
        #print(str(cuadrado))
    else:
        cuadrado=x[int(len(x)/2)]
    #print(str(cuadrado))
    return modulo(int(cuadrado))
    
        
f=44
print('centro del cuadrado')
print('el hash para: '+str(f)+' es: '+str(cuadrado(f)))
