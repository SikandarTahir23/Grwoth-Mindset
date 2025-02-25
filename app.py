import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import os
from io import BytesIO

# App Title
st.title("🚀 Growth Mindset Challenge")

# Sidebar for Navigation
st.sidebar.header("📌 Quick Navigation")
page = st.sidebar.radio("Go to:", [
    "🏡 Home", "📊 Progress Tracker", "📝 Daily Challenge", "💡 Tips for Growth",
    "📖 Success Stories", "🎯 Goal Setting", "🤔 Self-Reflection", "📊 Data Analysis"
])

# Home Page
if page == "🏡 Home":
    st.header("Welcome to the Growth Mindset Challenge! 🎯")
    st.markdown("""
    ### Why Adopt a Growth Mindset?
    ✅ **Embrace Challenges**: View obstacles as opportunities to learn rather than setbacks.  
    ✅ **Learn from Mistakes**: Mistakes help you improve.  
    ✅ **Persist Through Difficulties**: Stay determined!  
    ✅ **Celebrate Effort**: Focus on growth, not just results.  
    ✅ **Stay Curious**: Always be open to learning.  
    """)
    st.image("https://media.istockphoto.com/id/1973623637/photo/mindset-loading-bar-concept.webp?a=1&b=1&s=612x612&w=0&k=20&c=_IrFcWJW6qoDNKpKgSNT4rY78RxoQYJo9kkPPXh7cFc=", use_container_width=True)

# Progress Tracker
elif page == "📊 Progress Tracker":
    st.header("📊 Your Growth Progress")

    days = st.slider("How many days have you been practicing a Growth Mindset?", 1, 30, 5)
    effort = st.slider("How much effort do you put in (1-10)?", 1, 10, 7)

    st.session_state["days"] = days  

    fig, ax = plt.subplots()
    ax.bar(["Days Practiced", "Effort Level"], [days, effort], color=["blue", "green"])
    ax.set_ylabel("Level")
    st.pyplot(fig)

# Daily Challenge
elif page == "📝 Daily Challenge":
    st.header("📝 Today's Growth Mindset Challenge")

    days = st.session_state.get("days", 1)

    challenges = [
        "🔹 Identify one mistake you made today and what you learned from it.",
        "🔹 Try something new that challenges you.",
        "🔹 Replace a negative thought with a positive one.",
        "🔹 Teach a new skill to a friend.",
        "🔹 Read about someone who overcame obstacles and got successful.",
        "🔹 Write down three things you're grateful for today.",
        "🔹 Step out of your comfort zone and do something bold.",
        "🔹 Set a small, realistic goal and accomplish it today.",
        "🔹 Avoid distractions and focus on one task at a time.",
        "🔹 Help someone else achieve their goal today.",
        "🔹 Take 10 minutes to meditate or practice mindfulness.",
        "🔹 Write a letter to your future self about your dreams and goals.",
        "🔹 Identify a habit you want to change and take the first step today."
    ]

    challenge_today = challenges[days % len(challenges)]
    st.write(f"💡 **Challenge for Today:** {challenge_today}")

# Tips for Growth (with MCQs)
elif page == "💡 Tips for Growth":
    st.header("💡 Daily Growth Tips")

    tips = [
        "🔥 **Learn from Feedback** – Constructive criticism helps you improve.",
        "🔥 **Be Persistent** – Hard work leads to success.",
        "🔥 **Surround Yourself with Positive People** – Learn from those with a growth mindset.",
        "🔥 **Stay Curious** – Ask questions and keep learning.",
        "🔥 **Break Big Goals into Small Steps** – Focus on progress, not perfection.",
        "🔥 **Celebrate Small Wins** – Every step forward counts!",
        "🔥 **Develop a Learning Habit** – Read books, watch tutorials, and improve every day."
    ]

    days = st.session_state.get("days", 1)
    st.markdown(f"💡 **Tip for Today:** {tips[days % len(tips)]}")

    st.subheader("📝 Growth Mindset Quiz")
    questions = [
        ("What is the key aspect of a growth mindset?", ["Fixed ability", "Effort and learning", "Talent only"], "Effort and learning"),
        ("How should you view challenges?", ["Avoid them", "Embrace them as learning opportunities", "Complain about them"], "Embrace them as learning opportunities"),
        ("What is the best way to handle mistakes?", ["Ignore them", "Learn from them", "Blame others"], "Learn from them"),
        ("What is an essential part of growth?", ["Giving up quickly", "Consistent effort", "Being born smart"], "Consistent effort"),
        ("How do you improve skills?", ["Practice and perseverance", "Natural talent", "Luck"], "Practice and perseverance")
    ]

    for question, options, correct_answer in questions:
        user_answer = st.radio(question, options)
        if st.button(f"Check Answer for: {question}"):
            if user_answer == correct_answer:
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Incorrect! The correct answer is: {correct_answer}")

