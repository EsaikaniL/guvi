//esai
a=str(input())
b=0
for i in range(len(a)):
    if ("," in a)or("." in a)or(";" in a)or(":" in a)or("<" in a)or(">" in a)or("/" in a)or("?" in a)or("'" in a)or("["in a)or("]"in a)or("{" in a)or("}" in a)or("~" in a)or("!" in a)or("@" in a)or("#" in a)or("$" in a)or("%"in a)or("^" in a)or("&" in a)or("*" in a)or("(" in a)or(")" in a)or("-" in a)or("+"in a)or("="in a):
            b=b+1
            print(b)
