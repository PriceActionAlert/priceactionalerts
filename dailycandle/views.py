from django.shortcuts import render,redirect
from users.models import *
from django.contrib import messages
from .models import *
from .form import *
from .emailnotification import *
from django.apps import apps
from django.contrib.auth.models import User

import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, date, timedelta
import sys
import datetime, calendar
from collections import OrderedDict
from pytz import timezone
import time
import math
import re
from nsetools import Nse


companyicon = {
                    "NTPC":"https://logo.clearbit.com/ntpc.co.in",
                    "UPL": "https://logo.clearbit.com/upl-ltd.com",
                    "SUNPHARMA":"https://logo.clearbit.com/sunpharma.com",
                    "TATACONSUM": "https://logo.clearbit.com/tataconsumer.com",
                    "INDUSINDBK":"https://logo.clearbit.com/indusind.com",
                    "ONGC": "https://logo.clearbit.com/ongcindia.com",
                    "MM": "https://logo.clearbit.com/mahindra.com",
                    "IOC":"https://logo.clearbit.com/iocl.com",
                    "BHARTIARTL": "https://logo.clearbit.com/airtel.in",
                    "ITC":"https://logo.clearbit.com/itcportal.com",
                    "WIPRO": "https://logo.clearbit.com/wipro.com",
                    "TCS":"https://logo.clearbit.com/tcs.com",
                    "BRITANNIA": "https://logo.clearbit.com/britannia.co.in",
                    "COALINDIA":"https://logo.clearbit.com/coalindia.in",
                    "GRASIM": "https://logo.clearbit.com/grasim.com",
                    "TATAMOTORS":"https://logo.clearbit.com/tatamotors.com",
                    "TITAN": "https://logo.clearbit.com/titancompany.in",
                    "BPCL":"https://logo.clearbit.com/bharatpetroleum.com",
                    "JSWSTEEL": "https://logo.clearbit.com/jsw.in",
                    "INFY":"https://logo.clearbit.com/infosys.com",
                    "HDFC": "https://logo.clearbit.com/hdfc.com",
                    "DIVISLAB":"https://logo.clearbit.com/divislabs.com",
                    "SHREECEM": "https://logo.clearbit.com/shreecement.com",
                    "CIPLA":"https://logo.clearbit.com/cipla.com",
                    "ADANIPORTS": "https://logo.clearbit.com/adaniports.com",
                    "HCLTECH":"https://logo.clearbit.com/hcltech.com",
                    "HINDALCO": "https://logo.clearbit.com/hindalco.com",
                    "BAJFINANCE":"https://logo.clearbit.com/bajajfinserv.in",
                    "KOTAKBANK": "https://logo.clearbit.com/kotak.com",
                    "ASIANPAINT":"https://logo.clearbit.com/asianpaints.com",
                    "NESTLEIND": "https://logo.clearbit.com/nestle.in",
                    "HDFCLIFE":"https://logo.clearbit.com/hdfclife.com",
                    "ULTRACEMCO": "https://logo.clearbit.com/ultratechcement.com",
                    "RELIANCE":"https://logo.clearbit.com/ril.com",
                    "TATASTEEL": "https://logo.clearbit.com/tatasteel.com",
                    "HINDUNILVR":"https://logo.clearbit.com/hul.co.in",
                    "SBILIFE": "https://logo.clearbit.com/sbilife.co.in",
                    "LT":"https://logo.clearbit.com/larsentoubro.com",
                    "DRREDDY": "https://logo.clearbit.com/drreddys.com",
                    "HDFCBANK":"https://logo.clearbit.com/hdfcbank.com",
                    "EICHERMOT": "https://logo.clearbit.com/eichermotors.com",
                    "SBIN":"https://logo.clearbit.com/sbi.co.in",
                    "BAJAJFINSV": "https://logo.clearbit.com/bajajfinserv.in",
                    "AXISBANK":"https://logo.clearbit.com/axisbank.com",
                    "HEROMOTOCO": "https://logo.clearbit.com/heromotocorp.com",
                    "ICICIBANK":"https://logo.clearbit.com/icicibank.com",
                    "POWERGRID": "https://logo.clearbit.com/powergrid.in",
                    "TECHM":"https://logo.clearbit.com/techmahindra.com",
                    "MARUTI": "https://logo.clearbit.com/marutisuzuki.com",
    }


def index(request):
    if not request.user.is_authenticated:
        return redirect('users:login')

    else:
        try:
            finance = []
            stock_list = []
            profile_obj = Profile.objects.get(user=request.user)
            profile_stocks = profile_obj.stocks
            profile_stocks = profile_stocks.replace("[", "")
            profile_stocks = profile_stocks.replace("]", "")
            profile_stocks = profile_stocks.replace("'", "")
            profile_stocks = profile_stocks.replace(",", "")
            profile_notification = profile_obj.notification

            user_stock_list = profile_stocks.split()
            for stock in user_stock_list:
                pe = []
                data = []
                candle = []
                data.append(stock)
                stock = ''.join(e for e in stock if e.isalnum())
                data.append(companyicon[stock])
                new_stock_finance_comment = ""
                priceregex = r"Stock: 200DayAverage: ([a-zA-Z0-9.\s-]+)\(ie ([0-9.a-zA-Z]+)\)"
                rsiregex = r"Stock: Relative Strength Index: ([0-9]+)"
                peregex = r"Financial: Forward PE: ([0-9a-zA-Z]+)"

                Model = apps.get_model('dailycandle', stock)
                stockdb = Model.objects.get(id=1)
                stock_finance_comment = stockdb.Finance.split(", ")

                for i in stock_finance_comment:
                    i = i.replace("[", "")
                    i = i.replace("'", "")
                    i = i.replace("]", "")
                    new_stock_finance_comment += i
                    new_stock_finance_comment += ". "
                    if re.search(peregex, i):
                        match = re.search(peregex, i)
                        pe.append(match.group(1))
                finance.append(new_stock_finance_comment)

                stock_monday_comment = stockdb.Monday.split(", ")
                if len(stock_monday_comment) == 1:
                    data.append(" ")
                    data.extend((" "," "," "))
                for i in stock_monday_comment:
                    i = i.replace("[", "")
                    i = i.replace("'", "")
                    i = i.replace("]", "")
                    if re.search(priceregex, i):
                        match = re.search(priceregex, i)
                        data.append(match.group(2))
                    if re.search(rsiregex, i):
                        match = re.search(rsiregex, i)
                        data.append(match.group(1))
                        data.append(pe[0])
                    if ('Price Zone: INCONCLUSIVE' in i):
                        data.append("INCONCLUSIVE")
                    if ('Price Zone: In SUPPORT Zone' in i):
                        data.append("SUPPORT")
                    if ('Price Zone: In RESISTANCE Zone' in i):
                        data.append("RESISTANCE")

                stock_tuesday_comment = stockdb.Tuesday.split(", ")
                if len(stock_tuesday_comment) == 1:
                    data.append(" ")
                    data.extend((" "," "," "))
                for i in stock_tuesday_comment:
                    i = i.replace("[", "")
                    i = i.replace("'", "")
                    i = i.replace("]", "")
                    if re.search(priceregex, i):
                        match = re.search(priceregex, i)
                        data.append(match.group(2))
                    if re.search(rsiregex, i):
                        match = re.search(rsiregex, i)
                        data.append(match.group(1))
                        data.append(pe[0])
                    if ('Price Zone: INCONCLUSIVE' in i):
                        data.append("INCONCLUSIVE")
                    if ('Price Zone: In SUPPORT Zone' in i):
                        data.append("SUPPORT")
                    if ('Price Zone: In RESISTANCE Zone' in i):
                        data.append("RESISTANCE")

                stock_wednesday_comment = stockdb.Wednesday.split(", ")
                if len(stock_wednesday_comment) == 1:
                    data.append(" ")
                    data.extend((" "," "," "))
                for i in stock_wednesday_comment:
                    i = i.replace("[", "")
                    i = i.replace("'", "")
                    i = i.replace("]", "")
                    if re.search(priceregex, i):
                        match = re.search(priceregex, i)
                        data.append(match.group(2))
                    if re.search(rsiregex, i):
                        match = re.search(rsiregex, i)
                        data.append(match.group(1))
                        data.append(pe[0])

                    if ('Price Zone: INCONCLUSIVE' in i):
                        data.append("INCONCLUSIVE")
                    if ('Price Zone: In SUPPORT Zone' in i):
                        data.append("SUPPORT")
                    if ('Price Zone: In RESISTANCE Zone' in i):
                        data.append("RESISTANCE")

                stock_thursday_comment = stockdb.Thursday.split(", ")
                if len(stock_thursday_comment) == 1:
                    data.append(" ")
                    data.extend((" "," "," "))
                for i in stock_thursday_comment:
                    i = i.replace("[", "")
                    i = i.replace("'", "")
                    i = i.replace("]", "")
                    if re.search(priceregex, i):
                        match = re.search(priceregex, i)
                        data.append(match.group(2))
                    if re.search(rsiregex, i):
                        match = re.search(rsiregex, i)
                        data.append(match.group(1))
                        data.append(pe[0])

                    if ('Price Zone: INCONCLUSIVE' in i):
                        data.append("INCONCLUSIVE")
                    if ('Price Zone: In SUPPORT Zone' in i):
                        data.append("SUPPORT")
                    if ('Price Zone: In RESISTANCE Zone' in i):
                        data.append("RESISTANCE")

                stock_friday_comment = stockdb.Friday.split(", ")
                if len(stock_friday_comment) == 1:
                    data.append(" ")
                    data.extend((" "," "," "))
                for i in stock_friday_comment:
                    i = i.replace("[", "")
                    i = i.replace("'", "")
                    i = i.replace("]", "")
                    if re.search(priceregex, i):
                        match = re.search(priceregex, i)
                        data.append(match.group(2))
                    if re.search(rsiregex, i):
                        match = re.search(rsiregex, i)
                        data.append(match.group(1))
                        data.append(pe[0])
                    if ('Price Zone: INCONCLUSIVE' in i):
                        data.append("INCONCLUSIVE")
                    if ('Price Zone: In SUPPORT Zone' in i):
                        data.append("SUPPORT")
                    if ('Price Zone: In RESISTANCE Zone' in i):
                        data.append("RESISTANCE")

                stock_list.append(data)

        except Exception as e:
            #print("Expection. Did not get data from DB")
            print("Index: Did not get data from DB for user: {} is {}".format(request.user.username, str(e)))

        return render(request, 'index.html',{
            "data": stock_list,

        })

