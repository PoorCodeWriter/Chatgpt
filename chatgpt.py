import openai

openai.api_key = "API-KEY"
while True:
    x = input("Ask me anything: ")
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": x}])
    print(completion.choices[0].message.content)
    var = True
