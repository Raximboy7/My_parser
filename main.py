from  base_parser import BaseParser

class UPGParser(BaseParser):
    def __init__(self, category):
        super().__init__(category)

    def get_data(self):
        data = []
        soup = self.get_soup()
        box = soup.find('div', class_='row-viewed col-catalog-grid product-grid')
        products = box.find_all('div', class_="col-lg-12 col-md-15 col-sm-20 col-xs-30 item-product")
        for item in products:
            title = item.find('a', class_='item-link').get_text(strip=True)
            link = item.find('a', class_='item-link')['href']
            image = 'https://upg.uz' + item.find('a',class_='item-link').find('img', class_='item-product-img center-block')['src']
            price = item.find('span', class_='item-price price-new').get_text().replace(' ','').replace('сум','')
            price = int(price)
            data.append({
                'title': title,
                'link': link,
                'image': image,
                'price': price
            })

        return data


notebook = UPGParser('kategory-mouses')
notebook.save_json(notebook.get_data(), 'mouses')