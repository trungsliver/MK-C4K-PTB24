a = [10, 5, 1, 2, 6, 4, 9, 3, 7, 8]
# Bài 1: Viết chương trình nhập từ bàn phím danh sách a. Hãy trả về kết quả các phần tử trong danh sách theo thứ tự tăng dần.
a.sort()    # Sắp xếp theo thứ tự từ nhỏ đến lớn
print(a)

# Bài 2: Viết chương trình nhập từ bàn phím danh sách a. Hãy tìm ra phần tử lớn nhất và nhỏ nhất từ danh sách a và trả về kết quả.
#     # Cách 1: Áp dụng với danh sách đã sắp xếp
#         # Phần tử lớn nhất là phần tử cuối cùng (index = -1)
print('Phần tử lớn nhất:', a[-1])
#         # Phần tử nhỏ nhất là phần tử cuối cùng (index = 0)
print('Phần tử nhỏ nhất:', a[0])

#     # Cách 2: Áp dụng với danh sách chưa sắp xếp
print('Phần tử lớn nhất:', max(a))
print('Phần tử nhỏ nhất:', min(a))

# Bài 3: Viết chương trình nhập từ bàn phím danh sách a. Hãy tính giá trị trung bình của các phần tử trong danh sách a và trả về kết quả giá trị trung bình.
    # Tính tổng các phần tử trong danh sách
sum_all = 0         
for item in a:          # Cách duyệt số 2: chỉ dùng value
    sum_all = sum_all + item
    # Tính số lượng phần tử trong danh sách
so_luong = len(a)
    # Tính giá trị trung bình = tổng giá trị / số lượng phần tử
tbc = sum_all / so_luong
print('Giá trị trung bình:', tbc)

# Bài 4: Viết chương trình nhập từ bàn phím danh sách a. Tính tổng các số lẻ và tổng các số chẵn trong danh sách a.
sum_odd = 0                     # Tổng số lẻ
sum_even = 0                    # Tổng số chẵn
for item in a:                  # Cách duyệt số 2: chỉ dùng value
    if item % 2 == 0:           # Kiểm tra số chẵn
        sum_even = sum_even + item
    if item % 2 == 1:           # Kiểm tra số lẻ
        sum_odd = sum_odd + item
print('Tổng số chẵn:', sum_even)
print('Tổng số lẻ:', sum_odd)

# Luyện tập: Danh sách
    # YC1: Nhập vào từ bàn phím 1 danh sách bao gồm 10 số nguyên
arr = [10, 5, 1, 2, 6, 4, 9, 3, 7, 8]

    # YC2: Thêm số '-5' vào vị trí thứ 2 (index=2) trong danh sách
arr.insert(2, -5)
print(arr)

    # YC3: Tính tổng các số chẵn trong danh sách
sum_even = 0
for item in arr:
    if item % 2 == 0:
        sum_even = sum_even + item
print('Tổng các phần tử chẵn:', sum_even)

    # YC4: Đếm số lượng số lẻ có trong danh sách
count_odd = 0
for item in arr:
    if item % 2 == 1:
        count_odd = count_odd + 1
print('Số lượng phần tử lẻ:', count_odd)

    # YC5: Tìm giá trị phần tử lớn nhất của danh sách
print('Giá trị phần tử lớn nhất:', max(arr))

    # YC6: Tìm vị trí phần tử nhỏ nhất của danh sách
for i in range(len(arr)):       # Cách duyệt số 1: dùng cả index và value
    if arr[i] == min(arr):
        print('Vị trí phần tử nhỏ nhất:', i)
    
        # cách ngắn gọn (bonus):
min_index = arr.index(min(arr))
print('Vị trí phần tử nhỏ nhất:', min_index)

    # YC7: Dùng hàm tính giá trị trung bình của các phần tử trong danh sách và làm tròn đến chữ số thập phân thứ 2
    # Tính giá trị trung bình
avg_value = sum(arr) / len(arr)
print('Giá trị trung bình:', avg_value)     # Trước khi làm tròn
    # Làm tròn đến chữ số thập phân thứ 2
avg_value = round(avg_value, 2)
print('Giá trị trung bình:', avg_value)     # Sau khi làm tròn
