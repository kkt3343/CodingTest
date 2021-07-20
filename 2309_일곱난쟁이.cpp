#include <iostream>

using namespace std;

int box[9] = { 0 };
int main(void)
{
	int sum = 0;
	for (int i = 0; i < 9; i++) {
		cin >> box[i];
		sum = sum + box[i];
	}
	bool key = false;
	int result = 0;
	int x, y;
	/*알고리즘 설명*/
	/*
	* 9개 중에 7개를 택하는 것은 복잡하기 때문에 반대로 9개를 모두 더한다음
	* 2개를 택하여 뺀다.
	* 이 때 2개는 중복이 되면 안된다.
	* 브루트포스이기 때문에 하나하나 다 해보는 수밖에 없다.
	*/
	for (int i = 0; i < 9 && key == false; i++) {
		for (int j = 0; j < 9 && key == false; j++) {
			result = sum - box[i] - box[j];
			if (result == 100 && box[i] != box[j])
			{
				key = true;
				x = i;
				y = j;
			}
		}
	}
	//선택된 두 값은 백설공주의 난쟁이가 아니기 때문에 -1로 치환한다.
	box[x] = -1; box[y] = -1;
	int tem;
	//정렬을 실시한다.(오름차순) / 이 때 간단한 버블정렬 사용
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9 - 1 - i; j++) {
			if (box[j] > box[j + 1]) {
				tem = box[j];
				box[j] = box[j + 1];
				box[j + 1] = tem;
			}
		}
	}
	// -1인 두 난쟁이를 제외하고 출력
	for (int i = 2; i < 9; i++) {
		printf("%d\n", box[i]);
	}
	return 0;
}