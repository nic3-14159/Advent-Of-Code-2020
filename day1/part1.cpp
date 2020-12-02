#include <cstdio>
#include <vector>
using namespace std;

int main(){
	vector <bool> entryPresent(2020, false);
	vector <int> entries;
	int i;
	while (scanf("%d", &i) != EOF){
		entryPresent[i] = true;
		entries.push_back(i);
	}
	for (int i : entries){
		if (entryPresent[2020-i]){
			printf("%d\n", i * (2020-i));
			break;
		}
	}
	return 0;
}
