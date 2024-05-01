import scrapy


class MenuItem(scrapy.Item):
    name = scrapy.Field()  # 菜谱名称
    img = scrapy.Field()  # 菜谱图片
    step = scrapy.Field()  # 做法步骤
    material1 = scrapy.Field()  # 主材料
    material2 = scrapy.Field()  # 辅料
    energy = scrapy.Field()  # 热量
    sugar = scrapy.Field()  # 含糖量
    fat = scrapy.Field()  # 脂肪
    needtime = scrapy.Field()  # 所需时间
    uptime = scrapy.Field()  # 上传时间（这条不需要通过爬虫获得，在生成每条爬虫记录时插入系统时间即可）
    level = scrapy.Field()  # 难度等级
