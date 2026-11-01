import streamlit as st

st.set_page_config(
    page_title="PLC Doctor",
    page_icon="⚡"
)

st.title("⚡ PLC Doctor")
st.subheader("AI智能PLC故障诊断助手")

st.write("欢迎使用 PLC Doctor！")

model = st.selectbox(
    "请选择PLC型号",
    ["三菱 FX3U", "三菱 FX5U"]
)

fault = st.text_area(
    "请描述你的故障",
    placeholder="例如：PLC运行正常，但是Y0没有输出"
)

if st.button("开始诊断"):
    if fault.strip():
        st.success("故障信息已提交！")
        st.write("PLC型号：", model)
        st.write("故障描述：", fault)
    else:
        st.warning("请先输入故障现象")

st.caption("PLC Doctor © 2026")
