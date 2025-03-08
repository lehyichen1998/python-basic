'''
什么是列表：
    list:(list是列表类型，同属于数据类型)
'''

a = '小白','小红','小蓝'
# print(type(a))

'''
变量的命名规则：
变量在命名时   不能用关键字 42 关键字class def and in if while as with while for try excepet or 
'''
'''
[]就代表为列表类型，在任何地方只要看见了[],# print(type(li))
'''
'''
传达列表中可以存放的数据类型
lis = ['小红',('小绿'),10,True,{"name":"楚楚","age":20},10.2,[7,8,9]]
    #  str   tuple  int  bool         字典            float   列表
'''
'''
第一列表可以放很多种的数据类型
第二放很多很多条数据
第三种： 增删改查
'''
"""
    #增删改查
        1:什么是索引 2: 增删改查（切片处理；） 
"""
'''#增加：饮料的信息'''
drink_mai = ['脉动',5,'123456',2020]
drink_coco = ['可乐',3,'654321',2020]
                    #索引
'''             增加    对脉动增加一条数据    '''
# drink_mai.append('md0001')   #普通的增加方式
# drink_mai.insert(2,'蜜桃')    #指定增加方式
v = drink_mai.extend(drink_coco) #extend的增加样式
'''             删除     对脉动的数据进行删除    '''
# drink_mai.pop()   #根据索引删除，或者默认删除最后一个
# drink_mai.remove()   #删除指定数据，或者将整个数据删除
# drink_mai.clear()   #清空指定的这个列表

'''             修改      对脉动的数据进行修改     '''
# drink_mai[0] = '脉动饮料'   #根据索引进行修改

'''             查找      对脉动进行查找      '''
# drink_mai.index(5)      #根据列表中的值进行查找
# print(drink_mai[0])      #根据提供的索引进行查找
# print(drink_mai[:-1])    #利用切片进行区域寻找
# print(drink_mai[:: -1])   #顺序反查询
# lis = ['小红',('小绿'),10,True,{"name":"小白","age":20},10.2,[7,[0,1,2,3,4],8,9]]
# print(lis[4]['name'])     #二位数组查询,还有三位数组

# print(drink_mai)

'''认识列表推导式
        求1-100，2次方,并保存在一个集合中
'''

# print([i ** 2 for i in range(1, 101)])

'''认识zip
        我们认识的zip是一个压缩文件啥的，来看看python的zip
        习题，在一个市场中中要查看一个产品他的名称和销量，怎样实现最好的展示效果？
'''
#首先我们需要两组数据
# commodity = ['保温杯','枸杞','洗发水','格子衬衫']
# sales = [20,30,40,50]
# # 入和将两组数据打包在一起
# print(list(zip(commodity, sales)))
# #zip是如何实现他的作用的
# result = list(zip([i for i in commodity], [i for i in sales])) #将他们两者的数据进行打包，封装成一个元组
# print(type(result[0]))     #元组，的作用就是封装好一串数组，保证数据的安全，不让别人进行变动
#
# #导入pyecharts 实现对数据的可视化操作
# from pyecharts.charts import Pie
# (Pie().add(series_name='占比',data_pair=[i for i in result])).render('qqqqq.html')

'''                   #利用列表实现敏感词汇的屏蔽         '''


# li = ['憨憨','笨蛋']
# while True:
#     a = input('请输入一句话，enter退出>>>')
#     for i in li:
#         if i==a or i in a:
#             print('***'.join(a.split(i)))
#     if a=='':
#         break



'''                  实现字符去重    '''
# names = ['张三', '李四', '大黄', '张三']
# new_names = []
# for name in names:
#     if name not in new_names:
#         new_names.append(name)
# names = new_names
# print(names)



b = [i for i in range(10)]

