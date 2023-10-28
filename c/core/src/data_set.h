typedef struct Pair {
	double* input;
	double* output;
} Pair;


typedef struct DataSet {
	int length;
	int input_length;
	int output_length;
	Pair** pairs;
} DataSet;

DataSet* DataSet_construct(int pairs_count, int input_length, int output_length, double data[]);
void DataSet_deconstruct(DataSet* data_set);

void DataSet_add(DataSet* data_set, double data[]);
