"""Cau 3: Xu ly danh sach so nguyen."""


def nhap_danh_sach():
    danh_sach = []
    print("Nhap cac so nguyen (nhap 0 de ket thuc):")

    while True:
        try:
            x = int(input("Nhap x: "))
            if x == 0:
                break
            danh_sach.append(x)
        except ValueError:
            print("Vui long nhap mot so nguyen.")

    return danh_sach


def tong_chan_duong(danh_sach):
    tong = 0
    for x in danh_sach:
        if x > 0 and x % 2 == 0:
            tong += x
    return tong


def main():
    danh_sach = nhap_danh_sach()
    print("Danh sach vua nhap:", danh_sach)
    print("Tong cac so duong chan:", tong_chan_duong(danh_sach))

    try:
        k = int(input("Nhap phan tu k can dem: "))
        print(f"So lan xuat hien cua {k}:", danh_sach.count(k))
    except ValueError:
        print("k phai la mot so nguyen.")


if __name__ == "__main__":
    main()
