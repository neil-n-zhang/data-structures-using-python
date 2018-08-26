weight=[2,3,4,5,9]
value=[3,4,8,8,10]
bag_vol=20
total_value=[0 for i in range(bag_vol+1)]
total_art=[[] for i in range(bag_vol+1)]

for total_weight in range(min(weight),bag_vol+1):
    total_value[total_weight]=total_value[total_weight-1]
    total_art[total_weight]=total_art[total_weight-1]
    for j in range(len(value)):
        if total_weight>=weight[j]:
            last_total_weight=total_weight-weight[j]
            if weight[j] in total_art[last_total_weight]:
                continue
            else:
                if total_value[last_total_weight]+value[j]>total_value[total_weight]:
                    total_value[total_weight]=total_value[last_total_weight]+value[j]
                    total_art[total_weight]=total_art[last_total_weight].copy()
                    total_art[total_weight].append(weight[j])
print('We should bring weight ',total_art[-1])
