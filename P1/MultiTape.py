import TapeSimpleRigth

class MultiTape:
    def __init__(self, word, states, cant_tipes):
        self.tapes = [cant_tipes]
        for i in self.tapes:
            if i == 0:
                self.tapes[i] = TapeSimpleRigth.TapeSimpleRight(word, states)
            else:
                self.tapes[i] = TapeSimpleRigth.TapeSimpleRight("", states)
        self.ends_right = [cant_tipes * [0]]
        self.empty_sym = "-"
        self.states = states
        self.actual_state = states[0]

    def moveReplace(self, sym, dir, num_tape, state):
        self.tapes[num_tape].moveReplace(sym, dir, state)

    def move(self, dir, num_tape, state):
        self.tapes[num_tape].move(dir, state)

    def getSymbol(self, num_tape):
        return self.tapes[num_tape].getSymbol()
