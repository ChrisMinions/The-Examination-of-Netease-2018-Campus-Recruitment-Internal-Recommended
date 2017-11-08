'''
[编程题] 交错01串
时间限制：1秒
空间限制：32768K
如果一个01串任意两个相邻位置的字符都是不一样的,我们就叫这个01串为交错01串。
例如: "1","10101","0101010"都是交错01串。

小易现在有一个01串s,小易想找出一个最长的连续子串,并且这个子串是一个交错01串。
小易需要你帮帮忙求出最长的这样的子串的长度是多少。 
输入描述:
输入包括字符串s,s的长度length(1 ≤ length ≤ 50),字符串中只包含'0'和'1'


输出描述:
输出一个整数,表示最长的满足要求的子串长度。

输入例子1:
111101111

输出例子1:
3
'''

'''
解题思路：注意审题
  题目中说的子串应该是连续子串，比如说11001101，这个01串最长的交错01串应该是最后三位101，不是10101
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

string = input()

temp = string[0]
results = []
length = len(string)
index = 0
count = 1

while index < length-1:
    if string[index] != string[index+1]:
        flag = True
        index += 1
        count += 1
        while flag and index < length-1:
            if string[index] != string[index+1]:
                index += 1
                count += 1
            else:
                flag = False
                results.append(count)
                index += 1
                count = 1
    else:
        index += 1

results.append(count)
print(max(results))
