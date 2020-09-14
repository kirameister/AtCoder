# 単純に入力を整数として取り込む
def i_input: 
    return int(input())
A = int(input())

# 複数の入力の値を整数として異なる変数に入れる
[A, B] = map(int, list(input().split(' ')))

# 最初の値は変数に、それ以降の値をリストにする
A, *B = map(int, list(input().split(' ')))
# または...
[A, *B] = map(int, list(input().split(' ')))



