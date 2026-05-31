# import streamlit as st
# import requests

# # API URL
# API_URL = "http://127.0.0.1:8000/predict"

# st.title("🚗 Car Price Prediction")

# st.write("Enter car details to predict price")

# # -------------------------------
# # Input fields
# # -------------------------------
# car_name = st.text_input("Car Name", "Hyundai i20")
# year = st.number_input("Year", min_value=2000, max_value=2025, value=2018)
# distance = st.number_input("Distance (km)", value=45000)
# owner = st.selectbox("Owner", [0, 1, 2, 3])

# fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "Electric"])
# location = st.text_input("Location", "Hyderabad")
# drive = st.selectbox("Drive Type", ["Manual", "Automatic"])
# car_type = st.selectbox("Car Type", ["Hatchback", "Sedan", "SUV"])

# # -------------------------------
# # Button
# # -------------------------------
# if st.button("Predict Price"):

#     payload = {
#         "Car_Name": car_name,
#         "Year": year,
#         "Distance": distance,
#         "Owner": owner,
#         "Fuel": fuel,
#         "Location": location,
#         "Drive": drive,
#         "Type": car_type
#     }

#     try:
#         response = requests.post(API_URL, json=payload)

#         if response.status_code == 200:
#             result = response.json()
#             st.success(f"💰 Predicted Price: ₹ {result['predicted_price']}")
#         else:
#             st.error(f"API Error: {response.text}")

#     except Exception as e:
#         st.error(f"Error: {e}")




# import streamlit as st
# import requests
# import base64

# # -------------------------------
# # Function to set background
# # -------------------------------
# def set_bg(image_file):
#     with open(image_file, "rb") as file:
#         encoded = base64.b64encode(file.read()).decode()
#     st.markdown(f"""
#     <style>
#     .stApp {{
#         background-image: url("data:image/jpg;base64,{encoded}");
#         background-size: cover;
#         background-position: center;
#         background-attachment: fixed;
#     }}

#     /* Transparent container */
#     .main {{
#         background-color: rgba(0, 0, 0, 0.6);
#         padding: 20px;
#         border-radius: 15px;
#     }}

#     /* Text color */
#     h1, h2, h3, label, p {{
#         color: white !important;
#     }}
#     </style>
#     """, unsafe_allow_html=True)

# # 🔥 Add your image here
# set_bg("jpg.avif")   # keep image in same folder

# # -------------------------------
# # API URL
# # -------------------------------
# API_URL = "http://127.0.0.1:8000/predict"

# # -------------------------------
# # Title
# # -------------------------------
# st.markdown("<h1 style='text-align: center;'> Car Resale Price Estimator</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align: center;'>AI-powered vehicle valuation system</p>", unsafe_allow_html=True)

# # -------------------------------
# # Layout (2 columns)
# # -------------------------------
# col1, col2 = st.columns(2)

# with col1:
#     car_name = st.text_input("Car Name", "Hyundai i20")
#     year = st.number_input("Year", min_value=2000, max_value=2025, value=2018)
#     distance = st.number_input("Distance (km)", value=45000)
#     owner = st.selectbox("Owner", [0, 1, 2, 3])

# with col2:
#     fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "Electric"])
#     location = st.text_input("Location", "Hyderabad")
#     drive = st.selectbox("Drive Type", ["Manual", "Automatic"])
#     car_type = st.selectbox("Car Type", ["Hatchback", "Sedan", "SUV"])

# st.write("")

# # -------------------------------
# # Button (centered)
# # -------------------------------
# if st.button("💰 Predict Price", use_container_width=True):

#     payload = {
#         "Car_Name": car_name,
#         "Year": year,
#         "Distance": distance,
#         "Owner": owner,
#         "Fuel": fuel,
#         "Location": location,
#         "Drive": drive,
#         "Type": car_type
#     }

#     try:
#         response = requests.post(API_URL, json=payload)

#         if response.status_code == 200:
#             result = response.json()
#             st.success(f"💰 Predicted Price: ₹ {result['predicted_price']:,}")
#         else:
#             st.error(f"API Error: {response.text}")

#     except Exception as e:
#         st.error(f"Error: {e}")


# import streamlit as st
# import requests
# import base64

