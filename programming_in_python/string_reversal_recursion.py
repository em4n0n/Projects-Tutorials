# def string_reverse(str):
#     if len(str) == 0:
#         return str
#     else:
#         return string_reverse(str[1:]) + str[0] #traversed from the front, skipping the first character in every loop
        
# str = "reversal"
# reverse = string_reverse(str)
# print(reverse)

def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]

str = "reversal"
reverse = string_reverse(str)
print(reverse)