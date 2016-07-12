__author__ = 'CC'
import os
import time
import datetime
import calendar

import sklearn.linear_model as lm
import sklearn.datasets as ds

from extract_profile_features import extract_profile_features
from extract_balance_features import extract_balance_features
from extract_interest_features import extract_interest_features


profile_features = None
interest_features = None
balance_features = None


def get_last_month_today(today):
     last_month = today.replace(day = 1) - datetime.timedelta(days = 1)
     last_month_days = calendar.monthrange(last_month.year, last_month.month)[-1]
     tmp_day = today.day if today.day <= last_month_days else last_month_days
     last_month_today = today.replace(month = last_month.month, day = tmp_day)
     return last_month_today.strftime('%Y%m%d')


def is_mon_to_thur(today):
     weekday = today.weekday()
     return weekday in xrange(0, 4)


def get_features(uid, today):
    global profile_features
    global interest_features
    global balance_features
    #print 'today:', today
    key = '%s:%s' % (uid, today)
    profile = profile_features[uid]
    today_ = datetime.datetime(*time.strptime(today, '%Y%m%d')[:3])
    yestoday = (today_ - datetime.timedelta(days = 1)).strftime('%Y%m%d')
    #print 'yestoday:', yestoday
    tmp_key = '%s:%s' % (uid, yestoday)
    if tmp_key not in balance_features:
        tmp_key = key
    if tmp_key in balance_features:
        yestoday_balance = balance_features[tmp_key]
    else:
        yestoday_balance = [1.0, 1.0]
    last_month_today = get_last_month_today(today_)
    #print 'last_month_today', last_month_today
    tmp_key = '%s:%s' % (uid, last_month_today)
    if tmp_key not in balance_features:
        tmp_key = key
    if tmp_key in balance_features:
        last_month_today_balance = balance_features[tmp_key]
    else:
        last_month_today_balance = [1.0, 1.0]
    is_mon_to_thur_ = [float(is_mon_to_thur(today_)),] #是否周一到周四
    #print 'is_mon_to_thur:', is_mon_to_thur_
    features = profile + yestoday_balance +\
        last_month_today_balance + is_mon_to_thur_ #+\
        #interest_features[today]
    #print 'features:', features
    return features


def predict():
    global profile_features
    global interest_features
    global balance_features
    path = os.path.abspath(os.path.dirname(__file__))
    user_profile_file_path = path + '/user_profile_table.csv'
    profile_features = extract_profile_features(user_profile_file_path)
    interest_file_path = path + '/mfd_day_share_interest.csv'
    interest_features = extract_interest_features(interest_file_path)
    user_balance_file_path = path + '/user_balance_table.csv'
    balance_features = extract_balance_features(user_balance_file_path)

    #feacture = profile_features + interest_features + balance_features
    #every user for every day
    x = []
    y1 = []
    y2 = []
    for key, val in balance_features.iteritems():
        uid, today = key.split(':')
        #print val[0]
        features = get_features(uid, today)
        x.append(features)
        y1.append(val[0])
        y2.append(val[1])

    clf1 = lm.LinearRegression()
    clf2 = lm.LinearRegression()
    clf1 = lm.LogisticRegression()
    clf2 = lm.LogisticRegression()
    clf1.fit(x, y1)
    clf2.fit(x, y2)
    purchase = []
    redeem = []
    for i in xrange(1, 31):
        today = '201409%02d' % (i,)
        p = 0
        r = 0
        for uid, val in profile_features.iteritems():
            features = get_features(uid, today)
            pp = clf1.predict([features,])[0]
            rr = clf2.predict([features,])[0]
            balance_features[key] = [pp, rr]
            p += pp
            r += rr
        print '%s,%s,%s' % (today, int(p), int(r))
        purchase.append(p)
        redeem.append(r)


if __name__ == '__main__':
    predict()
