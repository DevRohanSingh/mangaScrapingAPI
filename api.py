from flask import Flask, jsonify, render_template
from flask_bootstrap import Bootstrap4
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
bootstrap = Bootstrap4(app)

HEADERS = {  
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,ar;q=0.6,hi;q=0.5"
}

# Fetch the webpage content
def get_soup(url):
    res = requests.get(url, headers=HEADERS)
    comic_page = res.text
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(comic_page, "lxml")
    return soup


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hot')
def get_hottest():
    soup = get_soup('https://manganato.com/genre-all?type=topview')
    hottest_comics = soup.find_all(class_='content-genres-item')   # list of html elements
    all_comics = []  # list of dicts
    for item in hottest_comics:
        all_comics.append({
            'title': item.find(name='a').get('title'),
            'id': item.find(name='a').get('href').split('/')[-1],  # slug: manga-ax951880
            # 'link': item.find(name='a').get('href'),
            'thumb': item.find(name='img').get('src'),
            # 'about': item.find(class_='genres-item-description').text.strip(),
            # 'author': item.find(class_='genres-item-author').text
        })
    return jsonify(all_comics)

@app.route('/today')
def get_latest():
    soup = get_soup('https://manganato.com/')
    latest_comics = soup.find_all(class_='content-homepage-item')   # list of html elements
    all_comics = []  # list of dicts
    for item in latest_comics:
        all_comics.append({
            'title': item.find(name='a').get('title'),
            'thumb': item.find(name='img', class_='img-loading').get('src'),
            'id': item.find(name='a').get('href').split('/')[-1],  # slug: manga-ax951880
        })
    return jsonify(all_comics)

# '/id': Returns a single comic's information by id
# Eg: /manga-ax951880
@app.route('/<string:id>')
def get_comic_info(id):
    soup = get_soup(f"https://chapmanganato.to/{id}")
    comic = soup.find(name='div', class_='panel-story-info')   # list of html elements
    if comic is None:
        return jsonify({'error': 'Comic not found'})
    return jsonify({
        'title': comic.find('h1').text,
        'about': comic.select_one('.panel-story-info-description').contents[-1].strip(),
        'genre': [genre.text for genre in comic.select(selector='.table-value .a-h') if genre.get('href').startswith('https://manganato.com/genre')],
        'thumb': comic.find(class_='img-loading').get('src'),
    })

# '/id/episodes': returns the latest episodes for a comic by id
@app.route('/<string:id>/episodes')
def get_comic_chapters(id):
    soup = get_soup(f'https://chapmanganato.to/{id}')
    thumb = soup.select_one('.info-image .img-loading').get('src')
    chapter_tags = soup.find(class_='row-content-chapter').find_all(name='li', class_='a-h')
    if chapter_tags is None:
        return jsonify({'error': 'Comic not found'})
    comic_chapters = []
    for tag in chapter_tags:
        comic_chapters.append({
            'thumb': thumb,
            'id': id,
            'link': tag.find(name='a', class_='chapter-name').get('href'),
            'title': tag.find(name='a', class_='chapter-name').text,
            'view': tag.find(name='span', class_='chapter-view').text,
            'date': tag.find(name='span', class_='chapter-time').text,
        })
    return jsonify(comic_chapters)


if __name__ == '__main__':
    app.run()
