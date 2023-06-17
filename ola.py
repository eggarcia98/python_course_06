def doSomething(something = "default"):
    print(f"|{(something)}|")

something = input("something: ")
something = something if len(something) > 0 else None

doSomething(something)

