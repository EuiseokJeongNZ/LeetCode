import sys

def merge_sort(lst):
    if len(lst) > 1:
        left_lst = lst[:len(lst) // 2]
        right_lst = lst[len(lst) // 2:]

        merge_sort(left_lst)
        merge_sort(right_lst)

        i = j = k = 0
        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] < right_lst[j]:
                lst[k] = left_lst[i]
                i += 1
            else:
                lst[k] = right_lst[j]
                j += 1
            k += 1

            while i < len(left_lst):
                lst[k] = left_lst[i]
                i += 1
                k += 1
            while j < len(right_lst):
                lst[k] = right_lst[j]
                j += 1
                k += 1

if __name__ =='__main__':
    lst = list(map(int, sys.stdin.readline().split()))

    merge_sort(lst)

    print(lst)