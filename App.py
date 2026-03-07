
from flask import Flask, render_template, request

app = Flask(__name__)

# Crop recommendation function
def recommend_crop(soil, weather, demand):
    soil_crops = {
        "loamy": ["Wheat", "Sugarcane", "Cotton"],
        "sandy": ["Millets", "Groundnuts"],
        "clay": ["Rice", "Soybean", "Potato"]
    }
    
    weather_conditions = {
        "hot": ["Millets", "Cotton", "Maize"],
        "humid": ["Rice", "Banana", "Coconut"],
        "rainy": ["Tea", "Coffee", "Rubber"],
        "dry": ["Wheat", "Mustard", "Pulses"]
    }
    
    market_demand = {
        "high": ["Wheat", "Rice", "Soybean"],
        "medium": ["Maize", "Sugarcane", "Potato"],
        "low": ["Quinoa", "Dragon Fruit", "Olives"]
    }

    crop_suggestions = set()
    
    if soil in soil_crops:
        crop_suggestions.update(soil_crops[soil])

    if weather in weather_conditions:
        crop_suggestions.update(weather_conditions[weather])

    if demand in market_demand:
        crop_suggestions.update(market_demand[demand])

    return list(crop_suggestions) if crop_suggestions else ["No recommendation available"]

# Fertilizer recommendation function
fertilizer_data = {
    "Rice": ["Urea", "Potassium Nitrate"],
    "Wheat": ["DAP", "Ammonium Sulfate"],
    "Cotton": ["NPK", "Calcium Nitrate"],
    "Maize": ["Super Phosphate", "Zinc Sulfate"]
}

def recommend_fertilizers(crops):
    fertilizers = []
    for crop in crops:
        fertilizers.extend(fertilizer_data.get(crop, ["No fertilizers available"]))
    return fertilizers

