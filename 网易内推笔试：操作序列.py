'''
[编程题] 操作序列
时间限制：2秒
空间限制：32768K
小易有一个长度为n的整数序列,a_1,...,a_n。然后考虑在一个空序列b上进行n次以下操作:
1、将a_i放入b序列的末尾
2、逆置b序列
小易需要你计算输出操作n次之后的b序列。 
输入描述:
输入包括两行,第一行包括一个整数n(2 ≤ n ≤ 2*10^5),即序列的长度。
第二行包括n个整数a_i(1 ≤ a_i ≤ 10^9),即序列a中的每个整数,以空格分割。


输出描述:
在一行中输出操作n次之后的b序列,以空格分割,行末无空格。

输入例子1:
4
1 2 3 4

输出例子1:
4 2 1 3
'''

'''
解题思路：找规律
  这题如果老老实实直接按照题目给定的操作操作序列必定导致超时，需要自己找规律
  找到规律后用条件结构实现即可（操作列表时不要用insert，复杂度太高，用append）
  我找到的规律是从原序列的最后一个元素append到输出序列，然后从最后一个开始隔一个元素append一次
  逆向遍历完原序列反向隔继续遍历，遍历一个元素便把它append到新序列中
  例如 1 2 3 4 5 的规律为
  5， 5 3， 5 3 1， 5 3 1 2， 5 3 1 2 3
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

n = int(input())
a_sequence = [i for i in input().split()]

b_sequence = []
count = n - 1
for i in range(n):
    if count >= 0:
        if count % 2 == (n - 1) % 2:
            b_sequence.append(a_sequence[count])
            count -= 2
        else:
            count += 2
            b_sequence.append(a_sequence[count])
    elif (n-1) % 2 == 1:
        count = 0
        b_sequence.append(a_sequence[count])
    else:
        count = 1
        b_sequence.append(a_sequence[count])

print(' '.join(b_sequence))
