# ----------------------------
# 092 ファイルの読み込み
# 読み込み方法が複数ある
# 一気に読み込む , 一行ずつ , ブロックごと

# f=TextIOWrapperクラスになりIOBASEのメソッドを使用する
# https://docs.python.org/ja/3/library/io.html?highlight=textiowrapper#i-o-base-classes

# ----------------------------

fileName = r"test.txt"

# 全文読み込む
with open(fileName, "r") as f:
    sentence = f.read()
    print(sentence)

# 一行ずつ読み込む
with open(fileName, "r") as f:
    while True:
        line = f.readline()
        # 文字をつなげて表示してみる。
        print(line, end="")
        if not line:
            break

# チャンク毎(ブロックごと)に読み込む
# プログラムのネットワークで使用
with open(fileName, "r") as f:
    while True:
        chunk = 2
        line = f.readline(chunk)

        print(line,end='')
        if not line:
            break
