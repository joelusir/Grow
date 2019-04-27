# -*- coding: utf-8 -*-

import timeit
import random
import copy


class Sort(object):
    """排序
        --内部排序
            --插入排序
                --直接插入排序
                --希尔排序
            --选择排序
                --简单选择排序
                --堆排序
            --交换排序
                --冒泡排序
                --快速排序
            --归并排序
            --基数排序
        --外部排序(使用内存和外部存储)
    """
    @staticmethod
    def bubble_sort(to_sort_datas):
        """
        :description:
        工作原理：比较相邻的元素,如果第一个比第二个大，就交换它们两个
        对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数

        时间复杂度: O(n^2)  范围：(O(n), O(n^2))
        空间复杂度：O(1)

        :param to_sort_datas: list, datas need to be sorted
        :return: None
        """
        for i in xrange(len(to_sort_datas)):
            for j in xrange(len(to_sort_datas)-1-i):
                if to_sort_datas[j] <= to_sort_datas[j+1]:
                    continue
                to_sort_datas[j], to_sort_datas[j+1] = to_sort_datas[j+1], to_sort_datas[j]

    @staticmethod
    def select_sort(to_sort_datas):
        """
        :description:
        工作原理：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，
        再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕

        时间复杂度： 最佳情况：T(n) = O(n2)  最差情况：T(n) = O(n2)  平均情况：T(n) = O(n2)
        空间复杂度：O(1)

        :param to_sort_datas: list, datas need to be sorted
        :return: None
        """
        for i in xrange(len(to_sort_datas)):
            min_index = i
            for j in xrange(i+1, len(to_sort_datas)):
                if to_sort_datas[min_index] <= to_sort_datas[j]:
                    continue
                min_index = j
            if not min_index == i:
                to_sort_datas[i], to_sort_datas[min_index] = to_sort_datas[min_index], to_sort_datas[i]

    @staticmethod
    def insert_sort(to_sort_datas):
        """
        :description:
        工作原理：通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入

        时间复杂度： 最佳情况：T(n) = O(n)   最坏情况：T(n) = O(n2)   平均情况：T(n) = O(n2)
        空间复杂度： O(1)

        :param to_sort_datas: list, datas need to be sorted
        :return: None
        """
        for i in xrange(len(to_sort_datas)):
            temp_data = to_sort_datas[i]
            swap_index = 0
            for j in xrange(i-1, -1, -1):
                if temp_data < to_sort_datas[j]:
                    to_sort_datas[j+1] = to_sort_datas[j]
                else:
                    swap_index = j + 1
                    break
            to_sort_datas[swap_index] = temp_data

    @staticmethod
    def shell_sort(to_sort_datas):
        """
        :description:
        工作原理：缩小增量排序，对数据列表进行分组（分组数目为len/2），对各个分组进行插入排序，排序完成后进行
        分组，分组数以2指数递减，再对各个分组进行插入排序，直到分组数为1并完成插入排序为止

        时间复杂度：最佳情况：T(n) = O(nlog2 n)  最坏情况：T(n) = O(nlog2 n)  平均情况：T(n) =O(nlog2n)　
        空间复杂度： O(1)

        :param to_sort_datas: list, datas need to be sorted
        :return: None
        """
        group_num = len(to_sort_datas) / 2
        while group_num >= 1:
            for i in xrange(group_num, len(to_sort_datas)):
                temp_data = to_sort_datas[i]
                swap_index = 0
                # 对分组内的数据进行插入排序
                for j in xrange(i - group_num, -1, -group_num):
                    if temp_data < to_sort_datas[j]:
                        to_sort_datas[j + group_num] = to_sort_datas[j]
                    else:
                        swap_index = j + group_num
                        break
                to_sort_datas[swap_index] = temp_data
            group_num /= 2

    @staticmethod
    def merge_sort(to_sort_datas):
        """
        :description:
        工作原理：使用分治法, 对列表不断进行二分，并对每个分组排序重组, 最后合为一体

        时间复杂度：最佳情况：T(n) = O(n)  最差情况：T(n) = O(nlogn)  平均情况：T(n) = O(nlogn)
        空间复杂度： O(n)   需要额外的内存用于排序重组使用

        :param to_sort_datas: list
        :return: list, sorted list from to_sort_datas
        """
        if len(to_sort_datas) < 2:
            return to_sort_datas
        middle_index = len(to_sort_datas)/2
        left_datas = Sort.merge_sort(to_sort_datas[:middle_index])
        right_datas = Sort.merge_sort(to_sort_datas[middle_index:])
        return Sort._merge(left_datas, right_datas)

    @staticmethod
    def _merge(left, right):
        """
        :description: combine and sort two list

        :param left: list
        :param right: list
        :return: list, sorted list from list left and list right
        """
        temp_datas = []
        nleft = nright = 0
        while nleft < len(left) and nright < len(right):
            if left[nleft] >= right[nright]:
                temp_datas.append(right[nright])
                nright += 1
            else:
                temp_datas.append(left[nleft])
                nleft += 1

        # 一个分组数据全部比较完后，依次添加另外一个列表的所有数据
        if nleft == len(left):
            [temp_datas.append(x) for x in right[nright:]]
        else:
            [temp_datas.append(x) for x in left[nleft:]]

        return temp_datas

    @staticmethod
    def quick_sort(to_sort_datas, begin_index, end_index):
        if begin_index >= end_index:
            return
        sep_index = Sort.partition(to_sort_datas, begin_index, end_index)
        # print "to_sort_datas : ", to_sort_datas
        # print "sep_index: ", sep_index
        Sort.quick_sort(to_sort_datas, begin_index, sep_index)
        Sort.quick_sort(to_sort_datas, sep_index+1, end_index)

    @staticmethod
    def partition(to_sort_datas, begin_index, end_index):
        # print "begin_index : ", begin_index
        # print "end_index : ", end_index
        ref_index = end_index  # random.randint(begin_index, end_index)
        swap_index = begin_index - 1
        for i in xrange(begin_index, end_index):
            if to_sort_datas[i] <= to_sort_datas[ref_index]:
                swap_index += 1
                to_sort_datas[i], to_sort_datas[swap_index] = to_sort_datas[swap_index], to_sort_datas[i]
        to_sort_datas[swap_index+1], to_sort_datas[ref_index] = to_sort_datas[ref_index], to_sort_datas[swap_index+1]

        return swap_index


