# Markov Chain Activity – Marina de Empresas
# This notebook guides you through building and analyzing a Markov chain
# using data collected during the outdoor activity.

# =============================
# 📌 CELL 1 — IMPORT LIBRARIES
# =============================
import pandas as pd
import numpy as np

# =============================
# 📌 CELL 2 — LOAD DATA
# =============================
# 👉 Replace this with your collected data
# Format: ("From", "To")

data = [
    ("EDEM", "Lanzadera"),
    ("Lanzadera", "Angels"),
    ("Angels", "Lanzadera"),
    ("EDEM", "EDEM"),
    ("Lanzadera", "Angels"),
]

df = pd.DataFrame(data, columns=["From", "To"])
df

# =============================
# 📌 CELL 3 — BUILD TRANSITION MATRIX
# =============================
counts = pd.crosstab(df['From'], df['To'])
P = counts.div(counts.sum(axis=1), axis=0)

print("Transition Matrix (P):")
display(P)

# =============================
# ✏️ EXERCISE 1
# =============================
# 👉 Compute manually (on paper or mentally):
# What is the probability of going from EDEM to Lanzadera?
# Then verify it in the matrix above.

# =============================
# 📌 CELL 4 — STATE ORDER
# =============================
states = ["EDEM", "Lanzadera", "Angels"]
P_np = P.loc[states, states].values

# =============================
# 📌 CELL 5 — EVOLUTION OF STATES
# =============================
# Initial distribution (all students start in EDEM)
pi = np.array([1, 0, 0])

print("Initial distribution:", pi)

for step in range(5):
    pi = pi @ P_np
    print(f"Step {step+1}: {pi}")

# =============================
# ✏️ EXERCISE 2
# =============================
# 👉 Change the initial distribution:
# Example: 50% EDEM, 50% Lanzadera
# What happens after 3 steps?

# Your code here:


# =============================
# ✏️ EXERCISE 3
# =============================
# 👉 Does the distribution seem to stabilize?
# Try running more steps (e.g., 10 or 20)

# Your code here:


# =============================
# 📌 CELL 6 — STATIONARY DISTRIBUTION
# =============================
eigvals, eigvecs = np.linalg.eig(P_np.T)
idx = np.argmin(np.abs(eigvals - 1))
stationary = eigvecs[:, idx].real
stationary = stationary / stationary.sum()

print("Stationary distribution:")
print(stationary)

# =============================
# ✏️ EXERCISE 4
# =============================
# 👉 Interpret the stationary distribution:
# Which state has the highest probability?
# Why do you think this happens based on your activity?

# =============================
# 📌 CELL 7 — LABELLED OUTPUT
# =============================
for s, val in zip(states, stationary):
    print(f"{s}: {val:.3f}")

# =============================
# ✏️ EXERCISE 5 (EXAM STYLE)
# =============================
# 👉 Answer these questions:
# 1. Compute the distribution after 2 steps starting from EDEM
# 2. Compute the distribution after 5 steps
# 3. Compare both with the stationary distribution
# 4. Does the initial state matter in the long run?

# =============================
# 🚀 BONUS (OPTIONAL)
# =============================
# Simulate random trajectories
import random

current_state = "EDEM"
trajectory = [current_state]

for _ in range(10):
    probs = P.loc[current_state]
    next_state = random.choices(probs.index, weights=probs.values)[0]
    trajectory.append(next_state)
    current_state = next_state

print("Sample trajectory:")
print(trajectory)
