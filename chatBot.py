# 5991666433:AAGmLCE4pJ9jZbG8x6FfDTi8ss9ZM2Uo8bw
import telebot
bot = telebot.TeleBot("5991666433:AAGmLCE4pJ9jZbG8x6FfDTi8ss9ZM2Uo8bw")
total_cost = 0
cartStock = {}
rphoto = {
    'Store': "images/gStore.jpeg",
    '500ml Milk': "images/halfLitre.jpeg",
    '250ml Milk': "images/normalPack.jpeg",
    'Curd':"images/curd.jpeg",
    'Bingo':'images/bingo.jpeg',
    'Lays':'images/lays.jpeg',
    'Pepsi':'images/pepsi.jpeg',
    'Coca-cola':'images/CocoCola.jpeg',
    'Pens':'images/pens.jpeg',
    'Santoor':'images/santoor.jpeg',
    'Gold Flake':'images/goldFlake.jpeg',
    'Books':'images/books.jpeg',
    'Battery':'images/battery.jpeg',
}

cost = {
    '500ml Milk':30,
    '250ml Milk':10,
    'Gold Flake':12,
    'Bingo':5,
    'Lays':5,
    'Pepsi':30,
    'Coca-cola':37,
    'Santoor':10,
    'Books':10,
    'Pens':10,
    'Curd':10,
    'Battery':10,
}
stock = {
    '500ml Milk':10,
    '250ml Milk':10,
    'Gold Flake':20,
    'Bingo':15,
    'Lays':10,
    'Pepsi':20,
    'Coca-cola':10,
    'Santoor':5,
    'Curd':0,
    'Books':15,
    'Pens':20,
    'Battery':12,
}
backList = {
    '500ml Milk':'HalfLitreback',
    '250ml Milk':'NormalPackback',
    'Bingo':'snacksback',
    'Lays':'snacksback',
    'Pepsi':'beveragesback',
    'Coca-cola':'beveragesback',
    'Santoor':'soapsback',
    'Curd':'Curdback',
    'Books':'stationeryback',
    'Pens':'stationeryback',
    'Battery':'electronicsback',
}
# define the categories
dairy_items = ['Milk', 'Curd']
snack_items = ['Bingo', 'Lays']
beverage_items = ['Coca-cola', 'Pepsi']
stationery_items  =['Books','Pens']
cleaning_items = ['Santoor']
smoking_items = ['Gold Flake']
electronic_items=['Battery']

commands= ['/start','/help','/myCart','/placeOrder','/work']
#buttons
remove_button = telebot.types.KeyboardButton('\U0001F6D1 Remove item')
order_button = telebot.types.KeyboardButton('\U0001F6D2 Order item')
back_button = telebot.types.KeyboardButton('\U0001F519 Back')
cart_button = telebot.types.KeyboardButton('\U0001F6D2My Cart')
placeOrder_button = telebot.types.KeyboardButton("Place Order")
@bot.message_handler(func=lambda message:message=='/myCart')
def printcart_handler(message):
    printCart(message)
def printCart(message):
    if len(cartStock)==0:
        bot.send_message(message.chat.id,"Nothing there is in you cart")
        bot.send_message(message.chat.id,"Let's buy in a few clicks and get delivered in a few hours")
        bot.send_message(message.chat.id,"Click on /help command to know bot commands and details")
    else:
        global  total_cost
        # data = [[k,v] for k,v in cartStock.items()]
        # df = pd.DataFrame(data,columns=["Items","      Quantity"])
        # bot.send_message(message.chat.id,f'Your cart\n{df.to_string(index=False)}\nTotal cost : {total_cost}')
        msg="Your Cart\n\n{:<23} {:<10} {:<10}\n".format('Item', 'Quantity','Cost')
        for i in cartStock.keys():
            # j=i
            # if i == '500ml Milk':
            #     j='1/2 Milk'
            # elif i == '250ml Milk':
            #     j = 'Normal Milk'
            # elif i=='Battery':
            #     j = 'Panasonic'
            msg = msg+"{:<23} {:<10} {:<10}".format(i,cartStock[i], cartStock[i]*cost[i])+'\n'
        msg = msg+f"\nTotal Cost {total_cost}"
        bot.send_message(message.chat.id,msg)
