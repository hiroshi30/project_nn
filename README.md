# Project NN

## Installing
```shell
pip install -r requirements.txt
```

## Versions
Множество информации о версиях и источниках я не нашёл или не вспомнил, поэтому это краткие экскурс в историю создания этой нейронки.

Версии:\
1.0 Создал простой перцептрон на JavaScript\
1.1 Переделал нейросеть с использованием ООП\
1.2 Добавил момент в алгоритм обратного распространения ошибки

2.0 Переделал нейросеть на Python\
2.1 Удалил функцию инииализации весов и встроил её в `__init__`\
2.2 Создал отдельную библиотеку (`library.py`), в которой подключил библиотеки\
2.3 Добавил новые функции активации\
2.4 Изменил способ ввода параметров нейросети\
2.5 Добавил `Softmax`\
2.6 Сделал переключаемый параметр softmax, который отвечает за использование функции активации `Softmax`\
2.7 Добавил новые функции потерь

3.0 Создал свёрточную нейронную сеть, добавил `convolution`, `paddiing` и `max_pooling`\
3.1 Переделал, используя ООП\
3.2 Добавил `Cross_Entorpy` и изменил производную `Soft_Max`\
3.3 Объединил `model1` и `model2` (`Perceptron`, `Convolution_NN`) в один класс `NN`, теперь можно использовать нейросеть и как свёрточную, и как полносвязную\
3.4 Пока что приостановил работу над свёрточной нейронной сетью, переименовал некоторые переменные и функции, отредактировал согласно PEP\
3.5 Ок

!!!Skip connection, dense слои в свёрточных нейронных сетях, Dropout layer Genetic algorithm Ensemble!!!

Источники:\
[Нейронные сети для начинающих. Часть 1](https://habr.com/ru/post/312450/)\
[Нейронные сети для начинающих. Часть 2](https://habr.com/ru/post/313216/)\
[Common Loss functions in machine learning](https://towardsdatascience.com/common-loss-functions-in-machine-learning-46af0ffc4d23)\
[Университете ИТМО Обратное распространение ошибки](https://neerc.ifmo.ru/wiki/index.php?title=Обратное_распространение_ошибки)\
[Understanding RMSprop — faster neural network learning](https://towardsdatascience.com/understanding-rmsprop-faster-neural-network-learning-62e116fcf29a)\
[A Step by Step Backpropagation Example](https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/)\
[English Wikipedia Backpropagation](https://en.wikipedia.org/wiki/Backpropagation#Derivation)\
[What is momentum in neural network?](https://datascience.stackexchange.com/questions/84167/what-is-momentum-in-neural-network)\
[Нейронная сеть с SoftMax слоем на c#](https://habr.com/ru/post/155235/)\
[Алгоритм обратного распространения ошибки с регуляризацией на c#](https://habr.com/ru/articles/154369/)\
[Сверточная сеть на python. Часть 1. Определение основных параметров модели](https://habr.com/ru/company/ods/blog/344008/)\
[Сверточная сеть на python. Часть 2. Вывод формул для обучения модели](https://habr.com/ru/company/ods/blog/344116/)\
[Stochastic Gradient Descent with momentum](https://towardsdatascience.com/stochastic-gradient-descent-with-momentum-a84097641a5d)\
[Генетический алгоритм. Просто о сложном](https://habr.com/ru/post/128704/)\
[Loss Functions in Neural Networks](https://www.theaidream.com/post/loss-functions-in-neural-networks)\
[Cross entropy](https://en.wikipedia.org/wiki/Cross_entropy)\
[Xgboost-How to use "mae" as objective function?](https://stackoverflow.com/questions/45006341/xgboost-how-to-use-mae-as-objective-function)\
[Обзор 7 основных функций потерь в машинном обучении (с кодом Python)](https://russianblogs.com/article/34271570686/)\
[A Gentle Introduction to Dropout for Regularizing Deep Neural Networks](https://machinelearningmastery.com/dropout-for-regularizing-deep-neural-networks/)\
[Convolutions and Backpropagations](https://pavisj.medium.com/convolutions-and-backpropagations-46026a8f5d2c)\
[What Are Channels in Convolutional Networks?](https://www.baeldung.com/cs/cnn-channels)\
[Backpropagation In Convolutional Neural Networks](https://www.jefkine.com/general/2016/09/05/backpropagation-in-convolutional-neural-networks/)\
[The Softmax function and its derivative](https://eli.thegreenplace.net/2016/the-softmax-function-and-its-derivative/)\
[Why do we rotate weights when computing the gradients in a convolution layer of a convolution network?](http://soumith.ch/ex/pages/2014/08/07/why-rotate-weights-convolution-gradient/)\
[Convolutional Neural Networks](https://andrew.gibiansky.com/blog/machine-learning/convolutional-neural-networks/)\
[Convolutional Neural Networks backpropagation: from intuition to derivation](https://grzegorzgwardys.wordpress.com/2016/04/22/8/#unique-identifier2)\
[Свёрточная нейронная сеть](https://ru.wikipedia.org/wiki/Свёрточная_нейронная_сеть#Архитектура_и_принцип_работы)\
[Backpropagation in a convolutional layer](https://towardsdatascience.com/backpropagation-in-a-convolutional-layer-24c8d64d8509)\
[Does bias in the convolutional layer really make a difference to the test accuracy?](https://stackoverflow.com/questions/51959507/does-bias-in-the-convolutional-layer-really-make-a-difference-to-the-test-accura)\
[Adam](https://optimization.cbe.cornell.edu/index.php?title=Adam)\
[Question about bias in Convolutional Networks](https://datascience.stackexchange.com/questions/11853/question-about-bias-in-convolutional-networks/)\
[Стохастический градиентный спуск](https://ru.wikipedia.org/wiki/Стохастический_градиентный_спуск)\