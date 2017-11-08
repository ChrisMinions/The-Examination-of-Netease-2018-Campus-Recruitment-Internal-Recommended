'''
[编程题] 小易喜欢的数列
时间限制：1秒
空间限制：32768K
小易非常喜欢拥有以下性质的数列:
1、数列的长度为n
2、数列中的每个数都在1到k之间(包括1和k)
3、对于位置相邻的两个数A和B(A在B前),都满足(A <= B)或(A mod B != 0)(满足其一即可)
例如,当n = 4, k = 7
那么{1,7,7,2},它的长度是4,所有数字也在1到7范围内,并且满足第三条性质,所以小易是喜欢这个数列的
但是小易不喜欢{4,4,4,2}这个数列。小易给出n和k,希望你能帮他求出有多少个是他会喜欢的数列。 
输入描述:
输入包括两个整数n和k(1 ≤ n ≤ 10, 1 ≤ k ≤ 10^5)


输出描述:
输出一个整数,即满足要求的数列个数,因为答案可能很大,输出对1,000,000,007取模的结果。

输入例子1:
2 2

输出例子1:
3
'''

'''
解题思路：动态规划
  用长度为k的列表dp来记录以不同数字结尾的满足条件的数列
  第一重循环不同的数字长度
  第二重循环不同的数字，来更新dp，每一次更新都是将原始的dp各项求和后减去不满足的项数的和
  例如，k=7，对以4结尾的数字进行更新，那么对原来的dp求和，然后减去原来dp中表示以1,2结尾的项的和（因为1,2不满足条件）
  第二重循环结束后更新dp
  
  同一种算法，用C实现就可以100%通过，用python只能通过40%，应该还有提高算法效率的技巧，欢迎指教
'''

'''
代码运行结果：
运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
case通过率为40.00%
'''

n, k = [each for each in map(int, input().split())]

dp = [1] * k

for i in range(1, n):
    dp_ = []
    for j in range(1, k+1):
        temp = sum(dp) - sum([dp[x-1] for x in range(2*j, k+1, j)])
        dp_.append(temp)
    dp = dp_

print(sum(dp))
