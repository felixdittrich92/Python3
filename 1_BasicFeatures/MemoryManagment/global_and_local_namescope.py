# local wenn die Variable zu Funktion oder Klasse gehört
# global wenn Sie überall verwendbar ist


POWER_OF = 2 # große Variablennamen => Konstante

def function(a):
    b = a ** POWER_OF # local scope
    print(a, b)

value = 3 # global scope
function(value)

def function2():
    print(value)

function2()

# global definiert
print("----------global----------")
print(globals())
# local definiert
print("----------local----------")
print(locals())


# Einstiegspunkt 
def main():
    print("ich bin die Main und werde als Einstiegspunkt ausgeführt")

if __name__=="__main__":
    main()