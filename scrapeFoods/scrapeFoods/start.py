from scrapy import cmdline

cmdline.execute('scrapy crawl getIngredients -o ingredients_data.csv'.split())  # getmenu应该换成自己创建的爬虫器名称，我上面创建的爬虫器名称是getmenu
