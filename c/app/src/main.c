#include <kazamori.h>
#include <print.h>


int main(int argc, char* argv[]) {
	MaxPooling* layer = MaxPooling_construct(
		2, // channels
		4, // height
		5, // width
		2, // matrix_h
		3  // matrix_w
	);
	ImageSet* image_set = ImageSet_construct(
		3, // length
		2, // channels
		4, // height
		5, // width
		2  // output_length
	);

	ImageSet_add(image_set,
		(double[]){
			// input
			1, 2, 3, 4, 5,
			6, 7, 8, 9, 10,
			11, 12, 13, 14, 15,
			16, 17, 18, 19, 20,

			2, 4, 6, 8, 10,
			12, 14, 16, 18, 20,
			22, 24, 26, 28, 30,
			32, 34, 36, 38, 40
		}, (double[]){
			// output
			5, 17
		}
	);
	
	for (int c = 0; c < layer->channels; ++c) {
		printf("{\n");
		for (int h = 0; h < layer->height; ++h) {
			printf("   {");
			for (int w = 0; w < layer->width; ++w) {
				printf("%lf, ", image_set->input[0][c][h][w]);
			}
			printf("},\n");
		}
		printf("},\n");
	}

	ImageSet_destruct(image_set);
	MaxPooling_destruct(layer);
	
	return 0;
}