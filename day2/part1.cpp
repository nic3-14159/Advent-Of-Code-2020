#include <iostream>
#include <cstdio>
using namespace std;

int main(){
	int low, high;
	int valid_count = 0;
	char letter;
	char buffer[100];
	while (scanf("%d-%d %c: %s", &low, &high, &letter, buffer) != EOF){
		int count = 0;
		for (char *i = buffer; *i != 0; i++){
			if (*i == letter){
				count ++;
			}
		}
		if (low <= count && count <= high){
			valid_count++;
		}
	}
	printf("%d\n", valid_count);
	return 0;
}
