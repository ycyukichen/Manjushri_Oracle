import streamlit as st
import random
import json
from PIL import Image

# Load the cards
with open('cards.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

# Streamlit page setting
st.set_page_config(page_title="文殊卦占卜", layout="centered")

st.markdown("<h1 style='text-align: center;'>文殊卦占卜</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>源自文殊師利菩薩占卜牌卡，提供靈性指引，占卜結果僅供參考</h6>", unsafe_allow_html=True)

image = Image.open('Ｍanjushri.jpeg') 
st.image(image, use_column_width=True)

st.write("**占卜規則:** ")
st.write("每次占卜僅問一個問題。對於重大問題，可進行覆卦，即重覆同一問題占卜。")
st.write(" ")
st.write("**占卜注意事項:**")
st.write("占卜時須保持心平氣和，且不要預設答案。")
st.write("再占時，最好先休息，唸誦文殊師利菩薩真言，平復情緒後再問。")
st.write("不可抱怨或報復心占卜，須知一切皆因業力而起，無論吉凶，應心平氣和應對。")
st.write(" ")
# Aspects
aspects = ["家宅", "事業", "謀望", "人事", "仇怨", "行人", "疾病", "魔祟", "失物", "請託", "婚姻", "其他"]
selected_aspects = st.selectbox("**選擇您想詢問的主題，靜心想著問題，然後按下開始占卜。**", list(aspects))

# Botton
if st.button("開始占卜"):
    selected_card = random.choice(cards)
    st.subheader(f"您抽到的卦是：{selected_card['卦象名']} - {selected_card['name']} ")
    
    # 顯示卦象
    st.write("### 卦象")
    for line in selected_card['卦象']:
        st.write(line)

    # 顯示訊號及解釋
    st.write("### 訊號")
    st.write(f"**訊號**:{selected_card['訊號']}")
    st.write("### 訊號解釋")
    for line in selected_card['訊號解釋']:
        st.write(line)

    # 顯示占斷解釋
    st.write("### 占斷")
    interpretations = selected_card['占断']
    
    
    # 僅顯示所詢問面向的解釋
    for aspect, explanation in interpretations.items():
        if aspect in selected_aspects:
            st.write(f"**{aspect}**:")
            if isinstance(explanation, list):  # 多行內容的處理
                for line in explanation:
                    st.write(line)
            else:
                st.write(explanation)

    # 顯示總體建議
    st.write("### 總體建議")
    overall_advice = selected_card['總體建議']
    for advice in overall_advice:
        st.write(advice)

# 各項占卜主題範圍及占卜法則說明

st.write("**各項占卜主題簡易判斷:**")
st.write("**家宅:** 包括家庭運勢、家族產業變動、人口平安等，尤其針對占問者自身的安危。有時也包括家庭成員的增減情況。")
st.write("**事業:** 指個人財富的增減和生意興衰。此類占卜僅做一般性指示。若有特定目的（如某筆交易是否成功），應參考「謀望」或「請託」條的指引。")
st.write("**謀望:** 關於事業和目標達成，例如所問之事是否順利、考試錄取等，判斷能否如願。")
st.write("**人事:** 主要涉及事業和財富方面的人際關係。若是其他人事問題，應參考「請託」條的說明。")
st.write("**仇怨:** 占問可能出現的敵人，包括官非及是非糾紛等。")
st.write("**行人:** 占問他人安危，或詢問何時能歸來等。")
st.write("**疾病:** 針對健康情況的占卜。最好是當事人自己占問，或直系親屬代問，準確性較高。若疾病較重，應由病患親屬占問。")
st.write("**魔祟:** 與宗教信仰相關，當遇到不順或長期病痛時占問，判斷是否有鬼神干擾。包括居住或辦公場所風水的影響。但若占問其他問題時，不宜受此條影響，以免誤判。")
st.write("**失物:** 詢問失物是否能找回，以及所在方位。")
st.write("**請託:** 占問洽談事項是否順利，或他人是否支持自己。")
st.write("**婚姻:** 包括已婚者的婚姻狀況及未婚者的婚姻願望。")
st.write("**其他:** 對未在上述範疇內的問題，進行一般性推測。")
