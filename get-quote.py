import random

def m():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  i1, i2 = random.sample(range(0, len(quotes)), 2)
  print(quotes[i1].strip())
  print(quotes[i2])

if __name__== "__main__":
  m()
