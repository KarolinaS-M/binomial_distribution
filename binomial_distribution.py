import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from math import comb

# --- Page setup ---
st.set_page_config(page_title="Binomial Distribution", layout="centered")
st.title("🎲 Binomial Distribution – Interactive Visualization")

st.markdown(
    """
    This app illustrates the **binomial distribution**,
    which describes the probability of having exactly *k* successes
    in *n* independent Bernoulli trials with probability *p* of success.
    """
)

# --- User input ---
p = st.slider("Probability of success (p)", min_value=0.0, max_value=1.0, value=0.7, step=0.01)
n = st.slider("Number of trials (n)", min_value=1, max_value=50, value=10, step=1)

# --- Compute probabilities (PMF) ---
k_values = np.arange(n + 1)
P = [comb(n, k) * (p**k) * ((1 - p)**(n - k)) for k in k_values]

# --- Plot ---
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(k_values, P, color="#4C72B0", edgecolor="black")

# Highlight the most likely number of successes (mode)
max_k = int(np.argmax(P))
bars[max_k].set_color("#55A868")
bars[max_k].set_edgecolor("black")

# Annotate the mode bar
ax.text(max_k, P[max_k] + max(P)*0.02, "mode", ha="center", va="bottom", fontsize=10)

# --- Fix overlapping labels: rotate vertically ---
ax.set_xticks(k_values)
ax.set_xticklabels(k_values, rotation=90, va="top", ha="center")

ax.set_xlabel("Number of Successes (k)")
ax.set_ylabel("Probability")
ax.set_title(f"Binomial Distribution (n = {n}, p = {p:.2f})")
ax.grid(axis="y", linestyle="--", alpha=0.7)

st.pyplot(fig)

# --- Numeric values table ---
st.subheader("Probability Values (PMF)")
st.dataframe(
    {
        "Number of Successes (k)": k_values,
        "Probability": [round(prob, 4) for prob in P],
    },
    use_container_width=True,
)

# --- Helpful facts ---
mean = n * p
var = n * p * (1 - p)
st.caption(
    f"Mean = n·p = {mean:.2f}, Variance = n·p·(1-p) = {var:.2f}. "
    "The highlighted bar shows the most probable number of successes (mode)."
)
