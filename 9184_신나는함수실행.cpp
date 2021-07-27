#include <iostream>
using namespace std;

int mybox[51][51][51];

int w(int a, int b, int c) {

	if (a <= 0 || b <= 0 || c <= 0) {
		return 1;
	}
	if (a > 20 || b > 20 || c > 20) {
		if (mybox[a][b][c] == 0)
		{
			mybox[a][b][c] = w(20, 20, 20);
			return mybox[a][b][c];
		}
		else
		{
			return mybox[a][b][c];
		}
	}
	if (a < b && b < c) {
		if (mybox[a][b][c] == 0)
		{
			mybox[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c);
			return mybox[a][b][c];
		}
		else
		{
			return mybox[a][b][c];
		}
		//return w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c);
	}
	else {
		if (mybox[a][b][c] == 0)
		{
			mybox[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1);
			return mybox[a][b][c];
		}
		else
		{
			return mybox[a][b][c];
		}

		//return w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1);
	}
}
// 1 1 1
// 0 1 1 + 0 0 1 + 0 1 0 - 0 0 0


//2 2 2
// 1 2 2 + 1 1 2 + 1 2 1 - 1 1 1
// 1 2 2 : 0 2 2 + 0 1 2 + 0 2 1 - 0 1 1
// 1 1 2 : 0 1 2 + 0 0 2 + 0 1 1 - 0 0 1

int main()
{
	int a, b, c;
	while (1)
	{
		cin >> a >> b >> c;
		if (a == -1 && b == -1 && c == -1)
		{
			break;
		}
		int result;
		result = w(a, b, c);
		cout << "w(" << a << ", " << b << ", " << c << ") = " << result << endl;
	}
	return 0;
}