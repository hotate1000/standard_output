# ------------------------------
# ------------------------------
h, w = input().split();
h = int(h);
w = int(w);

a1, a2 = input().split();
a1 = int(a1);
a2 = int(a2);

a3, a4 = input().split();
a3 = int(a3);
a4 = int(a4);

# 横の増加量
x2_1_y1 = a2 - a1; # 4
x2_1_y2 = a4 - a3; # 3
x_w = x2_1_y2 - x2_1_y1; # -1
# 縦の増加量
x1_y2_1 = a3 - a1; # -3
x2_y2_1 = a4 - a2; # -4
x_h = x2_y2_1 - x1_y2_1; # -1

# 一番左の縦の増加量を求める。
# 一列づつの横の増加量を求める。
for j in range(h):
    answer = '';
    for i in range(w):
        if i == 0:
            answer += str(a1 + j * x1_y2_1);
        if i != 0:
            answer += ' ' + str((a1 + j * x1_y2_1) + ((x2_1_y1 + x_h * j)  * i));
    print(answer);


# ------------------------------
# ------------------------------
N,M = input().split();
N = int(N);
M = int(M);

length = M + M * N;
value_list = [];
value_list_int = [];
anser_list = [];

for i in range(length):
    value_list.append(input());
for i in value_list:
    value_list_int.append(int(i));

score = 100;
for j in range(N):
    score = 100;
    for i in range(M):
        value = abs(value_list_int[i] - value_list_int[i + (M * (j + 1))]);
        if value <= 5: 
            score -= 0;
        elif value <= 10:
            score -= 1;
        elif value <= 20:
            score -= 2;
        elif value <= 30:
            score -= 3;
        else:
            score -= 5;
        if score <= 0:
            score = 0;
    anser_list.append(score);
print(max(anser_list));


# ------------------------------
# ------------------------------
a = int(input());
value_list = [];
value_list_int = [];
check = 1;

for i in range(a):
    value_list.append(input());

for i in value_list:
    value_list_int.append(int(i));

max_val = max(value_list_int);

for i,j in enumerate(range(max_val)):
    for ii,x in enumerate(value_list_int):
        if x == check:
            check += 1;
            if check-1 == max_val:
                print(i);
                break;


# ------------------------------
# paizaはberakを利用するとエラーとなる。
# ------------------------------
N, C1, C2 = input().split();
N  = int(N);
C1 = int(C1);
C2 = int(C2);

cost = 0;
anser = 0;
value_list_int = [];

for i in range(N):
    value_list_int.append(int(input()));

for x,i in enumerate(value_list_int):
    if x == len(value_list_int) - 1:
        if cost > 0:
            anser += i * cost;
            cost = 0;
    elif i <= C1:
        cost += 1;
        anser -= i;
    elif C1 < i and i < C2:
        break;
    elif C2 <= i:
        if cost > 0:
            anser += i * cost;
            cost = 0;
        else:
            break;

print(anser);
