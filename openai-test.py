from openai import OpenAI
import os
from rich import print

client = OpenAI()

query = "你知道朱威達是誰嗎"
temperature = 0
print('query:',query)
print('========================================')
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        { "role": "system", "content": "你是一位媽咪，總是用耐心和愛心回答女鵝跟鵝子的問題，用尊重且溫柔的口吻對話。" },
        {"role": "user", "content": query}
    ],
    temperature=temperature
)

print(f'gpt-4o-mini回覆:{completion.choices[0].message.content}')

print('========================================')

completion = client.chat.completions.create(
    model="ft:gpt-4o-mini-2024-07-18:gdg-on-campus-ncku::AcDl4vvp",
    messages=[
        { "role": "system", "content": "你是一位媽咪，總是用耐心和愛心回答女鵝跟鵝子的問題，用尊重且溫柔的口吻對話。" },
        {"role": "user", "content": query}
    ],
    temperature=temperature
)
print(f'微調後的 gpt-4o-mini 回覆:{completion.choices[0].message.content}')
