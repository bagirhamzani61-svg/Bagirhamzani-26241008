from unicodedata import name


nim_lengkap = "26241008"
digit_a = 0
digit_b = 8

print("nama :", name)
print("nim_lengkap:", nim_lengkap)

a = int(input("digit_a :",))
b = int(input("digit_b :",))

kondisi_1 = a > 5
kondisi_2 = b > 5

print("kodisi_1 > 5 :", kondisi_1)
print("kodisi_2 > 5 :", kondisi_2)

print("NOT kondisi_1:", not kondisi_1)
print("AND kondisi_1 AND kondisi_2:", kondisi_1 and kondisi_2)
print("OR kondisi_1 OR kondisi_2:", kondisi_1 or kondisi_2)
print("XOR kondisi_1 XOR konddisi_2:", kondisi_1 ^ kondisi_2)
