import math


def main():
    a = 3
    b = 3
    c = 3
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(f"A triangle with sides 3, 3, 3 has an area of {area}")

    a = 3
    b = 4
    c = 5
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(f"A triangle with sides 3, 4, 5 has an area of {area}")

    a = 7
    b = 8
    c = 9
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(f"A triangle with sides 7, 8, 9 has an area of {area}")

    a = 5
    b = 12
    c = 13
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(f"A triangle with sides 5, 12, 13 has an area of {area}")

    a = 10
    b = 9
    c = 11
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(f"A triangle with sides 10, 9, 11 has an area of {area}")
    
    a = 8
    b = 15
    c = 17
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(f"A triangle with sides 8, 15, 17 has an area of {area}")

    a = 9
    b = 9
    c = 9
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"a triangle with sides 9,9,9 has an area of {area}") #in main function, harder to produce compared to the one with function


if __name__ == "__main__":
    main()

# harder to patch the bug, even though I could use find/replace