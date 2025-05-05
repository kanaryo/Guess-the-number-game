import sys
import random

#最小値の入力
sys.stdout.buffer.write(b'Enter a minimum value.\n')
sys.stdout.flush()
n = int(sys.stdin.buffer.readline().decode().strip())

#最大値の入力 test
sys.stdout.buffer.write(b'Enter a maximum value.\n')
sys.stdout.flush()
m = int(sys.stdin.buffer.readline().decode().strip())

if n > m:
    sys.stdout.buffer.write(b'Error: Minimum value must be less than or equal to maximum value.\n')
    sys.stdout.flush()
    sys.exit(1) 

#乱数の生成
random_number = random.randint(n, m)

#推測値の入力
while True:
    sys.stdout.buffer.write(b'What would you guess the number is?\n')
    sys.stdout.flush()
    guessed_number = int(sys.stdin.buffer.readline().decode().strip())

    if random_number == guessed_number:
        sys.stdout.buffer.write(b'Correct.\n')
        sys.stdout.flush()
        break
    else:
        sys.stdout.flush()
        sys.stdout.buffer.write(b'Incorrect.\n')