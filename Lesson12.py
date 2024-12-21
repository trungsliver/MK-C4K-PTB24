# Hàm - chương trình con

# Hàm không có giá trị trả về
def hello():
    print('Xin chào Dũng')
    print('Xin chào Ngọc')
    print('Xin chào Giang')
    
    # Gọi hàm khi cần sử dụng
hello()

# Hàm có tham số truyền vào
def hello(name):
    print(f'Xin chào {name}')

hello('Nam')
hello('An')

# Hàm có giá trị trả về
def dtich_HCN(a, b):
    return a * b

print('Dien tich HCN:', dtich_HCN(5,3))

# ============ LUYỆN TẬP ===============
# Bài 1: Viết hàm truyền vào 1 số nguyên dương n
# Yêu cầu: trả về tổng các số chẵn từ 1 đến n
def sum_even(n:int):
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum += i
    return sum
print('Tổng các số chẵn từ 1 đến 10 =', sum_even(10))