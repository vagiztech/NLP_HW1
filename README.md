# Вступление
Был сделан веб-сервис на Flask, который принимает сообщение от пользователя, передаёт его в функцию find_best_reply и возвращает ответ от имени Грегори Хауса. Интерфейс простенький, сверху находится область для вывода ответа, а внизу — форма с полем для ввода текста и кнопкой «Отправить».

Подготовка данных из все CSV-файлы с диалогами и объединили их в один DataFrame.

Привел текст к нижнему регистру, убрал лишние знаки, выполнили токенизацию, убрал стоп-слова и сделали стемминг. Это помогло нормализовать данные.

На основе обработанных реплик создал матрицу с помощью TfidfVectorizer для дальнейшего поиска.

Функция find_best_reply принимает запрос пользователя, также предобрабатывает его, считает TF-IDF вектор и определяет самую похожую реплику по косинусному сходству.

Создал приложение Flask с одним маршрутом ("/"). При GET запросе отдается страница с формой, а при POST — берется сообщение из формы, передается в find_best_reply и результат возвращается на страницу.

Запустив приложение, можно перейти в браузере по адресу http://46.8.226.51:5000 и попробовать отправить какой-нибудь текст. Ответ от функции сразу отобразится на странице.

Боле побробно о ходе эксперемента можно прочесть в HouseMD.ipynb


# Инструкция по запуску

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-chatbot
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

5. **Run the Flask application:**
   ```
   flask run
   ```

6. **Access the web service:**
   Open your web browser and go to `http://127.0.0.1:5000`.



# Flask Chatbot

This project is a simple Flask web service that utilizes a dialogue processing function to provide responses based on user input. The service is designed to mimic a chat interface similar to ChatGPT.

## Project Structure

```
flask-chatbot
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── static
│   │   └── style.css
│   └── templates
│       └── index.html
├── housemd.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-chatbot
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

5. **Run the Flask application:**
   ```
   flask run
   ```

6. **Access the web service:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- Enter your message in the text input field and click the submit button.
- The application will process your message and display the best reply based on the dialogue data.

## Dependencies

- Flask
- pandas
- nltk
- scikit-learn

Make sure to check the `requirements.txt` file for the complete list of dependencies.