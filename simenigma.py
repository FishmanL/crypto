import random
groupsize = 10
sumsknown = []
for i in range(groupsize):
    sumsknown.append([])
def ismaj (a, size, start):
    ctr = 0
    for b in range (size):
        ctr += a[start+b][0]
    for i in range(size):
        if ctr == (size - i):
          #print(i)
          sum = 0
          for b in range(size):
            if a[start + b][0] == 0:
                sum += a[start + b][1]
          if sum not in sumsknown[i-1]:
              #print("new sum " + str(sum))
              sumsknown[i-1].append(sum)
    if ctr > size/2:
        return 1
    else:
        return 0

numtests = 40
def flatten_list(ls, flattened_list):
    for elem in ls:
        if not isinstance(elem, list): 
            flattened_list.append(elem)
        else:
            flatten_list(elem, flattened_list)
    return flattened_list

def recursive_len(item):

    return len(flatten_list(item, []))
for i in range(5, numtests):
    groupsize = i #comment out to switch to advpower testing
    secretsize = 900
    secretnum = 800
    advpower = 0.3
    #advpower = random.uniform(0.2, 0.8) for advpower testing
    numtildone = 0
    numtrials = 20
    for j in range(numtrials):
        x = []
        
        secby = 0
        advknown = []
        for k in range(len(sumsknown), groupsize):
            sumsknown.append([])
        for k in range(groupsize):
            sumsknown[k]=[]
        for y in range(secretsize):
            if random.uniform(0, 1) < advpower:
                r = 1
                advknown.append(y)
            else:
                r = 0
            x.append([r, y])
        #print(sumsknown)
        while ((recursive_len(sumsknown) + len(advknown)) < secretsize) and (len(sumsknown[0]) + len(advknown) < secretnum):
            random.shuffle(x)
            advgroups =0
            #sprint ("new trial")
            numtildone += 1


            for b in range(int(len(x)/groupsize)):
                advgroups += ismaj (x, groupsize, groupsize*b)
        #print(len(advknown))
        #print(len(sumsknown[0]))
        #print(len(sumsknown[1]))
        #print(len(sum2known))
        #print(len(sum3known))


    print(str(groupsize) + ", " + str(numtildone/numtrials))