# # -------------------------------
# # Background Image
# # -------------------------------
# def set_bg(image_file):
#     with open(image_file, "rb") as file:
#         encoded = base64.b64encode(file.read()).decode()

#     st.markdown(f"""
#     <style>

#     .stApp {{
#         background-image: url("data:image/jpg;base64,{encoded}");
#         background-size: cover;
#         background-position: center;
#         background-attachment: fixed;
#     }}

#     /* Glass container */
#     .block-container {{
#         background: rgba(0, 0, 0, 0.55);
#         padding: 2rem;
#         border-radius: 20px;
#     }}

#     /* Headings */
#     h1 {{
#         color: #ffffff;
#         text-align: center;
#         font-size: 42px;
#         font-weight: 700;
#     }}

#     p {{
#         color: #d1d5db;
#         text-align: center;
#         font-size: 16px;
#     }}

#     /* Labels */
#     label {{
#         color: #f9fafb !important;
#         font-weight: 500;
#     }}

#     /* Input fields */
#     input, textarea {{
#         color: #ffffff !important;
#         background-color: rgba(255, 255, 255, 0.1) !important;
#         border-radius: 10px !important;
#         border: 1px solid rgba(255,255,255,0.3) !important;
#     }}

#     /* Placeholder text */
#     input::placeholder {{
#         color: #cbd5e1 !important;
#         opacity: 1;
#     }}

#     /* Selectbox */
#     div[data-baseweb="select"] > div {{
#         background-color: rgba(255,255,255,0.1) !important;
#         color: white !important;
#         border-radius: 10px !important;
#     }}

#     /* Button */
#     .stButton button {{
#         background: linear-gradient(90deg, #ff7e5f, #feb47b);
#         color: white;
#         font-size: 18px;
#         border-radius: 12px;
#         height: 50px;
#         border: none;
#     }}

#     .stButton button:hover {{
#         background: linear-gradient(90deg, #ff6a4d, #fda763);
#     }}

#     /* Result box */
#     .result-box {{
#         background: rgba(0, 0, 0, 0.6);
#         padding: 15px;
#         border-radius: 12px;
#         color: #00ffcc;
#         font-size: 20px;
#         text-align: center;
#         margin-top: 20px;
#     }}

#     </style>
#     """, unsafe_allow_html=True)


# # Apply background
# set_bg("jpg.avif")

# # -------------------------------
# # API URL
# # -------------------------------
# API_URL = "http://127.0.0.1:8000/predict"

# # -------------------------------
# # Title
# # -------------------------------
# st.markdown("<h1>Car Resale Price Estimator</h1>", unsafe_allow_html=True)
# st.markdown("<p>AI-powered vehicle valuation system</p>", unsafe_allow_html=True)

# # -------------------------------
# # Layout
# # -------------------------------
# col1, col2 = st.columns(2)

# with col1:
#     car_name = st.text_input("Car Name", placeholder="Enter car name...")
#     year = st.number_input("Year", min_value=2000, max_value=2025, value=2018)
#     distance = st.number_input("Distance (km)", value=45000)
#     owner = st.selectbox("Owner", [0, 1, 2, 3])

# with col2:
#     fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "Electric"])
#     location = st.text_input("Location", placeholder="Enter city...")
#     drive = st.selectbox("Drive Type", ["Manual", "Automatic"])
#     car_type = st.selectbox("Car Type", ["Hatchback", "Sedan", "SUV"])

# st.write("")

# # -------------------------------
# # Button
# # -------------------------------
# if st.button("💰 Predict Price", use_container_width=True):

#     payload = {
#         "Car_Name": car_name,
#         "Year": year,
#         "Distance": distance,
#         "Owner": owner,
#         "Fuel": fuel,
#         "Location": location,
#         "Drive": drive,
#         "Type": car_type
#     }

#     try:
#         response = requests.post(API_URL, json=payload)

#         if response.status_code == 200:
#             result = response.json()

#             st.markdown(
#                 f"<div class='result-box'>💰 Predicted Price: ₹ {result['predicted_price']:,}</div>",
#                 unsafe_allow_html=True
#             )
#         else:
#             st.error(f"API Error: {response.text}")

