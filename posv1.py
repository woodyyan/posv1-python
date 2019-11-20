def decode_barcodes(tags):
    barcodes = []
    for tag in tags:
        if '-' in tag:
            segments = tag.split('-')
            count = int(segments[1])
            for i in range(count):
                barcodes.append(segments[0])
        else:
            barcodes.append(tag)

    return barcodes


def load_all_items():
    return [
        {"id": "ITEM000001", "name": "Coca Cola", "price": 3},
        {"id": "ITEM000002", "name": "Diet Coke", "price": 4},
        {"id": "ITEM000003", "name": "Pepsi-Cola", "price": 5},
        {"id": "ITEM000004", "name": "Mountain Dew", "price": 6},
        {"id": "ITEM000005", "name": "Dr Pepper", "price": 7},
        {"id": "ITEM000006", "name": "Sprite", "price": 8},
        {"id": "ITEM000007", "name": "Diet Pepsi", "price": 9},
        {"id": "ITEM000008", "name": "Diet Mountain Dew", "price": 10},
        {"id": "ITEM000009", "name": "Diet Dr Pepper", "price": 11},
        {"id": "ITEM0000010", "name": "Fanta", "price": 12}
    ]


def load_all_promotions():
    return [
        {
            'type': 'BUY_TWO_GET_ONE_FREE',
            'barcodes': [
                'ITEM000000',
                'ITEM000001'
            ]
        },
        {
            'type': 'OTHER_PROMOTION',
            'barcodes': [
                'ITEM000003',
                'ITEM000004'
            ]
        }
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
    combined_items = combine_items(barcodes)
    return combined_items


def promote_receipt_items(items, all_promotions):
    return items


def calculate_receipt_items(items):
    for item in items:
        count = item['count']
        price = item['price']
        item['total'] = price * count
    return items
    # all_promotions = load_all_promotions()
    # return promote_receipt_items(items, all_promotions)


def calculate_receipt_total(items):
    total = 0
    for item in items:
        total += item['total']
    return total


def calculate_receipt_saving(receipt_items):
    return 0


def calculate_receipt(items):
    receipt = {}
    receipt_items = calculate_receipt_items(items)
    total = calculate_receipt_total(receipt_items)
    saving = calculate_receipt_saving(receipt_items)
    receipt['items'] = receipt_items
    receipt['total'] = total
    receipt['saving'] = saving
    return receipt


def render_header():
    return "***<没钱赚商店>收据***"


def render_items(receipt_items):
    receipt = ''
    for item in receipt_items:
        item_str = "名称：%s，数量：%s瓶，单价：%s(元)，小计：%s(元) \n" % (item['name'], item['count'], item['price'], item['total'])
        receipt += item_str
    receipt += "----------------------"
    return receipt


def render_total(total):
    return "总计：%s(元)" % total


def render_saving(saving):
    return "节省：%s(元)" % saving


def render_footer():
    return "**********************"


def render_receipt(receipt):
    header = render_header()
    item_str = render_items(receipt['items'])
    total_str = render_total(receipt['total'])
    saving_str = render_saving(receipt['saving'])
    footer = render_footer()
    return '\n'.join([header, item_str, total_str, saving_str, footer])


def print_receipt(tags):
    decoded_items = decode_tags(tags)
    receipt = calculate_receipt(decoded_items)
    return render_receipt(receipt)


class Receipt:
    items = []
    total = 0
    saving = 0


class Employee:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id


r = Receipt()
r.name = 'a'
r.age = 10

current_tags = [
    'ITEM000001',
    'ITEM000001',
    'ITEM000001',
    'ITEM000001',
    'ITEM000001',
    'ITEM000003-2',
    'ITEM000005',
    'ITEM000005',
    'ITEM000005'
]
# result = print_receipt(current_tags)
print(r.name)
print(r.age)
