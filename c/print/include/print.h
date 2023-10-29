void DataSet_print(DataSet* data_set);

void FullConnected_print_weights(FullConnected* layer);
void FullConnected_print_biases(FullConnected* layer);
void FullConnected_print_x(FullConnected* layer);
void FullConnected_print_delta_weights(FullConnected* layer);
void FullConnected_print_delta_biases(FullConnected* layer);
void FullConnected_print_gradient(FullConnected* layer);

void MaxPooling_print_input(MaxPooling* layer);
void MaxPooling_print_x(MaxPooling* layer);
void MaxPooling_print_err(MaxPooling* layer);
