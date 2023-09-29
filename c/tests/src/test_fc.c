#include <stdio.h>

#include "library_math.h"
#include "library.h"
#include "full_connected.h"
#include "print.h"


int main(void) {
	DataSet *train_set = DataSet_construct(6, 3, 2, (double []){
	//  input       output
		1, 0, 1,    1, 0,
		1, 0, 0,    1, 0,
		0, 1, 1,    0, 1,
		1, 1, 1,    1, 0,
		0, 0, 0,    0, 1,
		0, 1, 0,    0, 1
	});

	int layers[] = {3, 2};
	int *ptr_layers = layers;

	FullConnected *layer = FullConnected_construct(2, ptr_layers, 0.5, 0.3);
	FullConnected_train_construct(layer);

	printf("%d\n", FullConnected_train_alpha(layer, train_set, 0.001));
	FullConnected_check(layer, train_set);

	FullConnected_train_deconstruct(layer);
	FullConnected_deconstruct(layer);

	DataSet_deconstruct(train_set);

	return 0;
}