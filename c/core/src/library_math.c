#include <stdlib.h>
#include <math.h>

#include "library_math.h"


// Function that return random double in [from; to]
double random(double from, double to) {
	return from + (double)rand() / (double)RAND_MAX * (to - from);
}

// Function that return random int in [from; to]
double random_int(int from, int to) {
	return from + rand() * (to - from) / RAND_MAX;
}


// Activation functions
double Sigmoid_f(double x) {
	return 1 / (1 + pow(e, -x));
}

double Sigmoid_df(double x) {
	return x * (1 - x);
}
ActivationFunction Sigmoid;
// Sigmoid.f = Sigmoid_f;
// Sigmoid.df = Sigmoid_df;

double ReLU_f(double x) {
	if (x > 0) {
		return x;
	}
	return 0;
}

double ReLU_df(double x) {
	if (x > 0) {
		return 1;
	}
	return 0;
}

void SoftMax_f(int length, double* x, double* y) {
	double summ = 0;
	for (int i = 0; i < length; ++i) {
		summ += pow(e, x[i]);
	}
	for (int i = 0; i < length; ++i) {
		y[i] = pow(e, x[i]) / summ;
	}
}

double SoftMax_df(double x) {
	return x * (1 - x);
}


// Loss functions
double MSE_f(double ideal, double output) {
    return (output - ideal) * (output - ideal);
}

double MSE_df(double ideal, double output) {
	return 2 * (output - ideal);
}