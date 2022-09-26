x = input("print: ")
def plus(pl):
     i = pl.split("+")
     print(int(i[0])+int(i[1]))
     return
def minus(mins):
    so = mins.split("-")
    print(int(so[0]) - int(so[1]))
    return
def multiply(mult):
    f = mult.split("*")
    print(int(f[0]) * int(f[1]))
    return
def division(div):
    g = div.split("/")
    print(int(g[0]) / int(g[1]))
    return
if x.find("+"):
    plus(x)
elif x.find("-"):
    minus(x)
elif x.find("*"):
    multiply(x)
elif x.find("/"):
   division(x)