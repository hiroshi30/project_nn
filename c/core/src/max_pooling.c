#include <stdlib.h>

#include "max_pooling.h"


MaxPooling* MaxPooling_construct(int channels, int height, int width, int matrix_h, int matrix_w) {
	MaxPooling* layer = (MaxPooling*)malloc(sizeof(MaxPooling));
	layer->channels = channels;
	layer->height = height;
	layer->width = width;
	layer->matrix_h = matrix_h;
	layer->matrix_w = matrix_w;
	layer->input = (double***)malloc(sizeof(double**) * channels);
	for (int i = 0; i < channels; ++i) {
		layer->input[i] = (double**)malloc(sizeof(double*) * height);
		for (int j = 0; j < height; ++j) {
			layer->input[i][j] = (double*)malloc(sizeof(double) * width);
		}
	}
}

void MaxPooling_deconstruct(MaxPooling* layer) {
	for (int i = 0; i < channels; ++i) {
		for (int j = 0; j < height; ++j) {
			free(layer->input[i][j]);
		}
		free(layer->input[i]);
	}
	free(layer->input);
	free(layer);
}

void MaxPooling_train_construct(MaxPooling* layer);
void MaxPooling_train_deconstruct(MaxPooling* layer);

void MaxPooling_forward(MaxPooling* layer, double* input);
void MaxPooling_backward(MaxPooling* layer, double* output);