def stockdetails(request,id):
    user_stock_list = []
    user_stock_list.append(id)
    if not request.user.is_authenticated:
        return redirect('users:login')

    else:
        try:
            profile_obj = Profile.objects.get(user=request.user)

            for stock in user_stock_list:
                new_stock_finance_comment = ""
                new_stock_monday_comment = ""
                new_stock_tuesday_comment = ""
                new_stock_wednesday_comment = ""
                new_stock_thursday_comment = ""
                new_stock_friday_comment = ""
                stock = ''.join(e for e in stock if e.isalnum())
                Model = apps.get_model('dailycandle', stock)
                stockdb = Model.objects.get(id=1)
                stock_finance_comment = stockdb.Finance.split(", ")
                for i in stock_finance_comment:
                    i = i.replace("[", "")
                    i = i.replace("'", "")
                    i = i.replace("]", "")
                    new_stock_finance_comment += i
                    new_stock_finance_comment += ". "

                stock_monday_comment = stockdb.Monday.split(", ")
                for i in stock_monday_comment:
                    i = i.replace("[", "")
                    i = i.replace("'", "")
                    i = i.replace("]", "")
                    new_stock_monday_comment += i
                    new_stock_monday_comment += ". "

                stock_tuesday_comment = stockdb.Tuesday.split(", ")
                for i in stock_tuesday_comment:
                    i = i.replace("[", "")
                    i = i.replace("'", "")
                    i = i.replace("]", "")
                    new_stock_tuesday_comment += i
                    new_stock_tuesday_comment += ". "

                stock_wednesday_comment = stockdb.Wednesday.split(", ")
                for i in stock_wednesday_comment:
                    i = i.replace("[", "")
                    i = i.replace("'", "")
                    i = i.replace("]", "")
                    new_stock_wednesday_comment += i
                    new_stock_wednesday_comment += ". "

                stock_thursday_comment = stockdb.Thursday.split(", ")
                for i in stock_thursday_comment:
                    i = i.replace("[", "")
                    i = i.replace("'", "")
                    i = i.replace("]", "")
                    new_stock_thursday_comment += i
                    new_stock_thursday_comment += ". "

                stock_friday_comment = stockdb.Friday.split(", ")
                for i in stock_friday_comment:
                    i = i.replace("[", "")
                    i = i.replace("'", "")
                    i = i.replace("]", "")
                    new_stock_friday_comment += i
                    new_stock_friday_comment += ". "

        except Exception as e:
            print("Expection. Did not get data from DB")
            message = "Expection Occurred: "+ str(e)
            return render(request, 'stockdetails.html', {
                "message": message,
            })

    return render(request, 'stockdetails.html', {
        "finance": new_stock_finance_comment.split(". "),
        "monday": new_stock_monday_comment.split(". "),
        "tuesday": new_stock_tuesday_comment.split(". "),
        "wednesday": new_stock_wednesday_comment.split(". "),
        "thursday": new_stock_thursday_comment.split(". "),
        "friday": new_stock_friday_comment.split(". "),
    })

