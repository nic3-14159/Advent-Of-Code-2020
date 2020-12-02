#include <cstdio>
#include <vector>
using namespace std;

int main(){
	vector <bool> entryPresent(2021, false);
	vector <int> entries;
	int i;
	while (scanf("%d", &i) != EOF){
		entryPresent[i] = true;
		entries.push_back(i);
	}
	for (int i = 0; i<entries.size(); i++){
		int target = 2020 - entries[i];
		for (int j = i+1; j<entries.size(); j++){	
			if ((target-entries[j]) < 0){
				continue;
			}
			if (entryPresent[target-entries[j]]){
				printf("%d\n", entries[i] * (entries[j]*(target-entries[j])));
				return 0;
			}
		}
	}
	return 0;
}
