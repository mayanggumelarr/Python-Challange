def multi(l_st):
    result = 1
    for i in l_st:
        result *= i
    return result

def add(l_st):
    result = 0
    for i in l_st:
        result += i
    return result

def revers(st):
    return st[::-1]

l_st = [1,2,3,4]
st = "Cherry"

print(f"hasil dari perkalian: {multi(l_st)}")
print(f"Hasil penjumlahan: {add(l_st)}")
print(f"hasil pembalikan kata: {revers(st)}")