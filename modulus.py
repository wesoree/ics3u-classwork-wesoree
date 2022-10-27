import time

for num in range(0,181,1):
    print(num)
    if num%10 == 0:
        print('BEEP')
    time.sleep(.05)
