#include <stdio.h>
#include <stdlib.h>

#include "data_set.h"


DataSet *DataSet_construct(int length, int input_length, int output_length, double data[]) {
	DataSet *data_set = malloc(sizeof(DataSet));
	data_set->length = length;
	data_set->input_length = input_length;
	data_set->output_length = output_length;
	data_set->input = (double**)malloc(sizeof(double*) * length);
	data_set->output = (double**)malloc(sizeof(double*) * length);

	for (int i = 0; i < length; ++i) {
		data_set->input[i] = (double*)malloc(sizeof(double) * input_length);
		for (int j = 0; j < input_length; ++j) {
			data_set->input[i][j] = data[i * (input_length + output_length) + j];
		}

		data_set->output[i] = (double*)malloc(sizeof(double) * output_length);
		for (int j = 0; j < output_length; ++j) {
			data_set->output[i][j] = data[i * (input_length + output_length) + input_length + j];
		}
	}

	return data_set;
}

void DataSet_deconstruct(DataSet *data_set) {
	for (int i = 0; i < data_set->length; ++i) {
		free(data_set->input[i]);
		free(data_set->output[i]);
	}
	free(data_set->input);
	free(data_set->output);
	free(data_set);
}

void DataSet_add(DataSet *data_set, double data[]) {
	data_set->length += 1;
	data_set->input = (double**)realloc(data_set->input, data_set->length * sizeof(double*));
	data_set->output = (double**)realloc(data_set->output, data_set->length * sizeof(double*));

	data_set->input[data_set->length - 1] = (double*)malloc(sizeof(double) * data_set->input_length);
	for (int j = 0; j < data_set->input_length; ++j) {
		data_set->input[data_set->length - 1][j] = data[j];
	}

	data_set->output[data_set->length - 1] = (double*)malloc(sizeof(double) * data_set->output_length);
	for (int j = 0; j < data_set->output_length; ++j) {
		data_set->output[data_set->length - 1][j] = data[data_set->input_length + j];
	}
}
