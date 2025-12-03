from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("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"))
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! What is AI?"}
    ]
)
print(completion.choices[0].message.content)


