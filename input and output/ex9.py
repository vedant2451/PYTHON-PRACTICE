# Check file is empty or not

import os

size = os.stat("input and output/test.txt").st_size
if size == 0:
    print('file is empty')