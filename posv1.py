def decode_barcodes(tags):
    pass


def load_all_items():
    return [
        {"id": "0001", "name": "Coca Cola", "price": 3},
        {"id": "0002", "name": "Diet Coke", "price": 4},
        {"id": "0003", "name": "Pepsi-Cola", "price": 5},
        {"id": "0004", "name": "Mountain Dew", "price": 6},
        {"id": "0005", "name": "Dr Pepper", "price": 7},
        {"id": "0006", "name": "Sprite", "price": 8},
        {"id": "0007", "name": "Diet Pepsi", "price": 9},
        {"id": "0008", "name": "Diet Mountain Dew", "price": 10},
        {"id": "0009", "name": "Diet Dr Pepper", "price": 11},
        {"id": "0010", "name": "Fanta", "price": 12}
    ]


def select_from_all_item_by_id(id):
    all_items = load_all_items()
    for item in all_items:
        if id == item['id']:
            item['count'] = 1
            return item


def select_item_by_barcode(barcode, combined_items):
    for item in combined_items:
        if item['id'] == barcode:
            return item
    return None


def combine_items(barcodes):
    combined_items = []
    for barcode in barcodes:
        item = select_from_all_item_by_id(barcode)
        current_item = select_item_by_barcode(barcode, combined_items)
        if current_item:
            current_item['count'] += 1
        else:
            combined_items.append(item)
    return combined_items


def decode_tags(tags):
    barcodes = decode_barcodes(tags)
    items = combine_items(barcodes)
    return items


def calculate_receipt(items):
    pass


def render_receipt(receipt):
    pass


def print_receipt(tags):
    items = decode_tags(tags)
    receipt = calculate_receipt(items)
    rendered_receipt = render_receipt(receipt)


tags = ['0001', '0003', '0005', '0003']
# print_receipt(tags)

items = combine_items(tags)
print(items)
