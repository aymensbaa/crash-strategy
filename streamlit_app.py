
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Crash Strategy Analyzer")

uploaded_file = st.file_uploader("Upload crash_data.csv", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if "multiplier" not in df.columns:
        st.error("CSV must contain a 'multiplier' column.")
    else:
        st.subheader("Data Preview")
        st.dataframe(df.head())

        st.subheader("Statistics")
        st.write(df["multiplier"].describe())

        st.subheader("Plot")
        fig, ax = plt.subplots()
        df["multiplier"].plot(kind="line", ax=ax)
        plt.xlabel("Game #")
        plt.ylabel("Multiplier")
        st.pyplot(fig)

        st.subheader("Best Auto Cashout Strategy")
        strategies = [1.5, 2.0, 2.5, 3.0, 5.0]
        best_profit = -float("inf")
        best_x = None
        for x in strategies:
            wins = df["multiplier"] >= x
            profit = (wins.sum() * (x - 1)) - (~wins).sum()
            if profit > best_profit:
                best_profit = profit
                best_x = x
        st.success(f"✅ Best auto cashout is at {best_x}x with estimated profit: {best_profit:.2f}")
