#文字列型
fruit = "apple"
print(fruit)
print(type(fruit))

print(fruit * 10)
fruit_10 = fruit * 10
print(fruit_10)

new_fruit = fruit + "banana"
print(new_fruit)

fruits = """apple
banana
grape
"""
print(fruits)

fruit = "banana"
print(fruit[-1])#後ろから１文字目

#encode, decode => bytes[]
byte_fruit = fruit.encode("utf-8")
print(byte_fruit)
print(type(byte_fruit))

#元々のstringする場合には、decode
str_fruit = byte_fruit.decode("utf-8")
print(str_fruit)
print(type(str_fruit))

#count
msg = "ABCDEFG"
print(msg.count("AB"))

# startswith, endswith
print(msg.startswith("AB")) # 始まりの文字が"AB"だったら=> True（返り値が真偽値）
print(msg.endswith("G"))# 終わりの文字が"G"だったら=> True（返り値が真偽値）

# strip(両端), rstrip(右端), lstrip(左端)
msg = " ABC "
print(msg)
print(msg.strip()) #デフォルトで、スペースを削除する

msg = "ABCDEFABC"
print(msg.strip("CBA")) #stripで指定した文字を削除する => "DEF"になる
print(msg.lstrip("CBA")) #lstripで指定した文字を削除する　=> 左端のABCが削除　=> "DEFABC"になる
print(msg.rstrip("CBA")) #rstripで指定した文字を削除する　=> 右端のABCが削除 => "ABCDEF"になる

# upper, lower, swapcase, replace, capitalize

msg = "abcABC"
msg_u = msg.upper() #大文字
msg_l = msg.lower() #小文字
msg_s= msg.swapcase() #大文字と小文字を入れ替え 
print(msg_u, msg_l, msg_s)

msg = "ABCDEABC"
msg_r = msg.replace("ABC", "FFF", 1) 
#第3引数に1を入れると、1番目だけの"ABC"だけを変換する
#第3引数のデフォルトは、"-1"になる　=> 該当するものは全て変換する
print(msg_r)

msg = "hello world"
print(msg.capitalize()) # 初めの文字のみを、大文字にする　=> "Hello world"になる

# 文字列の一部取り出し、format, islower, isupper
msg = "hello, my name is taro"
print(msg[:5]) #msgの初めから6文字目までを取り出す => "hello"になる
print(msg[5:]) #msgの初めから6文字目以降を取り出す => ", my name is taro"になる
print(msg[0:6]) #msgのインデックス0から5まで取り出す => "hello,"になる
print(msg[0:10:2]) #一つ飛ばしで取り出す => "hlo y"になる
print(msg[1:10:3]) #二つ飛ばしで取り出す => "eom"になる

print("hello {}".format("Taro"))
name = "Jiro"
print(f"hello {name}") #3.6以上
print(f"{name=}") #3.8以上 

msg = "apple"
print(msg.islower()) #全て小文字ならtrue
print(msg.isupper()) #全て大文字ならtrue

# find, index, rfind, rindex
msg = "ABCDEABC"
print(msg.find("ABC")) #存在するインデックスを表示　=> 0
print(msg.rfind("ABC")) #右端から存在するインデックスを表示　=> 5
print(msg.index("ABC"))
print(msg.rindex("ABC"))

print(msg.find("ABCF")) #
print(msg.index("ABCF"))