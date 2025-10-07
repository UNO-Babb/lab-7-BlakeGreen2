#Problem2.py
#Project Euler problem 4

def main():
  largest = 0

  for i in range(100, 1000):
    for j in range(100, 1000):
      product = i * j
      product_str = str(product)
      reversed_str = ""

      # make the reverse of the number
      for ch in product_str:
        reversed_str = ch + reversed_str

      if product_str == reversed_str and product > largest:
        largest = product

  print("The largest palindrome made from the product of two 3-digit numbers is", largest)

if __name__ == '__main__':
  main()
