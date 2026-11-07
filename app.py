import streamlit as st

st.set_page_config(
    page_title="Pak Pulse AI",
    page_icon="🥇",
    layout="wide"
)

st.title("🥇 PAK PULSE AI")
st.subheader("XAUUSD Gold Trading System")

st.success("System Initialized")

st.markdown("---")

st.header("📊 Gold Market Analysis")

price = st.number_input(
    "XAUUSD Current Price",
    min_value=0.0,
    value=4000.0,
    step=0.1
)

ema20 = st.number_input("EMA 20", value=4000.0)
ema50 = st.number_input("EMA 50", value=3995.0)
rsi = st.number_input(
    "RSI",
    min_value=0.0,
    max_value=100.0,
    value=55.0
)

if st.button("Analyze Market"):
    if ema20 > ema50 and 50 < rsi < 70:
        st.success("BUY SIGNAL")
    elif ema20 < ema50 and 30 < rsi < 50:
        st.error("SELL SIGNAL")
    else:
        st.warning("WAIT - No clear signal")

    st.write("Entry Price:", price)
    st.write("EMA 20:", ema20)
    st.write("EMA 50:", ema50)
    st.write("RSI:", rsi)

st.markdown("---")
st.caption(
    "Pak Pulse AI | Educational and paper trading only"
)
