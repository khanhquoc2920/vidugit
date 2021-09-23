tongtien = int(input("Ban da co so tien "))
songdonggong = 0 

while tongtien < 100000 :
    donggop = int(input("moi ban dong gop vao :"))
    tongtien += donggop 
    if tongtien > 100000: continue
    songdonggong += 1
else:
    print("ban da co du tien choi game!!!")
print("da quyen gop duoc {} tu {} nguoi".format(tongtien,songdonggong))