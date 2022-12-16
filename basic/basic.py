# 標準出力、コメント文、変数

print("Hello Python") #Hello Python

#　コメント
"""
複数文のコメントが書けるらしい
"""

# ここをコメントしたい場合は、ctrl＋スラッシュでコメントになる

# 標準出力
name = input("あなたの名前はなんですか？:")
age = 30
print("あなたの名前は:", name)

# format関数 変数の埋め込み
print("私の名前は = {}, 年齢は{}".format(name, age))

# 複数の変数に同じ文字列を入れる
a = b = "Hello"

print(a,b)