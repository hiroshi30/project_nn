typedef struct DataSet {
	int length;
	int input_length;
	int output_length;
	double** input;
	double** output;
} DataSet;

DataSet* DataSet_construct(int length, int input_length, int output_length, double data[]);
void DataSet_deconstruct(DataSet* data_set);

void DataSet_add(DataSet* data_set, double data[]);