def holding(request):
    nudgedata = []
    profile_obj = Profile.objects.get(user=request.user)
    if profile_obj.nudgedata is not None:
        try:
            profile_nudge_stocklist = profile_obj.nudgedata['nudgeStockList']
            profile_nudge_stockprice = profile_obj.nudgedata['nudgeStockListPrice']
            profile_maxprofit = profile_obj.nudgedata['maxprofit']
            profile_maxloss = profile_obj.nudgedata['maxloss']
            if len(profile_maxprofit) == 0:
                profile_maxprofit = 30
            if len(profile_maxloss) == 0:
                profile_maxloss = 15
        except Exception as e:
            print("Holding Error:", str(e))

        today_day = datetime.datetime.now().strftime('%A')
        priceregex = r"Stock: 200DayAverage: ([a-zA-Z0-9.\s-]+)\(ie ([0-9.a-zA-Z]+)\)"

        for i in range(len(profile_nudge_stocklist)):
            data = []
            if profile_nudge_stocklist[i]:
                profile_nudge_stocklist[i] = ''.join(e for e in profile_nudge_stocklist[i] if e.isalnum())
                data.append(profile_nudge_stocklist[i])
                data.append(companyicon[profile_nudge_stocklist[i]])
                buyprice = profile_nudge_stockprice[i]
                data.append(int(buyprice))
                try:
                    Model = apps.get_model('dailycandle', profile_nudge_stocklist[i])
                    stockdb = Model.objects.get(id=1)

                    if today_day == 'Saturday':
                        stockcomment = stockdb.Friday.split(", ")
                    if today_day == 'Sunday':
                        stockcomment = stockdb.Friday.split(", ")
                    if today_day == 'Monday':
                        stockcomment = stockdb.Monday.split(", ")
                    if today_day == 'Tuesday':
                        stockcomment = stockdb.Tuesday.split(", ")
                    if today_day == 'Wednesday':
                        stockcomment = stockdb.Wednesday.split(", ")
                    if today_day == 'Thursday':
                        stockcomment = stockdb.Thursday.split(", ")
                    if today_day == 'Friday':
                        stockcomment = stockdb.Friday.split(", ")

                    for i in stockcomment:
                        i = i.replace("[", "")
                        i = i.replace("'", "")
                        i = i.replace("]", "")
                        if re.search(priceregex, i):
                            match = re.search(priceregex, i)
                            if match.group(2) == 'nan':
                                data.append(float(match.group(2)))
                            else:
                                data.append(int(match.group(2)))
                    if math.isnan(data[3]):
                        data.append(float('nan'))
                        data.append(float('nan'))
                        data.append("Active")
                    else:
                        if data[3] >= data[2]:
                            data.append(data[3])
                            profit = data[3] - data[2]
                            data.append(round((profit / data[2]) * 100, 2))
                            if round((profit / data[2]) * 100, 2) >= int(profile_maxprofit):
                                data.append("Profit Target Reached")
                            else:
                                data.append("Active")
                        else:
                            data.append(data[2])
                            loss = data[3] - data[2]
                            data.append(round((loss / data[3]) * 100, 2))
                            if abs(round((loss / data[3]) * 100, 2)) >= int(profile_maxloss):
                                data.append("Loss Target Reached")
                            else:
                                data.append("Active")

                except Exception as e:
                    pass
                    print("Holding Error for user: {} is {}".format(request.user.username,str(e)))

            nudgedata.append(data)

        return render(request, 'holding.html', {
            "profile_nudge_stocklist": profile_nudge_stocklist,
            "profile_nudge_stockprice": profile_nudge_stockprice,
            "nudgedata": nudgedata,
        })
    else:
        return render(request, 'holding.html', {})
    
def profile(request):

    if not request.user.is_authenticated:
        return redirect('users:login')

    else:
        #print("Profile Page:",request.user)
        nse = Nse()
        nudgestocklist = []
        nudgestocklistprice = []
        profile_settings = []
        profile_settings_nudge = []
        profile_nudge_stocklist = []
        profile_nudge_stockprice = []
        stocks = []

        profile_obj = Profile.objects.get(user=request.user)
        try:
            profile_nudge_stocklist = profile_obj.nudgedata['nudgeStockList']
            profile_nudge_stockprice = profile_obj.nudgedata['nudgeStockListPrice']
        except Exception as e:
            #print("Profile Error:", str(e) )
            print("Profile Error for user: {} is {}".format(request.user.username, str(e)))

        if request.method == 'POST':
            nudgestocklist = []
            nudgestocklistprice = []
            profile_settings = []
            profile_settings_nudge = []
            profile_nudge_stocklist = []
            profile_nudge_stockprice = []
            stocks = []
            email_notification = request.POST.get('emailnotification')
            nudge_notification = request.POST.get('nudgenotification')
            maxloss = request.POST.get('maxloss')
            maxprofit = request.POST.get('maxprofit')
            nudegstocklist = request.POST.getlist('product_name[]')
            nudegstocklistprice = request.POST.getlist('product_price[]')

            for i in range(len(nudegstocklist)):
                if len(nudegstocklist[i]) != 0:
                    if len(nudegstocklistprice[i]) != 0:
                        try:
                            nudegstocklist[i] = ''.join(e for e in nudegstocklist[i] if e.isalnum())
                            Model = apps.get_model('dailycandle', nudegstocklist[i])
                            stockdb = Model.objects.get(id=1)
                            profile_nudge_stocklist.append(nudegstocklist[i])
                            profile_nudge_stockprice.append(nudegstocklistprice[i])
                        except Exception as e:
                            message = "{}: Invalid Inputs. The Stock is not part of Nifty".format(nudegstocklist[i])
                            return render(request, 'profile.html', {
                                "message": message,
                                "notification": profile_obj.notification,
                                "stocks": profile_obj.stocks,
                                "nudgedata": profile_obj.nudgedata,
                                "profile_nudge_stocklist": nudegstocklist,
                                "profile_nudge_stockprice": nudegstocklistprice,
                            })
                    else:
                        message = "{}: Incomplete Inputs. Empty Buy Price field in the Stock Nudge List.".format(
                            nudegstocklist[i])
                        return render(request, 'profile.html', {
                            "message": message,
                            "notification": profile_obj.notification,
                            "stocks": profile_obj.stocks,
                            "nudgedata": profile_obj.nudgedata,
                            "profile_nudge_stocklist": nudegstocklist,
                            "profile_nudge_stockprice": nudegstocklistprice,
                        })

            for selected_stocks in request.POST.values():
                stocks.append(selected_stocks)

            if email_notification and nudge_notification:
                profile_obj.stocks = stocks[7:]
            if email_notification and not nudge_notification:
                profile_obj.stocks = stocks[6:]
            if nudge_notification and not email_notification:
                profile_obj.stocks = stocks[6:]
            if not nudge_notification and not email_notification:
                profile_obj.stocks = stocks[5:]

            if request.POST.get('emailnotification') == 'on':
                profile_settings.append(True)
            else:
                profile_settings.append(False)
            if request.POST.get('nudgenotification') == 'on':
                profile_settings_nudge.append(True)
            else:
                profile_settings_nudge.append(False)

            profile_obj.notification = profile_settings[0]
            profile_obj.nudgedata = {'nudgenotification': profile_settings_nudge[0], 'maxloss': maxloss,
                                     'maxprofit': maxprofit, 'nudgeStockList': nudegstocklist,
                                     'nudgeStockListPrice': nudegstocklistprice}
            profile_obj.save()

            message = "Profile Updated Successfully..."
            return render(request, 'profile.html', {
                "message": message,
                "notification": profile_obj.notification,
                "stocks": profile_obj.stocks,
                "nudgedata": profile_obj.nudgedata,
                "profile_nudge_stocklist": profile_nudge_stocklist,
                "profile_nudge_stockprice": profile_nudge_stockprice,
            })
        else:
            return render(request, 'profile.html', {
                "notification": profile_obj.notification,
                "stocks": profile_obj.stocks,
                "nudgedata": profile_obj.nudgedata,
                "profile_nudge_stocklist": profile_nudge_stocklist,
                "profile_nudge_stockprice": profile_nudge_stockprice,
            })

def metrics(request):
    if not request.user.is_authenticated:
        return redirect('users:login')

    else:
        if request.user.username == 'djays':
            userlogin = {}
            userlogin_list = []
            userlogin_count_by_days = {}
            users = User.objects.all()
            today = datetime.datetime.today()

            for i in users:
                if int(today.year) == int(i.last_login.strftime('%Y')) and int(today.month) == int(i.last_login.strftime('%m')):
                    userlogin[i.last_login.strftime('%Y-%m-%d')] = i
                    userlogin_list.append(i.last_login.strftime('%Y-%m-%d'))
            for i in userlogin_list:
                if i in userlogin_count_by_days:
                    userlogin_count_by_days[i] += 1
                else:
                    userlogin_count_by_days[i] = 1

            users_count = User.objects.all().count()
            watchlist_alert_count = Profile.objects.filter(notification=True)
            holding_alert_count = Profile.objects.filter(nudgedata__nudgenotification=True)
            return render(request, 'metrics.html', {
                "users_count": users_count,
                "watchlist_alert_count": len(watchlist_alert_count),
                "holding_alert_count": len(holding_alert_count),
                "userlogin_count_by_days": userlogin_count_by_days,
            })
        else:
            return redirect('users:login')


