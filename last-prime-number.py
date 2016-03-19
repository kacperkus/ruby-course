numbers = [2]
prime_numbers = [2]

is_prime = False

for number in range(3, 1000):
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime:
        numbers.append(number)

for number in numbers:
    number = str(number)
    if number == number[::-1]:
        prime_numbers.append(number)

print(prime_numbers[-1])