@bot.message_handler(func=lambda message:message.text=='/help')
def help_handler(message):
    help(message)
def help(message):
    msg = "/start : to start the bot\n" \
          "/help : to know details and commands about bot\n" \
          "/myCart : to view your cart\n" \
          "/placeOrder : to place an order for your cart items" \
          "/work : to apply for delivery work" \
          "You can also directly enter the category name"
    bot.send_message(message.chat.id,msg)
@bot.message_handler(func= lambda message: 'Place Order' in message.text or message.text=='/placeOrder')
def placeOrder(message):
    orderHelper(message)
def orderHelper(message):
    if len(cartStock)==0:
        printCart(message)
    else:
        printCart(message)
        keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True,row_width=2)
        confirm_button = telebot.types.KeyboardButton('Confirm Order')
        cancel_button = telebot.types.KeyboardButton('Cancel Order')
        keyboard.add(confirm_button,cancel_button,back_button)
        bot.send_message(message.chat.id,'Confirm your order',reply_markup=keyboard)
        bot.register_next_step_handler(message,lambda msg:finalorder(msg))
def finalorder(message):
    if message.text == 'Confirm Order':
        with open('gif/delivery.gif','rb') as gif:
            bot.send_document(chat_id=message.chat.id,document=gif,caption="Your order has been confirmed\nGet your items withing hours")
    elif message.text == 'Cancel Order':
        start(message)
    elif 'Back' in message.text:
        start(message)
    else:
        bot.send_message(message.chat.id, 'Invalid input')
        bot.send_message(message.chat.id, 'Choose once again')
        bot.register_next_step_handler(message,lambda msg:finalorder(msg))
@bot.message_handler(commands=['start'])
def start_message(message):
    print(cartStock)
    with open(rphoto["Store"], 'rb') as photo:
        bot.send_photo(chat_id=message.chat.id,photo= photo,caption=f'Hello {message.from_user.first_name}! Welcome to Renuka Store \U0001F6D2 \nWhat would you like to buy?')
    bot.send_message(message.chat.id, 'You can select categories from buttons')
    # with open('gif/buy.gif','rb') as gif:
    #     bot.send_document(chat_id=message.chat.id, document=gif, caption="What would you like to buy?")
    # bot.send_message(message.chat.id, )
    start(message)
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    uploadPhoto_button = telebot.types.KeyboardButton('\U0001F4F7Upload Photo')
    dairy_button = telebot.types.KeyboardButton('\U0001F375 Dairy')
    snack_button = telebot.types.KeyboardButton('\U0001F36A Snacks')
    beverage_button = telebot.types.KeyboardButton('\U0001F379 Beverages')
    stationery_button = telebot.types.KeyboardButton('\U0001F4DA Stationery')
    cleaning_button = telebot.types.KeyboardButton('\U0001F9FC Soaps')
    electronic_button = telebot.types.KeyboardButton('\U0001F50B Electronics')
    keyboard.add(uploadPhoto_button,dairy_button, snack_button, beverage_button, stationery_button, cleaning_button, electronic_button,cart_button,placeOrder_button)
    bot.send_message(message.chat.id, 'Choose a category:', reply_markup=keyboard)
def remove(message):
    if message.text in commands:
        handle_commands(message)
    elif len(cartStock)==0:
        printCart(message)
    else:
        printCart(message)
        bot.send_message(message.chat.id,'Enter the item you want to remove',reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id,'Please enter the name as it appears in your cart')
        bot.register_next_step_handler(message,lambda msg: remove_handler(msg))
def remove_handler(message):
    if message.text in commands:
        handle_commands(message)
    item = message.text
    print(f'remove item entered: {item}')
    # cartStock_lower = [x.lower() for x in list(cartStock.keys())]
    print(cartStock.keys())
    if item in cartStock.keys():
        print("present in cart")
        bot.send_message(message.chat.id,"No. of items you want to remove")
        bot.register_next_step_handler(message, lambda msg: remove_helper(msg,item))
    else:
        print('not present')
        bot.send_message(message.chat.id,'Item is not in the cart')
        remove(message)
