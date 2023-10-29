#include <stdio.h>
#include <stdlib.h>

#include <kazamori.h>
#include <print.h>


int main(int argc, char* argv[]) {
	MaxPooling* layer = MaxPooling_construct(3, 4, 6, 2, 3);

	double*** input = (double***)malloc(sizeof(double**) * layer->channels);
	for (int c = 0; c < layer->channels; ++c) {
		input[c] = (double**)malloc(sizeof(double*) * layer->height);
		for (int h = 0; h < layer->height; ++h) {
			input[c][h] = (double*)malloc(sizeof(double) * layer->width);
			for (int w = 0; w < layer->width; ++w) {
				input[c][h][w] = c * layer->height * layer->width + h * layer->width + w;
			}
		}
	}

	for (int c = 0; c < layer->channels; ++c) {
		printf("{\n");
		for (int h = 0; h < layer->height; ++h) {
			printf("   {");
			for (int w = 0; w < layer->width; ++w) {
				printf("%lf, ", input[c][h][w]);
			}
			printf("},\n");
		}
		printf("},\n");
	}

	MaxPooling_print_input(layer);

	for (int c = 0; c < layer->channels; ++c) {
		for (int h = 0; h < layer->height; ++h) {
			free(input[c][h]);
		}
		free(input[c]);
	}
	free(input);

	MaxPooling_destruct(layer);
	
	return 0;
}