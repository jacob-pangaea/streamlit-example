import pandas as pd
import streamlit as st

st.set_page_config(layout="centered", page_title="Data Editor", page_icon="🧮")

st.title("✍️ OB Shipping Rate Card Editor")
st.caption("This is a a template app showing off the Streamlit UI, which can be used to create complete rate schedules that correspond to the data structure used in OMS so that these can be piped directly in, pending review and approval.")

st.write("")

"""Just a quick example of what we can do here..."""

data = [
    {
        "Brand Code": "Bla bla Cosmetics",
        "Origin Country": "US",
        "Destination Country": "GB",
        "0-1 lbs": 4.50,
        "1-2.5 lbs": 5.15,
        "2.5 - 5 lbs": 5.95,
        "... to ... lbs": "X.YZ"
    },
     {
        "Brand Code": "Bla bla Cosmetics",
        "Origin Country": "US",
        "Destination Country": "CZ",
        "0-1 lbs": 4.50,
        "1-2.5 lbs": 5.15,
        "2.5 - 5 lbs": 5.95,
        "... to ... lbs": "X.YZ"
    },
     {
        "Brand Code": "Bla bla Cosmetics",
        "Origin Country": "US",
        "Destination Country": "FR",
        "0-1 lbs": 4.50,
        "1-2.5 lbs": 5.15,
        "2.5 - 5 lbs": 5.95,
        "... to ... lbs": "X.YZ"
    },
     {
        "Brand Code": "Bla bla Cosmetics",
        "Origin Country": "US",
        "Destination Country": "CA",
        "0-1 lbs": 4.50,
        "1-2.5 lbs": 5.15,
        "2.5 - 5 lbs": 5.95,
        "... to ... lbs": "X.YZ"
    },
]

df = pd.DataFrame(data)
df.sentiment = df.sentiment.astype("category")
#df.sentiment = df.sentiment.cat.add_categories(("☯ Neutral", "😤 Negative"))


annotated = st.data_editor(df, hide_index=True, use_container_width=True, disabled=["Brand Code"])

st.download_button(
    "⬇️ Download Rate Schedule as 'rate_schedule.csv'", annotated.to_csv(), "rate_schedule.csv", use_container_width=True
)
