def insertar(A,i,n):
    if i <0 or i>len(A):
        print("Índice fuera de rango")
        return
    A.insert(i, n)

def ins(A,i,n):
    if i < 0 or i > len(A):
        print("Índice fuera de rango.")
    B=A[:i]+ str(n) + A[i:]
    return B

def insertar_supremo(A,i,n):
    if type(A) is list:
        insertar(A,i,n)
    else:
        return ins(A,i,n)

def permutar(num, A):
    lista = []
    for i in range(len(A) + 1):
        lista.append(insertar_supremo(A, i, num))
    return lista