#     except Exception as e:
#         st.error(f"Error: {e}")


import streamlit as st
import requests
import base64

# -------------------------------
# Background Image
# -------------------------------
def set_bg(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    st.markdown(f"""
    <style>

    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Glass Card */
    .block-container {{
        max-width: 900px;
        margin: auto;
        background: rgba(0, 0, 0, 0.65);
        padding: 40px;
        border-radius: 20px;
        backdrop-filter: blur(12px);
    }}

    /* Labels */
    label {{
        color: #e5e7eb !important;
        font-size: 14px !important;
    }}

    /* Inputs */
    .stTextInput input,
    .stNumberInput input {{
        background-color: rgba(0,0,0,0.6) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255,255,255,0.25) !important;
        border-radius: 12px !important;
        padding: 10px !important;
    }}

    /* Placeholder */
    .stTextInput input::placeholder {{
        color: #9ca3af !important;
    }}

    /* Selectbox */
    div[data-baseweb="select"] > div {{
        background-color: rgba(0,0,0,0.6) !important;
        color: white !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255,255,255,0.25) !important;
    }}

    div[data-baseweb="select"] span {{
        color: white !important;
    }}

    /* Button */
    .stButton button {{
        background: linear-gradient(90deg, #ff7e5f, #f4a261);
        color: white;
        font-size: 18px;
        font-weight: 600;
        border-radius: 14px;
        height: 55px;
        border: none;
        margin-top: 15px;
    }}

    .stButton button:hover {{
        background: linear-gradient(90deg, #ff6a4d, #e76f51);
    }}

    /* Result Box */
    .result-box {{
        background: rgba(0, 0, 0, 0.75);
        border-radius: 15px;
        padding: 18px;
        text-align: center;
        font-size: 20px;
        color: #00f5d4;
        margin-top: 20px;
        border: 1px solid rgba(0,255,200,0.3);
    }}

    </style>
    """, unsafe_allow_html=True)


# Apply background
set_bg("jpg.avif")

# -------------------------------
# API URL
# -------------------------------
# API_URL = "https://your-api-name.onrender.com/predict"
API_URL = "https://price-api-0c6p.onrender.com"

# -------------------------------
# Title (BLUE + OUTSIDE CARD)
# -------------------------------
st.markdown("""
<h1 style='
    text-align: center;
    color: #3b82f6;
    font-size: 48px;
    font-weight: 800;
    text-shadow: 2px 2px 10px rgba(0,0,0,0.7);
'>
Car Resale Price Estimator
</h1>

<p style='
    text-align: center;
    color: #e5e7eb;
    font-size: 18px;
    margin-bottom: 30px;
'>
AI-powered vehicle valuation system
</p>
""", unsafe_allow_html=True)

# -------------------------------
# START Glass Card
# -------------------------------
st.markdown("<div class='block-container'>", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns(2)

with col1:
    car_name = st.text_input("Car Name", placeholder="Maruti Vitara Brezza")
    year = st.number_input("Year", min_value=2000, max_value=2025, value=2018)
    distance = st.number_input("Distance (km)", value=45000)
    owner = st.selectbox("Owner", [0, 1, 2, 3])

with col2:
    fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "Electric"])
    location = st.text_input("Location", placeholder="Enter city...")
    drive = st.selectbox("Drive Type", ["Manual", "Automatic"])
    car_type = st.selectbox("Car Type", ["Hatchback", "Sedan", "SUV"])

st.markdown("<br>", unsafe_allow_html=True)

# Button
if st.button("💰 Predict Price", use_container_width=True):

    payload = {
        "Car_Name": car_name,
        "Year": year,
        "Distance": distance,
        "Owner": owner,
        "Fuel": fuel,
        "Location": location,
        "Drive": drive,
        "Type": car_type
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()

            st.markdown(
                f"<div class='result-box'>💰 Predicted Price: ₹ {result['predicted_price']:,}</div>",
                unsafe_allow_html=True
            )
        else:
            st.error(f"API Error: {response.text}")

    except Exception as e:
        st.error(f"Error: {e}")

# -------------------------------
# END Glass Card
# -------------------------------
st.markdown("</div>", unsafe_allow_html=True)


