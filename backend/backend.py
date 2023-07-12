from fastapi import FastAPI
import os
import openai
from news_catcher import searchHeadlines

app = FastAPI()
content = ""


@app.get("/prompt")
def getContentFromChatGPT(country: str, topic: str, news_outlets: str, language: str):
    prompt_data = searchHeadlines(
        countries=country, topic=topic, news_outlets=news_outlets
    )

    openai.api_key = os.getenv("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")

    prompt_intro = f"You are now writing a newsletter. The mission of this newsletter is to create a summary so that every person reading it stays informed about the most important news about {topic}. You have a python dict consisting of the title and the respective summary of the article. Create a newsletter consisting of the following sections: 1) 3 things you need to know about what happened yesterday 2) 2 Things that you need to follow-up on in the next period, 1) 1 question to think about. The resulting text should be in {language}"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt_intro + "\n" + prompt_data,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.5,
    )

    content = response

@app.post("/addUser/{email}/{category}/{keywords}/{language}/{country}")
def addUser():
    
