j = 0
k = 0
def check_bullets(f, r):
    f = int(input("Сколько боевых? "))
    r = int(input("сколько холостых? "))
    return f, r

j, k = check_bullets(j, k)
z = j + k
while z != 0:
    t = input("Какой выпал патрон? ")
    if t == "r":
        j -= 1
        print(f"боевых {j}, холостых {k}")
        z = j + k
    if t == "f":
        k -= 1
        print(f"боевых {j}, холостых {k}")
        z = j + k
    if t == "нв":   
        j, k = check_bullets(j, k)
        z = j + k