def get_analyze_data(stock):
    high_closingPrice = []
    low_closingPrice = []
    all_high_peak_dict = {}
    all_low_peak_dict = {}
    peaks = []
    bottoms = []
    high_begining = 0
    high_end = 3
    low_begining = 0
    low_end = 3
    h1 = 0
    h2 = 1
    h3 = 2
    l1 = 0
    l2 = 1
    l3 = 2
    trend_direction = []
    trend = 0
    down_swing = []
    up_swing = []
    relative_threshold = 30
    volume_movement = []
    price_movement = []
    price_delta = []
    trend_end = []
    N_DAYS_AGO = 1095
    end_date = date.today() + timedelta(days=1)
    #end_date = date.today()
    start_date = date.today() - timedelta(days=N_DAYS_AGO)

    try:
        stock_info = yf.Ticker(stock.upper() + '.NS').info
        stock_data = yf.download(stock.upper() + '.NS', start=start_date, end=end_date)
        #print("Tracking Stock:", stock.upper())
        #print("Before Modification:")
        #print(stock_data[-5:])
        check_last_traded_day = stock_data[-1:].index[0].strftime('%A')
        check_today_day = datetime.datetime.now().strftime('%A')
        if check_today_day != check_last_traded_day:
            print("Confirm Trading Day: There is a mismatch in trading date")
            NseDate, NseOpen, NseHigh, NseLow, NseClose, NseAdjClose, NseVolume = get_nse_date()
            stock_data.loc[len(stock_data.index)] = [NseOpen, NseHigh, NseLow, NseClose, NseAdjClose, NseVolume]
            stock_data.rename({stock_data.index[-1]: NseDate}, inplace=True)
            #print("After Modification:")
            #print(stock_data[-5:])
    except Exception as e:
        print("Yahoo Connection:",e)

    # Find the average movement in price
    threshold = 0
    avg_price_movement = int(round(abs(stock_data['Close'][-248:] - stock_data['Open'][-248:]).sum() / len(stock_data[-248:]), 0)) + threshold

    # Convert the DateTime indexs to normal string indexs:
    pydate_array = stock_data.index.to_pydatetime()
    date_only_array = np.vectorize(lambda s: s.strftime('%Y-%m-%d'))(pydate_array)
    date_only_series = pd.Series(date_only_array)
    stock_data.index = date_only_series

    # Prepare dictionary of date:closing price:
    closingPrice = stock_data['Close']
    closingPrice_values = stock_data['Close'].values

    data_dict = {}
    for i in range(len(closingPrice)):
        data_dict[closingPrice.index[i]] = closingPrice.values[i]

    data_dict_keys = list(data_dict.keys())
    data_dict_values = list(data_dict.values())

    # Finding all high peaks:
    for i in range(len(closingPrice)):
        if len(closingPrice[high_begining:high_end]) < 0:
            pass
        else:
            high_closingPrice.append(closingPrice[high_begining:high_end].max())

        high_begining = high_begining + 3
        high_end = high_end + 3

    while h1 <= len(high_closingPrice) - 2:

        if (high_closingPrice[h1] < high_closingPrice[h2]) and (high_closingPrice[h2] > high_closingPrice[h3]):
            peaks.append(high_closingPrice[h2])

        h1 = h1 + 1
        h2 = h2 + 1
        h3 = h3 + 1

    for i in peaks:
        all_high_peak_dict[data_dict_keys[data_dict_values.index(i)]] = i

    # Finding all low bottoms:
    for i in range(len(closingPrice)):
        if len(closingPrice[low_begining:low_end]) < 0:
            pass
        else:
            low_closingPrice.append(closingPrice[low_begining:low_end].min())

        low_begining = low_begining + 3
        low_end = low_end + 3

    while l1 <= len(low_closingPrice) - 2:

        if (low_closingPrice[l1] > low_closingPrice[l2]) and (low_closingPrice[l2] < low_closingPrice[l3]):
            bottoms.append(low_closingPrice[l2])
            # print(high_closingPrice[l2])

        l1 = l1 + 1
        l2 = l2 + 1
        l3 = l3 + 1

    for i in bottoms:
        all_low_peak_dict[data_dict_keys[data_dict_values.index(i)]] = i

    # Get all values to a list
    peak_highs_lists = list(all_high_peak_dict.values())
    peak_low_lists = list(all_low_peak_dict.values())

    # Detect the trend:
    num_of_peaks = len(peak_highs_lists)

    for i in range(len(peak_highs_lists[-num_of_peaks:])):

        if i != len(peak_highs_lists[-num_of_peaks:]) - 1:

            if peak_highs_lists[-num_of_peaks:][i] >= peak_highs_lists[-num_of_peaks:][i + 1]:
                trend_direction.append(0)
            else:
                trend_direction.append(1)

    if trend_direction.count(1) > trend_direction.count(0):
        trend = 1
    elif trend_direction.count(1) == trend_direction.count(0):
        trend = 1
    else:
        trend = 0

    # Get today's closing price:
    today_price = stock_data['Close'][-1:].values
    today_volume = stock_data['Volume'][-1:].values
    # today_price = 1288

    # Detect reversal swing
    for i in peak_highs_lists:
        if math.isclose(today_price, i, abs_tol=avg_price_movement):
            down_swing.append(data_dict_keys[data_dict_values.index(i)])
            down_swing.append(i)

    for i in peak_low_lists:
       if math.isclose(today_price, i, abs_tol=avg_price_movement):
            up_swing.append(data_dict_keys[data_dict_values.index(i)])
            up_swing.append(i)

    # Find the difference in up and down swing
    if up_swing:
        for i in peak_highs_lists:
            if i > up_swing[1]:
                price_delta.append(i - up_swing[1])
                price_movement.append(i)
                price_delta.sort()
                price_movement.sort()
        trend_end.append(data_dict_keys[data_dict_values.index(stock_data['Close'].loc[up_swing[0]:].max())])
        trend_end.append(stock_data['Close'].loc[up_swing[0]:].max())

    if down_swing:
        for i in peak_low_lists:
            if i < down_swing[1]:
                price_delta.append(down_swing[1] - i)
                price_movement.append(i)
                price_delta.sort(reverse=True)
                price_movement.sort(reverse=True)
        trend_end.append(data_dict_keys[data_dict_values.index(stock_data['Close'].loc[down_swing[0]:].min())])
        trend_end.append(stock_data['Close'].loc[down_swing[0]:].min())

    if stock_data[-1:]['Close'].values[0] - stock_data[-1:]['Open'].values[0] > 0:
        wick = stock_data[-1:]['High'].values[0] - stock_data[-1:]['Close'].values[0]
        tail = stock_data[-1:]['Open'].values[0] - stock_data[-1:]['Low'].values[0]

    else:
        wick = stock_data[-1:]['High'].values[0] - stock_data[-1:]['Open'].values[0]
        tail = stock_data[-1:]['Close'].values[0] - stock_data[-1:]['Low'].values[0]

    candle_body = stock_data['Close'][-1] - stock_data['Open'][-1]

    try:
        stock_averageDailyVolume10Day = stock_info['averageDailyVolume10Day']
    except Exception as e:
        print("No Volume Data:", e)
        stock_averageDailyVolume10Day = 0

    # Calculate RSI
    close = stock_data['Adj Close']
    delta = close.diff()
    delta = delta[1:]
    up, down = delta.clip(lower=0), delta.clip(upper=0).abs()
    window_length = 14
    alpha = 1 / window_length
    roll_up = up.ewm(alpha=alpha).mean()
    roll_down = down.ewm(alpha=alpha).mean()
    rs = roll_up / roll_down
    rsi = 100.0 - (100.0 / (1.0 + rs))

    # Volume
    volume_10days = list(stock_data[-10:]['Volume'].values)
    for i in range(len(volume_10days)):
        if volume_10days[i] > stock_averageDailyVolume10Day:
            volume_movement.append(1)
        else:
            volume_movement.append(0)

    return (trend, down_swing, up_swing, price_delta, price_movement, trend_end, today_price, wick, tail, stock_averageDailyVolume10Day,volume_movement,today_volume,candle_body, rsi[-1])


