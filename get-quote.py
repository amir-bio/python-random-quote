import random

def m():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  i = random.randint(0, len(quotes) - 1)
  print(quotes[i])

if __name__== "__main__":
  m()
