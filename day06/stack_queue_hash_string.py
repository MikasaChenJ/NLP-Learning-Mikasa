# ===== LeetCode 20: 有效的括号 =====
def is_valid_parentheses(s):
    """
    栈结构，检查括号是否匹配
    """
    # 新建一个空栈
    stack=[]
    # 建立左右括号映射关系
    mapping={'{':'}','(':')','[':']'}
    # 遍历输入字符串次数
    for char in s:
        # 判断输入字符串是否有左括号
        if char in mapping.keys():
            # 左括号入栈
            stack.append(s)
        # 如何栈不空 或者 栈顶的左括号和右括号不匹配 返回False
        elif not stack or stack[-1]!=mapping[char]:
            return False
        else: return False
    return not stack




# ===== LeetCode 1: 两数之和 =====
# 输入：nums = [2, 7, 11, 15], target = 9
# 输出：[0, 1]
def two_sum(nums, target):
    """
    哈希表，一遍遍历找到目标和
    """
    hashmap={}
    for i in range(len(nums)):
        num=target-nums[i]
        if num in hashmap:
            return [hashmap[num],i]

        else: hashmap[nums[i]]=i

    return[]


# ===== LeetCode 232: 用栈实现队列 =====
class MyQueue:
    """
    使用两个栈实现队列结构
    """
    def __init__(self):
        self._in_stack=[]
        self._out_stack=[]
        pass

    def push(self, x):
        self._in_stack.append(x)

    def pop(self):
        if not self._out_stack:
            while self._in_stack:
                self._out_stack.append(self._in_stack.pop())
            return self._out_stack.pop()


    def peek(self):
        if not self._out_stack:
            while self._in_stack:
                self._out_stack.append(self._in_stack.pop())
        return self._out_stack[-1]

    def empty(self):
        return not self._in_stack and not self._out_stack


# ===== LeetCode 49: 字母异位词分组 =====
def group_anagrams(strs):
    """
    哈希 + 排序，分组字母异位词
    """



# ===== LeetCode 239: 滑动窗口最大值 =====
from collections import deque

def max_sliding_window(nums, k):
    """
    双端队列维护窗口最大值
    """
    pass
