#include <iostream>
#include <string>
using namespace std;
int box[100000] = { 0 };
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;
	string tem;
	int numtem;
	int p = 0;
	for (int i = 0; i < N; i++) {
		cin >> tem;
		if (tem == "push") {
			cin >> numtem;
			box[p] = numtem;
			p++;
		}
		else if (tem == "pop") {
			if (p <= 0) {
				cout << -1 << "\n";
			}
			else {
				p--;
				cout << box[p] << "\n";
				box[p] = 0;
			}
		}
		else if (tem == "size") {
			cout << p << "\n";

		}
		else if (tem == "empty") {
			if (p == 0) {
				cout << 1 << "\n";
			}
			else {
				cout << 0 << "\n";
			}
		}
		else if (tem == "top") {
			if (p <= 0) {
				cout << -1 << "\n";
			}
			else {
				cout << box[p - 1] << "\n";
			}
		}
		else {

		}
	}
	return 0;
}