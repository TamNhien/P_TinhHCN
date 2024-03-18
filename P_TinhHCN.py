def main():
    a = float(input("Nhập chiều dài của hình chữ nhật : "))
    b = float(input("Nhập chiều rộng của hình chữ nhật : "))

    P = 2 * (a + b)
    S = a * b

    print(f"Chu vi của hình chữ nhật là : {P}")
    print(f"Diện tích của hình chữ nhật là : {S}")

if __name__ == "__main__":
    main()

