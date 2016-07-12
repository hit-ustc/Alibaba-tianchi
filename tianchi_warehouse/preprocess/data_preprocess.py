__author__ = 'CC'

import time
from split_by_item import splitByItems
from split_by_store_item import splitByStoreItems
from split_by_store import splitByStores
from statistics_two_week import StatisticsTwoWeek
from store1_two_week import StatisticsStore1TwoWeek
from store2_two_week import StatisticsStore2TwoWeek
from store3_two_week import StatisticsStore3TwoWeek
from store4_two_week import StatisticsStore4TwoWeek
from store5_two_week import StatisticsStore5TwoWeek
from result import myResult
from store1_result import store1Result
from store2_result import store2Result
from store3_result import store3Result
from store4_result import store4Result
from store5_result import store5Result
from predict import predict
from split_by_tag import splitByTag


if __name__ == "__main__":

      # print"**************START*****************"
      # start = time.time()
      # splitByItems()
      # end = time.time()
      # print "It takes %f s to get dataset" %(end - start)
      # print"**************OVER******************"
      #
      # print"**************START*****************"
      # start = time.time()
      # splitByStoreItems()
      # end = time.time()
      # print "It takes %f s to get dataset" %(end - start)
      # print"**************OVER******************"

      # print"**************START*****************"
      # StatisticsTwoWeek()
      # print"**************OVER******************"


      # print"**************START*****************"
      # StatisticsStore5TwoWeek()
      # print"**************OVER******************"

      # print"**************START*****************"
      # StatisticsStoreTwoWeek()
      # print"**************OVER******************"

      print"**************START*****************"
      myResult()
      store1Result()
      store2Result()
      store3Result()
      store4Result()
      store5Result()
      # predict()
      # splitByTag()
      print"**************OVER******************"