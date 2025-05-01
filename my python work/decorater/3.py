#anything meaningful?
import time
def timer(func):
  def wrapper(*args):
    start = time.time() # start the timer.
    func(*args)
    print('time taken by',func.__name__,time.time()-start,'secs')
  return wrapper

@timer
def hello():
  print('hello wolrd')
  time.sleep(2)

@timer
def abc():
  print("in abc function.")
  time.sleep(2)

@timer
def square(num):
  print(num**2)
hello()
abc()
square(2)