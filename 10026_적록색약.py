#일단 값을 받아온다.
N = input()

#공간선언 및 빈 리스트 선언
Tbox = [[0] * 101 for i in range(101)]
box = [[0] * 101 for i in range(101)]
cbox = [[0] * 101 for i in range(101)]

# 100 X 100 배열 코드
TTT = [[0]*100]*100

xstr = []
ystr = []

def cal(boxx):
    count = 0

    for i in range(0,int(N),1):
        for j in range(0,int(N),1):
            x = i
            y = j
            if (boxx[i][j] != 'Z'):
                mychar = boxx[i][j]
                boxx[i][j] = "Z"

                xstr.append(x)
                ystr.append(y)
                
                while(True):
                    nflag,eflag,sflag,wflag = False
                    x = xstr[0]
                    y = ystr[0]
                    if(x==0):
                        nflag = True
                    if(x==int(N)-1):
                        sflag = True
                    if(y==0):
                        wflag = True
                    if(y==int(N)-1):
                        eflag = True
                    del xstr[0]
                    del ystr[0]

                    if(eflag==False and boxx[x][y+1]!='Z' and boxx[x][y+1] == mychar):
                        boxx[x][y+1] = 'Z'

                        xstr.append(x)
                        ystr.append(y+1)

                    if (sflag == False and boxx[x + 1][y] != 'Z' and boxx[x + 1][y] == mychar):
                        boxx[x + 1][y] = 'Z'

                        xstr.append(x + 1)
                        ystr.append(y)

                    if (wflag == False and boxx[x][y - 1] != 'Z' and boxx[x][y - 1] == mychar):
                        boxx[x][y - 1] = 'Z'

                        xstr.append(x)
                        ystr.append(y - 1)

                    if (nflag == False and boxx[x - 1][y] != 'Z' and boxx[x - 1][y] == mychar):
                        boxx[x - 1][y] = 'Z'

                        xstr.append(x - 1)
                        ystr.append(y)

                    if(not xstr and not ystr):
                        count = count + 1
                        break
    return count

#값 얻기
for i in range(0,int(N),1):
    Tbox[i] = input()

#input으로 값을 얻어오면 str형식으로 저장되어서 직접 하나하나 복사 때어온다.
for i in range(0,int(N),1):
    for j in range(0,int(N),1):
        box[i][j] = Tbox[i][j]

#색명전용 복사하기
for i in range(0,int(N),1):
    for j in range(0,int(N),1):
        if(box[i][j] == 'G'):
            cbox[i][j] = 'R'
        else:
            cbox[i][j] = box[i][j]

#값을 저장할 곳 및 출력
normal = cal(box)
abnormal = cal(cbox)
print("%d %d" %(normal,abnormal))