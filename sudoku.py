 _*_ coding = utf-8 _*_

def gather_col_row(row, col, sudoku):
    """收集二维数组sudoku(mxm)中元素(row, col)所在行的元素至rows中，所在列的元素至cols中"""
    rows = []
    cols = []
    m    = len(sudoku)
    for i in range(m):
        rows.append(sudoku[row][i])
        cols.append(sudoku[i][col])
    return rows, cols

def gather_block(row, col, sudoku):
    """收集二维数组sudoku(mxm)中元素(row, col)所在的宫中的元素的列表"""
    blocks = []
    i = row // 3
    j = col // 3
    for k in range(i*3, (i+1)*3):
        blocks += sudoku[k][j*3 : (j+1)*3]
    return blocks

def position(sudoku):
    """返回sudoku中0所在的位置(row, col),即没有数的位置的列表，如[(2,3),(0,8)]"""
    return [(row, col) for row in range(9) for col in range(9) if sudoku[row][col] == 0]

def possible_dict(sudoku):
    """以字典形式返回sudoku中所有0元素位置中可能放置的数字，键为(row,col)对，值为可能数的集合，如{(2, 3):{2,4,5}}"""
    digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    ans = {}
    for pos in position(sudoku):
        row, col = pos
        rows, cols = gather_col_row(row, col, sudoku)
        blocks = gather_block(row, col, sudoku)
        possible   = digits - set(rows) - set(cols) - set(blocks)
        ans[pos] = possible
    return ans

def possible_set(row, col, sudoku):
    """以集合形式返回sudoku中(row, col)元素中可能放置的数字，如{2,4,5}"""
    digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    rows, cols = gather_col_row(row, col, sudoku)
    blocks = gather_block(row, col, sudoku)
    possible_num   = digits - set(rows) - set(cols) - set(blocks)
    return possible_num

def by_row_col(seq, row_or_col):
    """按行或按列收集序列seq中的元素,row_or_col=0,按行，1，按列,用于解法二"""
    row = list(set([i[row_or_col] for i in seq]))
    ans = []
    for r in row:
        tmp = []
        for s in seq:
            if s[row_or_col] == r:
                tmp.append(s)
        ans.append(tmp)
    return ans

def solve1(sudoku):
    # 解法一：元素所在位置的行、列及块的交集中只有一个数的情况，也是最简单的情况
    update = True
    while update:
        update = False
        for k, v in possible_dict(sudoku).items():
            if len(v) == 1:
                sudoku[k[0]][k[1]] = list(v)[0]
                update = True
    return None

def unique(seq):
    # 返回系列seq中只出现一次的数字和它的位置
    # seq形如[((2,6),{9,5,6}),((2,7),{9,6}),((row,col),{possible_number})]
    numbers = []
    unique_num = []
    for a in seq:
       for i in a[1]:
           numbers.append(i)
    for num in numbers:
       if numbers.count(num) == 1:
           unique_num.append(num)
    position = []
    for unum in  unique_num:
        for a in seq:
            if unum in a[1]:
                position.append(a[0])
    return position, unique_num

def solve2(sudoku):
    # 解法二：分别按照行、按列、按块，如果某个数仅出现一次，则该位置为该数
    # 如(8,8):{8,9,2,7},(8,7):{8,9,2},(8,5):{8,2},(8,1):{8,9,2},则(8,8):{7}
    update = True
    while update:
        update = False
        pos = position(sudoku)
        possible = possible_dict(sudoku)
        # 按行
        rows = by_row_col(pos, 0)
        for row in rows:
            pos_num = unique([(p, possible[p]) for p in row])
            if pos_num[0]:
                for i in range(0, len(pos_num), 2):   # pos_num中可能返回的数不止一个
                    sudoku[pos_num[i][0][0]][pos_num[i][0][1]] = pos_num[i+1][0]
                    update = True
        # 按列
        cols = by_row_col(pos, 1)
        for col in cols:
            pos_num = unique([(p, possible[p]) for p in col])
            if pos_num[0]:
                for i in range(0, len(pos_num), 2):   # pos_num中可能返回的数不止一个
                    sudoku[pos_num[i][0][0]][pos_num[i][0][1]] = pos_num[i+1][0]
                    update = True
        solve1(sudoku)
    return None

if __name__ == "__main__":
    """sudoku = [[0, 0, 2, 0, 4, 0, 8, 0, 0],
              [9, 5, 0, 0, 0, 0, 0, 4, 1],
              [0, 0, 0, 2, 0, 3, 0, 0, 0],
              [0, 6, 0, 9, 0, 5, 0, 1, 0],
              [7, 0, 0, 0, 0, 0, 0, 0, 4],
              [0, 3, 0, 6, 0, 4, 0, 5, 0],
              [0, 0, 0, 7, 0, 6, 0, 0, 0],
              [4, 7, 0, 0, 0, 0, 0, 3, 5],
              [0, 0, 6, 0, 3, 0, 1, 0, 0]]"""
    sudokus = []
    difficulty = []
    f = open('sudoku.txt', 'r')
    for line in f.readlines():
        line = line.strip()
        if line.startswith('#'):
            difficulty.append(line[1:])
        else:
            numbers = line.split(',')
            sudoku = []
            for number in numbers:
                tmp = []
                for num in number:
                    tmp.append(int(num))
                sudoku.append(tmp)
            sudokus.append(sudoku)
    f.close()
    cnt = 0
    for sudoku in sudokus:
        print(difficulty[cnt//3])
        sdk = sudoku[:]
        solve1(sudoku)
        solve2(sudoku)
        for i in range(9):
            print(sudoku[i], "\t", sdk[i])
        cnt += 1
        input()
