# 🛒 YieldSense AI: Behavioral Dynamic Pricing

Turning Retail Waste into Strategic Revenue using High-Speed AI Inference.

## 🌟 The Vision

Every year, grocery retailers lose billions of dollars to food waste. The standard solution—a flat "50% OFF" sticker—creates a Perverse Incentive: frequent shoppers become "Strategic Consumers" who stop buying at full price and wait for the stickers, destroying retailer margins.

YieldSense AI breaks this cycle. By using LLMs to analyze inventory health alongside consumer personas, we determine not just if a discount should be given, but to whom and when. We save food while protecting the bottom line.

## ✨ Key Features

### 🏪 Seller Dashboard (Backend)

**Inventory Health Monitoring:** Managers input product status, including expiry windows (from 1 week down to 4 hours) and physical condition (perfect, dented, or bruised).

**Live Database Sync:** Real-time updates that feed directly into the consumer-facing storefront.

### 🛒 Customer Storefront (Frontend)

**Persona-Based Pricing:** The AI identifies the shopper (e.g., Student, Loyal Customer, or Deal Hunter) and adjusts prices in real-time.

**AI Marketing Hooks:** Instead of just showing a price, the AI generates personalized taglines (e.g., "Save this avocado for a perfect guacamole tonight!") to increase conversion.

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

- **Framework:** Streamlit
- **AI Model:** llama-3.3-70b-versatile via Groq Cloud
- **Language:** Python 3.10+
- **Styling:** Custom CSS Injection for a mobile-app aesthetic

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.10 or higher
- A Groq API Key

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

### 3. Environment Variables

To run the app securely, create a `.streamlit/secrets.toml` file or set your key in the Streamlit Cloud Dashboard:

```toml
GROQ_API_KEY = "your_gsk_key_here"
```

## 🛡️ License

Distributed under the MIT License. See LICENSE for more information.

---

Built for the Gemini 3 Hackathon to solve global food waste through Behavioral AI.
