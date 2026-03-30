"""筋トレサイエンスラボ - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "筋トレサイエンスラボ"
BLOG_DESCRIPTION = "科学的根拠に基づく筋トレ・トレーニング情報ブログ"
BLOG_URL = "https://musclelove-777.github.io/muscle-science-lab"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/muscle-science-lab"

TARGET_CATEGORIES = [
    "筋肥大メカニズム",
    "トレーニングプログラム",
    "運動生理学",
    "筋力アップ科学",
    "スポーツサイエンス",
]

THEME = {
    "primary": "#dc2626",
    "accent": "#f97316",
    "gradient_start": "#dc2626",
    "gradient_end": "#ea580c",
    "dark_bg": "#1a0a0a",
    "dark_surface": "#2d1515",
    "light_bg": "#fef2f2",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 2500
ARTICLES_PER_DAY = 2
SCHEDULE_HOURS = [7, 19]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 70
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "プロテイン・サプリ": [
        {"service": "マイプロテイン", "url": "https://www.myprotein.jp", "description": "高品質プロテイン・サプリメント"},
        {"service": "Amazon サプリメント", "url": "https://www.amazon.co.jp", "description": "筋トレサプリメント各種"},
    ],
    "トレーニング器具": [
        {"service": "Amazon スポーツ", "url": "https://www.amazon.co.jp", "description": "トレーニング器具・グッズ"},
        {"service": "楽天市場 フィットネス", "url": "https://www.rakuten.co.jp", "description": "フィットネス用品"},
    ],
    "オンライン講座": [
        {"service": "Udemy", "url": "https://www.udemy.com", "description": "筋トレ・フィットネス講座"},
        {"service": "NSCA公式", "url": "https://www.nsca-japan.or.jp", "description": "NSCA認定トレーナー資格"},
    ],
    "書籍": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "筋トレ・運動生理学の書籍"},
        {"service": "楽天ブックス", "url": "https://books.rakuten.co.jp", "description": "トレーニング関連書籍"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
DASHBOARD_PORT = 8080

# Google Analytics (GA4)
GOOGLE_ANALYTICS_ID = "G-CSFVD34MKK"

# Google Search Console 認証ファイル
SITE_VERIFICATION_FILES = {
    "googlea31edabcec879415.html": "google-site-verification: googlea31edabcec879415.html",
}
