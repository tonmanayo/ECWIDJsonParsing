import csv
import json
from pprint import pprint

data = json.load(open('products.json'))
dataCategories = json.load(open('categories.json'))

shopifyCSV = open('shopify.csv', 'w')

headers = ['Handle', 'Title',
           'Body (HTML)',
           'Vendor',
           'Type',
           'Tags',
           'Published',
           'Option1 Name',
           'Option1 Value',
           'Option2 Name',
           'Option2 Value',
           'Option3 Name',
           'Option3 Value',
           'Variant SKU',
           'Variant Price',
           'Variant Inventory Qty',
           'Image Src',
           'Variant SKU',
           'Variant Grams',
           'Variant Inventory Tracker',
           'Variant Inventory Qty',
           'Variant Inventory Policy',
           'Variant Fulfillment Service',
           'Variant Price',
           'Variant Compare At Price',
           'Variant Requires Shipping',
           'Variant Taxable',
           'Variant Barcode',
           'Image Src',
           'Image Alt Text',
           'Gift Card'
           ]
writer = csv.DictWriter(shopifyCSV, fieldnames=headers)
writer.writeheader()
# pprint(data['items'])
for item in data['items']:
    # pprint("Name:" + item['name'])
    pName = item['name']
    if 'priceInProductList' in item:
        pPrice = item['priceInProductList']
    else:
        pPrice = 0
    if 'description' in item:
        pDescription = item['description']
    else:
        pDescription = ""
    pCategory = ""
    if 'categoryIds' in item:
        for ids in item['categoryIds']:
            for values in dataCategories['items']:
                if ids == values['id']:
                    if 'parentId' in values:
                        for parentID in dataCategories['items']:
                            if values['parentId'] == parentID['id']:
                                pCategory += parentID['name']
                    pCategory += ";" + values['name']
    if 'enabled' in item:
        pEnabled = item['enabled']
    else:
        pEnabled = 0
    if 'imageUrl' in item:
        pImageURL = item['imageUrl']
    else:
        pImageURL = ""
    if 'sku' in item:
        pSKU = item['sku']
    else:
        pSKU = '0'
    if 'quantity' in item:
        pQuantity = item['quantity']
    else:
        pQuantity = 0
    if len(item['combinations']) > 0:
        i = 0
        for combo in item['combinations']:
            if 'price' in combo:
                pPrice = combo['price']
            if 'quantity' in combo:
                pQuantity = combo['quantity']
            options1Name = ""
            options1Value = ""
            options2Name = ""
            options2Value = ""
            options3Name = ""
            options3Value = ""
            if len(combo['options']) > 0:
                if 'name' in combo['options'][0]:
                    options1Name = combo['options'][0]['name']
                    options1Value = combo['options'][0]['value']
            if len(combo['options']) > 1:
                if 'name' in combo['options'][1]:
                    options2Name = combo['options'][1]['name']
                    options2Value = combo['options'][1]['value']
            if len(combo['options']) > 2:
                if 'name' in combo['options'][2]:
                    options3Name = combo['options'][2]['name']
                    options3Value = combo['options'][2]['value']
            if i == 0:
                info = {'Handle': pName,
                        'Title': pName,
                        'Body (HTML)': pDescription,
                        'Vendor': '',
                        'Type': pCategory,
                        'Tags': "",
                        'Published': pEnabled,
                        'Option1 Name': options1Name,
                        'Option1 Value': options1Value,
                        'Option2 Name': options2Name,
                        'Option2 Value': options2Value,
                        'Option3 Name': options3Name,
                        'Option3 Value': options3Value,
                        'Variant SKU': pSKU,
                        'Variant Grams': "",
                        'Variant Inventory Tracker': "",
                        'Variant Inventory Qty': pQuantity,
                        'Variant Inventory Policy': 'deny',
                        'Variant Fulfillment Service': 'manual',
                        'Variant Price': pPrice,
                        'Variant Compare At Price': "",
                        'Variant Requires Shipping': "TRUE",
                        'Variant Taxable': 'TRUE',
                        'Variant Barcode': "",
                        'Image Src': pImageURL,
                        'Image Alt Text': "",
                        'Gift Card': "FALSE"}
            else:
                info = {'Handle': pName,
                        'Title': "",
                        'Body (HTML)': "",
                        'Vendor': "",
                        'Type': "",
                        'Tags': "",
                        'Published': pEnabled,
                        'Option1 Name': options1Name,
                        'Option1 Value': options1Value,
                        'Option2 Name': options2Name,
                        'Option2 Value': options2Value,
                        'Option3 Name': options3Name,
                        'Option3 Value': options3Value,
                        'Variant SKU': pSKU + "-" + str(i),
                        'Variant Grams': "",
                        'Variant Inventory Tracker': "",
                        'Variant Inventory Qty': pQuantity,
                        'Variant Inventory Policy': '',
                        'Variant Fulfillment Service': '',
                        'Variant Price': pPrice,
                        'Variant Compare At Price': "",
                        'Variant Requires Shipping': "",
                        'Variant Taxable': '',
                        'Variant Barcode': "",
                        'Image Src': pImageURL,
                        'Image Alt Text': "",
                        'Gift Card': ""}
            writer.writerow(info)
            i += 1

    else:
        info = {'Handle': pName,
                'Title': pName,
                'Body (HTML)': pDescription,
                'Vendor': "",
                'Type': pCategory,
                'Tags': "",
                'Published': pEnabled,
                'Option1 Name': "",
                'Option1 Value': "",
                'Option2 Name': "",
                'Option2 Value': "",
                'Option3 Name': "",
                'Option3 Value': "",
                'Variant SKU': pSKU,
                'Variant Grams': "",
                'Variant Inventory Tracker': "",
                'Variant Inventory Qty': pQuantity,
                'Variant Inventory Policy': 'deny',
                'Variant Fulfillment Service': 'manual',
                'Variant Price': pPrice,
                'Variant Compare At Price': "",
                'Variant Requires Shipping': "TRUE",
                'Variant Taxable': 'TRUE',
                'Variant Barcode': "",
                'Image Src': pImageURL,
                'Image Alt Text': "",
                'Gift Card': "FALSE"}
        pprint(info)
        writer.writerow(info)
