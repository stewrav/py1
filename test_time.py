import time

x = time.monotonic()
#x = time.CLOCK_MONOTONIC
print( "x ==", x )

time.sleep(1)

y = time.monotonic()
print( "y ==", y )
