import requests
from bs4 import BeautifulSoup


def get_avito_reviews(profile_url):
    response = requests.get(profile_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    reviews = soup.find_all('div', class_='feedback-item')  # Пример класса для отзыва, подставьте свой

    data = []
    for review in reviews:
        item_name = review.find('a', class_='item-link').text.strip()
        review_count = review.find('span', class_='review-count').text.strip()
        data.append({'item_name': item_name, 'review_count': review_count})

    return data


def update_text_file(data, profile_url):
    profile_name = profile_url.split("/")[-1]  # Извлекаем название из ссылки профиля
    file_name = f"{profile_name}_data.txt"

    with open(file_name, "a", encoding="utf-8") as file:
        for entry in data:
            line = f"{entry['item_name']} - {entry['review_count']}\n"
            file.write(line)


profile_url = "https://avito.ru/user/profile/username"
reviews_data = get_avito_reviews(profile_url)
update_text_file(reviews_data, profile_url)