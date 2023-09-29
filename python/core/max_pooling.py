class MaxPooling:
    def __init__(self, channels, height, width,
                 matrix_h=2,
                 matrix_w=2
                 ):

        self.height = height
        self.width = width
        self.channels = channels

        self.matrix_h = matrix_h
        self.matrix_w = matrix_w

        self.data_input = []
        for c in range(self.channels):
            self.data_input.append([])
            for h in range(self.height):
                self.data_input[c].append([])
                for w in range(self.width):
                    self.data_input[c][h].append(0)

        self.x = []
        for c in range(self.channels):
            self.x.append([])
            for hh in range(self.height // self.matrix_h):
                self.x[c].append([])
                for ww in range(self.width // self.matrix_w):
                    self.x[c][hh].append(0)

    def define_err(self):
        self.err = []
        for c in range(self.channels):
            self.err.append([])
            for h in range(self.height):
                self.err[c].append([])
                for w in range(self.width):
                    self.err[c][h].append(0)

    def forward(self, data_input):
        for c in range(self.channels):
            for hh in range(self.height // self.matrix_h):
                for ww in range(self.width // self.matrix_w):
                    self.x[c][hh][ww] = data_input[c][hh * self.matrix_h][ww * self.matrix_w]
                    for mh in range(self.matrix_h):
                        for mw in range(self.matrix_w):
                            self.data_input[c][hh * self.matrix_h + mh][ww * self.matrix_w + mw] = data_input[c][hh * self.matrix_h + mh][ww * self.matrix_w + mw]
                            self.x[c][hh][ww] = max(self.x[c][hh][ww], self.data_input[c][hh * self.matrix_h + mh][ww * self.matrix_w + mw])

    def backward(self, err):
        for c in range(self.channels):
            for hh in range(self.height // self.matrix_h):
                for ww in range(self.width // self.matrix_w):
                    for mh in range(self.matrix_h):
                        for mw in range(self.matrix_w):
                            self.err[c][hh * self.matrix_h + mh][ww * self.matrix_w + mw] = 0
                            if self.x[c][hh][ww] == self.data_input[c][hh * self.matrix_h + mh][ww * self.matrix_w + mw]:
                                self.err[c][hh * self.matrix_h + mh][ww * self.matrix_w + mw] = err[c][hh][ww]
