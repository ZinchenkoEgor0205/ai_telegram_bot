import openai

messages = []


async def answer_the_question(message, key, username):
    openai.api_key = key
    answer = 'something went wrong'
    try:
        messages.append({
            'role': 'user',
            'content': message
        })
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages
        )
        answer = response['choices'][0]['message']['content']
        messages.append({
            'role': 'assistant',
            'content': answer
        })
    except Exception as err:
        print(err)

    return answer
