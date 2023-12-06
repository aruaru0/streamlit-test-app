import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import random
import time

st.write(
"""
# これはH1です
## これはH2です
### これはH3です

これは**本文**です。

* リスト１
* リスト２

1. リスト１
2. リスト２

|A|B|C|
|:-|:-|:-:|
|one|2|3|
|two|5|6|
|thres|10|-|
""")

st.write("## pandas")

df = pd.DataFrame({"x":[1,2,3], "y":['a','b','c']})
st.write(df)

edited_df = st.data_editor(df) # 👈 An editable dataframe


st.write("## matplotlib")

x = [i for i in range(100)]
y = [random.random() for _ in range(100)]
fig, ax = plt.subplots()
ax.plot(x, y)
st.write(fig)

st.write("## Text")

st.text("文字列です")

st.write("button")
click = st.button("Click")
if click :
    st.write("ボタンが押されました: click = ", click)

st.write("## slider")
val = st.slider("値を設定してください", min_value = 0, max_value = 100, value = 50, step = 2)
st.write(f"スライダーの値＝{val}")

st.write("## radio button")
sel = st.radio(
    "以下を選択してください", 
    ("Aを選択", "Bを選択", "Cを選択"),
    index = None,
)

if sel == None :
    st.write("**どれかを選択してください**")
elif sel == "Aを選択" :
    st.write(":rainbow[正解！]")
else : 
    st.write("不正解！")


st.write("## selectbox")
option = st.selectbox(
   "どれを選択しますか？",
   ("メール", "電話", "AIチャット"),
   index=None,
   placeholder="連絡手段を選んでください...",
)
st.write(f"選択は{option}ですね。")


st.write("## text input")
input = st.text_input(
    '意見を入力してください', 
    'サンプルの入力')
st.write(f"入力は「{input}」ですね")

input = st.text_input(
    '意見を入力してください', 
    placeholder = 'ここに入力')
st.write(f"入力は「{input}」ですね")

st.write("## text area")

txt = st.text_area(
    "感想をいれてください",
    "たのしめました。また、よろしくお願いします",)
st.write(f":red[入力は以下の通りです]")
st.write(txt)

txt = st.text_area(
    "感想をいれてください",
    placeholder = 'ここに入力')
st.write(f":red[入力は以下の通りです]")
st.write(txt)

st.write("## ダウンロード")

df = pd.DataFrame({"x":[1,2,3], "y":['a','b','c']})
st.write(df)
st.download_button(
    label="CSVファイルでダウンロード",
    data=df.to_csv().encode('utf-8'),
    file_name='df.csv',
    mime='text/csv',
)

uploaded_file = st.file_uploader("画像ファイルを選択してください", type=['png', 'jpg'])
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, uploaded_file.name)



## 同じものを配置する場合は、keyを設定しないとエラーになる。
## ウィジェットの一意のキーとして使用するオプションの文字列または整数。これを省略すると、ウィジェットのコンテンツに基づいてキーが生成されます。同じタイプの複数のウィジェットが同じキーを共有できない場合があります。
with st.sidebar :
    sel2 = st.selectbox(
        "どれを選択しますか？",
        ("メール", "電話", "AIチャット"),
        index=None,
        placeholder="連絡手段を選んでください...",
        key = "sel2"
    )


st.write("## spinner")

if st.button('処理を開始'):
    with st.spinner('処理中です...'):
        # ここに時間のかかる処理を書く
        time.sleep(2)
        st.write('終了しました')


    
st.write("## line chart")
x = [i for i in range(100)]
y = [random.random() for _ in range(100)]
df = pd.DataFrame({'x' : x , 'y' : y})
st.line_chart(df, x = 'x', y = 'y')

st.write("## scatter_chart")
x = [i for i in range(100)]
y = [random.random() for _ in range(100)]
df = pd.DataFrame({'x' : x , 'y' : y})
st.scatter_chart(df, x = 'x', y = 'y')

st.write("## bar_chart")
x = [i for i in range(100)]
y = [random.random() for _ in range(100)]
df = pd.DataFrame({'x' : x , 'y' : y})
st.bar_chart(df, x = 'x', y = 'y')


if "x" not in st.session_state :
    st.session_state.x = random.random()
st.write(f"xは{st.session_state.x}です")
