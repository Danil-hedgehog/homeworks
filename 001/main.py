f =  "C:/Python3/python.exe"
#-----0123456789012345678920
#g = f[start:end]

g1 = f[11:]
g2 = f[18:]
g3 = f[3:10]
g4 = f[:10]

count = 0
for ch in f: 
    print(f"{count}\t{ch}")
    count += 1

print(f"Имя файла: {g1}")
print(f"Расширение: {g2}")
print(f"Имя каталога: {g3}")
print(f"Полный путь к каталогу: {g4}")
