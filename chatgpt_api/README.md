# Introduction to ChatGPT API
<br></br>

## API 발급
- [OpenAI](https://platform.openai.com/)에 접속 후, API 발급 필요
- 우측 내정보 클릭 > View API keys > Create new secret key
- Pricing 관련 참조 : [https://openai.com/pricing](https://openai.com/pricing)
<br>

## Python ChatGPT API Guide
- [tutorial](https://holypython.com/python-api-tutorial/openai-gpt-4-api-quick-guide/)
<br>

## ChatGPT Arguments
- openai.ChatCompletion.create의 Argument는 [tutorial](https://holypython.com/python-api-tutorial/learn-openai-official-chatgpt-api-comprehensive-developer-tutorial/) 참조
<br>

## ChatGPT API에서 제공하는 ChatGPT Model
- 참조 : [stackoverflow](https://stackoverflow.com/questions/75773786/cant-access-gpt-4-model-via-python-api-although-gpt-3-5-works)
```python
import openai
openai.api_key = "OPENAI_API_KEY"

def list_all_models():
    model_list = openai.Model.list()['data']
    model_ids = [x['id'] for x in model_list if x['id'].upper().find('GPT')>=0]
    model_ids.sort()
    display(model_ids)

if __name__ == '__main__':
    list_all_models()
```