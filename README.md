# 🛒 YieldSense AI: Behavioral Dynamic Pricing

**Powered by Google Gemini AI & Groq** | Turning Retail Waste into Strategic Revenue

> 🏆 Built for Google Gemini API Developer Competition - Addressing Global Food Waste Through AI

## 🌟 The Vision

Every year, grocery retailers lose billions of dollars to food waste. The standard solution—a flat "50% OFF" sticker—creates a Perverse Incentive: frequent shoppers become "Strategic Consumers" who stop buying at full price and wait for the stickers, destroying retailer margins.

YieldSense AI breaks this cycle. By leveraging **Google Gemini Pro** and LLMs to analyze inventory health alongside consumer personas, we determine not just if a discount should be given, but to whom and when. We save food while protecting the bottom line.

## ✨ Key Features

### 🤖 Google Gemini AI Integration - The Innovation Core

**🍳 AI-Powered Recipe Generator:** Our flagship Gemini Pro feature analyzes current inventory and generates personalized recipe ideas that prioritize items nearing expiry. This innovative approach:
- Transforms "near-expiry" perception from negative to positive
- Helps customers discover creative ways to use discounted items immediately
- Reduces food waste by suggesting recipes before products expire
- Creates value beyond pricing alone - "dinner inspiration at your fingertips"
- Generates 3 quick recipes (under 30 minutes) tailored to available stock
- Smart prioritization: items with shorter shelf life appear first in suggestions

**Real-World Impact:** When a customer sees milk expiring in 2 days and bruised avocados at 40% off, Gemini suggests: *"Creamy Avocado Smoothie Bowl - 10 mins, perfect for breakfast! Uses your discounted milk and avocados."*

### 🏪 Seller Dashboard (Backend)

**Inventory Health Monitoring:** Managers input product status, including expiry windows (from 1 week down to 4 hours) and physical condition (perfect, dented, or bruised).

**Live Database Sync:** Real-time updates that feed directly into the consumer-facing storefront.

### 🛒 Customer Storefront (Frontend)

**Persona-Based Pricing:** The AI identifies the shopper (e.g., Student, Loyal Customer, or Deal Hunter) and adjusts prices in real-time.

**AI Marketing Hooks:** Instead of just showing a price, the AI generates personalized taglines (e.g., "Save this avocado for a perfect guacamole tonight!") to increase conversion.

**Gemini-Powered Inspiration:** One-click access to recipe ideas that make near-expiry items desirable instead of undesirable.

## 🧠 The Brain: Behavioral Pricing Model

Unlike traditional linear markdown algorithms, YieldSense utilizes Llama 3.3 70B to calculate a "Yield Potential." The pricing logic follows this heuristic:

$$P_f = P_b \times (1 - (E_r \cdot C_s \cdot H_u))$$

Where:

- $P_f$: Final Price
- $P_b$: Base Price
- $E_r$: Expiry Risk (Time-weighted decay)
- $C_s$: Condition Score (Physical integrity)
- $H_u$: User History Multiplier (To prevent training users to wait for deals)

## 🛠️ Technical Stack

### Core AI Models
- **🌟 Google Gemini Pro:** Primary AI engine for recipe generation and food waste reduction strategies
- **Groq Cloud (Llama 3.3 70B):** High-speed inference for real-time behavioral pricing calculations

### Infrastructure
- **Framework:** Streamlit (Interactive web application)
- **Language:** Python 3.10+
- **APIs:** Google Generative AI SDK, Groq API
- **Styling:** Custom CSS injection for mobile-app aesthetic

### Why Dual AI Architecture?
- **Gemini Pro:** Excels at creative content generation (recipes, meal planning) and understanding complex food combinations
- **Llama 3.3 (via Groq):** Optimized for sub-second pricing calculations with structured JSON output
- **Result:** Best-of-both-worlds - creative intelligence + computational speed

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.10 or higher
- **Google Gemini API Key** ([Get it here](https://aistudio.google.com/app/apikey))
- Groq API Key ([Get it here](https://console.groq.com/keys))

### 2. Local Installation

```bash
# Clone the repository
git clone https://github.com/harshwannawin/yieldsense-ai.git
cd yieldsense-ai

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### 3. Configure API Keys

**For Local Development:**

Create a `.streamlit/secrets.toml` file in the project root:

```toml
GEMINI_API_KEY = "your_gemini_api_key_here"
GROQ_API_KEY = "your_groq_api_key_here"
```

**For Streamlit Cloud Deployment:**

1. Go to your app dashboard on Streamlit Cloud
2. Click "⚙️ Settings" → "Secrets"
3. Add the following:
```toml
GEMINI_API_KEY = "your_gemini_api_key_here"
GROQ_API_KEY = "your_groq_api_key_here"
```

**Important:** Both API keys are required for full functionality:
- **Gemini:** Powers the recipe suggestions feature
- **Groq:** Handles real-time pricing calculations

**Note:** The `.streamlit/` directory is already in `.gitignore` to keep your secrets safe.

## 🎯 Google Gemini API Integration Details

### How We Use Gemini Pro

YieldSense leverages Google Gemini Pro's advanced natural language and reasoning capabilities to solve a critical problem: **making near-expiry food desirable instead of undesirable**.

**Technical Implementation:**
```python
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Generate contextual recipes based on inventory
response = model.generate_content(prompt_with_inventory_data)
```

**Key Use Cases:**
1. **Recipe Discovery:** Analyzes available inventory (names, conditions, expiry times) and generates practical recipes
2. **Waste Reduction Logic:** Prioritizes items with shorter shelf life in recipe suggestions
3. **User-Friendly Output:** Provides cooking time, ingredients, and descriptions that make discounted items appealing

**Why Gemini for This Task?**
- **Contextual Understanding:** Recognizes food combinations and dietary patterns
- **Creative Generation:** Creates engaging, practical recipes that inspire action
- **Speed:** Fast enough for real-time user interactions
- **Reliability:** Consistent quality output for user-facing features

### Hackathon Alignment: Food Waste Crisis

**Global Impact:**
- 🌍 1.3 billion tons of food wasted annually
- 💰 $1 trillion in economic losses
- 🌡️ 8-10% of global greenhouse gas emissions

**Our Gemini-Powered Solution:**
- Transforms "waste" into "opportunity" through AI-generated recipes
- Behavioral pricing + creative inspiration = 2x waste reduction potential
- Scalable to any grocery retailer globally

## 🛡️ License

Distributed under the MIT License. See LICENSE for more information.

---

**🏆 Built for Google Gemini API Developer Competition**  
*Leveraging Gemini Pro to tackle the $1 trillion global food waste crisis through intelligent recipe generation and behavioral economics.*
