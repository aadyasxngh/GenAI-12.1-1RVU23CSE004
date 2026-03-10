import streamlit as st
from tools import get_weather, get_flights, get_hotels
from agent import generate_trip_plan

# Page config
st.set_page_config(page_title="AI Trip Planner", page_icon="✈️", layout="wide")

st.title("✈️ AI Trip Planner Agent")
st.write("Plan your perfect trip using AI — powered by Gemini + real-time data!")

st.divider()

# User inputs
col1, col2 = st.columns(2)
with col1:
    city = st.text_input("🌍 Enter Destination City", placeholder="e.g. Tokyo, Udaipur, Paris")
with col2:
    days = st.number_input("📅 Number of Days", min_value=1, max_value=10, step=1, value=3)

st.divider()

if st.button("🗺️ Plan My Trip", use_container_width=True):

    if not city.strip():
        st.warning("⚠️ Please enter a destination city.")
    else:
        # ✅ FIXED: Added spinner for better UX while fetching data
        with st.spinner(f"Fetching data and generating your {days}-day trip to {city}..."):
            weather = get_weather(city)
            flights = get_flights(city)
            hotels = get_hotels(city)
            plan = generate_trip_plan(city, days, weather, flights, hotels)

        # Display results in columns
        col_a, col_b, col_c = st.columns(3)

        with col_a:
            st.subheader("🌤️ Current Weather")
            st.info(weather)

        with col_b:
            st.subheader("✈️ Flight Options")
            st.info(flights)

        with col_c:
            st.subheader("🏨 Hotel Options")
            st.info(hotels)

        st.divider()
        st.subheader(f"📋 Your {days}-Day Trip Plan to {city}")
        st.markdown(plan)