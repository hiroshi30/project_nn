#include <stdio.h>

#include "library_math.h"
#include "library.h"
#include "full_connected.h"
#include "print.h"


int main(void) {


	// check random() function
	const int random_count = 10;
	double random_arr[random_count];
	for (int i = 0; i < random_count; ++i) {
		random_arr[i] = random(-100, 100);
	}

	int random_same_count = 0;
	for (int i = 0; i < random_count; ++i) {
		for (int j = 0; j < random_count; ++j) {
			if (i != j && random_arr[i] == random_arr[j]) {
				++random_same_count;
			}
		}
	}

	if (random_same_count == random_count) {
		printf("ERROR IN random() FUNCTION, ALL OUTPUTS ARE THE SAME\n");
		printf("{");
		for (int i = 0; i < random_count; ++i) {
			if (i < random_count - 1) {
				printf("%lf, ", random_arr[i]);
			} else {
				printf("%lf", random_arr[i]);
			} 
		}
		printf("}\n");
	}
	if (random_same_count >= 0.8 * (double)random_count) {
		printf("TOO MANY SAME RESULTS FROM random() FUNCTION\n");
		printf("{");
		for (int i = 0; i < random_count; ++i) {
			if (i < random_count - 1) {
				printf("%lf, ", random_arr[i]);
			} else {
				printf("%lf", random_arr[i]);
			} 
		}
		printf("}\n");
	} else {
		printf("random() function correct\n");
	}


	// check random_int() function
	const int random_int_count = 10;
	int random_int_arr[random_int_count];
	for (int i = 0; i < random_int_count; ++i) {
		random_int_arr[i] = random_int(-100, 100);
	}

	int random_int_same_count = 0;
	for (int i = 0; i < random_int_count; ++i) {
		for (int j = 0; j < random_int_count; ++j) {
			if (i != j && random_int_arr[i] == random_int_arr[j]) {
				++random_int_same_count;
			}
		}
	}

	if (random_int_same_count == random_int_count) {
		printf("ERROR IN random_int() FUNCTION, ALL OUTPUTS ARE THE SAME\n");
		printf("{");
		for (int i = 0; i < random_int_count; ++i) {
			if (i < random_int_count - 1) {
				printf("%d, ", random_int_arr[i]);
			} else {
				printf("%d", random_int_arr[i]);
			} 
		}
		printf("}\n");
	}
	if (random_int_same_count >= 0.8 * (double)random_int_count) {
		printf("TOO MANY SAME RESULTS FROM random_int() FUNCTION\n");
		printf("{");
		for (int i = 0; i < random_int_count; ++i) {
			if (i < random_int_count - 1) {
				printf("%d, ", random_int_arr[i]);
			} else {
				printf("%d", random_int_arr[i]);
			} 
		}
		printf("}\n");
	} else {
		printf("random_int() function correct\n");
	}


	// // check DataSet
	// DataSet *train_set = DataSet_construct(5, 3, 2, (double []){
	// 	1, 0, 1,    1, 0,
	// 	1, 0, 0,    1, 0,
	// 	0, 1, 1,    0, 1,
	// 	1, 1, 1,    1, 0,
	// 	0, 0, 0,    0, 1
	// });

	// DataSet *check_set = DataSet_construct(3, 3, 2, (double []){
	// 	0, 1, 0,    0, 1,
	// 	0, 0, 1,    0, 1,
	// 	1, 1, 0,    1, 0
	// });

	// double layers[] = {3, 4, 2};
	// double *ptr_layers = layers;

	// FullConnected *layer = FullConnected_construct(3, ptr_layers, 0.7, 0.5);
	// FullConnected_train_construct(layer);


	// DataSet_deconstruct(train_set);

	// FullConnected_train_deconstruct(layer);
	// FullConnected_deconstruct(layer);

	return 0;
}