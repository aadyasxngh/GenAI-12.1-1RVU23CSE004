import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API keys
load_dotenv()

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",   # ✅ FIXED: removed "models/" prefix
    temperature=0.7,
    google_api_key=os.getenv("GEMINI_API_KEY")
)

def generate_trip_plan(city, days, weather, flights, hotels):
    # ✅ FIXED: Convert lists to strings if needed
    if isinstance(flights, list):
        flights = "\n".join(f"- {f}" for f in flights)
    if isinstance(hotels, list):
        hotels = "\n".join(f"- {h}" for h in hotels)

    prompt = f"""
You are an expert travel planner. Plan a {days}-day trip to {city}.

Your response must include:

1. **City Overview** – One paragraph about the city's cultural and historical significance.

2. **Weather Information**:
{weather}

3. **Available Flights**:
{flights}

4. **Hotel Options**:
{hotels}

5. **Day-by-Day Itinerary** – A detailed itinerary for all {days} days, including:
   - Morning, afternoon, and evening activities
   - Key attractions, cultural sites, local food recommendations
   - Practical travel tips

Make the plan engaging, informative, and easy to follow for a traveler.
"""

    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        # ✅ FIXED: Proper error handling with useful message
        return f"❌ Error generating trip plan: {str(e)}\n\nPlease check your GEMINI_API_KEY in the .env file."