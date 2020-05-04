# Iterator: 
# iter macht Objekt iterrierbar  
# next nimmt immer das nächste Element / am Anfang das Erste

print("---------------Iterator------------------")

class PowerOfTwo:
    def __init__(self, N):
        self.N = N

    def __iter__(self):
        self.current_n = 0
        return self # returnt das iterierbare Objekt

    def __next__(self):
        if self.current_n <= self.N:
            current_result = 2**self.current_n
            self.current_n += 1
            return current_result
        else:
            raise StopIteration # beendet Iterration -> wird unbedingt benötigt wenn der Iterator enden soll (endlicher / unendlicher Iterator)

p = PowerOfTwo(10)
p_iter = iter(p) # macht Objekt iterrierbar

for i in p:
    print(i)

power_of_twos = [power for power in PowerOfTwo(10)]
print(power_of_twos)

print("---------------Generator------------------")

# Generator: 
# besser (effizienter) als Iterator speichert allerdings immer nur den letzten Wert ab und nicht wie der Iterator alle
# Funktion mit einem yield statement, 

def PowerOfTwoGenerator(N):
    current_n = 0
    while current_n <= N:
        yield 2**current_n # yield returnt Wert und speichert diesen ab um in im nächsten Aufruf zu verwenden / return "vergisst" diesen Wert
        current_n += 1

g = PowerOfTwoGenerator(10)

for i in g:
    print(i)