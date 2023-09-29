#include <stdio.h>

#include "library.h"
#include "full_connected.h"
#include "print.h"


void DataSet_print(DataSet *data_set) {
	printf("DataSet {\n");
	for (int i = 0; i < data_set->length; ++i) {
		printf("    {");

		printf(" {");
		for (int j = 0; j < data_set->input_length; ++j) {
			if (j < data_set->input_length - 1) {
				printf("%lf, ", data_set->pairs[i]->input[j]);
			} else {
				printf("%lf", data_set->pairs[i]->input[j]);
			}
		}
		printf("}, ");

		printf("{");
		for (int j = 0; j < data_set->output_length; ++j) {
			if (j < data_set->output_length - 1) {
				printf("%lf, ", data_set->pairs[i]->output[j]);
			} else {
				printf("%lf", data_set->pairs[i]->output[j]);
			}
		}

		printf("} ");
		
		if (i < data_set->length - 1) {
			printf("},\n");
		} else {
			printf("}\n");
		}
	}
	printf("}\n");
}


void FullConnected_print_weights(FullConnected *layer) {
	printf("weights {\n");
	for (int i = 0; i < layer->layers_length - 1; ++i) {
		printf("    {\n");
		for (int j = 0; j < layer->layers[i]; ++j) {
			printf("        {");
			for (int l = 0; l < layer->layers[i + 1]; ++l) {
				if (l < layer->layers[i + 1] - 1) {
					printf("%lf, ", layer->weights[i][j][l]);
				} else {
					printf("%lf", layer->weights[i][j][l]);
				}
			}

			if (j < layer->layers[i] - 1) {
				printf("},\n");
			} else {
				printf("}\n");
			}
		}

		if (i < layer->layers_length - 2) {
			printf("    },\n");
		} else {
			printf("    }\n");
		}
	}

	printf("}\n");
}

void FullConnected_print_biases(FullConnected *layer) {
	printf("biases {\n");
	for (int i = 0; i < layer->layers_length - 1; ++i) {
		printf("    {");
		for (int j = 0; j < layer->layers[i + 1]; ++j) {
			if (j < layer->layers[i + 1] - 1) {
				printf("%lf, ", layer->biases[i][j]);
			} else {
				printf("%lf", layer->biases[i][j]);
			}
		}

		if (i < layer->layers_length - 2) {
			printf("},\n");
		} else {
			printf("}\n");
		}
	}

	printf("}\n");
}

void FullConnected_print_x(FullConnected *layer) {
	printf("x {\n");
	for (int i = 0; i < layer->layers_length; ++i) {
		printf("    {");
		for (int j = 0; j < layer->layers[i]; ++j) {
			if (j < layer->layers[i] - 1) {
				printf("%lf, ", layer->x[i][j]);
			} else {
				printf("%lf", layer->x[i][j]);
			}
		}

		if (i < layer->layers_length - 1) {
			printf("},\n");
		} else {
			printf("}\n");
		}
	}
	
	printf("}\n");
}


void FullConnected_print_delta_weights(FullConnected *layer) {
	printf("delta_weights {\n");
	for (int i = 0; i < layer->layers_length - 1; ++i) {
		printf("    {\n");
		for (int j = 0; j < layer->layers[i]; ++j) {
			printf("        {");
			for (int l = 0; l < layer->layers[i + 1]; ++l) {
				if (l < layer->layers[i + 1] - 1) {
					printf("%lf, ", layer->delta_weights[i][j][l]);
				} else {
					printf("%lf", layer->delta_weights[i][j][l]);
				}
			}

			if (j < layer->layers[i] - 1) {
				printf("},\n");
			} else {
				printf("}\n");
			}
		}

		if (i < layer->layers_length - 2) {
			printf("    },\n");
		} else {
			printf("    }\n");
		}
	}

	printf("}\n");
}

void FullConnected_print_delta_biases(FullConnected *layer) {
	printf("delta_biases {\n");
	for (int i = 0; i < layer->layers_length - 1; ++i) {
		printf("    {");
		for (int j = 0; j < layer->layers[i + 1]; ++j) {
			if (j < layer->layers[i + 1] - 1) {
				printf("%lf, ", layer->delta_biases[i][j]);
			} else {
				printf("%lf", layer->delta_biases[i][j]);
			}
		}

		if (i < layer->layers_length - 2) {
			printf("},\n");
		} else {
			printf("}\n");
		}
	}

	printf("}\n");
}

void FullConnected_print_gradient(FullConnected *layer) {
	printf("gradient {\n");
	for (int i = 0; i < layer->layers_length; ++i) {
		printf("    {");
		for (int j = 0; j < layer->layers[i]; ++j) {
			if (j < layer->layers[i] - 1) {
				printf("%lf, ", layer->gradient[i][j]);
			} else {
				printf("%lf", layer->gradient[i][j]);
			}
		}

		if (i < layer->layers_length - 1) {
			printf("},\n");
		} else {
			printf("}\n");
		}
	}
	
	printf("}\n");
}