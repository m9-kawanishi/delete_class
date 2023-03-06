import numpy as np
import os

###############################################################

# ディレクトリ設定
directory = "/content/a/"

# 削除するクラスID
delete_num = 8

################################################################



for file in os.listdir(directory):
    base, ext = os.path.splitext(file)
    # txtファイルだけ抽出
    if ext == '.txt':
        fileName = directory + file

    # ファイルオープン
    with open(fileName, encoding="cp932") as f:
        annotation = f.read().split( )  # 空白で分割しリストに保存

    # 数値に変換
    annotation = [float(num) for num in annotation]
    annotation = np.array(annotation).reshape(-1,5)
        
    for i in range(annotation.shape[0]):
        try:
          if np.count_nonzero(annotation[i][0] == delete_num) > 0:
              annotation = np.delete(annotation, i, 0)
        except:
          pass

    np.savetxt(fileName, annotation, fmt ='%.6f')

    with open(fileName, encoding="cp932") as f:
        annotation = f.read()

    # float -> int
    annotation = annotation.replace(".000000 ", " ")

    with open(fileName, mode="w", encoding="cp932") as f:
        f.write(annotation)

print("finish!")
