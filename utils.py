import re
import requests


def get_raw_data(url):
    response = requests.get(url)
    return response.text


def extract_news(raw_data):
    pattern = r'(class="feed-post-link gui-color-primary gui-color-hover" elementtiming="text-ssr">[^<]+<\/a>)+((<\/div>){3}<div class="_label_event"><div class="feed-post-body-resumo" elementtiming="text-ssr">[^<]+<\/div>)?'
    news = re.findall(pattern, raw_data)
    cleaned_news = []
    for n in news:
        title, resume, _ = n
        title = title.split(">")[1].split("<")[0].strip() if title else ""
        resume = resume.split(">")[-2].split("<")[0].strip() if resume else ""
        cleaned_news.append({"title": title, "resume": resume})

    return cleaned_news


def get_news(url):
    raw_data = get_raw_data(url)
    cleaned_news = extract_news(raw_data)
    return cleaned_news
