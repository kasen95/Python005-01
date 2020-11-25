# 内置类型

##逻辑值检测
import sys
from decimal import Decimal

'''
1.假值对象
1）假值常量：None和False
2）任何数值类型的0：0，0.0，0j，Decimal(0)
3）空的序列和多项集：'',(),[],{},set(),range(0)
'''
list1 = [None, False, 0, 0.0, 0j, Decimal(0), '', (), [], {}, set(), range(0)]
for i in list1:
    if i:
        print('{}为假值'.format(i))

'''
2.布尔运算
1）not的优先级比非布尔运算符低，因此not a == b正确，a== not b错误
'''


'''
3.数字类型---int,float,complex
'''
print(int(1.1))
print(float(1.1))
print(complex(1.1))

'''
4.列表
'''
list2=[1,5,34,'2342','dwfsd','胜多负少',False]
list2.append('123')
list2[2]=23
print(list2)
#此方法会对列表进行原地排序，只使用 < 来进行各项间比较。 异常不会被屏蔽 —— 如果有任何比较操作失败，整个排序操作将失败
#print(sorted(list1,reverse=False))

'''
5.元组
'''
tuple1=(1,4,54,'sdf',[1,4,6,'234'],(55,66))
print(tuple1[4][3])

'''
6.range
range类型相比常规list和tuple的优势在于一个range对象总是占用固定数量的内存，不论其所表示的范围有多大
'''
print(list(range(1,12,3)))

'''
7.文本序列类型----str
'''
str1='niaho阿道{}夫'
print(str1.encode('utf-8'))
#首字母大写，其他小写
print(str1.capitalize())
#消除大小写
print(str1.casefold())
#索引
print(str1.find('h'))
print(str1.index('ho'))
#字符串格式化操作
print(str1.format('123'))
#拼接
str1.join('adasda')
#小写
str1.lower()
#大写
str1.upper()
#替换
str1.replace('nihao','asdad')
#分割
str1.split('i')