import sys
import json

# Input lists
dist_list = ['AHMEDNAGAR', 'AKOLA', 'AMRAVATI', 'AURANGABAD', 'BEED', 'BHANDARA', 
             'BULDHANA', 'CHANDRAPUR', 'DHULE', 'GADCHIROLI', 'GONDIA', 'HINGOLI', 
             'JALGAON', 'JALNA', 'KOLHAPUR', 'LATUR', 'NAGPUR', 'NANDED', 
             'NASHIK', 'OSMANABAD', 'PARBHANI', 'PUNE', 'SANGLI', 'SATARA', 
             'THANE', 'WARDHA', 'WASHIM', 'YAVATMAL']

crop_list = ['Jowar', 'Bajra', 'Wheat']
soil_list = ['chalky', 'clay', 'loamy', 'sandy', 'silty']

# Get input from PHP
district = sys.argv[1]
crop = sys.argv[2]
area = int(sys.argv[3])
soil = sys.argv[4]

# Validation and Prediction Logic
if district not in dist_list:
    print(json.dumps({"error": "Invalid district."}))
elif crop not in crop_list:
    print(json.dumps({"error": "Invalid crop."}))
elif soil not in soil_list:
    print(json.dumps({"error": "Invalid soil type."}))
elif area <= 0:
    print(json.dumps({"error": "Area must be greater than zero."}))
else:
    # Example prediction logic (modify as needed)
    if crop == 'Jowar':
        yield_prediction = area * 30  # Example yield factor for Jowar
    elif crop == 'Bajra':
        yield_prediction = area * 25  # Example yield factor for Bajra
    elif crop == 'Wheat':
        yield_prediction = area * 20  # Example yield factor for Wheat

    print(json.dumps({"predicted_yield": yield_prediction}))
