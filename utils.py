import time

def handleMathProblem(inp: str):
    l = []
    oprand = ""
    if "+" in inp:
        oprand = "+"
        l = inp.split("+")
    elif "-" in inp:
        oprand = "-"
        l = inp.split("-")
    elif "*" in inp:
        oprand = "*"
        l = inp.split("*")
    elif "/" in inp:
        oprand = "/"
        l = inp.split("/")
    num1 = int(l[0])
    num2 = int(l[1])
    if oprand == "+":
        result = num1 + num2
        return str(result)
    elif oprand == "-":
        result = num1 - num2
        return str(result)
    elif oprand == "*":
        result = num1 * num2
        return str(result)
    elif oprand == "/":
        result = num1 / num2
        return str(result)


def giveTime():
    fullTime = time.localtime(time.time())
    ti = ""
    ti += str(fullTime.tm_hour)
    ti += ":"
    ti += str(fullTime.tm_min)
    ti += ":"
    ti += str(fullTime.tm_sec)
    return ti


def giveDate():
    fullTime = time.localtime(time.time())
    da = ""
    da += str(fullTime.tm_year)
    da += "/"
    da += str(fullTime.tm_mon)
    da += '/'
    da += str(fullTime.tm_mday)
    return da
