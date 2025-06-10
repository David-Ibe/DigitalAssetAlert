# DigitalAssetAlert

DigitalAssetAlert is a real-time cryptocurrency data Telegram bot. It provides users with live cryptocurrency prices, market capitalization, trading volume, and top cryptocurrency rankings directly within the Telegram messaging platform.

## Features

- **Get Real-Time Crypto Data**: Fetch current price, 24-hour percentage change, market capitalization, and 24-hour trading volume for any specified cryptocurrency.
- **Top Cryptocurrencies**: List the top 10 cryptocurrencies by market capitalization.
- **User-Friendly Commands**: Easy-to-use commands to interact with the bot.

## Commands

- `/start`: Initializes the bot and displays a welcome message.
- `/data <crypto-symbol>`: Shows detailed information for the specified cryptocurrency symbol (e.g., `/data BTC` for Bitcoin, `/data ETH` for Ethereum).
- `/ranks`: Displays a list of the top 10 cryptocurrencies by market capitalization.

## Setup and Installation

Follow these steps to set up and run the DigitalAssetAlert bot:

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

### 1. Clone the Repository (Optional)

If you haven't already, you can clone this repository:
```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Obtain API Keys

- **CoinMarketCap API Key**:
    1. Go to [CoinMarketCap API](https://coinmarketcap.com/api/) and sign up for an account.
    2. Generate an API key from your developer dashboard.
    3. Open `cryptobot1.py` and replace `'YOUR_COINMARKETCAP_API_KEY'` with your actual CoinMarketCap API key in the following line:
       ```python
       api_key = 'YOUR_COINMARKETCAP_API_KEY'
       ```

- **Telegram Bot Token**:
    1. Open Telegram and search for "BotFather".
    2. Start a chat with BotFather and use the `/newbot` command to create a new bot.
    3. Follow the instructions and BotFather will give you a token.
    4. Open `cryptobot1.py` and replace `'YOUR_TELEGRAM_BOT_TOKEN'` with your actual Telegram bot token in the following line:
       ```python
       app = ApplicationBuilder().token('YOUR_TELEGRAM_BOT_TOKEN').build()
       ```

### 3. Install Dependencies

Install the required Python libraries using pip:
```bash
pip install python-telegram-bot requests
```

### 4. Run the Bot

Execute the Python script to start the bot:
```bash
python cryptobot1.py
```
Once the bot is running, you can interact with it on Telegram using the commands listed above.

## Usage Examples

- **Starting the bot:**
  Send `/start` to the bot.
  The bot will reply with: `Hello! I am your Digital Asset Alert Bot. I can provide real-time data for any cryptocurrency. Use /data <crypto-symbol> to get started.`

- **Getting data for a specific cryptocurrency:**
  Send `/data BTC`
  The bot might reply with:
  `The current price of Bitcoin is $60123.45678901. The price change in the last 24 hours is 1.23%.`
  `The market cap is $1123456789012.34.`
  `The total volume in the last 24 hours is $45678901234.56.`
  *(Note: Prices and values are examples and will vary.)*

- **Getting the top 10 cryptocurrencies:**
  Send `/ranks`
  The bot will reply with a list similar to this:
  ```
  Here are the largest 10 cryptocurrencies:
  1. *Bitcoin* (BTC):
  - Current price is $60123.45678901
  - Market cap is $1123456789012.34
  - Total volume in the last 24 hours is $45678901234.56

  2. *Ethereum* (ETH):
  - Current price is $3012.34567890
  - Market cap is $361234567890.12
  - Total volume in the last 24 hours is $23456789012.34

  ...and so on for the top 10.
  ```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some YourFeature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Open a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details (if one is created).
