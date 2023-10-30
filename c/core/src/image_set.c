#include <stdlib.h>

#include "image_set.h"


ImageSet* ImageSet_construct(int length, int channels, int height, int width, int output_length) {
	ImageSet* image_set = (ImageSet*)malloc(sizeof(ImageSet));

	image_set->length = length;
	image_set->channels = channels;
	image_set->height = height;
	image_set->width = width;
	image_set->input = (double****)malloc(sizeof(double***) * layer->length);
	for (int i = 0; i < layer->length; ++i) {
		image_set->input[i] = (double***)malloc(sizeof(double**) * layer->channels);
		for (int c = 0; c < layer->channels; ++c) {
			image_set->input[i][c] = (double**)malloc(sizeof(double*) * layer->height);
			for (int h = 0; h < layer->height; ++h) {
				image_set->input[i][c][h] = (double*)malloc(sizeof(double) * layer->width);
			}
		}
	}

	image_set->output_length = output_length;
	return image_set;
}

void ImageSet_destruct(ImageSet* image_set) {
	for (int i = 0; i < layer->length; ++i) {
		for (int c = 0; c < layer->channels; ++c) {
			for (int h = 0; h < layer->height; ++h) {
				free(image_set->input[i][c][h]);
			}
			free(image_set->input[i][c]);
		}
		free(image_set->input[i]);
	}
	free(image_set->input);


	
	free(image_set);
}
