import openai

MODEL = 'gpt-3.5-turbo-0301'
OPENAI_API_KEY = 'XXX'
openai.api_key = OPENAI_API_KEY

# 사용가능한 ChatGPT 모델 확인
def list_all_models():
    model_list = openai.Model.list()['data']
    model_ids = [x['id'] for x in model_list if x['id'].upper().find('GPT')>=0]
    model_ids.sort()
    display(model_ids)
    
list_all_models()

#--------------------------------------------------------------------------------------------------------------------------------#
# (1) Basic : 1회 응답, 대화형 X
#--------------------------------------------------------------------------------------------------------------------------------#
completion = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": "Where was the last Olympics held? Just tell me the year & country?"}
    ]
)
print(completion.choices[0].message.content)


#--------------------------------------------------------------------------------------------------------------------------------#
# (2) 대화형 API 호출 : 다회 응답, 대화형 O
#--------------------------------------------------------------------------------------------------------------------------------#
# - 'role':'user'로 질문 후, ChatGPT API의 응답을 'role':''
# - (참조) https://medium.com/mlearning-ai/using-chatgpt-api-to-ask-contextual-questions-within-your-application-a80b6a76da98

# - We call this function and pass the new question and the last messages
def get_message_memory(self,newquestion,lastmessage,model):
    # Append the new question to the last message
    lastmessage.append({"role": "user", "content": newquestion})

    msgcompletion = openai.ChatCompletion.create(
        model=MODEL,
        messages=lastmessage,
        timeout=self.timeout,
        #max_tokens=1000,
        #temperature=1.2,
    )

    # Print the new answer
    msgresponse = msgcompletion.choices[0].message.content
    #print(msgresponse)

    # We return the new answer
    return msgresponse

# list of question
question_list = [
    "Where was the last olympics held? Just tell me the year & country?",
    "Which country won the most medals in that? Just tell me the country name?",
    "How many medals did they win in that? Just tell me the number",
    "How many gold medals did they win in that? Just tell me the number",
]

# for loop by question_list
messages = []
answer_list = []
for question in tqdm(question_list):
    answer = get_message_memory(question, messages)
    messages.append({"role": "assistant", "content": answer})
    answer_list.append(answer)