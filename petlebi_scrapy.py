import filelock
import scrapy
import json


class PetlebiSpider(scrapy.Spider):
    name = "petlebi"
    start_urls = ["https://www.petlebi.com/"]

    def parse(self, response):
        product_urls = []
        # returns the url for popular products
        for i in range(1, 13):
            product_urls.append(response.xpath(
                f"/html/body/div[3]/div[2]/div[6]/div/div/div/div[{i}]/div/div[1]/a/@href")
                                .extract_first())
        # Follow product URLs and parse product details
        for product_url in product_urls:
            yield response.follow(product_url, callback=self.parse_product)

    def parse_product(self, response):
        # Extract desired attributes
        item = {
            "product_url": response.url,
            "product_name": response.xpath("/html/body/div[3]/div[2]/div/div/div[2]/h1/text()").get(),
            "product_barcode": response.xpath("/html/body/div[3]/div[5]/div[1]/div[2]/div[2]/div[1]/div[2]/div["
                                              "2]/text()").get(),
            "product_price": response.xpath("/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/span/span/p/text()").get(),
            "product_stock": None,  # unavailable
            "product_images": None,  # couldnt do it since it has different images for each slide
            "product_description": response.xpath("/html/body/div[3]/div[5]/div[1]/div[2]/div[2]/div[1]/span/text()").getall(),
            "product_skt": response.xpath("/html/body/div[3]/div[5]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/text()").get(),
            "product_category": response.xpath("/html/body/div[3]/div[1]/div/div/div[1]/ol/li[3]/a/span/text()").get(),
            "product_id": response.xpath("/html/body/div[3]/div[5]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/text()").get(), # ??
            "product_brand": response.xpath("/html/body/div[3]/div[1]/div/div/div[1]/ol/li[5]/a/span/text()").get()
        }
        yield item
        # Write data to JSON file
        with open('petlebi_products.json', 'a') as f:
            json.dump(item, f, ensure_ascii=False, indent=4)
            f.write("endjson")

