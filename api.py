import requests
from bs4 import BeautifulSoup
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

def scrape_medium_blog(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": "Failed to fetch the webpage"}
    
    soup = BeautifulSoup(response.text, "html.parser")
    main_container = soup.find("div", class_="l ae")
    
    if not main_container:
        return {"error": "No posts found inside the main container"}
    
    articles = main_container.find_all("article")
    data = []
    
    for index, article in enumerate(articles, start=1):
        title_tag = article.find("h2", class_="bf mj mk ml mm jt mn mo mp mq jy mr ka kb ms mt ke mu mv mw mx my mz na nb nc nd hh hj hk hm ho bk")
        title = title_tag.get_text(strip=True) if title_tag else "No title found"

        description_tag = article.find("h3", class_="bf b ge z hh nf hj hk ng hm ho ds")
        description = description_tag.get_text(strip=True) if description_tag else "No description found"

        url_tag = article.find("div", {"data-href": True})
        post_url = url_tag["data-href"] if url_tag else "No URL found"

        data.append({
            "pno": index,
            "title": title,
            "description": description,
            "url": post_url
        })
    
    return data

@app.route("/scrape", methods=["GET"])
def scrape_api():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400
    
    result = scrape_medium_blog(url)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
