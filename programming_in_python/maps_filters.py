from re import L


menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]
# I want all of the coffees with the letter 'c'. Pass the list to comnpare it to the letter c
def find_coffee(coffee):
    if coffee[0] == 'c': # 0 sets in action on the first letter of the variable
        return coffee

# map_coffee = map(find_coffee, menu) # not calling the function, just passing it in like an argument
# print(map_coffee)
# for x in map_coffee: # iterates throught the map object
#     print(x)

filter_coffee = filter(find_coffee, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)