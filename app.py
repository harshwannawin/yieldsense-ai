import streamlit as st
import json
import time
import random

# --- CONFIGURATION & SETUP ---
st.set_page_config(
    page_title="EcoCart | Smart Grocery",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- GROQ SETUP ---
try:
    from groq import Groq
except ImportError:
    st.error("⚠️ `groq` library missing. Run `pip install groq`")
    st.stop()

# Load environment variables
import os
from dotenv import load_dotenv
load_dotenv()

# Get API key from Streamlit secrets (cloud) or environment (local)
try:
    api_key = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY", ""))
except:
    api_key = os.getenv("GROQ_API_KEY", "")

# --- CUSTOM CSS (Phone App Look) ---
st.markdown("""
<style>
    .product-card {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border: 1px solid #eee;
    }
    .product-card h3 {
        color: #000000;
        font-weight: bold;
    }
    .price-tag {
        font-size: 1.4rem;
        font-weight: bold;
        color: #2c3e50;
    }
    .discount-tag {
        background-color: #ff4757;
        color: white;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        margin-left: 10px;
    }
    .stButton>button {
        border-radius: 20px;
    }
    .seller-header {
        background-color: #2c3e50;
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if 'inventory' not in st.session_state:
    st.session_state.inventory = [
        # Default items
        {"id": 1, "name": "Organic Milk", "category": "Dairy", "base_price": 5.00, "expiry": "7 Days", "condition": "Perfect", "image": "🥛"},
        {"id": 2, "name": "Sourdough Bread", "category": "Bakery", "base_price": 4.50, "expiry": "2 Days", "condition": "Good", "image": "🍞"},
    ]
    st.session_state.next_id = 3  # Track next available ID

# --- SIDEBAR (App Navigation) ---
with st.sidebar:
    st.title("📱 EcoCart Navigation")
    app_mode = st.radio("Select View:", ["🏪 Seller Dashboard", "🛒 Customer Storefront"])

# --- AI LOGIC ---
def get_groq_client():
    if not api_key: return None
    return Groq(api_key=api_key)

def calculate_dynamic_price(item, user_persona, purchase_history):
    """
    Calls Groq to determine price for a specific item + user combo.
    """
    client = get_groq_client()
    if not client: return None

    prompt = f"""
    Act as a Pricing Algorithm. Return ONLY JSON.
    
    Item: {item['name']}
    Condition: {item['condition']}
    Expiry: {item['expiry']}
    Base Price: ${item['base_price']}
    
    User Persona: {user_persona}
    User History: {purchase_history}
    
    RULES:
    1. If Expiry is 'Critical (4 hrs)' AND User is 'Loyal' -> 50% Discount.
    2. If User is 'Strategic (Waits for deals)' -> NO Discount (Break the habit).
    3. If Condition is 'Dented' -> 20% Discount for everyone.
    4. If Expiry is 'Fresh' -> NO Discount.
    
    JSON Output format:
    {{
        "final_price": 0.00,
        "discount_percent": 0,
        "tagline": "Short marketing text"
    }}
    """
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            response_format={"type": "json_object"}
        )
        return json.loads(completion.choices[0].message.content)
    except:
        return {"final_price": item['base_price'], "discount_percent": 0, "tagline": "Standard Price"}

# ==========================================
# VIEW 1: SELLER DASHBOARD (Inventory Mgmt)
# ==========================================
if app_mode == "🏪 Seller Dashboard":
    st.markdown("<div class='seller-header'><h2>🏪 Store Manager Backend</h2></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Add/Edit Stock")
        with st.form("inventory_form"):
            name = st.selectbox("Select Product", ["Amul Gold Milk", "Farm Eggs", "Avocados", "Whole Wheat Bread", "Greek Yogurt"])
            expiry = st.selectbox("Time Until Expiry", ["Fresh (1 Week)", "Medium (3 Days)", "High Risk (1 Day)", "Critical (4 Hours)"])
            condition = st.selectbox("Condition", ["Perfect", "Dented Box", "Slightly Bruised"])
            price = st.number_input("Base Price ($)", value=4.00, step=0.50)
            
            submitted = st.form_submit_button("Update Inventory")
            
            if submitted:
                # Remove old duplicates for demo simplicity
                st.session_state.inventory = [i for i in st.session_state.inventory if i['name'] != name]
                
                # Add to session state inventory with unique ID
                new_item = {
                    "id": st.session_state.next_id,
                    "name": name,
                    "category": "Groceries",
                    "base_price": price,
                    "expiry": expiry,
                    "condition": condition,
                    "image": "🥑" if "Avocado" in name else "🥛" if "Milk" in name else "🍞"
                }
                st.session_state.next_id += 1  # Increment for next item
                st.session_state.inventory.insert(0, new_item) # Add to top
                st.success(f"✅ {name} updated in Live Database!")

    with col2:
        st.subheader("Live Inventory Database")
        st.markdown("This data feeds into the customer app real-time.")
        for item in st.session_state.inventory:
            status_color = "red" if "Critical" in item['expiry'] else "green"
            st.markdown(f"""
            <div style='padding: 10px; border: 1px solid #ddd; border-radius: 8px; margin-bottom: 10px; background: white;'>
                <b>{item['image']} {item['name']}</b> | 💲{item['base_price']} <br>
                <span style='color:{status_color}'>⏰ {item['expiry']}</span> | 📦 {item['condition']}
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# VIEW 2: CUSTOMER STOREFRONT (The App)
# ==========================================
elif app_mode == "🛒 Customer Storefront":
    st.title("🛒 EcoCart Shop")
    
    # --- PERSONA SWITCHER (The Magic Trick) ---
    st.markdown("### 👤 Who is shopping?")
    persona_col1, persona_col2, persona_col3 = st.columns(3)
    
    with persona_col1:
        if st.button("👩‍🎓 Student (Budget)", use_container_width=True):
            st.session_state.current_user = {"type": "Student", "history": "Mostly Full Price (Loyal)"}
    with persona_col2:
        if st.button("🕵️ Deal Hunter (Strategic)", use_container_width=True):
            st.session_state.current_user = {"type": "Strategic", "history": "Always Waits for Discounts"}
    with persona_col3:
        if st.button("👑 Loyal Customer (Premium)", use_container_width=True):
            st.session_state.current_user = {"type": "Loyal", "history": "Mostly Full Price (Loyal)"}

    # Default if not selected
    if 'current_user' not in st.session_state:
        st.session_state.current_user = {"type": "Student", "history": "Mostly Full Price (Loyal)"}
    
    user = st.session_state.current_user
    st.info(f"Viewing store as: **{user['type']}** (History: {user['history']})")
    
    st.markdown("---")
    
    # --- PRODUCT GRID ---
    # We trigger the AI Pricing Engine for displayed items
    
    cols = st.columns(3)
    
    for index, item in enumerate(st.session_state.inventory):
        with cols[index % 3]:
            # CALL AI FOR DYNAMIC PRICING
            pricing = calculate_dynamic_price(item, user['type'], user['history'])
            
            # Fallback if AI pricing fails
            if pricing is None:
                pricing = {
                    "final_price": item['base_price'],
                    "discount_percent": 0,
                    "tagline": "Standard Price"
                }
            
            # CARD UI
            with st.container():
                st.markdown(f"""
                <div class="product-card">
                    <div style="font-size: 3rem; text-align: center;">{item['image']}</div>
                    <h3>{item['name']}</h3>
                    <p style="color: #666; font-size: 0.9rem;">
                        ⏰ {item['expiry']} <br> 📦 {item['condition']}
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                # Dynamic Price Display
                if pricing['discount_percent'] > 0:
                    st.markdown(f"""
                    <div>
                        <span class="discount-tag">🔥 {pricing['discount_percent']}% OFF</span>
                        <div style="margin-top: 5px;">
                            <span style="text-decoration: line-through; color: #999;">${item['base_price']}</span>
                            <span class="price-tag" style="color: #00D26A;"> ${pricing['final_price']}</span>
                        </div>
                        <p style="color: #00D26A; font-size: 0.8rem; margin-top:5px;"><i>"{pricing['tagline']}"</i></p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div>
                        <div style="margin-top: 5px;">
                            <span class="price-tag">${item['base_price']}</span>
                        </div>
                         <p style="color: #666; font-size: 0.8rem; margin-top:5px;"><i>"{pricing['tagline']}"</i></p>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.button(f"Add to Cart", key=f"btn_{item['id']}")