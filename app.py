import streamlit as st
import requests
import json
import streamlit.components.v1 as components

# ---------------------------------------------------
# 🎭 APP HEADER
# ---------------------------------------------------
st.set_page_config(page_title="Cross Culture Humor Mapper", page_icon="😂", layout="centered")
st.title("🌏 Cross Culture Humor Mapper")
st.caption("Translate humor across cultures — with tone, context, and a touch of laughter!")

# ---------------------------------------------------
# 🎯 INPUT SECTION
# ---------------------------------------------------
st.markdown("### Enter your humor or joke:")
user_input = st.text_area("Type here...", placeholder="e.g. My boss said we need to think outside the box... so I went home.")

target_culture = st.selectbox(
    "Select Target Culture/Language:",
    ["Indian", "Japanese", "German", "French", "Chinese", "Gen Z", "Corporate"],
)

# ---------------------------------------------------
# 🚀 TRANSLATION FUNCTION (dummy example – replace with your model API)
# ---------------------------------------------------
def translate_humor(text, culture):
    # This is just a placeholder for your API/model logic
    response = {
        "Indian": "मेरे बॉस ने कहा कि हमें नए तरीके से सोचना चाहिए, तो मैं घर चला गया!",
        "Japanese": "上司が「枠の外で考えろ」と言ったので、家に帰りました！",
        "German": "Mein Chef sagte, ich solle außerhalb der Box denken – also ging ich nach Hause!",
        "French": "Mon patron a dit de penser hors des sentiers battus, alors je suis rentré chez moi !",
        "Chinese": "老板说要跳出框框思考，所以我回家了！",
        "Gen Z": "Boss said think outside the box — I left the group chat 💀",
        "Corporate": "Per leadership's directive to ideate unconventionally, I relocated my workspace — home."
    }
    return response.get(culture, "Translation not found.")

# ---------------------------------------------------
# 🎛️ BUTTON + RESULT
# ---------------------------------------------------
translated_text = ""
if st.button("✨ Translate Humor"):
    if user_input.strip() == "":
        st.warning("Please enter some text first!")
    else:
        with st.spinner("Translating with cultural adaptation..."):
            translated_text = translate_humor(user_input, target_culture)

# ---------------------------------------------------
# 🎙️ DISPLAY RESULT + MULTILINGUAL TTS
# ---------------------------------------------------
if translated_text:
    st.success("✅ Culturally adapted humor:")
    st.markdown(f"### {translated_text}")

    # Language code mapping for accurate TTS
    lang_map = {
        "indian": "hi-IN",
        "japanese": "ja-JP",
        "german": "de-DE",
        "french": "fr-FR",
        "chinese": "zh-CN",
        "gen z": "en-US",
        "corporate": "en-GB"
    }
    lang_code = lang_map.get(target_culture.strip().lower(), "en-US")

    # Multilingual Text-to-Speech button
    speak_button = f"""
    <script>
    function speakText(text, lang) {{
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = lang;
        utterance.rate = 1.0;
        utterance.pitch = 1.0;
        // Try to pick a matching voice if available
        const voices = window.speechSynthesis.getVoices();
        const voice = voices.find(v => v.lang === lang) || voices.find(v => v.lang.startsWith(lang.split('-')[0]));
        if (voice) utterance.voice = voice;
        speechSynthesis.speak(utterance);
    }}
    </script>
    <button 
        style="background-color:#f0f0f0;
               border:none;
               border-radius:8px;
               padding:8px 12px;
               margin-top:10px;
               cursor:pointer;
               font-size:16px;">
        🔊 Click to Listen
    </button>
    <script>
    const button = document.currentScript.previousElementSibling;
    button.addEventListener('click', () => {{
        speakText({json.dumps(translated_text)}, {json.dumps(lang_code)});
    }});
    </script>
    """
    components.html(speak_button, height=60)

# ---------------------------------------------------
# 📜 FOOTER
# ---------------------------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit, Mistral, and a sense of humor.")
