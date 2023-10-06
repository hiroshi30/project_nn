typedef struct FullConnected {
	int layers_length;
	int* layers;
	double learning_rate, momentum;
	double** x;
	double*** weights;
	double** biases;
	double** gradient;
	double*** delta_weights;
	double** delta_biases;

} FullConnected;

FullConnected* FullConnected_construct(int layers_length, int* layers, double learning_rate, double momentum);
void FullConnected_deconstruct(FullConnected* layer);

void FullConnected_train_construct(FullConnected* layer);
void FullConnected_train_deconstruct(FullConnected* layer);

void FullConnected_forward(FullConnected* layer, double* input);
void FullConnected_backward(FullConnected* layer, double* output);

double FullConnected_calculate_error(FullConnected* layer, DataSet* data_set);
void FullConnected_train(FullConnected* layer, DataSet* data_set, int epochs);
int FullConnected_train_alpha(FullConnected* layer, DataSet* data_set, double alpha);
void FullConnected_check(FullConnected* layer, DataSet* data_set);