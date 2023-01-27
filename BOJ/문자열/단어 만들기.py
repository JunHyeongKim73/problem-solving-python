import sys
input = sys.stdin.readline

dict = []
while True:
    word = input().rstrip()
    if word == '-':
        break
    dict.append(word)


def is_possible(word, puzzle):
    nums = {}
    for alpha in puzzle:
        if alpha in nums:
            nums[alpha] += 1
        else:
            nums[alpha] = 1

    for alpha in word:
        if alpha not in nums:
            return False
        if nums[alpha] == 0:
            return False
        nums[alpha] -= 1

    return True


while True:
    puzzle = input().rstrip()
    if puzzle == '#':
        break

    alpha_set = set(puzzle)
    res = {}
    for alpha in alpha_set:
        res[alpha] = 0

    for word in dict:
        if not is_possible(word, puzzle):
            continue
        for alpha in alpha_set:
            if alpha in word:
                res[alpha] += 1

    lists = [(alpha, res[alpha]) for alpha in res]
    lists.sort()

    max_num = -1
    min_num = 1e9
    for alpha, num in lists:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    min_strs = ''
    max_str = ''
    for alpha, num in lists:
        if num == min_num:
            min_strs += alpha
        if num == max_num:
            max_str += alpha

    print(min_strs, min_num, max_str, max_num)
