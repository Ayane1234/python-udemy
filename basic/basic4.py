# 数値型
value = 1
# print(value)
# value = -2
# print(value)
# value += 3
# print(value // 2 ) 

value += 3 # value = value + 3
# value -= 2 # value = value -2
# print(value)
# print(value ** 3) #べき乗

# 浮動小数点数
heigth = 175.5
print(heigth)
print(type(heigth))
print(heigth + 10) #175.5 + 10.0(10がfloat型に変換されてから足される)

#シフト演算
value = 8
print(value >> 2)
 # 8を二進数で表すと、1000
 # それを2つ右にシフトさせると、0010→その結果、十進数に変えると「2」に変わる 
print(value << 3)
 #8を二進数で表すと、1000
 #それを左に３つ0を足すと、100000となる→その結果、十進数に変えると「64」

 #ビット演算
print(12 & 21) # 01100 and 10101 => 00100 => 4
print(12 | 21) # 01100 or 10101 => 11101 => 29

value = 12
value &= 21 # value = value & 21
print(value) # 4