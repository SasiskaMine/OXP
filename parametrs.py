import os
import requests
from urllib.parse import urlparse
import shutil


def help_info():
    info = """oxp packet manager"""
    commands = """Commands Z$: 
        -i == install packet: oxp -i URL_FILE CUSTOM_PACKET_NAME
        -r == uninstall packet: oxp -r CUSTOM_PACKET_NAME
        -l == list installed: oxp -l
        -h == help: oxp -h"""
    print(info, commands)


def install(URL: str, PACKET_NAME: str):
    url = URL if URL.startswith(('http://', 'https://')) else f'https://{URL}'

    parsed_url = urlparse(url)
    original_filename = os.path.basename(parsed_url.path)

    if original_filename and '.' in original_filename:
        filename = os.path.join(PACKET_NAME, original_filename)
    else:
        response = requests.get(url, stream=True)
        content_type = response.headers.get('content-type', '')

        ext_map = {
            'text/html': 'html',
            'text/plain': 'txt',
            'application/xml': 'xml',
            'application/json': 'json',
            'application/zip': 'zip',
            'application/gzip': 'gz',
            'text/xml': 'xml'
        }

        ext = ext_map.get(content_type, 'bin')
        filename = os.path.join(PACKET_NAME, f"{PACKET_NAME}.{ext}")

    os.makedirs(PACKET_NAME, exist_ok=True)
    response = requests.get(url)
    with open(filename, "wb") as pac:
        pac.write(response.content)
    print(f"Установлен: {filename}")


def remove(PACKET_NAME: str):
    folder_path = PACKET_NAME
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f"Удален: {folder_path}")
    else:
        print(f"Пакет '{PACKET_NAME}' не найден")


def list_packages():
    packages = []
    all_items = os.listdir('.')

    for item in all_items:
        if (os.path.isdir(item) and
                not item.startswith('.') and
                item != '__pycache__' and
                item not in ['.venv', '.idea', '.git']):
            packages.append(item)

    if packages:
        print("Установленные пакеты:")
        for pkg in packages:
            files = os.listdir(pkg)
            print(f"  {pkg}/ {' '.join(files)}")
    else:
        print("Пакетов не установлено")