# Success Stories
elif page == "📖 Success Stories":
    st.header("📖 Real-Life Growth Mindset Stories")

    stories = [
        ("💪 **Thomas Edison**", "Failed over 1,000 times before inventing the light bulb."),
        ("🌍 **Oprah Winfrey**", "Was fired from her first TV job but never gave up."),
        ("🎶 **Eminem**", "Rejected multiple times before becoming a rap legend."),
        ("🏀 **Michael Jordan**", "Cut from his high school basketball team, but became a legend."),
        ("📚 **J.K. Rowling**", "Harry Potter was rejected by 12 publishers before success.")
    ]

    for name, story in stories:
        st.subheader(name)
        st.write(story)

# Goal Setting
elif page == "🎯 Goal Setting":
    st.header("🎯 Set Your Goals")

    goal = st.text_input("📝 Write your goal:")
    deadline = st.date_input("📅 Set a deadline:")

    if st.button("Save Goal"):
        st.success(f"🎯 Goal '{goal}' set for {deadline}!")

# Self-Reflection
elif page == "🤔 Self-Reflection":
    st.header("🤔 Daily Self-Reflection")

    journal = st.text_area("📖 Write about your day, your challenges, and what you learned:")

    if st.button("Save Reflection"):
        st.success("📝 Reflection saved! Keep learning and growing.")

# Data Analysis (Replaced Brain Exercises)
elif page == "📊 Data Analysis":
    st.header("📑 Data Analysis")
    uploaded_files = st.file_uploader("📤 Upload your files (CSV or Excel):", type=["csv", "xlsx", "xls"], accept_multiple_files=True)
    if uploaded_files:
        for file in uploaded_files:
            file_ext = os.path.splitext(file.name)[-1].lower()
            try:
                if file_ext == ".csv":
                    df = pd.read_csv(file)
                elif file_ext in [".xlsx", ".xls"]:
                    df = pd.read_excel(file, engine='openpyxl')
                else:
                    st.error(f"Unsupported file type: {file_ext}")
                    continue
                st.write(f"**File Name:** {file.name}")
                st.write("🔍 Preview of Data:")
                st.dataframe(df.head())
                st.subheader("🛠️ Data Cleaning Options")
                if st.checkbox(f"Clean data for {file.name}"):
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button(f"🧹 Remove Duplicates for {file.name}"):
                            df.drop_duplicates(inplace=True)
                            st.success("✅ Duplicates removed successfully!")
                    with col2:
                        if st.button(f"🛠️ Fill missing values for {file.name}"):
                            numeric_cols = df.select_dtypes(include=['number']).columns
                            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                            st.success("✅ Missing values filled successfully!")
                st.subheader("🎯 Select Columns to Keep")
                columns = st.multiselect(f"Select columns to keep for {file.name}", df.columns, default=df.columns)
                df = df[columns]
                st.subheader("📊 Data Visualization")
                if st.checkbox(f"📈 Visualize data for {file.name}"):
                    st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])
                st.subheader("🔄 Convert File")
                conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
                if st.button(f"🔄 Convert {file.name}"):
                    buffer = BytesIO()
                    if conversion_type == "CSV":
                        df.to_csv(buffer, index=False)
                        file_name = file.name.replace(file_ext, ".csv")
                        mime_type = "text/csv"
                    elif conversion_type == "Excel":
                        df.to_excel(buffer, index=False, engine="openpyxl")
                        file_name = file.name.replace(file_ext, ".xlsx")
                        mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    buffer.seek(0)
                    st.download_button(
                        label=f"⬇️ Download {file_name} as {conversion_type}",
                        data=buffer,
                        file_name=file_name,
                        mime=mime_type
                    )
            except Exception as e:
                st.error(f"❌ Error processing file {file.name}: {e}")
        st.success("🎉 All files processed successfully!")

# Footer
st.markdown("---")
st.markdown("🌱 *Developed by Sikandar Tahir using Streamlit. Keep Growing!*")