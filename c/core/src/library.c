#include <stdlib.h>

#include "library.h"


DataSet *DataSet_construct(int pairs_count, int input_length, int output_length, double data[]) {
	DataSet *data_set = malloc(sizeof(DataSet));
	data_set->length = pairs_count;
	data_set->input_length = input_length;
	data_set->output_length = output_length;
	data_set->pairs = (Pair **)malloc(sizeof(Pair *) * pairs_count);

	for (int i = 0; i < pairs_count; ++i) {
		data_set->pairs[i] = (Pair *)malloc(sizeof(Pair));

		data_set->pairs[i]->input = (double *)malloc(sizeof(double) * input_length);
		for (int j = 0; j < input_length; ++j) {
			data_set->pairs[i]->input[j] = data[i * (input_length + output_length) + j];
		}

		data_set->pairs[i]->output = (double *)malloc(sizeof(double) * output_length);
		for (int j = 0; j < output_length; ++j) {
			data_set->pairs[i]->output[j] = data[i * (input_length + output_length) + input_length + j];
		}
	}

	return data_set;
}

void DataSet_deconstruct(DataSet *data_set) {
	for (int i = 0; i < data_set->length; ++i) {
		free(data_set->pairs[i]->input);
		free(data_set->pairs[i]->output);
		free(data_set->pairs[i]);
	}
	free(data_set->pairs);
	free(data_set);
}

void DataSet_add(DataSet *data_set, double data[]) {
	data_set->length += 1;
	data_set->pairs = (Pair **)realloc(data_set->pairs, data_set->length * sizeof(Pair *));
	data_set->pairs[data_set->length - 1] = (Pair *)malloc(sizeof(Pair));
	data_set->pairs[data_set->length - 1]->input = (double *)malloc(sizeof(double) * input_length);
	for (int j = 0; j < input_length; ++j) {
		data_set->pairs[data_set->length - 1]->input[j] = data[data_set->length - 1 * (input_length + output_length) + j];
	}

	data_set->pairs[data_set->length - 1]->output = (double *)malloc(sizeof(double) * output_length);
	for (int j = 0; j < output_length; ++j) {
		data_set->pairs[data_set->length - 1]->output[j] = data[data_set->length - 1 * (input_length + output_length) + input_length + j];
	}
}