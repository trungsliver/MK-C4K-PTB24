# Danh sách - Array / List
# Thao tác: CRUD: Create - Read - Update - Delete

# Create - Khởi tạo danh sách
    # Danh sách rỗng - không có phần tử
arr = []
    # Danh sách có sẵn phần tử
arrHS = ['Dũng', 'An', 'Ngọc', 'Nam', 'N.Giang', 'P.Giang']
    # len() - trả về độ dài / số lượng phần tử của danh sách
# print(len(arr))         # Output: 0
# print(len(arrHS))       # Output: 6

# # Read - Duyệt, hiện phần tử danh sách
#     # Hiện phần tử bằng chỉ số index (bắt đầu từ 0)
# print(arrHS[0])         # Output: Dũng
#     # Hiện phần tử cuối cùng (index = -1)
# print(arrHS[5])         # Output: P.Giang
# print(arrHS[-1])        # Output: P.Giang

#     # Duyệt và hiện tất cả phần tử danh sách
#         # Cách 1: Dùng cả index và value
# for i in range(len(arrHS)):
#     print(f'[{i}] {arrHS[i]}')
#         # Cách 2: Chỉ dùng value
# for item in arrHS:
#     print(item)
#         # Cách 3: Sử dụng hàm có sẵn
# for index, value in enumerate(arrHS):
#     print(f'[{index}] {value}')
#         # Cách 4: Để test
# print(arrHS)

# Update - Chỉnh sửa danh sách
    # Thêm phần tử vào cuối danh sách - append(value)
arrHS.append('Huy')
    # Thêm phần tử vào vị trí bất kì - insert(index, value)
arrHS.insert(5, 'Imposter')
    # Chỉnh sửa value phần tử
arrHS[0] = 'Loopy'

# Delete - Xóa phần tử danh sách
    # Xóa phần tử bằng giá trị - remove(value)
arrHS.remove('Huy')
    # Xóa phần tử bằng chỉ số - pop(index)
arrHS.pop(5)
    # Xóa tất cả phần tử danh sách - clear()
arrHS.clear()

# Sắp xếp phần tử danh sách - sort()
num_list = [5, 2, 9, 7, 1, 6, 3, 8, 4]
    # Theo thứ tự từ nhỏ đến lớn
num_list.sort()
# print(num_list)
    # Theo thứ tự từ lớn đến nhỏ
num_list.sort(reverse=True)
# print(num_list)

# Tìm phần tử lớn nhất & nhỏ nhất
# print('Phần tử lớn nhất:', max(num_list))
# print('Phần tử nhỏ nhất:', min(num_list))

# ============== LUYỆN TẬP ================
# Bài 1: Nhập từ bàn phím 1 số nguyên n
# Yêu cầu: Kiểm tra xem n có phải là số nguyên tố hay không
# Biết rằng số nguyên tố là số chỉ chia hết cho 1 và chính nó

# n = int(input('Nhập số nguyên n: '))
# count = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         count = count + 1
# if count == 2:
#     print(n, 'là số nguyên tố')
# else:
#     print(n, 'không phải là số nguyên tố')

# Bài 2: In ra các số nguyên tố trong khoảng [10,30] và tính tổng các số đó
sum = 0
for n in range(10, 31):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1
    if count == 2:
        print(n, end = ' ')
        sum = sum + n
print('\nTổng các số nguyên tố trong khoảng [10,30]:', sum)