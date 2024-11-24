# # Vòng lặp vô hạn - vòng lặp while

# # Đề bài: In ra màn hình các số nguyên từ 1 đến 5
#     # Vòng lặp for:
# for i in range(1,6):
#     print(i, end = ' ')

#     # Vòng lặp while:
# i = 1
# while i <= 5:
#     print(i, end = ' ')
#     i = i + 1   # i += 1

# # Bài 1: Nhập số nguyên n trong khoảng [0,100]
# # Nếu nhập sai (n<0 hoặc n >100) thì yêu cầu nhập lại
# n = int(input('Nhập số nguyên trong khoảng [0,100]: '))
# while n < 0 or n > 100:
#     print('Bạn đã nhập sai, hihi!')
#     n = int(input('\nNhập số nguyên trong khoảng [0,100]: '))
# print('Bạn đã nhập đúng, hihi!')

# # =============== ÔN TẬP ===============
# # Dạng 1: In/Hiển thị ra màn hình
#     # 1.1. In ra màn hình các số trong khoảng [a,b]
# a = int(input('Nhập a: '))
# b = int(input('Nhập b: '))
# for i in range(a, b + 1):
#     print(i, end = ' ')

#     # 1.2. In ra màn hình các số chẵn trong khoảng [a,b]
# a = int(input('Nhập a: '))
# b = int(input('Nhập b: '))
# for i in range(a, b + 1):
#     if i % 2 == 0:
#         print(i, end = ' ')

#     # 1.3. In ra màn hình các số lẻ trong khoảng [a,b]
# a = int(input('Nhập a: '))
# b = int(input('Nhập b: '))
# for i in range(a, b + 1):
#     if i % 2 != 0:
#         print(i, end = ' ')

# # Dạng 2: Tính tổng
#     # 2.1. Tính tổng các số nguyên trong khoảng [a,b]
# a = int(input('Nhập a: '))
# b = int(input('Nhập b: '))
# sum = 0
# for i in range(a, b + 1):
#     sum = sum + i       # sum += i
# print(f'Tổng các số nguyên trong khoảng [{a},{b}]: {sum}')

#     # 2.2. Tính tổng các số lẻ trong khoảng [a,b]
# a = int(input('Nhập a: '))
# b = int(input('Nhập b: '))
# sum = 0
# for i in range(a, b + 1):
#     if i % 2 != 0:
#         sum = sum + i       # sum += i
# print(f'Tổng các số lẻ trong khoảng [{a},{b}]: {sum}')

# # Dạng 3: Đếm số phần tử
#     # 3.1. Đếm số phần tử trong khoảng [a,b]
# a = int(input('Nhập a: '))
# b = int(input('Nhập b: '))
# count = 0
# for i in range(a, b + 1):
#     count = count + 1    # count += 1
# print(f'Số phần tử trong khoảng [{a},{b}]: {count}')

    # 3.2. Đếm số phần tử chẵn trong khoảng [a,b]
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
count = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        count = count + 1    # count += 1
print(f'Số phần tử chẵn trong khoảng [{a},{b}]: {count}')

    # 3.3. Đếm số phần tử âm trong khoảng [a,b]
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
count = 0
for i in range(a, b + 1):
    if i < 0:
        count = count + 1    # count += 1
print(f'Số phần tử âm trong khoảng [{a},{b}]: {count}')