# Translations for multi-language support
translations = {
    "english": {
        "title": "Crop Recommendation System",
        "soil_type": "Soil Type:",
        "weather": "Weather Condition:",
        "market_demand": "Market Demand:",
        "recommendation_button": "Get Recommendation",
        "fertilizer_label": "Recommended Fertilizers:",
        "soil_options": {"loamy": "Loamy", "sandy": "Sandy", "clay": "Clay"},
        "weather_options": {"hot": "Hot", "humid": "Humid", "rainy": "Rainy", "dry": "Dry"},
        "demand_options": {"high": "High", "medium": "Medium", "low": "Low"},
        "crop_names": {
            "Wheat": "Wheat", "Rice": "Rice", "Millets": "Millets", "Cotton": "Cotton",
            "Sugarcane": "Sugarcane", "Groundnuts": "Groundnuts", "Potato": "Potato",
            "Tea": "Tea", "Coffee": "Coffee", "Banana": "Banana", "Soybean": "Soybean",
            "Maize": "Maize", "Rubber": "Rubber", "Quinoa": "Quinoa", "Dragon Fruit": "Dragon Fruit",
            "Olives": "Olives", "Mustard": "Mustard", "Pulses": "Pulses"
        },
        "fertilizers": {
            "Urea": "Urea", "Potassium Nitrate": "Potassium Nitrate",
            "DAP": "DAP", "Ammonium Sulfate": "Ammonium Sulfate",
            "NPK": "NPK", "Calcium Nitrate": "Calcium Nitrate",
            "Super Phosphate": "Super Phosphate", "Zinc Sulfate": "Zinc Sulfate",
            "No fertilizers available": "No fertilizers available"
        }
    },
    "hindi": {
        "title": "फसल सिफारिश प्रणाली",
        "soil_type": "मिट्टी का प्रकार:",
        "weather": "मौसम की स्थिति:",
        "market_demand": "बाजार की मांग:",
        "recommendation_button": "सिफारिश प्राप्त करें",
        "fertilizer_label": "अनुशंसित खाद:",
        "soil_options": {"loamy": "दोमट", "sandy": "बलुई", "clay": "चिकनी"},
        "weather_options": {"hot": "गर्म", "humid": "आर्द्र", "rainy": "बरसाती", "dry": "शुष्क"},
        "demand_options": {"high": "उच्च", "medium": "मध्यम", "low": "कम"},
        "crop_names": {
            "Wheat": "गेहूं", "Rice": "चावल", "Millets": "ज्वार", "Cotton": "कपास",
            "Sugarcane": "गन्ना", "Groundnuts": "मूंगफली", "Potato": "आलू",
            "Tea": "चाय", "Coffee": "कॉफ़ी", "Banana": "केला", "Soybean": "सोयाबीन",
            "Maize": "मक्का", "Rubber": "रबर", "Quinoa": "क्विनोआ", "Dragon Fruit": "ड्रैगन फ्रूट",
            "Olives": "जैतून", "Mustard": "सरसों", "Pulses": "दालें"
        },
        "fertilizers": {
            "Urea": "यूरिया", "Potassium Nitrate": "पोटैशियम नाइट्रेट",
            "DAP": "डीएपी", "Ammonium Sulfate": "अमोनियम सल्फेट",
            "NPK": "एनपीके", "Calcium Nitrate": "कैल्शियम नाइट्रेट",
            "Super Phosphate": "सुपर फॉस्फेट", "Zinc Sulfate": "जिंक सल्फेट",
            "No fertilizers available": "कोई उर्वरक उपलब्ध नहीं है"
        }
    },
    "telugu": {
        "title": "పంటల సిఫార్సు వ్యవస్థ",
        "soil_type": "మట్టి రకం:",
        "weather": "వాతావరణ పరిస్థితి:",
        "market_demand": "మార్కెట్ డిమాండ్:",
        "recommendation_button": "సిఫారసు పొందండి",
        "fertilizer_label": "సిఫారసు చేసిన ఎరువులు:",
        "soil_options": {"loamy": "లోమీ", "sandy": "ఇసుక", "clay": "మట్టి"},
        "weather_options": {"hot": "వెచ్చగా", "humid": "తేమగా", "rainy": "వర్షం", "dry": "పొడి"},
        "demand_options": {"high": "అధిక", "medium": "మధ్యస్థ", "low": "తక్కువ"},
        "crop_names": {
            "Wheat": "గోధుమ", "Rice": "బియ్యం", "Millets": "జొన్నలు", "Cotton": "పత్తి",
            "Sugarcane": "చెరుకు", "Groundnuts": "పల్లీలు", "Potato": "బంగాళాదుంప",
            "Tea": "టీ", "Coffee": "కాఫీ", "Banana": "అరటి", "Soybean": "సోయాబీన్",
            "Maize": "మొక్కజొన్న", "Rubber": "రబ్బర్", "Quinoa": "క్వినోవా", "Dragon Fruit": "డ్రాగన్ ఫ్రూట్",
            "Olives": "ఒలివ్స్", "Mustard": "ఆవాలు", "Pulses": "పప్పులు"
        },
        "fertilizers": {
            "Urea": "యూరియా", "Potassium Nitrate": "పోటాషియం నైట్రేట్",
            "DAP": "డీఎపీ", "Ammonium Sulfate": "అమోనియం సల్ఫేట్",
            "NPK": "ఎన్పికె", "Calcium Nitrate": "క్యాల్సియం నైట్రేట్",
            "Super Phosphate": "సూపర్ ఫాస్ఫేట్", "Zinc Sulfate": "జింక్ సల్ఫేట్",
            "No fertilizers available":  "ఎరువులు లభ్యం కావు"

        }
    }
}

@app.route('/')
def home():
    selected_language = request.args.get('lang', 'english')  # Default to English
    lang_content = translations[selected_language]
    return render_template('index.html', lang_content=lang_content)

@app.route('/recommend', methods=['POST'])
def recommend():
    soil_type = request.form['soil_type']
    weather_condition = request.form['weather']
    market_trend = request.form['demand']
    selected_language = request.form.get('lang', 'english')

    recommended_crops = recommend_crop(soil_type, weather_condition, market_trend)
    recommended_crops_translated = [
        translations[selected_language]["crop_names"].get(crop, crop) for crop in recommended_crops
    ]

    recommended_fertilizers = recommend_fertilizers(recommended_crops)
    recommended_fertilizers_translated = [
        translations[selected_language]["fertilizers"].get(fertilizer, fertilizer) for fertilizer in recommended_fertilizers
    ]
    
    return render_template('result.html', lang_content=translations[selected_language], 
                           crops=recommended_crops_translated, fertilizers=recommended_fertilizers_translated)

if __name__ == '__main__':
    app.run(debug=True)