def format_save_data():

    end_date = date.today() + timedelta(days=1)
    #end_date = date.today()
    start_date = date.today() - timedelta(days=1)
    stock_data = yf.download('HCLTECH.NS', start=start_date, end=end_date)

    last_traded_day = stock_data[-1:].index[0].strftime('%A')
    today_day = datetime.datetime.now().strftime('%A')

    if today_day != last_traded_day:
        print("Date: There is a mismatch in trading date")
        NseDate, NseOpen, NseHigh, NseLow, NseClose, NseAdjClose, NseVolume = get_nse_date()
        last_traded_day = NseDate.strftime('%A')

    if today_day == 'Sunday':
        print("Start DB Cleanup")
        stock_names = ['NTPC', 'UPL', 'SUNPHARMA', 'TATACONSUM', 'INDUSINDBK', 'ONGC', 'M&M', 'IOC', 'BHARTIARTL', 'ITC', 'WIPRO', 'TCS', \
                       'BRITANNIA', 'COALINDIA', 'GRASIM', 'TATAMOTORS', 'TITAN', 'BPCL', 'JSWSTEEL', 'INFY', 'HDFC','DIVISLAB', \
                       'SHREECEM', 'CIPLA', 'ADANIPORTS', 'HCLTECH', 'HINDALCO', 'BAJFINANCE', 'KOTAKBANK', 'ASIANPAINT', 'NESTLEIND', \
                       'HDFCLIFE', 'ULTRACEMCO', 'RELIANCE', 'TATASTEEL', 'HINDUNILVR', 'SBILIFE', 'LT', 'DRREDDY', 'HDFCBANK', 'EICHERMOT', \
                       'SBIN', 'BAJAJFINSV', 'AXISBANK', 'HEROMOTOCO', 'ICICIBANK', 'POWERGRID', 'TECHM', 'MARUTI']
        for stock in stock_names:
            stock = ''.join(e for e in stock if e.isalnum())
            Model = apps.get_model('dailycandle', stock)
            stockdb = Model.objects.get(id=1)
            stockdb.Finance = ""
            stockdb.Monday = ""
            stockdb.Tuesday = ""
            stockdb.Wednesday = ""
            stockdb.Thursday = ""
            stockdb.Friday = ""
            stockdb.save()
        print("Cleanup DB Complete")

    elif(today_day == 'Saturday'):
        print("Today is Saturday, Market is Closed ")
        pass

    else:
        if today_day == last_traded_day:
            #stock_names = ['M&M','NTPC']
            stock_names = ['NTPC', 'UPL', 'SUNPHARMA', 'TATACONSUM', 'INDUSINDBK', 'ONGC', 'M&M', 'IOC', 'BHARTIARTL', 'ITC','WIPRO', 'TCS', \
                           'BRITANNIA', 'COALINDIA', 'GRASIM', 'TATAMOTORS', 'TITAN', 'BPCL', 'JSWSTEEL', 'INFY', 'HDFC','DIVISLAB', \
                           'SHREECEM', 'CIPLA', 'ADANIPORTS', 'HCLTECH', 'HINDALCO', 'BAJFINANCE', 'KOTAKBANK','ASIANPAINT','NESTLEIND',\
                           'HDFCLIFE','ULTRACEMCO','RELIANCE','TATASTEEL','HINDUNILVR','SBILIFE','LT','DRREDDY','HDFCBANK','EICHERMOT',\
                           'SBIN','BAJAJFINSV','AXISBANK','HEROMOTOCO','ICICIBANK','POWERGRID','TECHM','MARUTI']

            for stock in stock_names:
                down_recent = []
                up_recent = []
                stock_comments = []
                stock_finance = []

                try:
                    stock_info = yf.Ticker(stock.upper() + '.NS').info
                    stock_beta = stock_info['beta']
                    stock_forwardPE = stock_info['forwardPE']
                    stock_forwardEps = stock_info['forwardEps']
                    stock_twoHundredDayAverage = stock_info['twoHundredDayAverage']
                    stock_yahoo_recommendationKey = stock_info['recommendationKey']
                    stock_currentRatio = stock_info['currentRatio']
                    stock_quickRatio = stock_info['quickRatio']
                    stock_debtToEquity = stock_info['debtToEquity']

                except Exception as e:
                    print("Stock Info:",stock_info)
                    print("Stock Connection:", e)

                if stock_info['regularMarketPrice'] is None:
                    print("{}: Invalid Stock Name. Closing the application".format(stock))
                else:
                    trend, down_swing, up_swing, price_delta, price_movement, trend_end, today_price, wick, tail, stock_averageDailyVolume10Day, volume_movement, today_volume, candle_body, rsi = get_analyze_data(stock)

                    stock_comments.append("Date: {}".format(date.today()))
                    stock_finance.append("Financial: Beta: {} - A high ratio indicates volatile stock".format(stock_beta))
                    if stock_forwardPE is None:
                        stock_finance.append("Financial: Forward PE: {}".format(stock_forwardPE))
                    else:
                        stock_finance.append("Financial: Forward PE: {}".format(round(stock_forwardPE)))
                    stock_finance.append("Financial: Forward EPS: {}".format(stock_forwardEps))
                    stock_finance.append("Financial: Current Ratio: {}".format(stock_currentRatio))
                    stock_finance.append("Financial: Quick Ratio: {}".format(stock_quickRatio))
                    stock_finance.append("Financial: DebtToEquity Ratio: {}".format(stock_debtToEquity))

                    if np.isnan(today_price):
                        stock_comments.append("Stock: 200DayAverage: {} - Todays shareprice (ie {}) is higher than 200DayAverage".format(stock_twoHundredDayAverage, (today_price[0])))
                    else:
                        if (today_price > stock_twoHundredDayAverage):
                            stock_comments.append("Stock: 200DayAverage: {} - Todays shareprice (ie {}) is higher than 200DayAverage".format(stock_twoHundredDayAverage,round(today_price[0])))
                        elif (today_price == stock_twoHundredDayAverage):
                            stock_comments.append("Stock: 200DayAverage: {} - Todays shareprice (ie {}) is same as 200DayAverage".format(stock_twoHundredDayAverage,round(today_price[0])))
                        else:
                            stock_comments.append("Stock: 200DayAverage: {} - Todays shareprice (ie {}) is lower than 200DayAverage".format(stock_twoHundredDayAverage,round(today_price[0])))

                    stock_comments.append("Stock: Relative Strength Index: {}% - Closer to 80 indicates overbought and closer to 20 indicates oversold".format(round(rsi)))

                    if not up_swing and not down_swing:
                        if trend == 1:
                           stock_comments.append("Last 3 Yrs Price Trend: Up")
                        elif trend == 0:
                            stock_comments.append("Last 3 Yrs Price Trend: Down")
                        else:
                            stock_comments.append("Last 3 Yrs Price Trend: Nondeterministic")

                        stock_comments.append("Price Zone: INCONCLUSIVE - No past reversal seen at this price range")
                        stock_comments.append("Candle: Wick length:{} - Longer Wick indicates selling pressure".format(wick))
                        if candle_body >= 0:
                            stock_comments.append("Candle: Body length:{} - Stock price increased by {}".format(candle_body, candle_body))
                        else:
                            stock_comments.append("Candle: Body length:{} - Stock price decreased by {}".format(candle_body, candle_body))
                        stock_comments.append("Candle: Tail length:{} - Longer Tail indicates buying pressure".format(tail))
                        stock_comments.append("Volume: In Last 10 days the average traded Volume is {} and on {} day(s) the daily traded volume exceeded the last 10 days average traded volume".format(stock_averageDailyVolume10Day, volume_movement.count(1)))
                        if (stock_averageDailyVolume10Day > today_volume):
                            volume_diff = ((stock_averageDailyVolume10Day - today_volume) / stock_averageDailyVolume10Day) * 100
                            stock_comments.append("Volume: Todays volume (ie {}) was lower than the last 10 days average traded volume by {} %".format(today_volume[0], volume_diff[0]))
                        else:
                            volume_diff = ((today_volume - stock_averageDailyVolume10Day) / stock_averageDailyVolume10Day) * 100
                            stock_comments.append("Volume: Todays volume (ie {}) was higher than the last 10 days average traded volume by {} %".format(today_volume[0], volume_diff[0]))

                    if up_swing and down_swing:
                        if trend == 1:
                            stock_comments.append("Last 3 Yrs Price Trend: Up")
                        elif trend == 0:
                            stock_comments.append("Last 3 Yrs Price Trend: Down")
                        else:
                            stock_comments.append("Last 3 Yrs Price Trend: Nondeterministic")

                        for i in down_swing:
                            if isinstance(i, str):
                                targetdate = datetime.datetime.strptime(i, '%Y-%m-%d')
                                deltadays = date.today() - targetdate.date()
                                if deltadays.days < 365:
                                    down_recent.append(deltadays.days)

                        for i in up_swing:
                            if isinstance(i, str):
                                targetdate = datetime.datetime.strptime(i, '%Y-%m-%d')
                                deltadays = date.today() - targetdate.date()
                                if deltadays.days < 365:
                                    up_recent.append(deltadays.days)

                        if len(down_recent) < len(up_recent):
                            stock_comments.append("Price Zone: In SUPPORT Zone")
                            stock_comments.append("Candle: Wick length:{} - Longer Wick indicates selling pressure".format(wick))
                            if candle_body >= 0:
                                stock_comments.append("Candle: Body length:{} - Stock price increased by {}".format(candle_body, candle_body))
                            else:
                                stock_comments.append("Candle: Body length:{} - Stock price decreased by {}".format(candle_body, candle_body))
                            stock_comments.append("Candle: Tail length:{} - Longer Tail indicates buying pressure".format(tail))
                            stock_comments.append("Volume: In Last 10 days the average traded Volume is {} and on {} day(s) the daily traded volume exceeded the last 10 days average traded volume".format(stock_averageDailyVolume10Day, volume_movement.count(1)))
                            if (stock_averageDailyVolume10Day > today_volume):
                                volume_diff = ((stock_averageDailyVolume10Day - today_volume) / stock_averageDailyVolume10Day) * 100
                                stock_comments.append("Volume: Todays volume (ie {}) was lower than the last 10 days average traded volume by {} %".format(today_volume[0],volume_diff[0]))
                            else:
                                volume_diff = ((today_volume - stock_averageDailyVolume10Day) / stock_averageDailyVolume10Day) * 100
                                stock_comments.append("Volume: Todays volume (ie {}) was higher than the last 10 days average traded volume by {} %".format(today_volume[0],volume_diff[0]))

                        elif len(down_recent) == len(up_recent):
                            stock_comments.append("Price Zone: INCONCLUSIVE - In last 1 year the stock has been in the SUPPORT and RESISTANCE zones equal number of times")
                            stock_comments.append("Candle: Wick length:{} - Longer Wick indicates selling pressure".format(wick))
                            if candle_body >= 0:
                                stock_comments.append("Candle: Body length:{} - Stock price increased by {}".format(candle_body, candle_body))
                            else:
                                stock_comments.append("Candle: Body length:{} - Stock price decreased by {}".format(candle_body, candle_body))
                            stock_comments.append("Candle: Tail length:{} - Longer Tail indicates buying pressure".format(tail))
                            stock_comments.append("Volume: In Last 10 days the average traded Volume is {} and on {} day(s) the daily traded volume exceeded the last 10 days average traded volume".format(stock_averageDailyVolume10Day, volume_movement.count(1)))
                            if (stock_averageDailyVolume10Day > today_volume):
                                volume_diff = ((stock_averageDailyVolume10Day - today_volume) / stock_averageDailyVolume10Day) * 100
                                stock_comments.append("Volume: Todays volume (ie {}) was lower than the last 10 days average traded volume by {} %".format(today_volume[0],volume_diff[0]))
                            else:
                                volume_diff = ((today_volume - stock_averageDailyVolume10Day) / stock_averageDailyVolume10Day) * 100
                                stock_comments.append("Volume: Todays volume (ie {}) was higher than the last 10 days average traded volume by {} %".format(today_volume[0],volume_diff[0]))

                        else:
                            stock_comments.append("Price Zone: In RESISTANCE Zone")
                            stock_comments.append("Candle: Wick length:{} - Longer Wick indicates selling pressure".format(wick))
                            if candle_body >= 0:
                                stock_comments.append("Candle: Body length:{} - Stock price increased by {}".format(candle_body, candle_body))
                            else:
                                stock_comments.append("Candle: Body length:{} - Stock price decreased by {}".format(candle_body, candle_body))
                            stock_comments.append("Candle: Tail length:{} - Longer Tail indicates buying pressure".format(tail))
                            stock_comments.append("Volume: In Last 10 days the average traded Volume is {} and on {} day(s) the daily traded volume exceeded the last 10 days average traded volume".format(stock_averageDailyVolume10Day, volume_movement.count(1)))
                            if (stock_averageDailyVolume10Day > today_volume):
                                volume_diff = ((stock_averageDailyVolume10Day - today_volume) / stock_averageDailyVolume10Day) * 100
                                stock_comments.append("Volume: Todays volume (ie {}) was lower than the last 10 days average traded volume by {} %".format(today_volume[0],volume_diff[0]))
                            else:
                                volume_diff = ((today_volume - stock_averageDailyVolume10Day) / stock_averageDailyVolume10Day) * 100
                                stock_comments.append("Volume: Todays volume (ie {}) was higher than the last 10 days average traded volume by {} %".format(today_volume[0],volume_diff[0]))

                        stock_comments.append("Price Action: Multiple SUPPORTs and RESISTANCEs are detected at the current price point. Here is the list:")
                        downcount = 0
                        for i in range(len(down_swing)):
                            if downcount < len(down_swing):
                                stock_comments.append("Stock faced RESISTANCE on date:{} at price:{}".format(down_swing[downcount],down_swing[downcount + 1]))
                                downcount = downcount + 2

                        upcount = 0
                        for i in range(len(up_swing)):
                            if upcount < len(up_swing):
                                stock_comments.append("Stock got SUPPORT on date:{} at price:{}".format(up_swing[upcount], up_swing[upcount + 1]))
                                upcount = upcount + 2

                    else:
                        if up_swing:
                            if trend == 1:
                                stock_comments.append("Last 3 Yrs Price Trend: Up")
                            elif trend == 0:
                                stock_comments.append("Last 3 Yrs Price Trend: Down")
                            else:
                                stock_comments.append("Last 3 Yrs Price Trend: Nondeterministic")

                            if len(up_swing) > 2:
                                stock_comments.append("Price Zone: In SUPPORT Zone")
                            else:
                                stock_comments.append("Price Zone: INCONCLUSIVE - In past less than 2 price reversals had occurred at this price range")
                            stock_comments.append("Candle: Wick length:{} - Longer Wick indicates selling pressure".format(wick))
                            if candle_body >= 0:
                                stock_comments.append("Candle: Body length:{} - Stock price increased by {}".format(candle_body, candle_body))
                            else:
                                stock_comments.append("Candle: Body length:{} - Stock price decreased by {}".format(candle_body, candle_body))
                            stock_comments.append("Candle: Tail length:{} - Longer Tail indicates buying pressure".format(tail))
                            stock_comments.append("Volume: In Last 10 days the average traded Volume is {} and on {} day(s) the daily traded volume exceeded the last 10 days average traded volume".format(stock_averageDailyVolume10Day, volume_movement.count(1)))
                            if (stock_averageDailyVolume10Day > today_volume):
                                volume_diff = ((stock_averageDailyVolume10Day - today_volume) / stock_averageDailyVolume10Day) * 100
                                stock_comments.append("Volume: Todays volume (ie {}) was lower than the last 10 days average traded volume by {} %".format(today_volume[0],volume_diff[0]))
                            else:
                                volume_diff = ((today_volume - stock_averageDailyVolume10Day) / stock_averageDailyVolume10Day) * 100
                                stock_comments.append("Volume: Todays volume (ie {}) was higher than the last 10 days average traded volume by {} %".format(today_volume[0],volume_diff[0]))

                            stock_comments.append("Price Action: In past SUPPORT was experienced at stock price {}".format(today_price))
                            stock_comments.append("The last detected SUPPORT happened on date:{} at price:{}".format(up_swing[0], up_swing[1]))
                            stock_comments.append("The UP trend reversal lasted till date:{} to price:{}".format(trend_end[0], trend_end[1]))
                            stock_comments.append("The UP trend reversal lasted for Rs:{}".format(trend_end[1] - up_swing[1]))

                        if down_swing:
                            if trend == 1:
                                stock_comments.append("Last 3 Yrs Price Trend: Up")
                            elif trend == 0:
                                stock_comments.append("Last 3 Yrs Price Trend: Down")
                            else:
                                stock_comments.append("Last 3 Yrs Price Trend: Nondeterministic")

                            if len(down_swing) > 2:
                                stock_comments.append("Price Zone: In RESISTANCE Zone")
                            else:
                                stock_comments.append("Price Zone: INCONCLUSIVE  - In past less than 2 price reversals had occurred at this price range")
                            stock_comments.append("Candle: Wick length:{} - Longer Wick indicates selling pressure".format(wick))
                            if candle_body >= 0:
                                stock_comments.append("Candle: Body length:{} - Stock price increased by {}".format(candle_body, candle_body))
                            else:
                                stock_comments.append("Candle: Body length:{} - Stock price decreased by {}".format(candle_body, candle_body))
                            stock_comments.append("Candle: Tail length:{} - Longer Tail indicates buying pressure".format(tail))
                            stock_comments.append("Volume: In Last 10 days the average traded Volume is {} and on {} day(s) the daily traded volume exceeded the last 10 days average traded volume".format(stock_averageDailyVolume10Day, volume_movement.count(1)))
                            if (stock_averageDailyVolume10Day > today_volume):
                                volume_diff = ((stock_averageDailyVolume10Day - today_volume) / stock_averageDailyVolume10Day) * 100
                                stock_comments.append("Volume: Todays volume (ie {}) was lower than the last 10 days average traded volume by {} %".format(today_volume[0],volume_diff[0]))
                            else:
                                volume_diff = ((today_volume - stock_averageDailyVolume10Day) / stock_averageDailyVolume10Day) * 100
                                stock_comments.append("Volume: Todays volume (ie {}) was higher than the last 10 days average traded volume by {} %".format(today_volume[0],volume_diff[0]))

                            stock_comments.append("Price Action: In past RESISTANCE was experience at stock price {}".format(today_price))
                            stock_comments.append("The last detected RESISTANCE happened on date:{} at price:{}".format(down_swing[0],down_swing[1]))
                            stock_comments.append("The down trend reversal lasted till date:{} to price:{}".format(trend_end[0], trend_end[1]))
                            stock_comments.append("The down trend lasted for Rs:{}".format(trend_end[1] - down_swing[1]))

                #for comment in stock_finance:
                #    print(comment)

                #for comment in stock_comments:
                #    print(comment)

                stock = ''.join(e for e in stock if e.isalnum())
                Model = apps.get_model('dailycandle', stock)
                stockdb = Model.objects.get(id=1)
                stockdb.Finance = str(stock_finance)
                if today_day == 'Monday':
                    stockdb.Monday = str(stock_comments)
                if today_day == 'Tuesday':
                    stockdb.Tuesday = str(stock_comments)
                if today_day == 'Wednesday':
                    stockdb.Wednesday = str(stock_comments)
                if today_day == 'Thursday':
                    stockdb.Thursday = str(stock_comments)
                if today_day == 'Friday':
                    stockdb.Friday = str(stock_comments)

                stockdb.save()
                #time.sleep(60)

            send_daily_email()

        else:
            print("Its {} - Market is closed today.".format(today_day))

    return

