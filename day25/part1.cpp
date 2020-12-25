#include <iostream>
using namespace std;

int main(){	
	unsigned long long doorPub, cardPub;
	unsigned long long doorLoops = 0;
	cin >> doorPub;
	cin >> cardPub;
	unsigned long long subject = 7;
	while (subject != doorPub){
		doorLoops++;
		subject *= 7;
		subject %= 20201227;
	}
	subject = cardPub;
	for (auto i = 0; i < doorLoops; i++){
		subject *= cardPub;
		subject %= 20201227;
	}
	cout << subject << endl;
	return 0;
}
