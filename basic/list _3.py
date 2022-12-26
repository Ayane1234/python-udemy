#remove, pop, count, index
list_g = [1,2,3,3,3,4]
list_g.remove(3) #左から数えて、最初に登場する3を削除する
print(f"list_g= {list_g}") # list_g= [1, 2, 3, 3, 4]

value = list_g.pop() #list_gの最後のインデックスの要素を取り出す
print(f"{list_g=}, {value=}") #list_g=[1, 2, 3, 3], value=4

list_h = [0,1,1,2,2,2,3,3,3]
print(f"{list_h.count(2)=}") # 2の数をカウントする　=> list_h.count(2)=3

print(f"{list_h.index(2)=}") # 2が初めて登場するインデックス表示　=> list_h.index(2)=3

# copy
list_1 = [0,1,1,2,2,2,3,3]
print("list_1={}".format(list_1))
list_2 = list_1
list_2[0] = "AAAA"
print("list_1={}".format(list_1)) # list_1=['AAAA', 1, 1, 2, 2, 2, 3, 3]
"""
list_2を書き換えると、メモリに格納されている参照元の
list_1の要素も書き換えられてしまう
"""
list_3=[0,1,1,2,2,2,3,3]
print("list_3={}".format(list_3))
list_4= list_3.copy()
list_4[0]= "AAA"
print("list_3={}".format(list_3))

"""
list.copy()によって、新たに作成list_4として作成。
別のメモリ上におき、別のメモリアドレスをlist_4に渡すことになるらしい
"""