from datetime import datetime

my_template = "Hello my name is Felix, nice to meet you. Today is the 24.04.2020."
print(my_template)

print("----------altes Format----------")
# %s = String
# %d = Integer
# %e, %f = Float
# %r = Lists, etc.
# %x = Hexa
# %o = Octa
print("Hallo ich heiße %s %s" % ("Hans", "Meier"))

print("----------neueres Format----------")
print("Hallo ich heiße {0} {1}".format("Hans", "Meier"))

number = 10.1
print("{:f}".format(number))

date = datetime.now()
date = "{:%Y-%m-%d}".format(date)
print(date)