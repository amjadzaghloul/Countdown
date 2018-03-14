import time
def countdown(seconds):
    i = 0
    while i < seconds:
        print seconds
        seconds -=1
        time.sleep(1)
    print "End countdown"
countdown(int(raw_input("Please enter the number of seconds")))