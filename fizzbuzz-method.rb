# Fizz Buzz (with method)

def fizzBuzz(num)
  divBy3 = (num % 3 == 0)
  divBy5 = (num % 5 == 0)

  case
    when divBy3 && divBy5
      puts "FizzBuzz"
    when divBy3
      puts "Fizz"
    when divBy5
      puts "Buzz"
    else
      puts num
  end
  
end

(1..100).each { |n| fizzBuzz n }
