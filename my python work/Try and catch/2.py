try:
  f = open('Hello.txt','r')
  print(s)
except FileNotFoundError:
  print('file nai mili')
except Exception as e:
  print("erro ya ha ",e)
else:
  print(f.read())
finally:
  print("it will executed all the time.")

