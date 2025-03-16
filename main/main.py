import streamlit as st
import subprocess
import tempfile
import os

# Streamlit Page Configuration
st.set_page_config(page_title="Multi-Language Online Code Editor", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .title { text-align: center; font-size: 36px; font-weight: bold; color: #D81B60; }
        .stTextArea textarea { font-size: 16px; font-family: "Courier New", monospace; background-color: #FFEBEE; border: 2px solid #D81B60; border-radius: 8px; padding: 10px; }
        .run-btn { background-color: #D81B60; color: white; border-radius: 8px; padding: 12px 25px; font-size: 18px; font-weight: bold; border: none; cursor: pointer; }
        .run-btn:hover { background-color: #AD1457; }
        .output-box { background-color: #FCE4EC; color: #880E4F; padding: 12px; border-radius: 5px; font-family: "Courier New", monospace; border: 2px solid #D81B60; }
        .footer { text-align: center; font-size: 18px; font-weight: bold; color: #C2185B; }
    </style>
""", unsafe_allow_html=True)

# Page Title + Image
st.image("https://cdn-icons-png.flaticon.com/512/4144/4144790.png", width=100)  # Online Image
st.markdown('<h1 class="title">💖 Multi-Language Online Code Editor</h1>', unsafe_allow_html=True)

# Language Selection
languages = {
    "Python": "python",
    "C": "c",
    "C++": "cpp",
    "Java": "java",
    "JavaScript": "js",
    "Bash": "sh",
}
selected_lang = st.selectbox("Select Language", list(languages.keys()))

# Layout with Image
col1, col2 = st.columns([3, 2])
with col1:
    code = st.text_area("Write your code here:", height=300)

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/2721/2721261.png", width=250)  # Online Image
    st.subheader("📌 Output:")
    output_placeholder = st.empty()

# Run Button
center = st.columns([1, 2, 1])[1]
with center:
    run = st.button("🚀 Run Code", key="run-btn")

# Execution Logic
if run:
    if code.strip():
        lang = languages[selected_lang]
        output = "No output"

        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{lang}") as temp_file:
            temp_file.write(code.encode())
            temp_file.close()

            try:
                if lang == "python":
                    result = subprocess.run(["python", temp_file.name], capture_output=True, text=True, timeout=5)
                elif lang == "c":
                    exe_file = temp_file.name.replace(".c", "")
                    subprocess.run(["gcc", temp_file.name, "-o", exe_file], capture_output=True, text=True, timeout=5)
                    result = subprocess.run([exe_file], capture_output=True, text=True, timeout=5)
                elif lang == "cpp":
                    exe_file = temp_file.name.replace(".cpp", "")
                    subprocess.run(["g++", temp_file.name, "-o", exe_file], capture_output=True, text=True, timeout=5)
                    result = subprocess.run([exe_file], capture_output=True, text=True, timeout=5)
                elif lang == "java":
                    subprocess.run(["javac", temp_file.name], capture_output=True, text=True, timeout=5)
                    class_file = temp_file.name.replace(".java", "")
                    result = subprocess.run(["java", class_file], capture_output=True, text=True, timeout=5)
                elif lang == "js":
                    result = subprocess.run(["node", temp_file.name], capture_output=True, text=True, timeout=5)
                elif lang == "sh":
                    result = subprocess.run(["bash", temp_file.name], capture_output=True, text=True, timeout=5)

                output = result.stdout if result.stdout else result.stderr

            except Exception as e:
                output = str(e)

            os.remove(temp_file.name)

        # Display Output
        output_placeholder.markdown(f"<pre class='output-box'>{output}</pre>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please write some code before running!")

# Footer with Image
st.markdown("---")
st.image("https://cdn-icons-png.flaticon.com/512/616/616489.png", width=50)  # Footer Icon
st.markdown('<p class="footer">🔹 Developed using Streamlit | 🚀 Supports Multiple Languages</p>', unsafe_allow_html=True)
st.markdown('<p class="footer">💡 Made by Saba Muhammad Riaz💖</p>', unsafe_allow_html=True)
