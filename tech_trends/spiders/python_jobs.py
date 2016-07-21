# -*- coding: utf-8 -*-
import scrapy


class PythonJobsSpider(scrapy.Spider):
    name = "python_jobs"
    allowed_domains = ["python.org/jobs"]
    start_urls = (
        'http://www.python.org/jobs/',
    )

    def parse(self, response):
        pass
