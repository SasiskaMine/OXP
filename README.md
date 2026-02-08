oxp — Universal Packet Manager

[ Libary`s:
[Requests,sys,urllib.parse,shutil]

oxp — простой пакетный менеджер для загрузки любых файлов по URL. Работает как pacman, но скачивает с любого сайта.
🚀 Быстрый старт

bash
oxp -i https://example.com/file.zip mypackage
oxp -l
oxp -r mypackage

📦 Команды
Команда	Описание	Пример
oxp -i URL NAME	Установить пакет	oxp -i google.com page
oxp -r NAME	Удалить пакет	oxp -r page
oxp -l	Список пакетов	oxp -l
oxp -h	Справка	oxp -h
💻 Установка
Linux

bash
wget https://github.com/user/oxp/releases/latest/download/oxp-linux
chmod +x oxp-linux
./oxp-linux -i httpbin.org/xml test

Windows

text
oxp-windows.exe -i https://example.com/app.exe program

macOS

bash
chmod +x oxp-macos
./oxp-macos -i github.com/archive/main.zip project

🛠️ Компиляция для всех ОС
📋 Требования

bash
pip install pyinstaller requests

🐧 Linux (Arch/Ubuntu/Fedora)

bash
pip install pyinstaller
pyinstaller --onefile oxp.py --name oxp
chmod +x dist/oxp
./dist/oxp -i google.com test

🪟 Windows

text
pip install pyinstaller
pyinstaller --onefile oxp.py --name oxp
dist\oxp.exe -i https://example.com/file.zip program

🍎 macOS

bash
pip install pyinstaller
pyinstaller --onefile oxp.py --name oxp
chmod +x dist/oxp
./dist/oxp -i google.com page

📦 Linux пакеты

DEB (Ubuntu/Debian):

bash
sudo apt install ruby fpm
pyinstaller --onefile oxp.py --name oxp
fpm -s dir -t deb -n oxp -v 1.0 dist/oxp=/usr/local/bin/oxp

RPM (Fedora/RHEL):

bash
sudo dnf install ruby fpm
fpm -s dir -t rpm -n oxp -v 1.0 dist/oxp=/usr/bin/oxp

☁️ GitHub Actions (автоматическая сборка)

.github/workflows/build.yml:

text
name: Build oxp Cross-Platform
on: [push, workflow_dispatch]
jobs:
  build:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
    runs-on: ${{ matrix.os }}
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v4
      with: {python-version: '3.11'}
    - run: pip install pyinstaller
    - run: pyinstaller --onefile oxp.py --name oxp
    - uses: actions/upload-artifact@v4
      with:
        name: oxp-${{ matrix.os }}
        path: dist/oxp*

Запуск: git tag v1.0.0 && git push origin v1.0.0
🌍 Многоязычность
🇷🇺 Русский

bash
oxp -i google.com тестовая_страница
oxp -l
oxp -r тестовая_страница

🇺🇸 English

bash
oxp -i google.com homepage
oxp -l
oxp -r homepage

🇪🇸 Español

bash
oxp -i google.com pagina
oxp -l
oxp -r pagina

📁 Структура

text
project/
├── oxp.py          # CLI + match-case
├── parametrs.py    # Функции
├── dist/
│   └── oxp         # Исполняемый файл
└── test/           # Пакеты
    └── test.html

🔗 Примеры

bash
oxp -i httpbin.org/xml data      # XML
oxp -i google.com page          # HTML  
oxp -i github.com/zip project   # ZIP
oxp -i example.com/data.json api # JSON

📄 Лицензия

MIT

⭐ Star на GitHub! pacman → oxp для всех файлов!
