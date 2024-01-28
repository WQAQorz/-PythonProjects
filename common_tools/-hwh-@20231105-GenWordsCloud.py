import wordcloud
import os
import jieba
import matplotlib.pyplot as plt

target_file = os.path.join(os.getcwd(), "words.csv")
text = ""
if os.path.isfile(target_file):
    with open(target_file, encoding="utf-8") as f:
        text = f.read()

if text:
    words_list = jieba.lcut(text)
    my_dict = {}  # 这里建一个列表用于记录列表中的所有唯一值出现的次数
    for key in words_list:
        key = key.replace("\n", "")
        if not key:
            continue

        # 增加筛选条件
        exclude_words = ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
        if key in exclude_words:
            continue

        if len(key) < 3:
            continue

        my_dict[key] = my_dict.get(key, 0) + 1

    font_path = r'D:\Windows\Fonts\simhei.ttf'

    wordcloud = wordcloud.WordCloud(
        width=800,
        height=400,
        background_color="white",  # 设置词云背景颜色为白色
        font_path=font_path,  # 设置词云中的字体样式
        colormap='viridis',  # 设置词云颜色方案为viridis
        max_words=1000,  # 词云中显示的最大词语数量
        max_font_size=500,  # 设置词云中的最大词语字体大小为500
        scale=10,  # 控制词云图像的清晰度，值越大越清晰
        collocations=True,  # 启用词语组合，使词云中的词语能够形成搭配
        prefer_horizontal=0.7  # 控制词云中横排文字的比例，值越大横排文字越多
    ).fit_words(my_dict)

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

    temp_text = ""
    with open("words.csv", "w", encoding="utf-8") as f:
        for key in my_dict.keys():
            temp_text += key + "," + str(my_dict[key]) + "\n"
        f.write(temp_text)
