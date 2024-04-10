@echo off
START util\Bullet.exe
title [+] Requirements 
echo Preparing requirements
pip install -r requirements.txt
title [+] Bullet - Made By bullet.org
python main.py