def remove_helper(message,item):
    if message.text in commands:
        handle_commands(message)
    if message.text.isdigit() and int(message.text)<=cartStock[item] and int(message.text)>=1:
        global total_cost
        cartStock[item] = cartStock[item]-int(message.text)
        total_cost = total_cost - (cost[item]*int(message.text))
        if int(message.text)==1:
            bot.send_message(message.chat.id,f'{message.text} item of {item} is removed')
        else:
            bot.send_message(message.chat.id,f'{message.text} items of {item} are removed')
        if cartStock[item]==0:
            cartStock.pop(item)
        printCart(message)
        help(message)
def handle(message,back):
    print(f"enter handled {message.text}")
    if 'Back' in message.text:
        handle_back(message,back)
    elif 'Remove' in message.text:
        remove(message)
        # bot.register_next_step_handler(message,lambda msg:handle(msg,back))
    elif message.text in commands:
        handle_commands(message)
    else:
        print(f"handled {message.text}")
        cls = message.text
        item = message.text
        msg = f'Details:\n' \
              f'Price- ₹{cost[item]}\n' \
              f'No. of items available- {stock[item]}'
        with open(rphoto[item], 'rb') as sticker:
            bot.send_document(message.chat.id,sticker, caption=msg)
        # bot.send_sticker(message.chat.id,'images/pepsi.png')
        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
        order_button = telebot.types.KeyboardButton('\U0001F6D2 Order')
        keyboard.add(order_button, remove_button, back_button)
        bot.send_message(chat_id=message.chat.id, text='Click Order', reply_markup=keyboard)
        bot.register_next_step_handler(message, lambda msg: chooseOrder(message, item, keyboard, msg))

def chooseOrder(message,item,keyboard,msg):
    if('Remove' in msg.text):
        remove(message)
        handle_back(message,backList[item])
    if message.text in commands:
        handle_commands(message)
    elif('Back' in msg.text):
        print(f'handle back called for {item} i.e {backList[item]}')
        handle_back(message,backList[item])
    elif('Order' not in msg.text):
        bot.send_message(msg.chat.id,'Choose Order from buttons',reply_markup=keyboard)
        bot.register_next_step_handler(message,lambda msg:chooseOrder(message,item,keyboard,msg))
    else:
        order(msg,item,keyboard)
def order(message,item,keyboard):
    if message.text in commands:
        handle_commands(message)
    print("Order Item: " + item)
    bot.send_message(message.chat.id, "Enter the no. of items you want to order",reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, lambda msg: handle_items(msg, item,keyboard))
def handle_items(message,item,keyboard):
    print(f"handle_items() {item} {message.text}")
    global total_cost
    if message.text.isdigit() and int(message.text) <= stock[item] and int(message.text)>=1:
        print(message.text)
        price = cost[item]
        total_cost = total_cost + int(message.text)*price
        print(cartStock)
        cst = 0
        if item not in cartStock.keys():
            cst = int(message.text)*price
            cartStock[item] = int(message.text)
            print(f'if cost {cst}')
        else:
            cst = int(message.text)*price*cartStock[item]
            cartStock[item] = cartStock[item] + int(message.text)
            print(f'else cost {cst}')
        # cartStock[item] = cartStock[item] + int(message.text) if cartStock.get(item) is not None else int(message.text)
        bot.send_message(message.chat.id,'Order confirmed')
        bot.send_message(message.chat.id, f"Total {item}  cost: {cst}")
        printCart(message)
        bot.send_message(message.chat.id,'Use /start command or Back button from keyboard to order more',reply_markup=keyboard)
        handle_back(message,backList[item])
    elif message.text.isdigit() and int(message.text)<=0:
        bot.send_message(message.chat.id, "Quantity is not accpetable")
        order(message,item,keyboard)
    elif message.text.isdigit() and int(message.text)>stock[item]:
        bot.send_message(message.chat.id,'Choose no. of items within available')
        bot.send_message(message.chat.id, f'No. of available {item}s: {stock[item]}')
        order(message,item,keyboard)
    else:
        bot.send_message(message.chat.id,"Enter valid no. of items")
        order(message,item,keyboard)
