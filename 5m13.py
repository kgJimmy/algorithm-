#   Greedy

a = 9860
count = 0 
coin_types = [500,100,50,10]

for coin in coin_types:
    count = count+a // coin
    a %= coin

print(count)


