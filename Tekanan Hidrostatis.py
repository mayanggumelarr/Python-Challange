''' Fungsi Penghitung Tekanan Hidrostatis
    P = pgh '''

def hidrostatis (p, g, h):
    P = p * g * h
    return P

print("=============== TEKANAN HIDROSTATIS ===============\n")

p = float(input("Masukkan massa jenis zat cair: "))
h = float(input("Masukkan kedalaman benda (m): "))
g = 9.8

P = hidrostatis(p, g, h)
print(f"Tekanan Hidrostatis pada Benda: {P:.2f} Pa")


