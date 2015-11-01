# Palindrome with ternary operator

is_pali = "It's a palindrome!"
not_pali = "It's not a palindrome!"

puts "Write a palindrome:"
palindrome = gets.chomp.downcase # Using .downcase method we ignore uppercases.

puts palindrome == palindrome.reverse ? is_pali : not_pali
