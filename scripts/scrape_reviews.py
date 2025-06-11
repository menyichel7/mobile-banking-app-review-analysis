from google_play_scraper import reviews, Sort
import pandas as pd

def scrape_reviews(app_id, bank_name):
    all_reviews = []
    for score in range(1, 6):
        r, _ = reviews(
            app_id,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=200,
            filter_score_with=score,
        )
        for item in r:
            all_reviews.append({
                "review": item["content"],
                "rating": item["score"],
                "date": item["at"].date(),
                "bank": bank_name,
                "source": "Google Play"
            })
    return all_reviews

# Add package names here
bank_apps = {
    "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
    "Dashen Bank": "com.cr2.amolelight",
    "Bank of Abyssinia": "com.boa.boaMobileBanking"
}

all_data = []

for bank, app_id in bank_apps.items():
    all_data.extend(scrape_reviews(app_id, bank))

df = pd.DataFrame(all_data)
df.drop_duplicates(subset='review', inplace=True)
df.to_csv("../data/raw_reviews.csv", index=False)
