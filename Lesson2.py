# # Khai báo biến: [Tên biến] = [Giá trị]
# name = 'Bao Nam'    # Khai báo 1 biến
# a,b,c = 8,9,10      # Khai báo nhiều biến 1 lúc

# # Variables - Biến số
#     # Dùng để lưu trữ dữ liệu
#     # Có thể thay đổi được khi lập trình

# # Data Types - Kiểu dữ liệu
#     # String: chuỗi ký tự / xâu ký tự
# name = 'Minh Ngọc'
#     # Int (interger): số nguyên
# age = 12
#     # Float: số thực
# score = 2.5
#     # Boolean: True/False - Đúng/Sai
# male = True

# # Kiểm tra kiểu dữ liệu - type()
# print('Kiểu dữ liệu của name:', type(name))
# print('Kiểu dữ liệu của age:', type(age))
# print('Kiểu dữ liệu của score:', type(score))
# print('Kiểu dữ liệu của male:', type(male))

# # Xác định kiểu dữ liệu khi nhập (ép kiểu)
# name = input('Nhập tên: ')
# age = int(input('Nhập tuổi: '))
# pi = float(input('Nhập số pi: '))
# robot = bool(input('Bạn có phải robot không: '))
# print(type(name), type(age), type(pi), type(robot))

# ================ BÀI TẬP ===================
# Bài 1: Chuyển đổi USD sang VND
    # Nhập số lượng USD muốn chuyển đổi
usd = float(input('Nhập số USD muốn chuyển đổi: $'))
    # Đổi USD sang VND, tỉ giá: 1 USD = 25000 VND
vnd = usd * 25000
    # Đổi kiểu dữ liệu của vnd từ float => int
vnd = int(vnd)
    # Hiển thị số tiền sau khi chuyển đổi
print(f'{usd} USD = {vnd} VND')

# Bài 2: Nhập chiều dài, chiều rộng HCN
# Tính chu vi, diện tích HCN và hiện ra màn hình
    # Bước 1: Nhập chiều dài, chiều rộng HCN
cd = float(input('Nhập chiều dài HCN: '))
cr = float(input('Nhập chiều rộng HCN: '))
    # Bước 2: Tính chu vi, diện tích HCN
chuvi = (cd + cr) * 2
dien_tich = cd * cr
    # Bước 3: Hiển thị kết quả lên màn hình
print('Chu vi HCN là:', chuvi)
print('Diện tích HCN là:', dien_tich)

# Bài 3: Nhập nhiệt độ ở độ C 
# Chuyển đổi sang độ F theo công thức: F = C * 9/5 + 32.
celsius = float(input('Nhập nhiệt độ C: '))
fahrenheit = celsius * 9/5 + 32
print(f'{celsius} độ C = {fahrenheit} độ F')

# Bài 4: Nhập vào giá trị của 2 biến a và b
# Hãy đổi giá trị của chúng cho nhau và hiện kết quả
    # Cách 1: Dùng biến trung gian
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
temp = a
a = b
b = temp
print(f'Kết quả: a = {a}, b = {b}')
    # Cách 2: Dùng toán tử gán
x = int(input('Nhập x: '))
y = int(input('Nhập y: '))
x, y = y, x
print(f'Kết quả: x = {x}, y = {y}')