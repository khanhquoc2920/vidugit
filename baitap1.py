dslop=[]

for i in range(5):
    hoten = input("Nhap ho ten  "+str(i) )
    dslop.append(hoten)

print(dslop)
vitri = int(input("ban muon sua vi tri  thu may")) 
hoten = input("nhap ho ten moi")
dslop[vitri] = hoten 
print(dslop.count()) 