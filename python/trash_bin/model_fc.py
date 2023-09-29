from core.library import *

class NN:
	def __init__(self, layers, activation=Sigmoid, loss=MSE, n=0.7, m=0.5):
		self.epochs = None
		self.error = None
		self.x = None
		self.err = None

		self.layers = layers

		self.activation = activation
		self.loss = loss

		self.matrices = []
		for layer in layers:
			if layer[0] == 'convolution':
				self.matrices.append([])
				for i in range(layer[1]):
					self.matrices[-1].append([[uniform(1, 5) for j in range(layer[2])] for i in range(layer[3])])
			elif layer[0] == 'full_connected':
				self.k = layer[1:]

		self.n = n
		self.m = m

		self.w = [[[uniform(-1, 1) for l in range(self.k[i + 1])] for j in range(self.k[i] + 1)] for i in range(len(self.k) - 1)]
		self.delta_w = [[[0 for l in range(self.k[i + 1])] for j in range(self.k[i] + 1)] for i in range(len(self.k) - 1)]

	def forward_fc(self, data_input):
		self.x = [[0 for j in range(self.k[i])] for i in range(len(self.k))]
		self.x[0] = [*data_input]
		for i in range(len(self.x) - 1):
			self.x[i].append(1)

		for i in range(len(self.k) - 1):
			for j in range(self.k[i + 1]):
				for l in range(self.k[i] + 1):
					self.x[i + 1][j] += self.x[i][l] * self.w[i][l][j]
				if i != len(self.k) - 2:
					self.x[i + 1][j] = self.activation().f(self.x[i + 1][j])
		self.x[-1] = SoftMax().f(self.x[-1])

	def backpropagation_fc(self, data_output):
		self.err = [[0 for _1 in range(self.k[i])] for i in range(len(self.k))]

		for i in range(len(data_output)):
			self.err[-1][i] = self.loss().df(data_output[i], self.x[-1][i]) * SoftMax().df(self.x[-1][i])

		for i in range(len(self.k) - 2, 0, -1):
			for j in range(self.k[i]):
				for l in range(self.k[i + 1]):
					self.err[i][j] += self.err[i + 1][l] * self.w[i][j][l] * self.activation().df(self.x[i][j])

		for i in range(len(self.k) - 1):
			for j in range(self.k[i + 1]):
				for l in range(self.k[i] + 1):
					self.delta_w[i][l][j] = -self.n * self.x[i][l] * self.err[i + 1][j] + self.m * self.delta_w[i][l][j]
					self.w[i][l][j] += self.delta_w[i][l][j]

	def calculate_error(self, data):
		self.error = 0
		for data_input, data_output in data:
			self.forward_fc(data_input)
			for ideal, output in zip(data_output, self.x[-1]):
				self.error += self.loss().f(ideal, output)
			self.error /= len(data_output)
		self.error /= len(data)

	def train(self, data, a=10000):
		self.epochs = 0
		while self.epochs < a:
			index = randint(0, len(data) - 1)
			self.forward_fc(data[index][0])
			self.backpropagation_fc(data[index][1])

			self.epochs += 1

		self.calculate_error(data)