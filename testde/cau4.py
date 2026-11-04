"""Cau 4: Quan ly sach trong thu vien bang dictionary."""


def nhap_thong_tin_sach():
    ma_sach = input("Ma so sach: ").strip()
    ten_sach = input("Ten sach: ").strip()
    ten_tac_gia = input("Ten tac gia: ").strip()
    nha_xuat_ban = input("Nha xuat ban: ").strip()

    while True:
        try:
            nam_xuat_ban = int(input("Nam xuat ban: "))
            break
        except ValueError:
            print("Nam xuat ban phai la so nguyen.")

    return ma_sach, {
        "Ten sach": ten_sach,
        "Ten tac gia": ten_tac_gia,
        "Nha xuat ban": nha_xuat_ban,
        "Nam xuat ban": nam_xuat_ban,
    }


def main():
    thu_vien = {}

    while True:
        try:
            so_luong = int(input("Nhap so luong sach: "))
            if so_luong >= 0:
                break
            print("So luong sach khong duoc am.")
        except ValueError:
            print("Vui long nhap mot so nguyen.")

    for i in range(so_luong):
        print(f"\nNhap thong tin sach thu {i + 1}:")
        ma_sach, thong_tin = nhap_thong_tin_sach()
        thu_vien[ma_sach] = thong_tin

    print("\nDanh sach sach trong thu vien:")
    for ma_sach, thong_tin in thu_vien.items():
        print("Ma sach:", ma_sach)
        for ten_truong, gia_tri in thong_tin.items():
            print(f"{ten_truong}: {gia_tri}")
        print("-" * 30)

    ma_can_xoa = input("\nNhap ma so sach can xoa: ").strip()
    if ma_can_xoa in thu_vien:
        del thu_vien[ma_can_xoa]
        print("Da xoa sach co ma:", ma_can_xoa)
    else:
        print("Khong tim thay cuon sach can xoa.")

    print("\nDictionary sau khi xu ly:")
    print(thu_vien)


if __name__ == "__main__":
    main()
