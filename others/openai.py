
import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  temperature = 0.2,
  max_tokens = 1000,
  messages = [
    {"role": "user", "content": "Who won the 2018 FIFA world cup?"}
  ]
)

print(response['choices'][0]['message']['content'])