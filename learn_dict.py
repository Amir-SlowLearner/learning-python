args = {
    "symbol" : "BTCUSDT", 
    "qty" : "0.01"
    }

symbol_1 = args.get("symbol").upper()
symbol_2 = args.get("symbol", "")
print(symbol_1)
print(symbol_2)
print(type(symbol_1))


user = {
    "height"  : 184,
    "weight"  : 84,
    "hobbies" : {"indoor":["music","movies","bodyweight_training"],"outdoor":["walking","eating","running","driving"]}
}

print(user["hobbies"]["indoor"])

list = user["hobbies"]["indoor"]

for i in list:
    print(i)