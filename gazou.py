from PIL import Image
import matplotlib.pyplot as plt

file_name = input('読み込むファイル名を入力してください：')
beautiful_view = Image.open(file_name)
plt.imshow(beautiful_view)
small_beautiful_view = beautiful_view.resize((1800, 2340))
plt.imshow(small_beautiful_view)
name = input("ファイル名を入力してください：")
small_beautiful_view.save(name)
