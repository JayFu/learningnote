# 将两个链表相加，得到一个链表，进位在下一个结点+1
# 链表的每个结点包含一个数字

# 输入: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
        # """

class ListNode(object):      
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

p = l1
q = l2
OutputNodeList = ListNode(0)
carry = 0

lenA = 1
lenB = 1
while l1.next is not None:
    lenA = lenA + 1
    l1 = l1.next

while l2.next is not None:
    lenB = lenB + 1
    l2 = l2.next

llen = max(lenA, lenB)

print(llen)
# while p.next and q.next is not None:
# 报错"'NoneType' object has no attribute 'val'"
# 可能存在数据越界
# 原因是and和is not的优先级没有按照顺序

# OutputNodeList必须被从头到尾初始化
# 可以考虑从l1和l2中选择长的那个进行深复制
# 复制之后从第一个结点开始初始化为0，再加一个val为0的结点
# 对这个初始化之后的链表进行每个结点的数值操作

while (p is not None) and (q is not None):
    OutputNodeList.val = p.val + q.val + carry
    if OutputNodeList.val >= 10:
        carry = 1
        OutputNodeList.val = OutputNodeList.val - 10
    else:
        carry = 0
    p = p.next
    q = q.next
    OutputNodeList = OutputNodeList.next

if p.next is not None:
    while p.next is not None:
        OutputNodeList.val = p.val + carry
        if OutputNodeList.val >= 10:
            carry = 1
            OutputNodeList.val = OutputNodeList.val - 10
        else:
            carry = 0
        p = p.next
        OutputNodeList = OutputNodeList.next
elif q.next is not None:
     while q.next is not None:
        OutputNodeList.val = q.val + carry
        if OutputNodeList.val >= 10:
            carry = 1
            OutputNodeList.val = OutputNodeList.val - 10
        else:
            carry = 0
        q = q.next 
        OutputNodeList = OutputNodeList.next
elif carry is not None: OutputNodeList.val = carry
else: pass

return OutputNodeList



def 