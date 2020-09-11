class SudokuSolver:
    def __init__(self, feld, groesse):
        self.vollstaendig = True
        self.feld = feld
        self.ur = self.feld
        self.alle = [self.feld]
        self.groesse = groesse
        self.alphabet = range(1, self.groesse + 1)
        if len(self.feld) == self.groesse:
            for i in self.feld:
                if len(i) != self.groesse:
                    # self.feld = None
                    exit("Feld nicht korrekt")
        else:
            exit("Feld nicht korrekt")
        self.ueberpruefen()

    def ueberpruefen(self):
        # Zeilen prüfen
        i = 0
        while i < len(self.feld):
            j = 0
            while j < len(self.feld):
                k = 0
                while k < len(self.feld):
                    if k == j:
                        k += 1
                        continue
                    if self.feld[i][j] is None:
                        k += 1
                        self.vollstaendig = False
                        continue
                    if self.feld[i][j] == self.feld[i][k]:
                        return False
                    k += 1
                j += 1
            i += 1
        # Spalten prüfen
        i = 0
        while i < len(self.feld):
            j = 0
            while j < len(self.feld):
                k = 0
                while k < len(self.feld):
                    if j == k:
                        k += 1
                        continue
                    if self.feld[k][i] is None:
                        k += 1
                        continue
                    if self.feld[j][i] == self.feld[k][i] and self.feld[j][i] is not None and self.feld[k][
                        i] is not None:
                        return False
                    k += 1
                j += 1
            i += 1
        # Unterteilung prüfen / Kleine "Quadrate" prüfen
        (x, y) = self.quadratgroesse()
        quadratex = self.groesse / x
        quadratey = self.groesse / y
        qx = 0
        qy = 0
        while qy < quadratey:
            while qx < quadratex:
                quadrat = []
                i = qy * y
                while i < (qy + 1) * y:
                    j = qx * x
                    while j < (qx + 1) * x:
                        quadrat += [self.feld[i][j]]
                        j += 1
                    i += 1
                i = 0
                while i < len(quadrat):
                    j = 0
                    if quadrat[i] is None:
                        i += 1
                        continue
                    while j < len(quadrat):
                        if i == j:
                            j += 1
                            continue
                        if quadrat[j] is None:
                            j += 1
                            continue
                        if quadrat[i] == quadrat[j]:
                            return False
                        j += 1
                    i += 1
                qx += 1
            qy += 1
        return True

    def quadratgroesse(self):
        global yalt
        x = 1
        y = self.groesse
        while x - y < 0:
            xalt = x
            yalt = y
            x = x + 1
            if (self.groesse // x) * x == self.groesse:
                y = self.groesse // x
        if xalt * yalt == self.groesse:
            return xalt, yalt
        while xalt * yalt != self.groesse:
            if xalt * yalt < self.groesse:
                xalt += 1
            else:
                xalt -= 1
        return xalt, yalt

    def loesen(self):
        """
            Lösen von einzelnen feldern
        """
        while not self.vollstaendig:
            i = 0
            while i < self.groesse:
                j = 0
                while j < self.groesse:
                    if self.feld[i][j] is not None:
                        j += 1
                        continue
                    # durchprobieren
                    print("durchprobieren")
                    k = 0
                    if self.ueberpruefen():
                        print("(i, j, k, self.alphabet, self.alphabaet[k], self.vollstaendig)",
                              (i, j, k, self.alphabet, self.alphabet[k], self.vollstaendig))
                        self.feld[i][j] = self.alphabet[k]
                        while self.ueberpruefen() and k < len(self.alphabet):
                            print("(i, j, k, self.alphabet, self.alphabaet[k], self.vollstaendig, self.ueberpruefen())",
                                  (i, j, k, self.alphabet, self.alphabet[k], self.vollstaendig, self.ueberpruefen()))
                            self.feld[i][j] = self.alphabet[k]
                            if self.ueberpruefen():
                                break
                            k += 1
                    else:
                        print("Fehler")
                    self.alle += [self.feld]
                    j += 1
                i += 1


def eingabe():
    sudoku = []
    zeile = input("Geben Sie die 1. Zeile mit Leerzeichen als Trennzeichen zwischen Feldern und Punkten für Leere Felder ein ")
    zeile = zeile.split()
    i = 0
    while i < len(zeile):
        if zeile[i] == ".":
            zeile[i] = None
        else:
            zeile[i] = int(zeile[i])
        i += 1
    sudoku += [zeile]
    groesse = len(zeile)
    a = 1
    while a < groesse:
        zeile = input("Geben Sie die " + str(
            a + 1) + ". Zeile mit Leerzeichen als Trennzeichen zwischen Feldern und Punkten für Leere Felder ein ")
        zeile = zeile.split()
        i = 0
        while i < len(zeile):
            if zeile[i] == ".":
                zeile[i] = None
            else:
                zeile[i] = int(zeile[i])
            i += 1
        groesse = len(zeile)
        sudoku += [zeile]
        a += 1
    print(sudoku)
    global s
    s = SudokuSolver(sudoku, groesse)


def test():
    global s
    s = SudokuSolver([[3, None, 5, 4, None, None, None, 7, 2], [None, 2, None, 1, None, None, None, None, 5],
                      [None, 8, None, None, None, None, None, 4, None], [None, 7, None, None, None, 2, None, None, 3],
                      [None, 4, None, None, 5, 3, 6, 1, 7], [None, 3, None, 6, 4, None, None, None, None],
                      [None, None, None, 3, 9, None, 2, None, None], [4, None, None, 5, None, 1, None, 6, 8],
                      [2, 5, None, None, None, None, None, 3, 1]], 9)


test()
s.loesen()
