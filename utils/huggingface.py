import requests

API_URL = "https://api-inference.huggingface.co/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
headers = {
    "Authorization": "Bearer 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"
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

response = query({
    "inputs": "Qual a capital da França?"
})

print(response)
