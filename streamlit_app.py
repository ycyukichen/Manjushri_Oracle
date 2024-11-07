import streamlit as st
import random
import json

# Load the cards
with open('cards.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

# Streamlit page setting
st.set_page_config(page_title="文殊卦占卜", layout="centered")

st.title("文殊卦占卜")
st.write("點擊下方按鈕開始占卜。")


# Aspects
aspects = ["家宅", "事業", "謀望", "人事", "仇怨", "行人", "疾病", "魔祟", "失物", "請託", "婚姻", "其他"]
selected_aspects = st.selectbox("選擇您想詢問的主題", list(aspects))

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
    st.write(f"**訊號**：{selected_card['訊號']}")
    st.write("### 訊號解釋")
    for line in selected_card['訊號解釋']:
        st.write(line)

    # 顯示占斷解釋
    st.write("### 占斷")
    interpretations = selected_card['占断']
    
    
    # 僅顯示所詢問面向的解釋
    for aspect, explanation in interpretations.items():
        if aspect in selected_aspects:
            st.write(f"**{aspect}**：")
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
