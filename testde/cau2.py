"""Cau 2: Xu ly chuoi."""


def dem_chu_hoa(s):
    dem = 0
    for ky_tu in s:
        if ky_tu.isupper():
            dem += 1
    return dem


def la_chuoi_doi_xung(s):
    return s == s[::-1]


def tinh_tong_chu_so(s):
    tong = 0
    for ky_tu in s:
        if ky_tu.isdigit():
            tong += int(ky_tu)
    return tong


def main():
    s = input("Nhap chuoi s: ")
    print("So ky tu chu hoa:", dem_chu_hoa(s))

    if la_chuoi_doi_xung(s):
        print("Chuoi doi xung.")
    else:
        print("Chuoi khong doi xung.")

    print("Tong cac chu so trong chuoi:", tinh_tong_chu_so(s))


if __name__ == "__main__":
    main()
