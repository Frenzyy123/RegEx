import re
email = "jovan.pesic17@gmail.com"
#do @ nam treba svi karakteri sem razmak ja mislim, onda neki neka mala slova i na kraju .com
re.match(r"^[A-Za-z\d._+-]+@[A-Za-z\d]+\.[a-z]+$",email)