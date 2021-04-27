from _collections import defaultdict
import numpy as np

same_arrays = defaultdict(list)
modified_logos = defaultdict(list)


def engrave(logos, logo):
    # engrave fnc
    directions = logos[logo][0]
    (x, y) = logos[logo][1]
    list_of_directions = list(directions)

    (rows, cols) = (21, 21)
    arr = [[' ' for i in range(rows)] for j in range(cols)]
    for i in range(11):
        for j in range(11):
            arr[2 * i][2 * j] = '.'

    for d in list_of_directions:
        if d == 'D':
            arr[x + 1][y] = '|'
            (x, y) = (x + 2, y)
        if d == 'U':
            arr[x - 1][y] = '|'
            (x, y) = (x - 2, y)
        if d == 'L':
            arr[x][y - 1] = '-'
            (x, y) = (x, y - 2)
        if d == 'R':
            arr[x][y + 1] = '-'
            (x, y) = (x, y + 2)

    logos[logo].append(arr)
    for r in arr:
        for c in r:
            print(c, end='')
        print()


def modify(logos, logo, x, y):
    directions = logos[logo][0]
    list_of_directions = list(directions)

    (rows, cols) = (21, 21)
    arr = [[' ' for i in range(rows)] for j in range(cols)]
    for i in range(11):
        for j in range(11):
            arr[2 * i][2 * j] = '.'

    for d in list_of_directions:
        if d == 'D':
            arr[x + 1][y] = '|'
            (x, y) = (x + 2, y)
        if d == 'U':
            arr[x - 1][y] = '|'
            (x, y) = (x - 2, y)
        if d == 'L':
            arr[x][y - 1] = '-'
            (x, y) = (x, y - 2)
        if d == 'R':
            arr[x][y + 1] = '-'
            (x, y) = (x, y + 2)

    modified_logos[logo].append(arr)
    # print("modified array is :")
    # for r in arr:
    #     for c in r:
    #         print(c, end='')
    #     print()


def canonicalize(modified_arr, logoname):
    arr_can = np.empty(441, dtype=int)
    d = 0
    for row in range(len(modified_arr)):
        for col in range(len(modified_arr)):
            if modified_arr[row][col] == '|':
                arr_can[d] = 0
            elif modified_arr[row][col] == '-':
                arr_can[d] = 0
            else:
                arr_can[d] = 1
            d += 1
    same_arrays[logoname].append(arr_can)
    # print("canonicalized array is: ", arr_can)


def compare(arr1, arr2):
    x1 = 0
    x2 = 0
    num_of_zero1 = 0
    num_of_zero2 = 0
    last_zero1 = 0
    last_zero2 = 0
    indicator1 = -1
    indicator2 = -1
    comparison = []
    for i in range(len(arr1)):
        if arr1[i] == 0:
            if indicator1 == -1:
                x1 = i
                indicator1 = 1
            num_of_zero1 += 1
            last_zero1 = i
    # print("x1 is: ", x1)
    # print("num_of_zero1 is ", num_of_zero1)
    # print("last zero 1 is ", last_zero1)
    for j in range(len(arr2)):
        if arr2[j] == 0:
            if indicator2 == -1:
                x2 = j
                indicator2 = 1
            num_of_zero2 += 1
            last_zero2 = j
    # print("x2 is: ", x2)
    # print("num_of_zero2 is ", num_of_zero2)
    # print("last zero 2 is ", last_zero2)
    copy_arr1 = np.empty(last_zero1 - x1 + 1, dtype=int)
    count = 0
    for i in range(x1, last_zero1 + 1):
        copy_arr1[count] = arr1[i]
        count += 1
    for k in range(x1, last_zero1 + 1):
        for t in range(x2, last_zero2 + 1):
            if arr1[k] == arr2[t]:
                comparison.append(arr2[k])

    comparison = np.array(comparison)

    # print("comparison array is ", comparison)
    # print("copy array is ", copy_arr1)
    if np.array_equal(copy_arr1, comparison):
        return True
    elif num_of_zero1 == num_of_zero2:
        return True
    else:
        return False


def main():
    logos = defaultdict(list)

    while 1:
        input_txt = input()
        input_list = input_txt.split()
        logo = input_list[1]

        if input_list[0] == 'LOGO':
            directions = input_list[2]
            logos[logo].append(directions)
            print(logo, "defined")
        elif input_list[0] == 'ENGRAVE':
            x = int(input_list[2])
            y = int(input_list[3])
            if logo in logos:
                logos[logo].append((2 * x - 2, 2 * y - 2))
                engrave(logos, logo)
            else:
                print("A logo with name '", logo, "' does not exist.")
                break
        elif input_list[0] == 'SAME':
            i = 1
            while i < len(input_list):
                if input_list[i] not in modified_logos:
                    modify(logos, input_list[i], 10, 10)
                i += 1
            count = 1
            # print("modified_logos dict is : ",modified_logos)
            while count < len(input_list):
                if input_list[count] not in same_arrays:
                    canonicalize(modified_logos[input_list[count]][0], input_list[count])
                count += 1
            comparison_arr1 = same_arrays[input_list[1]][0]
            comparison_arr2 = same_arrays[input_list[2]][0]
            result = compare(comparison_arr1, comparison_arr2)
            if result:
                print("Yes")
            else:
                print("No")
        # print("logos dict is:", logos)


if __name__ == '__main__':
    main()
