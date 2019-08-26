N, *V = map(int, open(0).read().split())
xs = V[0::3]
ys = V[1::3]
hs = V[2::3]
MAX = 101
high_cand = int()

for y in range(MAX):
  for x in range(MAX):
    high_cand = -1
    for i in range(N):
      # 最初に高さ > 0 の場合を調べる
      if(hs[i] > 0):
        tmp = hs[i] + abs(xs[i] - x) + abs(ys[i] - y)
        if(high_cand == -1):
          high_cand = tmp
        else:
          if(high_cand != tmp):
            high_cand = -2
      # その結果矛盾していれば次を見る
      if(high_cand == -2):
        continue;
    # 高さ 0 の場合を調べる
    for i in range(N):
      if(hs[i] == 0):
        a = hs[i] + abs(xs[i] - x) + abs(ys[i] - y)
        if(high_cand > a):
          high_cand = -2
          break
    # その結果矛盾していれば次を見る
    if(high_cand == -2):
      continue;
    # ここまで矛盾なければその値を出力して終了
    print(str(x) + ' ' + str(y) + ' ' + str(high_cand))