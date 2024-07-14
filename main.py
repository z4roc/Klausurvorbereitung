import re
from vector import Vector
from stringcontainer import StringContainer
from names import writenames, readnames
from functools import reduce
from pokemon import Pokemon
def suffix(s: str):
    if type(s) is not str:
        raise TypeError("s is not a valid String")
    if "." not in s:
        raise ValueError("s is not a valid String")

    sub = s.split(".")[-1]
    print(sub)
    if sub != "png" and sub != "jpp" and sub != "gif":
        raise ValueError("s is not a valid String")
    return sub

def email():
    e: str = input("Bitte Email eingeben")
    match = re.search("^[a-zA-Z][a-zA-Z_-]*@[a-zA-Z][a-zA-Z_-]*.de", e)
    if match:
        return e
    else:
        raise Exception("Invalid Email")


def main():
    try:
        email()

    except Exception as e:
       raise e

def myMinimum(l):
    return reduce(lambda x, y: x if x < y else y, l)

def mySort(l):
    newL = []
    while len(l) > 0:
        lowestnum = myMinimum(l)
        newL.append(lowestnum)
        l.remove(lowestnum)
    return newL


if __name__ == '__main__':

    glumanda = Pokemon("glumanda", 10, "fire")
    bisasam = Pokemon("bisasam", 9, "grass")
    #glumanda.scanWithPokedex()
    #glumanda.callBackOrRelease()
    #bisasam.callBackOrRelease()
    print([i for i in range(3)])

    #glumanda.attack(bisasam)
    #bisasam.attack(glumanda)
    #glumanda.attack(bisasam)

    print("hello world!")

    l = [1, 2, 3, 4]
    s= 'ich du er sie es'.split()[::2]
    print(len(str("Anfang" + ",bis," + "Ende").split(",")))
    print({1: "Eduard", 2: "Helena", 3: "Brat"}[2][-3:-1])
    print(l[::2])
    print(s)
    if s is not list:
        Exception("s is not a valid List")

    print(suffix("Hello.World.gif"))

    # print(email())

    v = Vector(1, 2, 3)
    w = Vector(1, 2, 3)

    z = eval(repr(v))
    print(z)

    print(v.scalar(w))
    mystr1 = StringContainer("c")
    mystr2 = StringContainer("bc")
    mystr3 = StringContainer("abc")

    myList = [mystr1, mystr2, mystr3]

    sorted(myList)

    writenames()

    names = readnames()

    print(names)

    names = list(filter(lambda x: "," in x, names))
    print(names)

    print([1, 2] * 2)

    print({a:len(a) for a in ["a", "aa", "aaa"]})
    d = {"a":1, "b":2, "c":3, "d":4}

    print(reduce(lambda x, y:x if x < y else y, [1, 2 ,3 ,4]))
    print(mySort([5,4,3,2,1]))




