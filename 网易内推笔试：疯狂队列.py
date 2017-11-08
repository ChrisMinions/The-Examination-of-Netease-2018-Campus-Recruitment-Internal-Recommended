'''
[编程题] 疯狂队列
时间限制：1秒
空间限制：32768K
小易老师是非常严厉的,它会要求所有学生在进入教室前都排成一列,并且他要求学生按照身高不递减的顺序排列。
有一次,n个学生在列队的时候,小易老师正好去卫生间了。学生们终于有机会反击了,于是学生们决定来一次疯狂的队列,
他们定义一个队列的疯狂值为每对相邻排列学生身高差的绝对值总和。
由于按照身高顺序排列的队列的疯狂值是最小的,他们当然决定按照疯狂值最大的顺序来进行列队。
现在给出n个学生的身高,请计算出这些学生列队的最大可能的疯狂值。小易老师回来一定会气得半死。 
输入描述:
输入包括两行,第一行一个整数n(1 ≤ n ≤ 50),表示学生的人数
第二行为n个整数h[i](1 ≤ h[i] ≤ 1000),表示每个学生的身高


输出描述:
输出一个整数,表示n个学生列队可以获得的最大的疯狂值。

如样例所示: 
当队列排列顺序是: 25-10-40-5-25, 身高差绝对值的总和为15+30+35+20=100。
这是最大的疯狂值了。

输入例子1:
5
5 10 25 40 25

输出例子1:
100
'''

'''
解题思路：找规律 + 仔细小心
  把原序列排序，先取出最大的数放在results中，然后在最大数的两边放两个最小的数，接着在两个最小的数两边放第二、第三大的数
  依次类推
  再放入最后一个数的时候要注意，计算它放在最左侧或最右侧时与相邻的元素差值的绝对值，选择把它放在绝对值大的那一侧
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

n = int(input())
heights = [each_height for each_height in map(int, input().split())]

s2l = sorted(heights)
l2s = s2l[::-1]

results = []
pop_small = True
left = True
for i in range(n):
    if i == 0:
        results.append(s2l.pop())
    elif i == n-1:
        if pop_small:
            temp = l2s.pop()
            if abs(results[0] - temp) > abs(results[n-2] - temp):
                results.insert(0, temp)
            else:
                results.append(temp)
        else:
            temp = s2l.pop()
            if abs(results[0] - temp) > abs(results[n - 2] - temp):
                results.insert(0, temp)
            else:
                results.append(temp)
    elif pop_small:
        if left:
            results.insert(0, l2s.pop())
            left = False
        else:
            results.append(l2s.pop())
            left = True
            pop_small = False
    else:
        if left:
            results.insert(0, s2l.pop())
            left = False
        else:
            results.append(s2l.pop())
            left = True
            pop_small = True

print(sum([abs(results[i] - results[i+1]) for i in range(n-1)]))
