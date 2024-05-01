# -*- coding: utf-8 -*-
import scrapy
import re


class IngredientsSpider(scrapy.Spider):
    name = 'getIngredients'
    allowed_domains = ['db.foodmate.net']
    start_urls = ['http://db.foodmate.net/yingyang/']

    def parse(self, response):
        categories = response.css('div#top > a')
        for category in categories:
            curCategory = category.css('::text').get()
            curCategoryHref = category.css('::attr(href)').get()
            yield response.follow(curCategoryHref, callback=self.parse2, cb_kwargs=dict(category=curCategory))

    def parse2(self, response, category: str):
        ingredientNames = response.css('li.lie > a')
        for ingredientName in ingredientNames:
            curIngredientName = ingredientName.css('::text').get()
            curIngredientHref = ingredientName.css('::attr(href)').get()
            yield response.follow(curIngredientHref, callback=self.parse3, cb_kwargs=dict(category=category, ingredientName=curIngredientName))

    def parse3(self, response, category:str, ingredientName:str):
        elementNames = response.css('div.list_m::text').getall()
        elementValues = list(
            map(lambda x: re.search('[0-9]+(\.?[0-9]+)?', x).group(0), response.css('div.list').getall()))
        res = {
            '类别': category,
            '食材名': ingredientName
        }
        for idx, elementName in enumerate(elementNames):
            res[elementName] = elementValues[idx]
        yield res
