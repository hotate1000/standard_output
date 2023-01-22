# 値の取得
n = int(input());
value_list = [];
for i in range(n):
    value_list.append(int(input()));


def main():
    for i in value_list:
        check = 'false';
        if i % 400 == 0:
            check = 'true';
        elif i % 100 == 0:
            check = 'false';
        elif i % 4 == 0:
            check = 'true';
        check_value(i, check);


# 出力用関数
def check_value(i, check):
    if check == 'true':
        print(str(i) + ' is a leap year');
    elif check == 'false':
        print(str(i) + ' is not a leap year');
    else:
        print('入力値が誤りがあります');


if __name__ == '__main__':
    main();
