import numpy as np
from matplotlib import pyplot as plt
a = np.load("attachment.npz")
# print(a.files)
id = a['index'] # 520
ip = a['input'] # 520 = 40 * 13
op = a['output']
tr = a['trace'] # 520 * 5000
# for i in range(100) :
    # print(tr[0][i])
x = np.arange(0,5000)
# for i in range(520) :
#     dst = str(id[i])+ip[i]+".png"
#     y = tr[i]
#     plt.figure()
#     plt.plot(x,y)
#     plt.savefig(dst)
m = []
for i in range(13) :
    t = []
    for j in range(40) :
        min = 9999
        for k in range(5000) :
            if tr[i*40+j][k] < min :
                min = tr[i*40+j][k]
                min_pos = k
        t.append(min_pos)
    m.append((max(t),t.index(max(t))))

dic = {}
for i in range(40) :
    dic[i] = ip[i]
for i in m :
    print(dic[i[1]],end='') 
