typedef struct MaxPooling {
	int channels, height, width, matrix_h, matrix_w;
	double*** data_input;
	double*** x;
	double*** err;
} MaxPooling;


MaxPooling* MaxPooling_construct(int channels, int height, int width, int matrix_h, int matrix_w);
void MaxPooling_deconstruct(MaxPooling* layer);

void MaxPooling_train_construct(MaxPooling* layer);
void MaxPooling_train_deconstruct(MaxPooling* layer);

void MaxPooling_forward(MaxPooling* layer, double* input);
void MaxPooling_backward(MaxPooling* layer, double* output);
