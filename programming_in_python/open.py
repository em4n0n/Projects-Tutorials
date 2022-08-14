f​unciton calculate_subtotal ​->

subtotal = 0    

for item in order:        

    subtotal += item['price']    

return float(subtotal)  

f​unction calculate_tax  ->

tax = subtotal * 0.15    

return round(float(tax), 2)  

f​unction summarize_order  ->

subtotal = calculate_subtotal(order)    

tax = calculate_tax(subtotal)    

total = round((subtotal + tax), 2)    

names = [item["name"] for item in order]    

return names, total  