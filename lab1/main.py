import math

def getRoots(A,B,C):
    roots = []
    D = B*B - 4*A*C
    if D == 0.0:
        roots.append(-B / (2*A))
    elif D > 0.0:
        roots.append((-B + math.sqrt(D))/(2*A))
        roots.append((-B - math.sqrt(D))/(2*A))
    return roots


def main():
    print("Введите коэффициент А:")
    A = float(input())
    print("Введите коэффициент B:")
    B = float(input())
    print("Введите коэффициент C:")
    C = float(input())
    roots = getRoots(A,B,C)
    if len(roots) == 0:
        print("Корней нет")
    elif len(roots) == 1:
        if roots[0] > 0:
            print("Два корня. Первый корень:",math.sqrt(roots[0]),"Второй корень:",-math.sqrt(roots[0]))
        elif roots[0] == 0:
           print("Один корень:",roots[0]) 
    elif len(roots) == 2:
        result = []
        for root in roots:
            if root > 0:
                result.append(math.sqrt(root))
                result.append(-math.sqrt(root))
            elif root == 0:
                result.append(math.sqrt(root))
        print("Кол-во корней:",len(result))
        for root in result:
            print("Корень:",root)
    
if __name__ == '__main__':
    main()