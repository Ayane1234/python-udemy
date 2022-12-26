# 辞書型のメソッド

car = {
    "brand": "Toyota",
    "model": "Prius",
    "year":2015,
}

tmp_car = {
    "country": "Japan",
    "prefecture": "Aichi",
    "model":"カローラ",
}

car.update(tmp_car)
print("新しいcar:{}".format(car)) 
"""
新しいcar:{'brand': 'Toyota', 
'model': 'カローラ', 
'year': 2015,
'country': 'Japan',
'prefecture': 'Aichi'}

ここでは、追加だけでなく、"model:カローラ"に更新されている。
新しいkeyは追加され、すでにあるkeyの場合はvalueが更新される
""" 

# 以上の更新のやり方以外に以下の方法もあり

car["city"] = "Toyota-shi" #新しいkeyの追加
car["year"] = 2020 #年を更新

print("二回目のcar:{}".format(car))

"""
二回目のcar:{
    'brand': 'Toyota',
    'model': 'カローラ',
    'year': 2020,
    'country': 'Japan',
    'prefecture': 'Aichi',
    'city': 'Toyota-shi'
    }
"""

#dicrionary.popitem
value = car.popitem()
print("car:{}".format(car))
# car:{'brand': 'Toyota', 'model': 'カローラ', 'year': 2020, 'country': 'Japan', 'prefecture': 'Aichi'}
#最後に、追加した"city":"Toyota-shi"が抜き出されている

print("value:{}".format(value)) 
# value:('city', 'Toyota-shi') <= タプル型で返ってくる



# dicrionary.pop
value_2 = car.pop("year")
print("car: {}".format(car)) # popしたkeyと値に抜き出した状態になる
print("value_2: {}".format(value_2)) # popした値が取れる => value_2: 2020

#dicrionary.clear
car.clear()
print("car:{}".format(car)) # => car:{}

# del dicrionary
del car # 変数そのものを削除
print("car:{}".format(car)) 
# =>NameError: name 'car' is not defined. Did you mean: 'chr'?
