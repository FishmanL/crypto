import random
def ismaj (a, size, start):
    ctr = 0
    for b in range (size):
        ctr += a[start+b][0]
    if ctr == (size - 3):
        sum = 0
        for b in range(size):
            if a[start + b][0] == 0:
                sum += a[start + b][1]

            if sum not in sum3known:
                sum3known.append(sum)
    if ctr == (size - 2):
        sum = 0
        for b in range(size):
            if a[start + b][0] == 0:
                sum += a[start + b][1]

            if sum not in sum2known:
                sum2known.append(sum)
    if ctr == (size - 1):
        for b in range(size):
            z = a[start + b][1]
            if z not in sum1known:
                sum1known.append(z)


    if ctr > size/2:
        return 1
    else:
        return 0
secretsize = 900
secretnum = 800
numtests = 150
for l in range(numtests):
    advpower = random.uniform(0.05, 0.5)
    groupsize = 4
    numtildone = 0
    numtrials = 20
    for j in range(numtrials):
        x = []

        secby = 0
        advknown = []
        sum2known = []
        sum3known = []
        sum1known = []
        for y in range(secretsize):
            if random.uniform(0, 1) < advpower:
                r = 1
                advknown.append(y)
            else:
                r = 0
            x.append([r, y])
        while ((len(sum2known) +len(sum3known) +len(sum1known) + len(advknown)) < secretsize) and (len(sum1known) + len(advknown) < secretnum):
            random.shuffle(x)
            advgroups =0
            #print ("new trial")
            numtildone += 1


            for b in range(int(len(x)/groupsize)):
                advgroups += ismaj (x, groupsize, groupsize*b)
        #print(len(advknown))
        #print(len(sum1known))
        #print(len(sum2known))
        #print(len(sum3known))


    print(str(advpower) + ", " + str(numtildone/numtrials))
