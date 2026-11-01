import streamlit as st

# =========================
# 页面配置
# =========================

st.set_page_config(
    page_title="PLC Doctor",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CSS 页面设计
# =========================

st.markdown("""
<style>

/* 全局背景 */
.stApp {
    background: #090b10;
    color: #f5f5f5;
}

/* 隐藏默认菜单 */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* 主内容区域 */
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* 侧边栏 */
section[data-testid="stSidebar"] {
    background: #10131b;
    border-right: 1px solid #242936;
}

/* 标题 */
.main-title {
    font-size: 42px;
    font-weight: 800;
    letter-spacing: -1px;
    color: #ffffff;
    text-align: center;
    margin-top: 55px;
}

.subtitle {
    color: #858b9b;
    text-align: center;
    font-size: 16px;
    margin-bottom: 40px;
}

/* 品牌 */
.brand {
    font-size: 25px;
    font-weight: 800;
    color: #ffffff;
    padding: 15px 0;
}

.brand span {
    color: #648cff;
}

/* 卡片 */
.feature-card {
    background: #141925;
    border: 1px solid #262e40;
    border-radius: 15px;
    padding: 20px;
    min-height: 120px;
    margin-bottom: 12px;
}

.feature-card h3 {
    color: #ffffff;
    font-size: 17px;
}

.feature-card p {
    color: #9299aa;
    font-size: 13px;
}

/* 输入框 */
.stTextArea textarea {
    background: #151a25 !important;
    color: white !important;
    border: 1px solid #30394c !important;
    border-radius: 14px !important;
}

/* 下拉框 */
.stSelectbox div[data-baseweb="select"] > div {
    background: #151a25;
    border-color: #30394c;
    color: white;
}

/* 按钮 */
.stButton button {
    background: linear-gradient(90deg, #3867ff, #7555ff);
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    min-height: 45px;
    width: 100%;
}

.stButton button:hover {
    border: 1px solid #8ca5ff;
    color: white;
}

/* 分割线 */
hr {
    border-color: #252b38;
}

/* 响应式 */
@media (max-width: 768px) {
    .main-title {
        font-size: 30px;
        margin-top: 25px;
    }

    .subtitle {
        font-size: 14px;
    }

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================
# 左侧导航栏
# =========================

with st.sidebar:

    st.markdown(
        '<div class="brand">⚡ PLC <span>DOCTOR</span></div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    page = st.radio(
        "导航菜单",
        [
            "🏠 首页",
            "🔧 故障诊断",
            "📚 PLC知识库",
            "🕘 历史记录"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown("### 系统状态")

    st.markdown("🟢 网站运行正常")

    st.markdown("⚪ AI引擎：尚未接入")

    st.markdown("---")

    st.caption("PLC Doctor © 2026")
    st.caption("AI Industrial Assistant")


# =========================
# 首页
# =========================

if page == "🏠 首页":

    st.markdown(
        '<div class="main-title">让 PLC 故障诊断更简单</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">你的智能工业自动化故障诊断助手</div>',
        unsafe_allow_html=True
    )

    st.markdown("### ⚡ 你今天遇到了什么问题？")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="feature-card">
        <h3>⚡ PLC 无输出</h3>
        <p>排查输出点、程序逻辑及外部接线问题</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
        <h3>🔌 PLC 无法启动</h3>
        <p>分析电源、运行状态及硬件异常</p>
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        <div class="feature-card">
        <h3>📡 通信异常</h3>
        <p>检查通信参数、线路及设备连接</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="feature-card">
        <h3>🛠 程序运行异常</h3>
        <p>辅助分析梯形图逻辑和运行条件</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 🚀 开始你的第一次诊断")

    if st.button("进入故障诊断 →"):
        st.session_state["page"] = "🔧 故障诊断"
        st.rerun()


# =========================
# 故障诊断
# =========================

elif page == "🔧 故障诊断":

    st.title("🔧 PLC 故障诊断")

    st.caption("描述你的设备故障，让 PLC Doctor 帮助你分析。")

    st.markdown("---")

    brand = st.selectbox(
        "PLC 品牌",
        ["三菱 Mitsubishi", "西门子 Siemens", "欧姆龙 Omron"]
    )

    model = st.selectbox(
        "PLC 型号",
        [
            "FX3U",
            "FX5U",
            "FX1N",
            "S7-1200",
            "S7-1500",
            "CP1H"
        ]
    )

    fault = st.text_area(
        "描述故障现象",
        placeholder="例如：PLC运行正常，但是Y0没有输出，请帮我分析可能原因……",
        height=160
    )

    if st.button("⚡ 开始 AI 诊断"):

        if fault.strip():

            st.info("当前为界面演示版本，AI诊断引擎尚未接入。")

            st.markdown("### 📋 诊断信息")

            st.write("PLC品牌：", brand)
            st.write("PLC型号：", model)
            st.write("故障描述：", fault)

            st.warning(
                "下一阶段将接入 DeepSeek API， "
                "实现真正的智能故障分析。"
            )

        else:

            st.warning("请先输入故障现象。")


# =========================
# PLC知识库
# =========================

elif page == "📚 PLC知识库":

    st.title("📚 PLC 知识库")

    st.caption("未来将在这里建立专业工业自动化知识库。")

    st.markdown("---")

    st.markdown("""
    ### 即将支持

    - 三菱 FX 系列 PLC
    - 西门子 S7 系列 PLC
    - 欧姆龙 PLC
    - PLC 常见故障代码
    - 输入输出点位说明
    - 梯形图基础知识
    - 工业电气故障案例
    """)

    st.info("专业知识库正在建设中。")


# =========================
# 历史记录
# =========================

elif page == "🕘 历史记录":

    st.title("🕘 诊断历史")

    st.caption("这里未来会保存用户的历史诊断记录。")

    st.info("目前还没有历史诊断记录功能。")


# =========================
# 底部
# =========================

st.markdown("---")

st.markdown(
    "<center style='color:#666;font-size:12px;'>"
    "PLC Doctor © 2026 · AI Industrial Diagnosis"
    "</center>",
    unsafe_allow_html=True
)
