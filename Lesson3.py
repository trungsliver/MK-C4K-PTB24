# # Toán tử số học
#     # Các phép toán thông thường: + - * /
#     # Chia lấy dư: %
# print('20 % 3 =', 20%3)
#     # Chia lấy nguyên: //
# print('20 // 3 =', 20//3)
#     # Lũy thừa: ** 
# print('2**2**3 =', 2**2**3)

# # Toán tử số học với string
#     # Phép nối: +
# print('Minh' + ' ' + 'Ngọc')
#     # Phép lặp: *
# print('hi'*3)
# print('Hoàng Nam' * 0)

# # Toán tử quan hệ: => True/False
#     # So sánh bằng: ==
# print(5 == 5)       # output: True
# print(5 == 3)       # output: False
#     # So sánh khác: !=
# print(5 != 3)       # output: True
# print(5 != 5)       # output: False
#     # So sánh lớn hơn, nhỏ hơn: >, >=, <, <=
# print(5 > 3)        # output: True
# print(4 < 7)        # output: True
# print( 6 >= 6)      # output: True
# print(7 <= 6)       # output: False
# print(8 >= 9)       # output: False

# # Toán tử logic: and - or - not
#     # Ví dụ: trà sữa - gà rán

# # Biểu thức logic
# x, y, z = 10, 6, 8
# a = x < 12 and z > 6
# b = x > 15 or y < 8
# c = not b
# print(a)       # output: True
# print(b)       # output: True
# print(c)       # output: False

# ============== LUYỆN TẬP =============
# Bài 1: Thầy Trung mang quà cho lớp nhân dịp Halloween. Túi quà có n viên kẹo và lớp có m học sinh. Số kẹo được chia đều cho các học sinh trong lớp.
# Yêu cầu: 
    # Nhập n & m là 2 số nguyên dương từ bàn phím
    # Hiện ra màn hình số kẹo mỗi học sinh nhận được
    # Hiện ra màn hình số kẹo còn thừa sau khi chia
n = int(input('Nhập số kẹo: '))
m = int(input('Nhập số học sinh: '))
print('Số kẹo mỗi học sinh nhận được:', n//m)
print('Số kẹo còn thừa:', n%m)

# Bài 2: Quy đổi thời gian
# Yêu cầu:
    # Nhập time là số giây cần xử lý (số nguyên)
    # Hiện ra màn hình thời gian sau khi quy đổi (giờ-phút-giây)
    # Ví dụ: 3661s = 1h 1m 1s
time = int(input('Nhập số giây cần xử lý: '))
h = time // 3600
m = (time % 3600) // 60
s = time % 60
print(f'{time}s = {h}h {m}m {s}s')
