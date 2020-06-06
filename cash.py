from cs50
import get_float

def main():
  while True:
  change = get_float("Change: \n")
if change > 0:
  break
cents = change * 100
total = int(change * 100)
coins = 0

for i in range(total):
  if cents - 25 >= 0:
  cents = cents - 25
coins += 1
elif cents - 10 >= 0:
  cents = cents - 10
coins += 1
elif cents - 5 >= 0:
  cents = cents - 5
coins += 1
elif cents - 1 >= 0:
  cents = cents - 1
coins += 1

print(coins)

main()