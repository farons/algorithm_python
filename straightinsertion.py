# encoding=utf-8
# 直接插入排序
__author__ = 'faron'


def straight_insertion(data_list):
    """
    实现直接插入排序
    """
    data = []
    if data_list:
        for m in range(0, data_list.__len__()):  # 逐个拿出，加入新的有序数组
            data.insert(0, data_list[m])
            k = 0
            if m == 0:
                continue
            for n in range(1, data.__len__()):
                if data[k] >= data[n]:
                    data[k], data[n] = data[n], data[k]
                    k = n
                else:
                    continue
        return data

if __name__ == '__main__':
    a = [3, 1, 5, 7, 2, 4, 9, 6]
    # a = [1]
    print(straight_insertion(a))
