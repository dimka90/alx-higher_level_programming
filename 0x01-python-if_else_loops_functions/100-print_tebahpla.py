#!/usr/bin/python3
diff = 0
for counter in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(counter - diff)), end="")
    diff = 32 if diff == 0 else 0
