from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码

colordict = {'张延钊':'sienna','王元玮':'slateblue','吕江枫':'purple','李书缘':'darkred','郭维泽':'orange','王云杰':'green'}
def draw(datas,name):
    plt.figure(figsize=(6,9)) #调节图形大小 
    labels = [key for key in colordict if key in datas]
    sizes = [datas[key] for key in labels]
    # labels = list(datas.keys())
    # sizes = list(datas.values())
    colors = [colordict[name] for name in labels]
    # labels = [u'大型',u'中型',u'小型',u'微型'] #定义标签
    # sizes = [46,253,321,66] #每块值
    # colors = ['red','yellowgreen','lightskyblue','yellow'] #每块颜色定义
    # explode = (0,0,0,0) #将某一块分割出来，值越大分割出的间隙越大
    patches,text1,text2 = plt.pie(sizes,
                          labels=labels,
                          colors = colors,
                          autopct = '%3.2f%%', #数值保留固定小数位
                          shadow = False, #无阴影设置
                          startangle =90, #逆时针起始角度设置
                          pctdistance = 0.6) #数值距圆心半径倍数距离
    #patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部的文本
    # x，y轴刻度设置一致，保证饼图为圆形
    plt.axis('equal')
    # plt.show()
    plt.savefig(name)
def deal(filename):
    datas = {}
    with open(filename) as f:
        next(f)
        for line in f:
            line = line.split(',')
            work = line[-1].strip()
            if work != '':
                lis = line[3:-1]
                for name in lis:
                    name = name.replace('"','')
                    datas.setdefault(name,0)
                    datas[name] += float(work)
    return datas
    # data_lis = [(key,datas[key]) for key in datas]
    # with open(filename.split('.')[0] +'_个人.CSV','w') as f:
    #     f.write('姓名,工作量\n')
    #     for ele in data_lis:
    #         f.write(ele[0] + ','+str(ele[1])+'\n')
    # draw(datas,filename.split('.')[0])

# filename = '总工作量统计.CSV'
# deal(filename)
tot_datas = {}
for ele in ['一','二','三','四','五','六','七','八']:
    filename = '实验'+ele+'工作量统计.CSV'
    datas = deal(filename)
    for ele in datas:
        tot_datas.setdefault(ele,0)
        tot_datas[ele] += datas[ele]
    data_lis = [(key,tot_datas[key]) for key in tot_datas]
    with open('总工作量统计_个人.CSV','w') as f:
        f.write('姓名,工作量\n')
        for ele in data_lis:
            f.write(ele[0] + ','+str(ele[1])+'\n')
    draw(tot_datas,'总工作量统计')