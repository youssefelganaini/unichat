from newscatcherapi import NewsCatcherApiClient
import json

newscatcher = NewsCatcherApiClient(
    x_api_key="gKJh_YJ67CU56KKyBZ8UzBNNMhXcQFhZ9WHVZ21_tXM"
)

# extra_outlets = "foxnews.com,abcnews.go.com,wsj.com,independent.co.uk,huffpost.com,usatoday.com,cbsnews.com,telegraph.co.uk,npr.org"
news_outlets = {
    "news_outlets_politics_en": "theguardian.com,nytimes.com,bbc.co.uk,cnn.com,reuters.com,politico.com,washingtonpost.com,aljazeera.com,apnews.com,bloomberg.com,nbcnews.com",
    "news_outlets_politics_de": "sueddeutsche.de,zeit.de,tagesschau.de,faz.net,handelsblatt.com,stern.de,welt.de,focus.de,n-tv.de",
    "news_outlets_finance_de": "handelsblatt.com,boersen-zeitung.de,finanzundwirtschaft.ch,wiwo.de,manager-magazin.de,boerse.ard.de,dasmaklermagazin.de,capital.de,deutsche-boerse.com,bloomberg.com/de",
    "news_outlets_finance_en": "cnbc.com,bloomberg.com,wsj.com,reuters.com,ft.com,cnbc.co.uk,investing.com,businessinsider.com,business-standard.com,marketwatch.com",
    "news_outlets_sport_en": "espn.com,bbc.co.uk/sport,skysports.com,goal.com,cbssports.com,sportingnews.com,bleacherreport.com,talksport.com,theguardian.com/football,eurosport.com",
    "news_outlets_sport_de": "kicker.de,sportbild.bild.de,spox.com,sportschau.de,sport1.de,transfermarkt.de,ran.de,fussballtransfers.com,sport.de,sportal.de",
}


def searchNews(keyword, language):
    json_result = newscatcher.get_search(
        q=keyword,
        lang=language,
        from_="1 week ago",
        # sources=news_outlets,
        sort_by="relevancy",
    )

    with open("./returnValue_3.json", "w", encoding="utf-8") as file:
        json.dump(json_result, file)


def searchHeadlines(countries: str, topic: str, news_outlets):
    json_result = newscatcher.get_latest_headlines_all_pages(
        when="24h",
        topic=topic,
        countries=countries,
        sources=news_outlets,
    )

    data_excerpt = json_result["articles"][0:10]
    prompt_data = {"articles": {}}
    for article in data_excerpt:
        prompt_data["articles"][article["title"]] = article["summary"]

    with open("./returnValue_4.json", "w", encoding="utf-8") as file:
        json.dump(json_result, file, ensure_ascii=False)

    with open("./returnValue_5.json", "w", encoding="utf-8") as file_1:
        json.dump(prompt_data, file_1, ensure_ascii=False)

    return prompt_data


# searchNews("", "en")
