from core.library import *


class NN:
	def __init__(self, layers):
		self.x = None
		self.err = None

		self.layers = layers

		self.activation = ReLU()
		self.loss = MSE()

		self.matrices = []
		for layer in layers:
			if layer[0] == 'convolution':
				for i in range(layer[1]):
					self.matrices.append([[uniform(1, 5) for j in range(layer[2])] for i in range(layer[3])])
			elif layer[0] == 'full_connected':
				self.k = layer[1:]

		self.n = 0.7
		self.m = 0.5

		self.w = [[[uniform(-1, 1) for l in range(self.k[i + 1])] for j in range(self.k[i] + 1)] for i in range(len(self.k) - 1)]
		self.delta_w = [[[0 for l in range(self.k[i + 1])] for j in range(self.k[i] + 1)] for i in range(len(self.k) - 1)]


	def calculate_error(self, data):
		error = 0

		for data_input, data_output in data:
			self.full_connected(data_input)
			for ideal, output in zip(data_output, self.x[-1]):
				error += self.loss.f(ideal, output)
			error /= len(data_output)
		error /= len(data)

		return error

	def train(self, data, a=10000):
		for epochs in range(a):
			index = randint(0, len(data) - 1)
			self.full_connected(data[index][0])
			self.backpropagation(data[index][1])

		print('error', self.calculate_error(data))

	def full_connected(self, data_input):
		self.x = [[0 for j in range(self.k[i])] for i in range(len(self.k))]
		self.x[0] = [*data_input]
		for i in range(len(self.x) - 1):
			self.x[i].append(1)

		for i in range(len(self.k) - 1):
			for j in range(self.k[i + 1]):
				for l in range(self.k[i] + 1):
					self.x[i + 1][j] += self.x[i][l] * self.w[i][l][j]
				if i != len(self.k) - 2:
					self.x[i + 1][j] = self.activation.f(self.x[i + 1][j])
		self.x[-1] = SoftMax().f(self.x[-1])

	def backpropagation(self, data_output):
		self.err = [[0 for _1 in range(self.k[i])] for i in range(len(self.k))]

		for i in range(len(data_output)):
			self.err[-1][i] = self.loss.df(data_output[i], self.x[-1][i]) * SoftMax().df(self.x[-1][i])

		for i in range(len(self.k) - 2, 0, -1):
			for j in range(self.k[i]):
				for l in range(self.k[i + 1]):
					self.err[i][j] += self.err[i + 1][l] * self.w[i][j][l] * self.activation.df(self.x[i][j])

		for i in range(len(self.k) - 1):
			for j in range(self.k[i + 1]):
				for l in range(self.k[i] + 1):
					self.delta_w[i][l][j] = -self.n * self.x[i][l] * self.err[i + 1][j] + self.m * self.delta_w[i][l][j]
					self.w[i][l][j] += self.delta_w[i][l][j]


	def convolution(self, image, matrix, stride_h=None, stride_w=None):
		new_image = []

		image = [[0 for i in range(len(image[0]))]] + image + [[0 for i in range(len(image[0]))]]
		for i in range(len(image)):
			image[i] = [0] + image[i] + [0]

		image_h = len(image)
		image_w = len(image[0])
		matrix_h = len(matrix)
		matrix_w = len(matrix[0])
		if stride_h == None:
			stride_h = matrix_h
		if stride_w == None:
			stride_w = matrix_w

		for y in range(0, image_h - matrix_h + 1, stride_h):
			new_image.append([])
			for x in range(0, image_w - matrix_w + 1, stride_w):
				s = 0
				for i in range(matrix_h):
					for j in range(matrix_w):
						s += image[y + i][x + j] * matrix[i][j]
				s = self.activation.f(s)
				new_image[y // stride_h].append(s)

		return new_image


	def max_pooling(self, image, stride_h=2, stride_w=2):
		new_image = []
		
		image_h = len(image)
		image_w = len(image[0])
		
		print(stride_h,stride_w)

		for y in range(0, image_h, stride_h):
			new_image.append([])
			for x in range(0, image_w, stride_w):
				s = image[y][x]
				for i in range(stride_h):
					for j in range(stride_w):
						s = max(s, image[y + i][x + j])
				new_image[y // stride_h].append(s)

		return new_image
