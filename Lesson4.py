# Câu điều kiện
    # Dạng thiếu
age = int(input('Hãy nhập tuổi của bạn: '))
if age >= 18:
    print('Bạn đã đủ 18 tuổi')

    # Dạng đủ
n = int(input('Nhập 1 số nguyên: '))
if n % 2 == 0:
    print(n, 'là số chẵn')
else:
    print(n, 'là số lẻ')

    # Dạng đa nhánh
        # [8, 10]: Giỏi, [6.5, 8): Khá, [5, 6.5): TB, [0, 5): Yếu
score = float(input('Hãy nhập điểm của bạn: '))
if 8 <= score <= 10:
    print('Xếp loại: Giỏi')
elif 6.5 <= score < 8:
    print('Xếp loại: Khá')
elif 5 <= score < 6.5:
    print('Xếp loại: Trung bình')
elif 0 <= score < 5:
    print('Xếp loại: Yếu')
else:
    print('Điểm không hợp lệ')

    # cách 2:
score = float(input('Hãy nhập điểm của bạn: '))
if score < 0 or score > 10:
    print('Điểm không hợp lệ')
else:
    if score >= 8:
        print('Xếp loại: Giỏi')
    elif score >= 6.5:
        print('Xếp loại: Khá')
    elif score >= 5:
        print('Xếp loại: Trung bình')
    else:
        print('Xếp loại: Yếu')
    
# Bài 1: Nhập số điện bạn sử dụng (kWh)
# Tính tiền điện theo dữ liệu sau và hiển thị ra màn hình
# Bậc 1:    0kWh - 50kWh           giá 1.8k VND
# Bậc 2:    51kWh - 100kWh         giá 2k VND
# Bậc 3:    101kWh - 200kWh        giá 2.3k VND
# Bậc 4:    trên 200kWh            giá 3k VND
            #  Bài làm
# Nhập số điện cần sử dụng
kWh = float(input('Nhập só điện đã sử dụng: '))
# Khai báo biến cash để tính tiền
cash = 0
# Tính tiền theo bậc giá điện
if kWh < 0:                 # Nhập sai
    print('Số điện không hợp lệ')
elif 0 <= kWh <= 50:        # Bậc 1
    cash = kWh * 1.8
elif 50 < kWh <= 100:       # Bậc 2
    cash = 50 * 1.8 + (kWh - 50) * 2
elif 100 < kWh <= 200:      # Bậc 3
    cash = 50 * 1.8 + 50 * 2 + (kWh - 100) * 2.3
else:                       # Bậc 4
    cash = 50 * 1.8 + 50 * 2 + 100 * 2.3 + (kWh - 200) * 3
# Hiển thị kết quả
print(f'Tiền điện bạn phải trả là: {cash}k VND')