j = 0
k = 0
def check_bullets(f, r):
    f = int(input("Сколько боевых?\what amount of armed bullets "))
    r = int(input("сколько холостых?what amount of unarmed bullets "))
    return f, r

j, k = check_bullets(j, k)
z = j + k
while z != 0:
    t = input("Какой выпал патрон? ")
    t=t.lower()
    if t == "боевой" or t=='armed':
        j -= 1
        print(f"боевых(armed) {j}, холостых(unarmed) {k}")
        z = j + k
    if t == 'unarmed' or t=='холостой':
        k -= 1
        print(f"боевых(armed) {j}, холостых(unarmed) {k}")
        z = j + k
    if t == 'нв' or t=='new game' or t=='новая игра' or t=='ng':   
        j, k = check_bullets(j, k)
        z = j + k