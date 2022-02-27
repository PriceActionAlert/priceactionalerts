import smtplib
from django.conf import settings
from django.core.mail import send_mail
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.template.loader import render_to_string
import jinja2
from jinja2 import Environment, FileSystemLoader
import os
import random
from datetime import datetime, date, timedelta


quotes = {
    1: ["American magic has always prevailed, and it will do so again.", "Warren Buffett"],
    2: ["Fear is the most contagious disease you can imagine. It makes the virus look like a piker.", "Warren Buffett"],
    3: ["You've got to understand accounting. You've got to. That's got to be like a language to you,", "Warren Buffett"],
    4: ["It's far better to buy a wonderful company at a fair price than a fair company at a wonderful price.", "Warren Buffett"],
    5: ["Price is what you pay. Value is what you get.", "Warren Buffett"],
    6: ["Lose money for the firm, and I will be understanding; lose a shred of reputation for the firm, and I will be ruthless.", "Warren Buffett"],
    7: ["A simple rule dictates my buying: Be fearful when others are greedy, and be greedy when others are fearful.", "Warren Buffett"],
    8: ["The important thing is to know what you know and know what you don’t know.", "Warren Buffett"],
    9: ["You cannot make a good deal with a bad person.", "Warren Buffett"],
    10: ["Just buy something for less than it’s worth.", "Warren Buffett"],
    11: ["The stock market is never obvious, it is designed to fool most of the people, most of the time.", "Jesse Livermore"],
    12: ["Every occupation has its aches and pains. If you keep bees, you get stung. Me, I get worried. It's either that or stay poor.", "Jesse Livermore"],
    13: ["If I've got a choice between worried and poor, I'll take worried anytime.", "Jesse Livermore"],
    14: ["Diversification may preserve wealth, but concentration builds wealth.", "Warren Buffett"],
    15: ["It's easy to a prophet. You make 25 predictions and the ones that come true are the ones you talk about", "Theodore Levitt"],
    16: ["Everybody wants to win, of course. But not everybody wants to bet, and therein lies a difference of the greatest magnitude.", "The Zurich Axioms"],
    17: ["People never get rich on salaries, and a lot of people get poor on them.", "The Zurich Axioms"],
    18: ["Worry is not a sickness but a sign of health. If you are not worried, you are not risking enough.", "The Zurich Axioms"],
    19: ["All investment is speculation. The only difference is that some people admit it and some don’t", "Gerald Loeb"],
    20: ["Only bet what you can afford to lose.", "The Zurich Axioms"],
    21: ["By reducing your greed, you improve your chances of getting rich.", "The Zurich Axioms"],
    22: ["Never check the price of a stock you’ve sold.", "The Zurich Axioms"],
    23: ["Decide in advance what gain you want from a venture, and when you get it, get out.", "The Zurich Axioms"],
    24: ["When the ship starts to sink, don’t pray. Jump.", "The Zurich Axioms"],
    25: ["The first obstacle is the fear of regret – what you fear is that a loser will turn into a winner after you’ve gone away.", "The Zurich Axioms"],
    26: ["The inability to abandon part of an investment becomes twice as bad a problem if you speculate on margin.", "The Zurich Axioms"],
    27: ["The willingness to abandon is usually the more trustworthy response.", "The Zurich Axioms"],
    28: ["Accept small losses cheerfully as a fact of life. Expect to experience several while awaiting a large gain.", "The Zurich Axioms"],
    29: ["The fact is of course, that all money phenomena are manifestations of human behavior.", "The Zurich Axioms"],
    29: ["Chaos is not dangerous until it begins to look orderly.", "The Zurich Axioms"],
    30: ["If you want to get rich, you need a sound rational approach. A Formula. Everybody is looking for this Formula. Unfortunately, there isn’t one.", "The Zurich Axioms"],
    31: ["Never get attached to things, only to people. Getting attached to things decreases your mobility, the capacity to move fast when the need arises.", "The Zurich Axioms"],
    32: ["The stock market really isn't a gamble, as long as you pick good companies that you think will do well.", "Peter Lynch"],
    33: ["In the short run, th emarket is a voting machine, but in the long run it is a weighing machine.", "Benjamin Graham"],
    34: ["Successful investing is about managing risk, not avoiding it.", "Benjamin Graham"],
    35: ["The intelligent investor is a realist who sells to optimists and buys from pessimists.", "Benjamin Graham"],
    36: ["A great company is not a great investment if you pay too much for the stock.", "Benjamin Graham"],
    37: ["Those who do not remember the past are condemned to repeat it.", "Benjamin Graham"],
    38: ["Be fearful when others are greedy and greedy only when others are fearful.", "Benjamin Graham"],
    39: ["Always go aganist the tide, buy when others are selling and sell when others are buying.", "Rakesh Jhunjhunwala"],
    40: ["Hold on to a stock only if it will give returns.", "Rakesh Jhunjhunwala"],
    41: ["Growth comes out of chaos.", "Rakesh Jhunjhunwala"],
}

