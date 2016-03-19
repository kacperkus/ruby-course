prime_numbers = []
is_palindrome = False


def palindrome(prime_number):
    prime_number = str(prime_number)
    if prime_number == prime_number[::-1]:
        prime_numbers.append(prime_number)

for number in range(999, 1, -1):
    for n in range(2, number):
        if number % n == 0:
            is_palindrome = False
            break
        else:
            is_palindrome = True
    if is_palindrome:
        palindrome(number)

print(prime_numbers[0])
