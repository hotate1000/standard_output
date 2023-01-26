# paizaはberakを利用するとエラーとなる。

# ---------------------------------------------
# 単一データ。
# 入力値：
# test1
# ---------------
value = input();
print(value);
# test1と出力。

# ---------------------------------------------
# 複数データ。
# 入力値：
# 3
# test1
# test2
# test3
# ---------------
a = int(input());
value_list = [];

for i in range(a):
    value_list.append(input());
print(value_list);
# ['test1','test2','test3']と出力。
# ---------------
# 違う書き方
# ---------------
n = int(input());

value_list = [input() for i in range(n)];
print(value_list);

# ---------------------------------------------
# 複数のデータ。数値。
# 入力値：
# 3
# 1
# 2
# 3
# ---------------
a = int(input());
value_list_int = [];

for i in range(a):
    value_list_int.append(int(input()));
print(value_list_int);
# [1, 2, 3]と出力。

# ---------------------------------------------
# 複数データの場合。スペース。
# 入力値：
# test1 test2 test3
# ---------------
a, b, c = input().split();
print(a);
# test1と出力。
print(c);
# test3と出力。

# ---------------------------------------------
# 複数データの場合。スペース。数値。
# 入力値：
# 1 2 3
# ---------------
value_list = input().split();
print(value_list);
# ['1', '2', '3']と出力。
value_list_int = [];

for i in value_list:
    value_list_int.append(int(i));
print(value_list_int);
# [1, 2, 3]と出力。

# ---------------------------------------------
# インデックスの取得
# ---------------
value_list = input().split();
print(value_list);
# ['1', '2', '3']と出力。
for i,x in enumerate(value_list):
    print(i, x);

# ---------------------------------------------
# ---------------------------------------------
# ---------------------------------------------
# ---------------
# 出力方法の参考
# ---------------
test1 = input();
test2 = int(test1) * 1.1;

print(test1, test2);
# '100'と入力する。
# '100 108'と表示される。
