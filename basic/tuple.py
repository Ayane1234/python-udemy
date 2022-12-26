# タプル

"""
タプルは、()に囲まれた変数を指す。
オブジェクトIDを変更せずに、
追加や更新、変更ができないことがリスト型との違いがある。

使い所としては、
1. 変更を許可しない変数の時 => pythonは定数がない
    例えば API_KEY=("xxx","yyy")
    再代入をしなければ、中身が変わっていないことが
    保証されるという前提で変数を使いまわせる。
2. 辞書型のkeyにできる
3.パフォーマンスを上げる => アクセスがリストより速いらしい
"""

fruit = ("apple", "banana", "lemon")
print(f"fruit={fruit}") # => fruit=('apple', 'banana', 'lemon')
print(f"fruitのタイプ={type(fruit)}") # => fruitのタイプ=<class 'tuple'>
print(f"fruitのインデックス0番目={fruit[0]}") # => fruitのインデックス0番目=apple
fruit[1] = "melon" # エラー文
