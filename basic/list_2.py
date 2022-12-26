# リストのメソッド
list_a = [1,2,3,4,5]

list_b = list_a[:3] #リストの3つ目まで取り出す
print(list_b) # [1,2,3]

list_c = list_a[3:]#リストの3つ目以降を取り出す
print(list_c) # [4,5]

list_d = list_a[1:4] #インデックス1から3までを取り出す
print("list_d= {}".format(list_d)) # list_d= [2, 3, 4]

list_e= list_a[1:4:2] ##インデックス1から3までを、一つ飛ばしで抜き出す
print("list_e= {}".format(list_e)) # list_e= [2, 4]


# append, extend, insert, clear

list_a.append("apple") #要素を追加したい
print("list_a= {}".format(list_a)) #list_a= [1, 2, 3, 4, 5, 'apple']

list_a.append(["banana, orange"]) #リストを追加する場合
print("list_a= {}".format(list_a)) #list_a= [1, 2, 3, 4, 5, 'apple', ['banana, orange']]

list_a.extend(["banana", "orange"]) # リストではなく、複数の要素を追加したい場合
print("list_a= {}".format(list_a)) # list_a= [1, 2, 3, 4, 5, 'apple', 'banana', 'orange']

list_f = [1,2,3,4,"apple"]
list_f.insert(1, "peach") # 第一引数にインデックス、第二引数に追加したい要素を入れる
print("list_f= {}".format(list_f)) #list_f= [1, 'peach', 2, 3, 4, 'apple']　<= インデックス１に追加されて他はずれる

list_f.clear() # 全部の要素を削除
print("list_f= {}".format(list_f)) #list_f= []

