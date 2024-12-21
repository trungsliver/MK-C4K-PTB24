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

# Bài 2: Viết hàm truyền vào 1 số nguyên âm n
# Yêu cầu: Trả về số lượng các số lẻ từ n đến 0
def count_odd(n:int):
    count = 0
    for i in range(n, 1):
        if i % 2 != 0:
            count += 1
    return count
print('Số lượng các số lẻ từ -10 đến 0 =', count_odd(-10))

# Bài 3: Viết hàm truyền vào 1 danh sách học sinh
# Yêu cầu: hiển thị toàn bộ các phần tử kèm chỉ số index
students = ['Dũng', 'Ngọc', 'An', 'Nam', 'Huy', 'Giang']
def show_arr(arr):
    for i in range(len(arr)):
        print(f'[{i}] {arr[i]}')
    # Sử dụng hàm
show_arr(students)

# Bài 1: Viết một hàm sum_odd(numbers) để tính tổng các số lẻ trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về tổng các số lẻ trong danh sách đó.
num_list = [1, 2, 3, 4, 5]
def sum_odd(numbers):
    sum = 0
    for item in numbers:
        if item % 2 != 0:
            sum += item
    return sum
print('Tổng các số lẻ trong danh sách:', sum_odd(num_list))

# Bài 2: Viết một hàm is_prime(n) để kiểm tra xem một số nguyên dương n có phải là số nguyên tố hay không.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về True nếu n là số nguyên tố, ngược lại trả về False.
def is_prime(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False
print("12:", is_prime(12))
print("13:", is_prime(13))

# Bài 3: Viết một hàm count_words(s) để đếm số lượng từ trong một chuỗi s.
# 	YC1: Hàm nhận vào một chuỗi ký tự s.
# 	YC2: Hàm trả về số lượng từ trong chuỗi đó.
def count_words(s):
    words = s.strip().split()
    return len(words)
str1 = 'Dũng không làm gì trong giờ học'
print('Số lượng từ trong chuỗi:', count_words(str1))

# Bài 4: Viết một hàm sum_of_digits(n) để tính tổng các chữ số của một số nguyên dương n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về tổng các chữ số của n.
def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum = sum + n%10
        n = n // 10
    return sum
num = 12345
print(f'Tổng các chữ số của {num} là: {sum_of_digits(num)}')

# Bài 5: Viết một hàm find_max(numbers) để tìm vị trí số lớn nhất trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về vị trí số lớn nhất trong danh sách đó.
num_list = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]
def find_max(numbers):
    for i in range(len(numbers)):
        if numbers[i] == max(numbers):
            return i
print('Vị trí phần tử lớn nhất:', find_max(num_list))

# Bài 6: Viết một hàm sum_to_n(n) để tính tổng các số từ 1 đến n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	Yc2: Hàm trả về tổng các số từ 1 đến n.
def sum_to_n(n:int):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
print('Tổng các số từ 1 đến 10 =', sum_to_n(10))


