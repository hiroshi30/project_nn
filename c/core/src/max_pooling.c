#include <stdlib.h>
#include <math.h>

#include "max_pooling.h"


MaxPooling* MaxPooling_construct(int channels, int height, int width, int matrix_h, int matrix_w) {
	MaxPooling* layer = (MaxPooling*)malloc(sizeof(MaxPooling));
	layer->channels = channels;
	layer->height = height;
	layer->width = width;
	layer->matrix_h = matrix_h;
	layer->matrix_w = matrix_w;

	layer->input = (double***)malloc(sizeof(double**) * layer->channels);
	for (int c = 0; c < layer->channels; ++c) {
		layer->input[c] = (double**)malloc(sizeof(double*) * layer->height);
		for (int h = 0; h < layer->height; ++h) {
			layer->input[c][h] = (double*)malloc(sizeof(double) * layer->width);
		}
	}

	layer->x = (double***)malloc(sizeof(double**) * layer->channels);
	for (int c = 0; c < layer->channels; ++c) {
		layer->x[c] = (double**)malloc(sizeof(double*) * (layer->height / layer->matrix_h));
		for (int h = 0; h < layer->height / layer->matrix_h; ++h) {
			layer->x[c][h] = (double*)malloc(sizeof(double) * (layer->width / layer->matrix_w));
		}
	}

	return layer;
}

void MaxPooling_destruct(MaxPooling* layer) {
	for (int c = 0; c < layer->channels; ++c) {
		for (int h = 0; h < layer->height; ++h) {
			free(layer->input[c][h]);
		}
		free(layer->input[c]);
	}
	free(layer->input);

	for (int c = 0; c < layer->channels; ++c) {
		for (int h = 0; h < layer->height / layer->matrix_h; ++h) {
			free(layer->x[c][h]);
		}
		free(layer->x[c]);
	}
	free(layer->x);

	free(layer);
}

void MaxPooling_train_construct(MaxPooling* layer) {
	layer->err = (double***)malloc(sizeof(double**) * layer->channels);
	for (int c = 0; c < layer->channels; ++c) {
		layer->err[c] = (double**)malloc(sizeof(double*) * layer->height);
		for (int h = 0; h < layer->height; ++h) {
			layer->err[c][h] = (double*)malloc(sizeof(double) * layer->width);
		}
	}
}

void MaxPooling_train_deconstruct(MaxPooling* layer) {
	for (int c = 0; c < layer->channels; ++c) {
		for (int h = 0; h < layer->height; ++h) {
			free(layer->err[c][h]);
		}
		free(layer->err[c]);
	}
	free(layer->err);
}

void MaxPooling_forward(MaxPooling* layer, double*** input) {
	for (int c = 0; c < layer->channels; ++c) {
		for (int hh = 0; hh < layer->height / layer->matrix_h; ++hh) {
			for (int ww = 0; ww < layer->width / layer->matrix_w; ++ww) {
				layer->x[c][hh][ww] = input[c][hh * layer->matrix_h][ww * layer->matrix_w];
                for (int mh = 0; mh < layer->matrix_h; ++mh) {
                	for (int mw = 0; mw < layer->matrix_w; ++mw) {
                        layer->input[c][hh * layer->matrix_h + mh][ww * layer->matrix_w + mw] = input[c][hh * layer->matrix_h + mh][ww * layer->matrix_w + mw];
                        layer->x[c][hh][ww] = fmax(layer->x[c][hh][ww], layer->input[c][hh * layer->matrix_h + mh][ww * layer->matrix_w + mw]);
                	}
                }
			}
		}
	}
}

void MaxPooling_backward(MaxPooling* layer, double*** output);
