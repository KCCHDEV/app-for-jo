import os
import requests
from pathlib import Path

class FontManager:
    FONT_URL = "https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@400;700&display=swap"
    
    def __init__(self):
        self.fonts_dir = Path("fonts")
        self.font_path = self.fonts_dir / "NotoSansThai-Regular.ttf"
        self.setup_thai_font()

    def setup_thai_font(self):
        """Download and setup Thai font if not present"""
        if not self.font_path.exists():
            self.download_font()
        return self.font_path

    def download_font(self):
        """Download the Thai font from Google Fonts"""
        self.fonts_dir.mkdir(exist_ok=True)
        
        try:
            response = requests.get(self.FONT_URL)
            font_css = response.text
            font_file_url = font_css.split("url(")[1].split(")")[0]
            
            font_response = requests.get(font_file_url)
            self.font_path.write_bytes(font_response.content)
            print(f"Successfully downloaded font to {self.font_path}")
        except Exception as e:
            print(f"Error downloading font: {e}") 