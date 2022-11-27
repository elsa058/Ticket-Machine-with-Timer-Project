def timer():
    import time
    t = int(input("Enter the time in second:"))
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d},{:02d}'.format(mins, secs)
        print(timeformat)
        time.sleep(1)
        t -= 1




