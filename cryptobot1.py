from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

# Define your CoinMarketCap API key
api_key = 'a54f775b-6504-48b2-805c-02ee36bc8362'

# Function to fetch cryptocurrency data from CoinMarketCap
def get_crypto_data(crypto):
    try:
        response = requests.get(
            f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest',
            headers={'X-CMC_PRO_API_KEY': api_key},
            params={'symbol': crypto}
        )
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as err:
        print("Something went wrong", err)
        return None

# Function to fetch top 10 cryptocurrencies from CoinMarketCap
def get_top_cryptos():
    try:
        response = requests.get(
            'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest',
            headers={'X-CMC_PRO_API_KEY': api_key},
            params={'limit': 10}
        )
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as err:
        print("Something went wrong", err)
        return None

# Telegram command to start the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_message = 'Hello! I am your Digital Asset Alert Bot. I can provide real-time data for any cryptocurrency. Use /data <crypto-symbol> to get started.'
    await update.message.reply_text(welcome_message)

# Telegram command to get the data of a cryptocurrency
async def data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    crypto_symbol = context.args[0] if context.args else None  # get the crypto symbol from the message
    if crypto_symbol:
        data = get_crypto_data(crypto_symbol)
        if data:
            crypto_data = list(data['data'].values())[0]
            crypto_name = crypto_data['name']
            price = crypto_data['quote']['USD']['price']
            percent_change_24h = crypto_data['quote']['USD']['percent_change_24h']
            market_cap = crypto_data['quote']['USD']['market_cap']
            volume_24h = crypto_data['quote']['USD']['volume_24h']
            await update.message.reply_text(
                f'The current price of {crypto_name} is ${price:.8f}. The price change in the last 24 hours is {percent_change_24h:.2f}%.\n'
                f'The market cap is ${market_cap:.2f}.\n'
                f'The total volume in the last 24 hours is ${volume_24h:.2f}.'
            )
        else:
            await update.message.reply_text(f'Sorry, I could not fetch the data for {crypto_symbol}. Please check the cryptocurrency symbol and try again.')
    else:
        await update.message.reply_text('Please provide a cryptocurrency symbol.')

# Telegram command to get the top 10 cryptocurrencies
async def ranks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = get_top_cryptos()
    if data:
        message = "Here are the largest 10 cryptocurrencies:\n"
        for i, crypto in enumerate(data['data'], start=1):
            crypto_name = crypto['name']
            symbol = crypto['symbol']
            price = crypto['quote']['USD']['price']
            market_cap = crypto['quote']['USD']['market_cap']
            volume_24h = crypto['quote']['USD']['volume_24h']
            message += (
                f'{i}. *{crypto_name}* ({symbol.upper()}):\n'
                f'- Current price is ${price:.8f}\n'
                f'- Market cap is ${market_cap:.2f}\n'
                f'- Total volume in the last 24 hours is ${volume_24h:.2f}\n\n'
            )
        await update.message.reply_text(message, parse_mode='Markdown')
    else:
        await update.message.reply_text('Sorry, I could not fetch the data for the top 10 cryptocurrencies. Please try again later.')

app = ApplicationBuilder().token('7047183236:AAGmr6yJXruMJBaFpYLKuJSDZZB0WPjQyks').build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("data", data))
app.add_handler(CommandHandler("ranks", ranks))

app.run_polling()
