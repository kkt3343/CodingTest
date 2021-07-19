#include <iostream>
#include <queue>
using namespace std;
char box[101][101] = { 0 };
char cbox[101][101] = { 0 };
queue<int> xstr;
queue<int> ystr;

int i, j, N, x , y;
char mychar = 'Z';
int cal(char (*boxx)[101])
{
	int count = 0;
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			x = i; y = j;
			if (boxx[i][j] != 'Z') {
				mychar = boxx[i][j];
				boxx[i][j] = 'Z';

				//Inqueue
				xstr.push(x);
				ystr.push(y);

				while (1) {
					bool nflag = false, eflag = false, sflag = false, wflag = false;
					bool key = false;

					x = xstr.front();
					y = ystr.front();
					//끝에 테두리에서 바깥으로 못나가게 하는 장치
					if (x == 0) {
						nflag = true;
					}
					if (x == N - 1) {
						sflag = true;
					}
					if (y == 0) {
						wflag = true;
					}
					if (y == N - 1) {
						eflag = true;
					}
					xstr.pop();
					ystr.pop();

					if (eflag == false && boxx[x][y + 1] != 'Z' && boxx[x][y + 1] == mychar) {
						boxx[x][y + 1] = 'Z';

						//Inqueue
						xstr.push(x);
						ystr.push(y + 1);
					}
					if (sflag == false && boxx[x + 1][y] != 'Z' && boxx[x + 1][y] == mychar) {
						boxx[x + 1][y] = 'Z';

						//Inqueue
						xstr.push(x + 1);
						ystr.push(y);
					}
					if (wflag == false && boxx[x][y - 1] != 'Z' && boxx[x][y - 1] == mychar) {
						boxx[x][y - 1] = 'Z';

						//Inqueue
						xstr.push(x);
						ystr.push(y - 1);
					}
					if (nflag == false && boxx[x - 1][y] != 'Z' && boxx[x - 1][y] == mychar) {
						boxx[x - 1][y] = 'Z';

						//Inqueue
						xstr.push(x - 1);
						ystr.push(y);
					}

					if (xstr.empty() == true && ystr.empty() == true)
					{
						count++;
						break;
					}
				}
			}
		}
	}
	return count;
}

int main(void){
	cin >> N;
	for (i = 0; i < N; i++){
		cin >> box[i];
	}	
	/*-----------------------*/
	//색맹전용칸 복사하기
	//적록색맹은 빨간색과 초록색을 구별 못하니까 초록색을 빨간색으로 퉁친다.
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			if (box[i][j] == 'G') {
				cbox[i][j] = 'R';
			}
			else {
				cbox[i][j] = box[i][j];
			}
		}
	}
	int normal, abnormal;
	normal = cal(&box[0]);
	abnormal = cal(&cbox[0]);

	//출력
	printf("%d %d\n", normal, abnormal);
	return 0;
}