def calc(a,b,c,d):
    var1=int(a**b)
    var2=int(c**d)
    var3=var1+var2
    return var3
if __name__ == '__main__':
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    print(calc(a,b,c,d))