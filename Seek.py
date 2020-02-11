# ----------------------------
# 093 seekを使って移動する
# ----------------------------
# test.txt
# [A][A][A][\n]
# [B][B][B][\n]
# [C][C][C][\n]
# [D][D][D][\n]
# [E][E][E][\n]

filename = r'test.txt'
with open(filename, "r") as f:
    # 現在の位置
    currentLocation = f.tell()
    print(currentLocation)

    # 指定の文字を読み込む
    char = f.read(1)
    print(char)

    # 移動
    f.seek(5)
    chars = f.read(2)
    print(chars)

    # 指定位置が大きい場合はどうなるのか→""が返ってくる
    f.seek(100)
    currentLocation = f.tell()
    print(currentLocation)
    char = f.read(currentLocation)
    print(char)
