#include <iostream>
#include <cstdlib>
using namespace std;
int main()
{
	int K;
	cin >> K;
	int* box = (int*)calloc(K , sizeof(int));

	int tem = 0, result = 0, p = 0;
	for (int i = 0; i < K; i++) {
		cin >> tem;
		if (tem == 0) {
			if (p == 0) {
				box[p] = 0;
			}
			else {
				p--;
				box[p] = 0;
			}
		}
		else {
			box[p] = tem;
			p++;
		}
	}
	for (int i = 0; i < K; i++) {
		result = result + box[i];
	}
	cout << result << endl;
	free(box);
	return 0;
}