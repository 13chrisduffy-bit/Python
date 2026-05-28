import requests
def AskGpt(question):
    gptkey = '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'
    url = 'https://api.openai.com/v1/responses'
    payload = {
        "model": "gpt-5.5",
        "instructions": "Talk like a pirate who is an expert in comedy",
        "input": question
    }
    headers = {
        "Authorization": f"Bearer {gptkey}"
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    return data['output'][1]['content'][0]['text']
