import requests
import numpy as np
from PIL import Image

# 1. Load image
img = Image.open("test.jpg").resize((256, 256))
img_array = np.array(img) / 255.0

# 2. Add batch dimension
payload = {
    "instances": [img_array.tolist()]
}

# 3. Send request
url = "http://localhost:8502/v1/models/model:predict"
response = requests.post(url, json=payload)

# 4. Print result
print(response.json())