def send_daily_email():
    stock_list = []
    today_day = datetime.datetime.now().strftime('%A')
    emails = User.objects.filter(is_active=True).exclude(email='').values_list('email', flat=True)
    for email in emails:
        user_obj = User.objects.get(email=email)
        if user_obj.username != 'admin':
            #print("User SendEmail:",user_obj.username)
            profile_obj = Profile.objects.get(user=user_obj.id)
            profile_stocks = profile_obj.stocks
            profile_notification = profile_obj.notification
            profile_nudge_notification = profile_obj.nudgedata['nudgenotification']

            finance = {}
            monday = {}
            tuesday = {}
            wednesday = {}
            thursday = {}
            friday = {}
            if profile_notification and len(profile_stocks) >= 3:

                for stock in profile_stocks.split(","):
                    stock = stock.replace("[", "")
                    stock = stock.replace("'", "")
                    stock = stock.replace("]", "")
                    stock = stock.strip()
                    stock_list.append(stock)
                    stock = ''.join(e for e in stock if e.isalnum())
                    Model = apps.get_model('dailycandle', stock)
                    stockdb = Model.objects.get(id=1)
                    stock_finance_comment = stockdb.Finance.split(", ")

                    new_stock_finance_comment = ""
                    new_stock_monday_comment = ""
                    new_stock_tuesday_comment = ""
                    new_stock_wednesday_comment = ""
                    new_stock_thursday_comment = ""
                    new_stock_friday_comment = ""
                    for i in stock_finance_comment:
                        i = i.replace("[", "")
                        i = i.replace("'", "")
                        i = i.replace("]", "")
                        new_stock_finance_comment += i
                        new_stock_finance_comment += ", "
                    finance[stock] =  new_stock_finance_comment

                    if today_day == 'Monday':
                        stock_monday_comment = stockdb.Monday.split(", ")
                        for i in stock_monday_comment:
                            i = i.replace("[", "")
                            i = i.replace("'", "")
                            i = i.replace("]", "")
                            new_stock_monday_comment += i
                            new_stock_monday_comment += ", "
                        monday[stock] =  new_stock_monday_comment
                    if today_day == 'Tuesday':
                        stock_tuesday_comment = stockdb.Tuesday.split(", ")
                        for i in stock_tuesday_comment:
                            i = i.replace("[", "")
                            i = i.replace("'", "")
                            i = i.replace("]", "")
                            new_stock_tuesday_comment += i
                            new_stock_tuesday_comment += ", "
                        tuesday[stock] = new_stock_tuesday_comment
                    if today_day == 'Wednesday':
                        stock_wednesday_comment = stockdb.Wednesday.split(", ")
                        for i in stock_wednesday_comment:
                            i = i.replace("[", "")
                            i = i.replace("'", "")
                            i = i.replace("]", "")
                            new_stock_wednesday_comment += i
                            new_stock_wednesday_comment += ", "
                        wednesday[stock] = new_stock_wednesday_comment
                    if today_day == 'Thursday':
                        stock_thursday_comment = stockdb.Thursday.split(", ")
                        for i in stock_thursday_comment:
                            i = i.replace("[", "")
                            i = i.replace("'", "")
                            i = i.replace("]", "")
                            new_stock_thursday_comment += i
                            new_stock_thursday_comment += ", "
                        thursday[stock] = new_stock_thursday_comment
                    if today_day == 'Friday':
                        stock_friday_comment = stockdb.Friday.split(", ")
                        for i in stock_friday_comment:
                            i = i.replace("[", "")
                            i = i.replace("'", "")
                            i = i.replace("]", "")
                            new_stock_friday_comment += i
                            new_stock_friday_comment += ", "
                        friday[stock] = new_stock_friday_comment

                finance[stock] = new_stock_finance_comment
                monday[stock] = new_stock_monday_comment
                tuesday[stock] = new_stock_tuesday_comment
                wednesday[stock] = new_stock_wednesday_comment
                thursday[stock] = new_stock_thursday_comment
                friday[stock] = new_stock_friday_comment


                if len(stockdb.Finance) != 0:
                    if today_day == 'Monday':
                        daily_notification = compose_email(user_obj.username,user_obj.email,stock_list,finance,monday)
                    if today_day == 'Tuesday':
                        daily_notification = compose_email(user_obj.username,user_obj.email,stock_list,finance,tuesday)
                    if today_day == 'Wednesday':
                        daily_notification = compose_email(user_obj.username,user_obj.email,stock_list,finance,wednesday)
                    if today_day == 'Thursday':
                        daily_notification = compose_email(user_obj.username,user_obj.email,stock_list,finance,thursday)
                    if today_day == 'Friday':
                        daily_notification = compose_email(user_obj.username,user_obj.email,stock_list,finance,friday)
                    #if today_day == 'Sunday':
                    #    daily_notification = compose_email(user_obj.username,user_obj.email,stock_list,finance,friday)

                    if user_obj.username == 'djays':
                        print("Send Mail:", daily_notification)
                else:
                    if user_obj.username == 'djays':
                        print("Send Mail: No data available, skipping the send email process.")

            if profile_nudge_notification:
                holding_notification = check_holding_threshold(user_obj.username,user_obj.email,profile_obj)
                if user_obj.username == 'djays':
                    print("Send Holding Email:",holding_notification)
            else:
                if user_obj.username == 'djays':
                    print("Send Holding Email: Holding Alert Flag is Off.")

    return


