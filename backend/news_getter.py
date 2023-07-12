from newsapi import NewsApiClient
import json
from datetime import datetime, timedelta

newsapi = NewsApiClient(api_key="4354ec4ed00746c9adc69751cfc8e0e6")

fashion_keywords = (
    "Fashion,Style,Design,Clothing,Trends,Runway,Fashion industry,Fashion week"
)

business_keywords = "Business,Economy,Finance,Stock market,Entrepreneurship,Corporate,Market analysis,Investments"
politics_keywords = "+Politics OR Government OR Elections OR Legislation OR Political parties OR International relations OR Public policy OR Diplomacy OR tensions"
sports_keywords = "Sports,Football,Basketball,Tennis,Soccer,Baseball,Olympics,Athletes"
technology_keywords = "Technology,Gadgets,Innovation,Artificial intelligence,Internet,Tech industry,Cybersecurity,Startups"
entertainment_keywords = "Entertainment,Celebrities,Movies,Music,Television,Hollywood,Pop culture,Celebrity gossip"
health_keywords = "Health,Wellness,Medicine,Nutrition,Fitness,Mental health,Healthcare,Medical research"
science_keywords = "Science,Research,Discoveries,Space,Technology advancements,Scientific studies,Innovation,Environment"
environment_keywords = "Environment,Climate change,Sustainability,Conservation,Renewable energy,Pollution,Wildlife,Environmental policy"
world_news_keywords = "World news,International news,Global affairs,Breaking news,Current events,Global politics,Major world events,World economy"


def get_headlines(keywords: str, language: str):
    # yesterday = datetime.now() - timedelta(1)
    json_return = newsapi.get_everything(
        q=keywords,
        language=language,
        page_size=100,
        sources="independent",
        # from_param=yesterday,
        sort_by="popularity",
    )
    with open("./returnValue.json", "w", encoding="utf-8") as file:
        json.dump(json_return, file)


# get_headlines(politics_keywords, "en")


def get_top_headlines(keywords: str, language: str, country: str, category: str):
    json_return = newsapi.get_top_headlines(
        # q=keywords,
        # language=language,
        page_size=100,
        # from_param=yesterday,
        country=country,
        # category=category,
    )
    with open("./returnValue_2.json", "w", encoding="utf-8") as file:
        json.dump(json_return, file, ensure_ascii=False)


get_top_headlines(None, "en", "us", None)
