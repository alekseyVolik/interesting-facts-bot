## About project

['_On this day_'](https://ru.wikipedia.org) events in your telegram chat in daily newsletter

## How to install

### Common installation

Prerequisites

- Installed [Git](https://git-scm.com/)
- Installed [Python](https://www.python.org/) version 3.9 or latest
- You need to create a [telegram bot](https://core.telegram.org/bots/faq) and get its token

Following installation steps runs on Windows:

1. Set 'TELEGRAM_BOT_TOKEN' system environment variable

2. Open terminal window and create new directory:
```commandline
mkdir 'directory_name'
```

3. Go to created directory:
```commandline
cd 'directory_path'
```

4. Clone repository ([Git](https://git-scm.com/) should be installed and add in system environment variable):
```commandline
git clone https://github.com/alekseyVolik/interesting-facts-bot.git
```

5. Create and activate python virtual environment ([Python](https://www.python.org/) should be installed and add in system 
environment variable):
```commandline
python -m venv env
```
```commandline
.\env\Script\activate
```

6. Installing dependencies:
```commandline
python -m pip install -r requirements.txt
```

7. Run DB migration:
```commandline
alembic upgrade head
```

8. Run bot application:
```commandline
python main.py
```
