import telebot
from telebot import types

# Initialize your bot with your token
bot = telebot.TeleBot("7104789587:AAEIamf1AxUmk2xaK9esi2lu3kc8WMKV_0I")

# Define the command handler for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Create a reply keyboard with the options
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_who_we_are = types.KeyboardButton("1. Who we are?")
    item_pre_sale_date = types.KeyboardButton("2. Pre-sale date.")
    item_supply = types.KeyboardButton("3. Supply")
    item_when_dex = types.KeyboardButton("4. When dex.")
    item_will_burn_pool = types.KeyboardButton("5. Will burn pool?")
    item_contract_address = types.KeyboardButton("6. What is the contract address (CA)?")
    item_mint_nfts = types.KeyboardButton("7. How we mint the ChillCapy NFTs?")
    item_how_many_nfts = types.KeyboardButton("8. How many NFT do we mint?")
    item_whitelist = types.KeyboardButton("9. Do we have whitelist?")
    item_future_plan = types.KeyboardButton("10. What is our plan for the future?")
    
    # Add the buttons to the reply keyboard
    markup.row(item_who_we_are, item_pre_sale_date)
    markup.row(item_supply, item_when_dex)
    markup.row(item_will_burn_pool, item_contract_address)
    markup.row(item_mint_nfts, item_how_many_nfts)
    markup.row(item_whitelist, item_future_plan)

    # Send the welcome message with the reply keyboard
    bot.send_message(message.chat.id, "Welcome! Please choose an option:", reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text.lower() == '/help')
# def help(message):
#     response = "Available commands:\n"
#     response += "/start - initiate the bot\n"

#     bot.reply_to(message, response)

# Define handler for each option selected by the user
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "1. Who we are?":
        bot.reply_to(message, "We are just some normal guys would like to bring new thoughts to the world. You are welcome to join our community! Please visit our website, discord, and X/twitter for more!\nWebsite: https://www.chillcapy.com/\nDiscord: https://discord.gg/EJD2TvANJy\nX/Twitter: https://twitter.com/ChillCapy_SOL")
    elif message.text == "2. Pre-sale date.":
        bot.reply_to(message, "The pre-sale date will be announced in the following weeks. Please be aware of our discord and website.")
    elif message.text == "3. Supply":
        bot.reply_to(message, "The token supply will be one billion with 50% for pre-sale and 50% for liquidity pool burnt. No token is for the team!")
    elif message.text == "4. When dex.":
        bot.reply_to(message, "The listing date will be announced in the following weeks. Please be aware of our discord and website.")
    elif message.text == "5. Will burn pool?":
        bot.reply_to(message, "Yes, we will burn pool for giving a free market to buyers.")
    elif message.text == "6. What is the contract address (CA)?":
        bot.reply_to(message, "The contract address will remain private until right before launching the token.")
    elif message.text == "7. How we mint the ChillCapy NFTs?":
        bot.reply_to(message, "We are going to establish a public mint in 'Launchmynft'. By doing so, you can mint any NFT you want in our collection. Please find more in link below.\nhttps://www.launchmynft.io/")
    elif message.text == "8. How many NFT do we mint?":
        bot.reply_to(message, "We have 3 stages for minting. Our first ChillCapy collection will contain 150 of NFT. Second collection will be 500 and third collection will be also 500. In total, we are appreciated to have 1150 of ChillCapy NFTs.")
    elif message.text == "9. Do we have whitelist?":
        bot.reply_to(message, "Yes, We offer whitelist to you for private sale if you really interested in our NFTs. Please dm us in X/twitter for more information.")
    elif message.text == "10. What is our plan for the future?":
        bot.reply_to(message, "Our ultimate goal is to spread the beliefs of being 'Chill'. Therefore, we would like to provide meditation courses platform, workshops and stationary product. The more importantly, we won’t forget to giving back the society as what Capy does so that we hopefully to collaborate with green organizations.")
    else:
        bot.reply_to(message, "Unknown command. Please use /start for a list of available commands.")

# Start polling for messages
bot.polling()