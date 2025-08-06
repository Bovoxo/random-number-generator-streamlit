import streamlit as st
import random

st.set_page_config(page_title="Random Number Generator", layout="centered")

st.title("🎲 Random Number Generator")

st.markdown("Zadej minimální a maximální číslo, klikni na **Generovat** a vygenerujeme náhodné číslo v daném rozsahu.")

# Vstupní hodnoty
min_number = st.text_input("Minimální číslo:")
max_number = st.text_input("Maximální číslo:")

if st.button("Generovat"):
    try:
        min_val = int(min_number)
        max_val = int(max_number)

        if min_val > max_val:
            st.warning("Maximální číslo musí být větší než minimální!")
        else:
            random_number = random.randint(min_val, max_val)
            st.success(f"🎉 Vygenerované číslo: **{random_number}**")

    except ValueError:
        st.warning("Zadej platná čísla do obou polí!")
