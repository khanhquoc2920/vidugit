# def hello(name,age):
#     print("Xin chào tôi là {} - {} tuổi".format(name,age))
# hello("Khanh",21)

# def hello2(*name):
#     print("số lượng tham số :{}".format(len(name)))
#     for x in name:
#         print("xin chào {}".format(x))
# hello2()
# hello2("khanh","Huy","Quang")

# def ttsinhvien(**sinhvien):
#     if "hoten" in sinhvien.keys():
#         print("Họ tên :{}".format(sinhvien["hoten"]))
#     if "diachi" in sinhvien.keys():
#         print("Địa chỉ :{}".format(sinhvien["diachi"]))
#     if "namsinh" in sinhvien.keys():
#         tuoi = 2021 - sinhvien["namsinh"]
#         print("Tuổi :{}".format(tuoi))
# ttsinhvien(hoten="khanh",diachi="hue",namsinh=2000)
def Xin_chao(ten, loi_chao = "nice day"):
    
    print("Xin chào",ten + ', ' + loi_chao)

Xin_chao("Hải")
Xin_chao("Dũng","bạn khỏe không?")

def xin_chao2(dstv):
    for tv in dstv:
        print(f" chao {tv}")
dstv = [" khanh","Nam","Cuong"]
xin_chao2(dstv)


test = lambda a : a * 2
print(test(10))


def luythua(n):
    x = lambda x : x** n
    return(x)
tinhmu = luythua(2)
print(tinhmu(10))