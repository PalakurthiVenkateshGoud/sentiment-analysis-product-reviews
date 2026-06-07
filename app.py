import streamlit as st
import pandas as pd
from textblob import TextBlob

st.set_page_config(
    page_title="Sentiment Analysis Dashboard",
    layout="wide"
)

st.title("Sentiment Analysis on Product Reviews")

st.markdown("""
### Business Objective
Analyze customer reviews and classify them into Positive, Negative, and Neutral sentiments to generate actionable business insights.
""")

df = pd.read_csv("Reviews_5000.csv")

df = df[['Text', 'Score']]
df = df.dropna().drop_duplicates()

def get_sentiment(text):
    score = TextBlob(text).sentiment.polarity

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Text"].apply(get_sentiment)
df["Polarity"] = df["Text"].apply(
    lambda x: TextBlob(x).sentiment.polarity
)

positive = (df["Sentiment"] == "Positive").sum()
negative = (df["Sentiment"] == "Negative").sum()
neutral = (df["Sentiment"] == "Neutral").sum()

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Overview",
        "Sentiment Analytics",
        "Advanced Analysis",
        "Insights"
    ]
)

if page == "Overview":

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Total Reviews", len(df))
    col2.metric("Positive", positive)
    col3.metric("Negative", negative)
    col4.metric("Neutral", neutral)
    col5.metric("Avg Polarity", round(df["Polarity"].mean(), 3))

    st.divider()

    st.subheader("Dataset Summary")

    st.write(f"Records Analyzed: {len(df)}")
    st.write("Source: Amazon Fine Food Reviews")
    st.write("Review Sample Size: First 5000 Reviews")

    st.info(
        "88.3% of reviews were positive, indicating strong customer satisfaction."
    )

    st.warning(
        "Negative reviews commonly referenced quality and packaging concerns."
    )

elif page == "Sentiment Analytics":

    st.header("Sentiment Analytics")

    c1, c2 = st.columns(2)

    with c1:
        st.image("charts/bar_chart.png")

    with c2:
        st.image("charts/pie_chart.png")

    st.image("charts/rating_vs_sentiment.png")

elif page == "Advanced Analysis":

    st.header("Customer Feedback Intelligence")

    c3, c4 = st.columns(2)

    with c3:
        st.image("charts/polarity_distribution.png")

    with c4:
        st.image("charts/review_length_vs_sentiment.png")

    st.image("charts/negative_wordcloud.png")

elif page == "Insights":

    st.header("Executive Insights")

    st.markdown("""
- Majority of customer reviews are positive.
- Sentiment polarity increases with rating score.
- Negative reviews frequently mention product quality, taste, and packaging issues.
- Longer reviews often contain detailed customer complaints.
- Sentiment analysis provides deeper understanding beyond ratings alone.
""")

    st.header("Strategic Recommendations")

    st.markdown("""
1. Improve product quality and packaging.
2. Continuously monitor customer sentiment.
3. Prioritize recurring complaint categories.
4. Use sentiment insights to improve customer satisfaction.
""")
