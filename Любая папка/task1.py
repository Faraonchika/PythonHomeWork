def word(N):
    if N % 3 == 0 and N % 5 == 0:
        print("Foobar")
    elif N % 3 == 0:
        print("Foo")
    elif N % 5 == 0:
        print("Bar")

N = int(input())

word(N)
