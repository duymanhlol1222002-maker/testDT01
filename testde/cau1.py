"""Cau 1: Kiem tra n, dem chu so le va tinh tong S."""


def nhap_n():
    while True:
        try:
            n = int(input("Nhap so nguyen duong n (1..1500): "))
            if 1 <= n <= 1500:
                return n
            print("n phai nam trong doan [1, 1500]. Vui long nhap lai.")
        except ValueError:
            print("Vui long nhap mot so nguyen.")


def dem_chu_so_le(n):
    dem = 0
    for chu_so in str(n):
        if int(chu_so) % 2 != 0:
            dem += 1
    return dem


def tinh_tong(n):
    tong = 0
    for i in range(1, n + 1):
        tong += 1 / (2 * i)
    return tong


def main():
    n = nhap_n()
    print("So luong chu so le:", dem_chu_so_le(n))
    print("Tong S =", tinh_tong(n))


if __name__ == "__main__":
    main()