def handle_back(message,cls):
    # include all items
    print(f"handle_back {cls}")
    classes= ['Dairy','Beverages','Snacks', 'Stationery', 'Soaps', 'Electronics']
    milkItemsback = ['HalfLitreback','NormalPackback']
    dairyback=['dairyback']
    beveragesback = ['beveragesback']
    stationeryback=['stationeryback']
    snacksback = ['snacksback']
    soapsback=['soapsback']
    electronicback=['electronicsback']
    if cls in classes:
        start(message)
    elif cls in beveragesback:
        beverage_message(message)
    elif cls in stationeryback:
        stationery_message(message)
    elif cls in snacksback:
        snack_message(message)
    elif cls in electronicback:
        electronic_message(message)
    elif cls in soapsback:
        cleaning_message(message)
    elif cls in dairyback:
        dairy_message(message)
    elif cls in milkItemsback:
        milk(message)

@bot.message_handler(func=lambda message: 'Upload Photo' in message.text)
def photo_handler(message):
    bot.send_message(message.chat.id, 'Upload photo of your list of items')
    bot.register_next_step_handler(message,photo)
def photo(message):
    if message.photo:
        # with open('gif/buy.gif','rb') as gif:
        #     bot.send_document(chat_id=message.chat.id, document=gif, caption="What would you like to buy?")
        msg = "If your uploaded photo is valid, then your items will get ready within minutes, and we'll contact you soon.\nYou can pay after delivery"
        with open('gif/verification.gif','rb') as gif:
            bot.send_document(chat_id=message.chat.id,document=gif,caption=msg)
        thank(message)
    elif message.text in commands:
        handle_commands(message.text)
    else:
        msg = "Not a valid photo. Please make sure upload photo only\nWe are waiting for your photo.Try Again"
        with open('gif/thinking.gif','rb') as gif:
            bot.send_document(message.chat.id,document=gif,caption=msg)
        start(message)
def handle_commands(message):
    if(message.text=='/start'):
        start(message)
    elif message.text=='/myCart':
        printCart(message)
    elif message.text=='/placeOrder':
        placeOrder(message)
    elif message.text=='/help':
        help(message)
    elif message.text=='work':
        work(message)
def work(message):
    bot.send_message("Enter your mobile number (Only Hyd people are acceptable)\n")
    bot.register_next_step_handler(message,lambda msg:handle_work(msg))
def handle_work(message):
    if message.text.isdigit() and len(message.text)==10:
        bot.send_message("We'll contact you soon. Stay tuned")
    else:
        bot.send_message(message.chat.id,'Enter valid mobile number')
        bot.register_next_step_handler(message,work)

# define handler functions for each category
@bot.message_handler(func=lambda message: ('Dairy' in message.text))
def dairy_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    milk_button = telebot.types.KeyboardButton('\U0001F95B Milk')
    curd_button = telebot.types.KeyboardButton('Curd')
    # back_button = telebot.types.KeyboardButton('\U0001F519 Back')
    keyboard.add(milk_button, curd_button,back_button)
    bot.send_message(message.chat.id, 'Choose a dairy item:', reply_markup=keyboard)
    bot.register_next_step_handler(message,lambda msg:dairyhelper(msg))
def dairyhelper(message):
    print(f'dairy helper {message.text}')
    if('Back' in message.text):
        handle_back(message,'Dairy')
    elif 'Curd' in message.text:
            curd(message)
    elif 'Milk' in message.text:
            milk(message)
def milk(message):
    # print('milk()')
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    halfLitre = telebot.types.KeyboardButton('500ml Milk')
    normalPack = telebot.types.KeyboardButton('250ml Milk')
    # back_button = telebot.types.KeyboardButton('\U0001F519 Back')
    keyboard.add(halfLitre,normalPack,remove_button,back_button)
    bot.send_message(message.chat.id, 'Choose Quanitity', reply_markup=keyboard)
    bot.register_next_step_handler(message,lambda msg:handle(msg,'dairyback'))
