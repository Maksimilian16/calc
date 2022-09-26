def plus(pl):
    i = pl.split("+")
    a = int(i[0])
    b = int(i[1])
    return a + b


def minus(mins):
    so = mins.split("-")
    a = int(so[0])
    b = int(so[1])
    return a - b


def multiply(mult):
    f = mult.split("*")
    a = int(f[0])
    b = int(f[1])
    return a * b


def division(div):
    g = div.split("/")
    a = int(g[0])
    b = int(g[1])
    return a / b


def execute():
    x = input("print: ")

    action_dict = {
        "*": multiply,
        "+": plus,
        "-": minus,
        "/": division
    }
    act = x[1]
    result = action_dict.get(act, "Wrong data")(x)
    print(result)


if __name__ == "__main__":
    execute()

