#include <stlib.h>

#include "library.h"
#include "convolution.h"


Convolution* Convolution_construct(int channels, int height, int width, int matrix_c, int matrix_h, int matrix_w, int padding, int stride_h, int stride_w) {
	Convolution* layer = (Convolution*)malloc(Convolution);

	layer->channels = channels;
	layer->height = height;
	layer->width = width;

	layer->matrix_c = matrix_c;
	layer->matrix_h = matrix_h;
	layer->matrix_w = matrix_w;
	
	layer->padding = padding;
	
	layer->stride_h = stride_h;
	layer->stride_w = stride_w;

	layer->input = (double***)malloc(sizeof(double**) * layer->channels);
    for (int c = 0; c < layer->channels; ++c) {
        layer->input[c] = (double**)malloc(sizeof(double*) * (layer->height + 2 * layer->padding));
        for (int hp = 0; hp < layer->height + 2 * layer->padding; ++hp) {
            layer->input[c][hp] = (double*)malloc(sizeof(double) * (layer->width + 2 * layer->padding));
        }
    }

    layer->output = (double***)malloc(sizeof(double**) * layer->channels);
    for (int c = 0; c < layer->channels; ++c) {
        layer->output[c] = (double**)malloc(sizeof(double*) * (layer->height / layer->matrix_h));
        for (int h = 0; h < layer->height / layer->matrix_h; ++h) {
            layer->output[c][h] = (double*)malloc(sizeof(double) * (layer->width / layer->matrix_w));
        }
    }

    layer->matrix = (double***)malloc(sizeof(double**) * layer->matrix_c);
    for (int mc = 0; mc < layer->matrix_c; ++mc) {
	    layer->matrix[mc] = (double**)malloc(sizeof(double*) * layer->matrix_h);
	    for (int mh = 0; mh < layer->matrix_h; ++mh) {
		    layer->matrix[mc][mh] = (double*)malloc(sizeof(double) * layer->matrix_w);
		    for (int mw = 0; mw < layer->matrix_w; ++mw) {
		    	layer->matrix[mc][mh][mw] = random(0, 1);
		    }
	    }
	}

	return layer;
}

void Convolution_destruct(Convolution* layer) {
    for (int c = 0; c < layer->channels; ++c) {
        for (int hp = 0; hp < layer->height + 2 * layer->padding; ++hp) {
            free(layer->input[c][hp]);
        }
        free(layer->input[c]);
    }
    free(layer->input);

    for (int c = 0; c < layer->channels; ++c) {
        for (int hp = 0; hp < layer->height + 2 * layer->padding; ++hp) {
            free(layer->input[c][hp]);
        }
        free(layer->input[c]);
    }
    free(layer->input);
    
    for (int mc = 0; mc < layer->matrix_c; ++mc) {
	    for (int mh = 0; mh < layer->matrix_h; ++mh) {
			free(layer->matrix[mc][mh]);
	    }
		free(layer->matrix[mc]);
	}
	free(layer->matrix);

    free(layer);
}

void Convolution_train_construct(Convolution* layer, double learning_rate, double momentum);
void Convolution_train_destruct(Convolution* layer);

void Convolution_forward(Convolution* layer, double*** input) {
	// copying input to the layer->input IT IS NOT EFFICIENT,
	// you can just change pointer layer->input to the input,
	// if you will not change layer->input data and you will not change data in input (ImageSet)
	for (int c = 0; c < layer->channels; ++c) {
		for (int h = 0; h < layer->height; ++h) {
			for (int w = 0; w < layer->width; ++w) {
				layer->input[c][layer->padding + h][layer->padding + w] = input[c][h][w];
			}
		}
	}

    for mc in range(self.matrix_c):
        for hh in range(1 + (self.height - self.matrix_h) / self.stride_h):
            for ww in range(1 + (self.width - self.matrix_w) / self.stride_w):
                self.x[mc][hh][ww] = self.bias[mc][hh][ww]
                for c in range(self.channels):
                    for mh in range(self.matrix_h):
                        for mw in range(self.matrix_w):
                            self.x[mc][hh][ww] += self.data_input[c][hh * self.stride_h + mh][ww * self.stride_w + mw] * self.w[mc][c][mh][mw]
                self.x[mc][hh][ww] = self.activation.f(self.x[mc][hh][ww])
}

void Convolution_backward(Convolution* layer, double*** output);