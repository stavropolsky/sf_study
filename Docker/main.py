import os
import requests

# Получаем URL сайта из переменной окружения
site_url = os.environ.get("SITE_URL")

if site_url:
    try:
        # Отправляем GET-запрос к сайту
        response = requests.get(site_url)

        # Проверяем успешность запроса
        if response.status_code == 200:
            # Ищем ссылку на favicon в HTML-коде страницы
            favicon_url = f"{site_url}/favicon.ico"

            # Скачиваем favicon
            favicon_response = requests.get(favicon_url)

            # Проверяем успешность скачивания
            if favicon_response.status_code == 200:
                # Сохраняем favicon в volume
                with open("/app/favicon.ico", "wb") as f:
                    f.write(favicon_response.content)
                    print("Favicon успешно сохранен.")
            else:
                print("Не удалось скачать favicon.")
        else:
            print("Ошибка при обращении к сайту.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
else:
    print("Пожалуйста, укажите переменную SITE_URL с адресом сайта.")