def curd(message):
    bot.send_message(message.chat.id,"We're sorry to inform you that Curd packets are not currently available. However, please be assured that we are working diligently to buy them as soon as possible.")
    dairy_message(message)
@bot.message_handler(func=lambda message: ('Snacks' in message.text) )
def snack_message_handler(message):
    snack_message(message)
def snack_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    bingo_button = telebot.types.KeyboardButton('Bingo')
    lays_button = telebot.types.KeyboardButton('Lays')
    keyboard.add(bingo_button, lays_button, remove_button, back_button)
    bot.send_message(message.chat.id, 'Choose a snack item:', reply_markup=keyboard)
    bot.register_next_step_handler(message, lambda msg: handle(msg,'Snacks'))
@bot.message_handler(func=lambda message:('Beverages' in message.text))
def beverage_message_handler(message):
    beverage_message(message)
def beverage_message(message):
    print("entered beverage")
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    coca_cola_button = telebot.types.KeyboardButton('Coca-cola')
    pepsi_button = telebot.types.KeyboardButton('Pepsi')
    keyboard.add(coca_cola_button,pepsi_button,remove_button,back_button)
    bot.send_message(message.chat.id, 'Choose a beverage item:', reply_markup=keyboard)
    bot.register_next_step_handler(message,lambda msg:handle(msg,'Beverages'))
@bot.message_handler(func=lambda message:('Stationery' in message.text))
def stationery_message_handler(message):
    stationery_message(message)
def stationery_message(message):
    print("stationery called")
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    books_button = telebot.types.KeyboardButton('Books')
    pens_button = telebot.types.KeyboardButton('Pens')
    keyboard.add(books_button,pens_button,remove_button,back_button)
    bot.send_message(message.chat.id, 'Choose a stationery item:', reply_markup=keyboard)
    bot.register_next_step_handler(message,lambda msg:handle(msg,'Stationery'))
@bot.message_handler(func=lambda message:('Soaps' in message.text))
def cleaning_message_handler(message):
    cleaning_message(message)
def cleaning_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1)
    santoor_button = telebot.types.KeyboardButton('Santoor')
    keyboard.add(santoor_button,remove_button,back_button)
    bot.send_message(message.chat.id, 'Choose a soap:', reply_markup=keyboard)
    bot.register_next_step_handler(message,lambda msg:handle(msg,'Soaps'))
@bot.message_handler(func=lambda message:('Electronic' in message.text))
def electronic_message_handler(message):
    electronic_message(message)
def electronic_message(message):
    print("electronic()")
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1)
    panasonic_battery = telebot.types.KeyboardButton('Battery')
    keyboard.add(panasonic_battery, remove_button, back_button)
    bot.send_message(message.chat.id, 'Click on Battery', reply_markup=keyboard)
    bot.register_next_step_handler(message, lambda msg: handle(msg,'Electronics'))
def thank(message):
    bot.send_message(message.chat.id,'Thank you')
@bot.message_handler(func=lambda message: 'My Cart' in message.text or '\myCart' == message.text)
def cart_handler(message):
    printCart(message)
@bot.message_handler(commands=['search'])
def search_message(message):
    # send a message with a list of available options
    options = ['Milk', 'Curd', 'Coca-cola', 'Book', 'Pens', 'Shampoos','Bingo','Sweet' ,'Detergent' ,'Cigarrette']
    bot.reply_to(message, 'Enter the name of the option you want to choose:\n' + '\n'.join(options))

# define a handler function for messages containing text

print("Bot started")
bot.polling()


# items = {
#     1: {"name": "milk", "price": 30, "stock": 10},
#     2: {"
#     3: {"name": "pens", "price": 10, "stock": 20}
# }
#
# sub_items = {
#     1: {"name": "liter", "price": 30},
#     2: {"name": "half liter", "price": 20}
# }
#
# user_data = {}

# def start(message):
#     with open('images/bingo.jpeg','rb') as photo:
#         bot.send_photo(message,photo=photo,caption="hii ra")
