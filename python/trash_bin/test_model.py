from temp.model import * # эта версия устарела
from colorama import Fore, init

init(autoreset=True)

x = [
	[[1, 1, 1], [1, 0]],
	[[1, 1, 0], [1, 0]],
	[[1, 0, 0], [0, 1]],
	[[0, 0, 0], [0, 1]],
	[[0, 0, 1], [0, 1]],
	[[0, 1, 1], [0, 1]],
	[[1, 0, 1], [0, 1]],
	[[0, 1, 0], [0, 1]]
]

y = [
	[[1, 1, 1], [1]],
	[[1, 1, 0], [1]],
	[[1, 0, 0], [0]],
	[[0, 0, 0], [0]],
	[[0, 0, 1], [0]],
	[[0, 1, 1], [0]],
	[[1, 0, 1], [0]],
	[[0, 1, 0], [0]]
]


for tests in (x, y):
	for activation in (ReLU, Sigmoid):
		for loss in (MSE, CrossEntropy):
			for last_layer_activation in (Sigmoid, SoftMax):

				if tests == y and last_layer_activation == SoftMax:
					continue

				layers = [['full_connected', 3, 2, len(tests[0][1])]]
				a = NN(layers=layers, activation=activation, loss=loss, last_layer_activation=last_layer_activation)

				a.train_fc(tests)

				k = True

				for test in tests:
					a.forward_fc(test[0])
					for i in range(len(a.x[-1])):
						if round(a.x[-1][i]) != test[1][i]:
							print(
								Fore.RED + f'Activation {activation.__name__}, loss {loss.__name__}, last_layer_activation {last_layer_activation.__name__}, tests {"x" * (x == tests) + "y" * (y == tests)}')
							print(Fore.YELLOW + f'Input {test[0]}, output {a.x[-1]}, ideal {test[1]}')
							k = False

				if k:
					print(Fore.GREEN	 + f'Activation {activation.__name__}, loss {loss.__name__}, last_layer_activation {last_layer_activation.__name__}, tests {"x" * (x == tests) + "y" * (y == tests)}')