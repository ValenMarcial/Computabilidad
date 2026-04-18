class TapeDoubleInf:
    def __init__(self, word, states):
        self.header_left = -1
        self.header_right = 0
        self.tape_left = []
        self.tape_right = []
        for i in range(len(word)):
            self.tape_right.append(word[i])
        self.end_right = len(word)
        self.end_left = 0
        self.empty_sym = "-"
        self.states = states
        self.actual_state = states[0]

    def moveReplace(self, sym, dir, state):
        """
        This method replace symbol to actually header and change configuration
            Args:
                sym: Symbol to replace
                dir: Direction to move
                state: State to change
        """
        if dir == "R":
            if self.header_right >= 0 and self.header_left == -1:
                if self.header_right == self.end_right:
                    self.tape_right.append(sym)
                    self.end_right += 1
                else:
                    self.tape_right[self.header_right] = sym
                self.header_right += 1
            elif self.header_right == -1 and self.header_left == 0:
                self.tape_left[0] = sym
                self.header_left = -1
                self.header_right = 0
            elif self.header_right == -1 and self.header_left >= 1:
                self.tape_left[self.header_left] = sym
                self.header_left -= 1
        else:
            # Move to Left
            if self.header_right >= 1 and self.header_left == -1:
                self.tape_right[self.header_right] = sym
                self.header_right -= 1
            elif self.header_right == 0 and self.header_left == -1:
                self.tape_right[0] = sym
                self.header_right = -1
                self.header_left = 0
                if self.header_left == self.end_left:
                    self.tape_left.append(self.empty_sym)
                    self.end_left += 1
            elif self.header_right == -1 and self.header_left >= 0:
                if self.header_left == self.end_left:
                    self.tape_left.append(self.empty_sym)
                    self.end_left += 1
                self.tape_left[self.header_left] = sym
                self.header_left += 1
        self.actual_state = state

    def move(self, dir, state):
        """
        This method move the header and change configuration
            Args:
                dir: Direction to move
                state: State to change
        """
        if dir == "R":
            if self.header_right >= 0 and self.header_left == -1:
                if self.header_right == self.end_right:
                    self.end_right += 1
                self.header_right += 1
            elif self.header_right == -1 and self.header_left == 0:
                self.header_left = -1
                self.header_right = 0
            elif self.header_right == -1 and self.header_left >= 1:
                self.header_left -= 1
        else:
            # Move to Left
            if self.header_right >= 1 and self.header_left == -1:
                self.header_right -= 1
            elif self.header_right == 0 and self.header_left == -1:
                self.header_right = -1
                self.header_left = 0
                if self.header_left == self.end_left:
                    self.tape_left.append(self.empty_sym)
                    self.end_left += 1
            elif self.header_right == -1 and self.header_left >= 0:
                if self.header_left == self.end_left:
                    self.tape_left.append(self.empty_sym)
                    self.end_left += 1
                self.header_left += 1
        self.actual_state = state

    def getSymbol(self):
        """
        This method obtain symbol to actually header
        """
        if self.header_right == -1:
            if self.header_left == self.end_left:
                return self.empty_sym
            else:
                return self.tape_left[self.header_left]
        else:
            if self.header_right == self.end_right:
                return self.empty_sym
            else:
                return self.tape_right[self.header_right]