def check_timeit(test_func):
    print(timeit.timeit(stmt=test_func, setup="from __main__ import Sort, datas, to_sort_datas", number=10000))


def datas_generator(nmin, nmax, ncount):
    while ncount > 0:
        yield random.randint(nmin, nmax)
        ncount -= 1

if __name__ == "__main__":
    datas = [x for x in datas_generator(0, 10000, 1000)]
    test_funcs = ["Sort.bubble_sort(to_sort_datas)",
                  "Sort.select_sort(to_sort_datas)",
                  "Sort.insert_sort(to_sort_datas)",
                  "Sort.shell_sort(to_sort_datas)",
                  "Sort.merge_sort(to_sort_datas)",
                  "Sort.quick_sort(to_sort_datas, 0, len(to_sort_datas)-1)"]

    for test_func in test_funcs:
        to_sort_datas = copy.deepcopy(datas)
        print("Cost time of %s:" % test_func)
        check_timeit(test_func)
    # datas = [3, 2, 1, 4, 6, 5, 7, 10, 8, 11, 9, 16, 111, 110]
    # Sort.quick_sort(datas, 0, len(datas)-1)
    # print datas
    # print("bubble_sort: ")
    # check_timeit("Sort.bubble_sort(datas)")
    # print("select_sort: ")
    # check_timeit("Sort.select_sort(datas)")
    # print("insert_sort: ")
    # check_timeit("Sort.insert_sort(datas)")
    # print("shell_sort: ")
    # check_timeit("Sort.shell_sort(datas)")
    # print("merge_sort: ")
    # check_timeit("Sort.merge_sort(datas)")
    # print("quick_sort: ")
    # check_timeit("Sort.quick_sort(datas, 0, len(datas)-1)")
    check_timeit("datas.sort()")
