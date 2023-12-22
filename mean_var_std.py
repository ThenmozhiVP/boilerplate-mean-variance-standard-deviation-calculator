import numpy as np

def calculate(list):

if len(list)<9:
    raise ValueError("List must contain nine numbers.")
    return

l1 = np.reshape(list,(3,3))

mean_x = l1.mean(axis = 0).tolist()
mean_y = l1.mean(axis = 1).tolist()
meann = l1.mean()
mean_list = [mean_x,mean_y,meann]

std_x = l1.std(axis = 0).tolist()
std_y = l1.std(axis = 1).tolist()
stdd = l1.std()
std_list = [std_x,std_y,stdd]

var_x = l1.var(axis = 0).tolist()
var_y = l1.var(axis=1).tolist()
varr = l1.var()
var_list = [var_x,var_y,varr]

max_x = l1.max(axis=0).tolist()
max_y = l1.max(axis=1).tolist()
maxx = l1.max()
max_list = [max_x,max_y,maxx]

min_x = l1.min(axis = 0).tolist()
min_y = l1.min(axis=1).tolist()
minn = l1.min()
min_list = [min_x,min_y,minn]

sum_x = l1.sum(axis=0).tolist()
sum_y=l1.sum(axis=1).tolist()
summ = l1.sum()
sum_list = [sum_x,sum_y,summ]

result = {}
result['mean'] = mean_list
result['variance'] = var_list
result['standard deviation'] = std_list
result['max'] = max_list
result['min'] = min_list
result['sum'] = sum_list

return result
                            


    
