import os
import openai
from backend.news_service.news_catcher import searchHeadlines
from backend.news_service.news_catcher import news_outlets
import tiktoken


def getContentFromChatGPTDaVinci(
    country: str, topic: str, news_outlets: str, language: str
):
    prompt_data = searchHeadlines(
        countries=country, topic=topic, news_outlets=news_outlets
    )

    openai.api_key = "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"

    prompt_intro = f"You are now writing a newsletter. The mission of this newsletter is to create a summary so that every person reading it stays informed about the most important news about {topic}. You have a python dict consisting of the title and the respective summary of the article. Create a newsletter consisting of the following sections: 1) 3 things you need to know about what happened yesterday 2) 2 Things that you need to follow-up on in the next period, 1) 1 question to think about. The resulting text should be in {language} "

    encoding = tiktoken.encoding_for_model("text-davinci-003")
    tokens = encoding.encode(prompt_intro + "\n" + str(prompt_data))
    token_amount = len(tokens)

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt_intro + "\n" + str(prompt_data),
        temperature=1,
        max_tokens=4097 - token_amount,
        top_p=1,
    )

    print(response)

    with open("contentValue.txt", "w", encoding="utf-8") as file:
        file.write(response["choices"][0]["text"])


def getContentFromChatGPTTurbo(
    country: str, topic: str, news_outlets: str, language: str
):
    prompt_data = searchHeadlines(
        countries=country, topic=topic, news_outlets=news_outlets
    )

    openai.api_key = "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"

    prompt_intro = f"You are now writing a newsletter. The mission of this newsletter is to create a summary so that every person reading it stays informed about the most important news about {topic}. You have a python dict consisting of the title and the respective summary of the article. Create a newsletter consisting of the following sections: 1) 3 things you need to know about what happened yesterday. This part should be a little descriptive. 2) 2 Things that you need to follow-up on in the next period, explaining why. 1) 1 question to reflect on in light of recent events. Correctness of statements is priority one. The resulting text should be in {language}. The newsletter should be a 3-5 minute read that is informative, interesting and a sound alternative to traditional ways of reading news."

    encoding = tiktoken.encoding_for_model("text-davinci-003")
    tokens = encoding.encode(prompt_intro + "\n" + str(prompt_data))
    token_amount = len(tokens)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt_intro + "\n" + str(prompt_data)}],
        presence_penalty=1,
        # max_tokens=4096 - token_amount,
    )

    print(response)

    with open("contentValue.txt", "w", encoding="utf-8") as file:
        file.write(response["choices"][0]["message"]["content"])


getContentFromChatGPTTurbo(
    "DE", "politics", news_outlets["news_outlets_politics_en"], "German"
)
