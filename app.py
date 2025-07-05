import streamlit as st
import random
from streamlit_lottie import st_lottie
import requests

# function to load Lottie JSON
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# your correct JSON animation
lottie_motivation = load_lottieurl(
    "https://lottie.host/6e15df1d-b5ce-4b24-9f1c-1f396e01671f/KFRyrJ85eT.json"
)

# improved background and text contrast
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #f5f7fa, #c3cfe2);
        background-attachment: fixed;
    }
    .stTextInput > div > div {
        background-color: rgba(255,255,255,0.9) !important;
        color: #333333 !important;
        border-radius: 8px;
    }
    .stButton > button {
        background-color: #ff69b4;
        color: white;
        font-weight: bold;
        border-radius: 8px;
    }
    .stSubheader, .stTextInput label, .stMarkdown h1 {
        color: #333333 !important;
    }
    </style>
""", unsafe_allow_html=True)

# motivation logic
def get_motivation(mood_input):
    mood_input = mood_input.lower()

    if "anxious" in mood_input or "anxiety" in mood_input:
        category = "feeling anxious"
    elif "focus" in mood_input or "concentrate" in mood_input:
        category = "need focus"
    elif "sad" in mood_input or "depressed" in mood_input:
        category = "feeling sad"
    elif "confidence" in mood_input or "confident" in mood_input:
        category = "need confidence"
    elif "energy" in mood_input or "tired" in mood_input or "lazy" in mood_input:
        category = "need energy"
    elif "anger" in mood_input or "angry" in mood_input:
        category = "anger"
    else:
        category = "general"

    motivations = {
        "feeling anxious": [
            "Take a deep breath. You are stronger than you think.",
            "Anxiety does not define you. You have faced challenges before and come out stronger.",
            "One step at a time. You are doing your best, and that’s enough.",
        ],
        "need focus": [
            "Eliminate distractions and trust yourself. You can do it.",
            "Stay in the moment. Every small step matters.",
            "Focus on progress, not perfection.",
        ],
        "feeling sad": [
            "This too shall pass. Brighter days are ahead.",
            "You have overcome tough times before. You will get through this.",
            "It’s okay to feel down. Be kind to yourself today.",
        ],
        "need confidence": [
            "Believe in yourself. You have unique strengths no one else has.",
            "You are capable of amazing things.",
            "Trust your journey. You’ve come this far for a reason.",
        ],
        "need energy": [
            "Get up, get moving! You are a powerhouse.",
            "Remember your ‘why’ — it will fuel you.",
            "You have the energy within you to make today amazing.",
        ],
        "anger": [
            "Anger is a fire: control it, or it will consume you.",
            "Breathe through anger, respond with calmness.",
            "Channel your anger into positive change.",
        ],
        "general": [
            "You are enough. Keep going and make today count!",
            "Every day is a fresh start. Believe in yourself.",
            "One small positive thought can change your whole day.",
        ],
    }

    return random.choice(motivations[category])

# UI
st.markdown(
    "<h1 style='text-align:center;'>🌟 Daily Motivation Generator 🌟</h1>",
    unsafe_allow_html=True,
)
st.subheader("Type how you feel today, and get inspired!")

# show the lottie animation
if lottie_motivation:
    st_lottie(lottie_motivation, height=300, key="motivation")

# user input
mood_input = st.text_input("📝 Your mood (for example: 'I feel anxious')")

if st.button("✨ Inspire Me"):
    if mood_input.strip() == "":
        st.warning("Please enter how you feel before pressing the button.")
    else:
        quote = get_motivation(mood_input)
        st.success(f"**{quote}**")
