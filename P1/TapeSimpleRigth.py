class TapeSimpleRight:
    """
    If inf == 0 then moving to right, else moving to left
    """

    def __init__(self, word, states):
        self.header = 0
        self.tape = []
        for i in range(len(word)):
            self.tape.append(word[i])
        self.end_right = len(word)
        self.empty_sym = "-"
        self.states = states
        self.actual_state = states[0]

    def moveReplace(self, sym, dir, state):
        if dir == "R":
            self.tape[self.header] = sym
            self.header += 1
            if self.header == self.end_right:
                self.tape.append(self.empty_sym)
                self.end_right += 1
        else:
            self.tape[self.header] = sym
            if self.header != 0:
                self.header -= 1
        self.actual_state = state

    def move(self, dir, state):
        if dir == "R":
            self.header += 1
        else:
            if self.header != 0:
                self.header -= 1
        self.actual_state = state

    def getSymbol(self):
        if self.header == self.end_right:
            return self.empty_sym
        else:
            return self.tape[self.header]
