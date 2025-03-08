i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('%dx%d=%d' % (i, j, j * i), end='\t')
        # print(str(i)+'x'+str(j)+'='+str(j*i),end='\t')
        j = j + 1
    print()  # 标识换行
    i = i + 1