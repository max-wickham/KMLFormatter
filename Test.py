

import string
import random
lst = [random.choice(string.ascii_letters + string.digits) for n in range(30)]
x = "".join(lst)
print(x)


