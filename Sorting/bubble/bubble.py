# coding=utf-8
"""
实践了冒泡排序
"""
__author__ = 'yanzhilong'


def bubble(data):
    """
    data: 包含数据的数组类型
    """
    if isinstance(data, list) and len(data) > 0:
        length = len(data)
        while length >= 2:
            for i in range(0, length-1):
                if data[i] <= data[i+1]:
                    data[i], data[i+1] = data[i+1], data[i]
            length += -1
        return data
    else:
        return

if __name__ == '__main__':
    data = [2, 3, 1, 4, 2, 5]
    bubble(data)
    print(data)