def random_quotes():
    return random.randint(1,10)

def send_email_notification(to_email,content,flag):

    try:
        today_day = datetime.now().strftime('%A')
        if flag == "watchlist":
            subject = 'TradeTheSwing: Watchlist Alert ('+today_day+')!'
        if flag == "holding":
            subject = 'TradeTheSwing: Holding Alert (' + today_day + ')!'
        message = MIMEMultipart()
        message['Subject'] = subject
        #message['From'] = settings.EMAIL_HOST_USER
        message['From'] = settings.DEFAULT_FROM_EMAIL
        message['To'] = to_email

        message.attach(MIMEText(content, "html"))
        msgBody = message.as_string()

        #server = smtplib.SMTP('smtp.gmail.com', 587)
        server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        server.starttls()
        #server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        server.login(settings.DEFAULT_FROM_EMAIL, settings.EMAIL_HOST_PASSWORD)
        server.sendmail(message['From'], message['To'], msgBody)

    except Exception as e:
        print("Email:",e)
        return e

    return "Email successfully sent!!!"

def compose_email(user,email,stock,finance,candle_data):
    stock_list = []
    finance_list = []
    candle_data_list = []

    for i, j in finance.items():
        stock_list.append(i)
        finance_list.append(j)
        try:
            candle_data_list.append(candle_data[i])
        except Exception as e:
            print("Compose Email Finanace:", e)

    data = {}
    for i in range(len(stock_list)):
        stock_details = ""
        stock_details = stock_details + finance_list[i]
        try:
            candle_data_list[i] = candle_data_list[i].strip()
            stock_details = stock_details + candle_data_list[i]
        except Exception as e:
            print("Compose Email Data:", e)
        data[stock_list[i]] = stock_details

    #print("Here:",data)
    env = Environment(loader=FileSystemLoader('%s/templates/' % os.path.dirname(__file__)))
    template = env.get_template('emailnotification.html')
    #output = template.render(data=data)
    todaysquote = quotes[random_quotes()]
    #print("Here",todaysquote)
    output = template.render({'data':data,'user':user,'todaysquote':todaysquote})
    flag = "watchlist"
    response = send_email_notification(email,output,flag)
    return response

def compose_holding_email(user,email,stock,NudgeData):
    data = {}
    for i in range(len(NudgeData)):
        if len(NudgeData[i]) != 0:
            Stock = "Stock: " + NudgeData[i][0]
            CostPrice = "Cost Per Stock: " + str(NudgeData[i][1])
            CurrentPrice = "Current Price Per Stock: " + str(NudgeData[i][2])
            Status = "Status: " + NudgeData[i][4]
            if NudgeData[i][3] >= 0:
                ProfitPerShare = "Profit Per Stock: " + str(NudgeData[i][3])
                data[NudgeData[i][0]] = Stock +", "+ CostPrice +", "+ CurrentPrice +", "+ ProfitPerShare +", "+ Status
            else:
                LossPerShare = "Loss Per Stock: " + str(NudgeData[i][3])
                data[NudgeData[i][0]] = Stock +", "+ CostPrice +", "+ CurrentPrice +", "+ LossPerShare +", "+ Status

    #print("Here:",data)
    env = Environment(loader=FileSystemLoader('%s/templates/' % os.path.dirname(__file__)))
    template = env.get_template('emailnotification.html')
    todaysquote = quotes[random_quotes()]
    output = template.render({'data': data, 'user': user, 'todaysquote': todaysquote})
    flag = "holding"
    response = send_email_notification(email,output,flag)
    return "Holding Alert Email: "+response
