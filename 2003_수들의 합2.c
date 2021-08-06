#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
int main()
{
	int N, M;
	scanf("%d", &N);
	scanf("%d", &M);

	int *box = (int*)calloc(N, sizeof(int));

	for (int i = 0; i < N; i++) {
		scanf("%d", &box[i]);
	}

	int s = 0, e = 0;
	
	/* How to Solve
	*  처음에 시작과 끝이 모두 0으로 설정된다.
	*  s위치(시작)부터 e위치(끝) 배열의 값을 모두 더한다.
	*  이 더한 값이 M보다 작게 된다면, e를 증가시킨다.
	*  그런데 값이 같거나 크게 된다면, 맨 앞의 값을 제외하고
	*  s를 더한다.
	*  그런식으로 모든 값을 구해봐서 M과 같은지 구한다.
	*/

	/* 투 포인터 알고리즘인데, 자연수가 아니라면 불가능하다. */

	int sum = 0, answer = 0;
	//end가 N에 도달할 때 까지 해본다.
	while (e <= N)
	{
		if (sum < M) {
			sum = sum + box[e];
			e++;
		}
		else if (sum >= M) {
			sum = sum - box[s];
			s++;
		}
		if (sum == M) {
			answer++;
		}
	}
	printf("%d\n", answer);
	free(box);
	return 0;
}