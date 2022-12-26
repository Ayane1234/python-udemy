#Dictionary(辞書型)

car = {
    "brand":"Toyota",
    "model":"Prius",
    "year":2015
}

print(car["brand"])
print(car.get("bran", "ないよ"))

"""
car["bra"]と、存在しないkeyになるとエラー文
car.get("bra")と、存在しないkeyになると"None"が返される
  第二引数には文字列や数値を入れることが可能
  car.get("bra", "Does not exist")などとすると、
  存在しないKeyの場合に、第二引数の値が表示される
"""

print(car.keys()) # key list
print(car.values()) # value list
print(car.items()) # key + item

# for文で、一つ一つのitemを取り出す
for key , value in car.items():
    print("key = {}, value = {}".format(key,value))

if "brand" in car:
    print("車のブランドは{}".format(car["brand"]))
