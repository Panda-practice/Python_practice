from statistics import mean,median,variance,stdev

data={1.5,500,680,9000}

m=mean(data)
med=median(data)
var=variance(data)
sd=stdev(data)

print('平均：{0:.2f}'.format(m))
print('中央値：{0:.2f}'.format(med))
print('分散：{0:.2f}'.format(var))
print('標準偏差：{0:.2f}'.format(sd))
