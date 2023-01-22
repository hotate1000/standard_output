# ---------------
# ---------------
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

# ---------------
# ---------------
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
