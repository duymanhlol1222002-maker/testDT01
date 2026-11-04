"""Auto test va cham diem 5 bai trong thu muc testde.

Cach chay:
    python autotest.py

Moi cau 2 diem, gom 2 bo test (moi bo 1 diem).
Khong can cai them thu vien.
"""
import ast
import math
import re
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
TIMEOUT = 5


def run_file(filename, input_data=""):
    path = BASE_DIR / filename
    if not path.is_file():
        return False, "", f"Khong tim thay {path.name}"

    try:
        result = subprocess.run(
            [sys.executable, str(path)],
            input=input_data,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=TIMEOUT,
            cwd=BASE_DIR,
        )
        output = result.stdout
        if result.returncode != 0:
            return False, output, result.stderr or f"Chuong trinh thoat voi ma {result.returncode}"
        return True, output, ""
    except subprocess.TimeoutExpired:
        return False, "", f"Qua {TIMEOUT} giay, co the chuong trinh dang lap vo han"
    except Exception as exc:
        return False, "", str(exc)


def compact(text):
    return re.sub(r"[\s,:=]", "", text.lower())


def has_value(output, label, expected):
    """Kiem tra gia tri nam sau nhan in ra."""
    text = output.lower()
    pos = text.find(label.lower())
    if pos < 0:
        return False
    tail = text[pos + len(label):]
    match = re.search(r"-?\d+(?:\.\d+)?", tail)
    if not match:
        return False
    try:
        return math.isclose(float(match.group()), float(expected), rel_tol=1e-5, abs_tol=1e-5)
    except ValueError:
        return False


def test_cau1(output, odd_count, total):
    return (
        has_value(output, "So luong chu so le:", odd_count)
        and has_value(output, "Tong S =", total)
    )


def test_cau2(output, uppercase_count, palindrome, digit_sum):
    text = compact(output)
    count_ok = f"sokytuchuhoa:{uppercase_count}" in text
    sum_ok = f"tongcacchusotrongchuoi:{digit_sum}" in text
    if palindrome:
        palindrome_ok = "chuoidoxung." in text
    else:
        palindrome_ok = "chuoi khong doi xung." in output.lower() or "chuoikhongdoixung." in text
    return count_ok and sum_ok and palindrome_ok


def test_cau3(output, even_sum, k, occurrences):
    return (
        has_value(output, "Tong cac so duong chan:", even_sum)
        and has_value(output, f"So lan xuat hien cua {k}:", occurrences)
    )


def test_cau4(output, expected_dictionary):
    # Chuong trinh in dictionary sau xu ly o dong cuoi cung.
    for line in reversed(output.splitlines()):
        line = line.strip()
        if line.startswith("{") and line.endswith("}"):
            try:
                return ast.literal_eval(line) == expected_dictionary
            except (ValueError, SyntaxError):
                pass
    return False


def test_cau5(output, expected_values):
    text = compact(output)
    return all(compact(value) in text for value in expected_values)


TESTS = [
    {
        "name": "Cau 1 - So nguyen va tong S",
        "file": "cau1.py",
        "cases": [
            ("135\n", lambda out: test_cau1(out, 2, sum(1 / (2 * i) for i in range(1, 136))), "n = 135"),
            ("2468\n", lambda out: test_cau1(out, 0, sum(1 / (2 * i) for i in range(1, 2469))), "n = 2468 (ngoai gioi han, khong dung test nay)"),
        ],
    },
    {
        "name": "Cau 2 - Xu ly chuoi",
        "file": "cau2.py",
        "cases": [
            ("Abba12\n", lambda out: test_cau2(out, 1, False, 3), "Chuoi Abba12"),
            ("A1b1A\n", lambda out: test_cau2(out, 2, True, 2), "Chuoi A1b1A"),
        ],
    },
    {
        "name": "Cau 3 - Danh sach so nguyen",
        "file": "cau3.py",
        "cases": [
            ("2\n-4\n6\n0\n2\n", lambda out: test_cau3(out, 8, 2, 1), "Danh sach 2, -4, 6; k = 2"),
            ("-2\n4\n4\n0\n4\n", lambda out: test_cau3(out, 8, 4, 2), "Danh sach -2, 4, 4; k = 4"),
        ],
    },
    {
        "name": "Cau 4 - Quan ly sach bang Dictionary",
        "file": "cau4.py",
        "cases": [
            (
                "2\nB01\nPython co ban\nAn\nNXB Tre\n2024\nB02\nLap trinh Python\nBinh\nNXB Giao Duc\n2023\nB01\n",
                lambda out: test_cau4(out, {
                    "B02": {
                        "Ten sach": "Lap trinh Python",
                        "Ten tac gia": "Binh",
                        "Nha xuat ban": "NXB Giao Duc",
                        "Nam xuat ban": 2023,
                    }
                }),
                "Nhap 2 sach va xoa B01",
            ),
            (
                "1\nS01\nCo so du lieu\nLan\nNXB Tre\n2022\nS99\n",
                lambda out: test_cau4(out, {
                    "S01": {
                        "Ten sach": "Co so du lieu",
                        "Ten tac gia": "Lan",
                        "Nha xuat ban": "NXB Tre",
                        "Nam xuat ban": 2022,
                    }
                }),
                "Nhap 1 sach, thu xoa ma khong ton tai",
            ),
        ],
    },
    {
        "name": "Cau 5 - Lop DienThoai",
        "file": "cau5.py",
        "cases": [
            (
                "",
                lambda out: test_cau5(out, [
                    "DT01", "iPhone 15 Pro", "Apple", "3274", "28990000",
                    "DT02", "Galaxy S24 Ultra", "Samsung", "5000", "29990000",
                ]),
                "Kiem tra hai doi tuong DT01 va DT02",
            ),
        ],
    },
]


def main():
    print("=" * 58)
    print("             AUTO TEST - DE PYTHON")
    print("=" * 58)
    total_score = 0.0
    max_score = 0.0

    for question in TESTS:
        print(f"\n{question['name']}")
        cases = question["cases"]
        points_per_case = 2.0 / len(cases)
        question_score = 0.0

        for index, (input_data, checker, description) in enumerate(cases, 1):
            ok, output, error = run_file(question["file"], input_data)
            passed = False
            if ok:
                try:
                    passed = bool(checker(output))
                except Exception as exc:
                    error = f"Loi khi kiem tra ket qua: {exc}"

            if passed:
                question_score += points_per_case
                print(f"  [DUNG] Test {index}: {description} (+{points_per_case:.2f})")
            else:
                print(f"  [SAI]  Test {index}: {description}")
                if error:
                    print(f"         Loi: {error}")
                elif output.strip():
                    print("         Dau ra:")
                    for line in output.strip().splitlines()[-5:]:
                        print("         " + line)
                else:
                    print("         Khong co dau ra.")

        question_score = round(question_score, 2)
        total_score += question_score
        max_score += 2.0
        print(f"  Diem cau nay: {question_score:.2f}/2.00")

    print("\n" + "=" * 58)
    print(f" TONG DIEM: {total_score:.2f}/{max_score:.0f}")
    print("=" * 58)


if __name__ == "__main__":
    main()
