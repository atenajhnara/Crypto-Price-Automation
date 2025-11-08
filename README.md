💰 Crypto Price Automation & Excel Logger | ثبت خودکار قیمت رمزارزها

A Python automation project that continuously fetches live cryptocurrency prices from the CoinGecko API and logs them into a CSV file.
Supports multiple coins (BTC, ETH, ADA, DOGE, SOL) and automatically appends data at each interval.

پروژه‌ای برای اتوماسیون دریافت قیمت لحظه‌ای رمزارزها از طریق API سایت CoinGecko و ذخیره در فایل CSV.
برنامه در فواصل زمانی معین اجرا می‌شود و قیمت‌ها را به‌صورت خودکار در فایل اضافه می‌کند.

⸻

🧠 Technologies Used | تکنولوژی‌های استفاده‌شده
 • Python 3.10+
 • requests → برای دریافت داده از API
 • pandas → برای ساخت و ذخیره DataFrame
 • datetime / time / os → برای مدیریت زمان و فایل‌ها

⸻

⚙️ How It Works | نحوه کار
 1. با استفاده از requests داده‌های قیمت از CoinGecko API گرفته می‌شود.
 2. هر ۶۰ ثانیه (قابل تنظیم) درخواست جدید ارسال می‌شود.
 3. داده‌ها شامل زمان، نام ارز و قیمت در قالب CSV ذخیره می‌شوند.
 4. در صورت بسته بودن فایل اصلی، داده‌ها در فایل جدید ذخیره می‌شوند.
 5. در صورت قطع اتصال اینترنت، اسکریپت منتظر مانده و مجدداً تلاش می‌کند.

⸻

🧩 Key Code Structure | ساختار اصلی کد

# Define main file & parameters
main_file = "crypto_prices.csv"
coins = 'bitcoin,ethereum,cardano,dogecoin,solana'
vs_currency = 'usd'
interval = 60  # seconds

while True:
    try:
        # Fetch live prices
        url = 'https://api.coingecko.com/api/v3/simple/price'
        params = {'ids': coins, 'vs_currencies': vs_currency}
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        # Store results with timestamp
        now = datetime.now(timezone.utc)
        rows = [{'Datatime': now, 'Coin': c, 'Price': data[c][vs_currency]} for c in data]

        # Save to CSV (append mode)
        df = pd.DataFrame(rows)
        df.to_csv(main_file, mode='a', index=False, header=not os.path.exists(main_file))
    except:
        time.sleep(10)
    time.sleep(interval)
