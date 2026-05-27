import requests

gptkey = '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'
url = 'https://api.openai.com/v1/responses'
payload = {
    "model": "gpt-5.5",
    "input": "Tell me a really funny joke."
}
headers = {
    "Authorization": f"Bearer {gptkey}"
}

response = requests.post(
    url,
    headers=headers,
    json=payload
)

print(response.status_code)
print(response.json())