def check_holding_threshold(username,email,profile_obj):
    nudgedata = []
    profile_nudge_stocklist = profile_obj.nudgedata['nudgeStockList']
    profile_nudge_stockprice = profile_obj.nudgedata['nudgeStockListPrice']
    profile_maxprofit = profile_obj.nudgedata['maxprofit']
    profile_maxloss = profile_obj.nudgedata['maxloss']
    if len(profile_maxprofit) == 0:
        profile_maxprofit = 30
    if len(profile_maxloss) == 0:
        profile_maxloss = 15

    today_day = datetime.datetime.now().strftime('%A')
    priceregex = r"Stock: 200DayAverage: ([a-zA-Z0-9.\s-]+)\(ie ([0-9.a-zA-Z]+)\)"

    for i in range(len(profile_nudge_stocklist)):
        data = []
        holdingData = []
        if profile_nudge_stocklist[i]:
            profile_nudge_stocklist[i] = ''.join(e for e in profile_nudge_stocklist[i] if e.isalnum())
            data.append(profile_nudge_stocklist[i])
            data.append(companyicon[profile_nudge_stocklist[i]])
            buyprice = profile_nudge_stockprice[i]
            data.append(int(buyprice))
            try:
                Model = apps.get_model('dailycandle', profile_nudge_stocklist[i])
                stockdb = Model.objects.get(id=1)

                if today_day == 'Saturday':
                    stockcomment = stockdb.Friday.split(", ")
                if today_day == 'Sunday':
                    stockcomment = stockdb.Friday.split(", ")
                if today_day == 'Monday':
                    stockcomment = stockdb.Monday.split(", ")
                if today_day == 'Tuesday':
                    stockcomment = stockdb.Tuesday.split(", ")
                if today_day == 'Wednesday':
                    stockcomment = stockdb.Wednesday.split(", ")
                if today_day == 'Thursday':
                    stockcomment = stockdb.Thursday.split(", ")
                if today_day == 'Friday':
                    stockcomment = stockdb.Friday.split(", ")

                for i in stockcomment:
                    i = i.replace("[", "")
                    i = i.replace("'", "")
                    i = i.replace("]", "")
                    if re.search(priceregex, i):
                        match = re.search(priceregex, i)
                        if match.group(2) == 'nan':
                            data.append(float(match.group(2)))
                        else:
                            data.append(int(match.group(2)))
                if math.isnan(data[3]):
                    data.append(float('nan'))
                    data.append(float('nan'))
                    data.append("Active")
                else:
                    if data[3] >= data[2]:
                        data.append(data[3])
                        profit = data[3] - data[2]
                        data.append(round((profit / data[2]) * 100, 2))
                        if round((profit / data[2]) * 100, 2) >= int(profile_maxprofit):
                            data.append("Profit Target Reached")
                            holdingData.extend((data[0],data[2],data[3],data[5],data[6]))
                        else:
                            data.append("Active")

                    else:
                        data.append(data[2])
                        loss = data[3] - data[2]
                        data.append(round((loss / data[3]) * 100, 2))
                        if abs(round((loss / data[3]) * 100, 2)) >= int(profile_maxloss):
                            data.append("Loss Target Reached")
                            holdingData.extend((data[0], data[2], data[3], data[5], data[6]))
                        else:
                            data.append("Active")

            except Exception as e:
                pass
                print("Check Holding Error for user: {} is {}".format(username,str(e)))

            nudgedata.append(holdingData)

    try:
        if len(nudgedata[0]) > 0:
            holding_alert = compose_holding_email(username,email,profile_nudge_stocklist,nudgedata)
            return holding_alert
        else:
            if username == 'djays':
                return "No Holding Alert."
    except Exception as e:
        print("Compose Holding Email for user: {} is {}".format(username,str(e)))

    return



def get_nse_date():
    nse = Nse()
    stock_quote = nse.get_quote('hcltech')
    NseDate = stock_quote['secDate']
    NseOpen = stock_quote['open']
    NseHigh = stock_quote['dayHigh']
    NseLow = stock_quote['dayLow']
    NseClose = stock_quote['closePrice']
    NseAdjClose = stock_quote['closePrice']
    NseVolume = stock_quote['quantityTraded']

    NseDate = datetime.datetime.strptime(NseDate, '%d-%b-%Y %H:%M:%S')

    return NseDate,NseOpen,NseHigh,NseLow,NseClose,NseAdjClose,NseVolume