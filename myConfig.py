import configparser
import os

# 設定ファイルのクラス
class Config():
    def __init__(self):
        self.filename = "config.ini"
        self.parser = configparser.ConfigParser()
        self.parser.optionxform = str               # 大文字小文字を区別する
        self.default_values = \
"""
[DEFAULT]
place = 名古屋
lat = 35.1667
lon = 136.9167
elev = 0
orning_offset = 0
evening_offset = 0
morning_minutes = 90
evening_minutes = 90
sensing_interval = 1
sensing_count = 2
output1 = 1
output2 = 1
output3 = 1
output4 = 1
Ah = 100
power = 12
LEDcnt = 150
voltage = 24
BTcnt = 8
charge = 1500        
"""

    def read(self):
        # 設定ファイルが存在しない場合、デフォルト設定を新規作成する
        if not os.path.exists(self.filename):
            with open(self.filename, mode="w", encoding="utf-8") as f:
                f.write(self.default_values)
        
        # 設定ファイルを読み込む 
        self.parser.read(self.filename, encoding="utf-8")
        return dict(self.parser["DEFAULT"])

    def write(self, dict):
        # 設定ファイルに書き込む
        self.parser["DEFAULT"].update(dict)
        with open(self.filename, mode="w",  encoding="utf-8") as f:
            self.parser.write(f)
