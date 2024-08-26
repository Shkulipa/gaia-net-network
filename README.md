about venv: https://www.youtube.com/watch?v=rsG1Y5k-9jo

создать окружение: python3 -m venv venv
зайти в окружени: source venv/bin/activate
выйти с окружения: deactivate

сохранить зависимости: pip freeze > requirements.txt
Установите только необходимые зависимости: pip install -r requirements.txt

run: python app.py


https://www.youtube.com/watch?v=NB8OceGZGjA
chomedrivers: https://sites.google.com/chromium.org/driver/downloads



по поводу поинтов:
https://discord.com/channels/1215232680942374912/1277064819949965322/1277671671737614469

# Установка
- Устанавливаем что к абочему столу подключиться
1) sudo apt update && sudo apt upgrade
2) sudo apt install ubuntu-desktop
3) sudo apt install xfce4 xfce4-goodies xorg dbus-x11 x11-xserver-utils
4) sudo apt install xrdp xorgxrdp

- Устанавливаем хром
1) wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
2) sudo apt install ./google-chrome-stable_current_amd64.deb

- Устанавливаем гит
1) sudo apt install git

- Устанавливаем питон
1) sudo apt install python3
2) sudo apt install python3-pip
3) sudo apt install python3-venv

Открыть бразуер 
- google-chrome --no-sandbox &