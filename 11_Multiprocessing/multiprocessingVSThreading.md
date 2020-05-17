Threading (gleichzeitig):
- Innerhalb des vorhandenen Prozesses wird ein neuer Thread erzeugt
- Das Starten eines Threads ist schneller als das Starten eines Prozesses
- Der Speicher wird von allen Threads gemeinsam genutzt
- Mutexe, die häufig erforderlich sind, um den Zugriff auf gemeinsam genutzte Daten zu steuern

Multiprocessing (Parallel):
- Ein neuer Prozess wird unabhängig vom ersten Prozess gestartet
- Das Starten eines Prozesses ist langsamer als das Starten eines Threads
- Der Speicher wird nicht zwischen Prozessen geteilt
- Mutexe nicht erforderlich (es sei denn, der neue Prozess wird eingefädelt)
