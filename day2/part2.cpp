#include <iostream>
#include <cstdio>
using namespace std;

int main(){
	int low, high;
	int valid_count = 0;
	char letter;
	char buffer[100];
	while (scanf("%d-%d %c: %s", &low, &high, &letter, buffer) != EOF){
		if (buffer[low-1] != buffer[high-1] && (buffer[low-1] == letter || buffer[high-1] == letter)){
			valid_count++;
		}
	}
	printf("%d\n", valid_count);
	return 0;
}
