#include <stdio.h>

#include "max_pooling.h"

#define TAB "   "


void MaxPooling_print_input(MaxPooling* layer) {
	printf("MaxPooling input {\n");
	for (int c = 0; c < layer->channels; ++c) {
		printf(TAB);
		printf("{\n");

		for (int h = 0; h < layer->height; ++h) {
			printf(TAB);
			printf(TAB);
			printf("{")

			for (int w = 0; w < layer->width; ++w) {
				if (w < layer->width - 1) {
					printf("%lf, ", layer->input[c][h][w]);
				} else {
					printf("%lf", layer->input[c][h][w]);
				}
			}

			if (h < layer->height - 1) {
				printf("}\n");
			} else {
				printf("},\n");
			}
		}

		if (c < layer->channels - 1) {
			printf("}\n");
		} else {
			printf("},\n");
		}
	}
}

void MaxPooling_print_x(MaxPooling* layer);
void MaxPooling_print_err(MaxPooling* layer);
