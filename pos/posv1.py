from pos.Receipt import Receipt
from pos.ReceiptItem import ReceiptItem


def decode_barcodes(tags):
    print(tags)
    barcodes = []
    for tag in tags:
        if '-' in tag:
            segments = tag.split('-')
            count = int(segments[1])
            for i in range(count):
                barcodes.append(segments[0])
        else:
            barcodes.append(tag)

    print(barcodes)
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
                'ITEM000001',
                'ITEM000003'
                'ITEM000005'
            ]
        }
    ]


def select_from_all_item_by_id(barcode):
    all_items = load_all_items()
    item = next(filter(lambda it: it['id'] == barcode, all_items), None)
    if item:
        return ReceiptItem(item['id'], item['name'], item['price'])
    return None


def select_item_by_barcode(barcode, combined_items):
    for item in combined_items:
        if item.barcode == barcode:
            return item
    return None


def combine_items(barcodes):
    print(barcodes)
    combined_items = []
    for barcode in barcodes:
        item = select_from_all_item_by_id(barcode)
        current_item = select_item_by_barcode(barcode, combined_items)
        if current_item:
            current_item.count += 1
        else:
            combined_items.append(item)
    print(combine_items)
    return combined_items


def decode_tags(tags):
    print(tags)
    barcodes = decode_barcodes(tags)
    combined_items = combine_items(barcodes)
    print(combined_items)
    return combined_items


def promote_receipt_items(items, all_promotions):
    print(items)
    print(all_promotions)

    for promotion in all_promotions:
        if promotion['type'] == 'BUY_TWO_GET_ONE_FREE':
            for item in items:
                if item.barcode in promotion['barcodes']:
                    if item.count > 1:
                        item.total = item.price * item.count/2
    print(items)
    return items


def calculate_receipt_items(items):
    print(items)
    for item in items:
        count = item.count
        price = item.price
        item.total = price * count
    all_promotions = load_all_promotions()
    promoted_items = promote_receipt_items(items, all_promotions)
    print(promoted_items)
    return promoted_items


def calculate_receipt_total(items):
    print(items)
    total = 0
    for item in items:
        total += item.total
    print(total)
    return total


def calculate_receipt_saving(receipt_items):
    print(receipt_items)
    total = 0
    promoted_total = 0
    for item in receipt_items:
        total += item.count * item.price
        promoted_total += item.total
    saving = total - promoted_total
    print(saving)
    return saving


def calculate_receipt(items):
    print(items)
    receipt_items = calculate_receipt_items(items)
    total = calculate_receipt_total(receipt_items)
    saving = calculate_receipt_saving(receipt_items)
    receipt = Receipt(items, total, saving)
    print(receipt)
    return receipt


def render_header():
    return "***<没钱赚商店>收据***"


def render_items(receipt_items):
    receipt = ''
    for item in receipt_items:
        item_str = "名称：%s，数量：%s瓶，单价：%s(元)，小计：%s(元) \n" % (item.name, item.count, item.price, item.total)
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
    print(receipt)
    header = render_header()
    item_str = render_items(receipt.items)
    total_str = render_total(receipt.total)
    saving_str = render_saving(receipt.saving)
    footer = render_footer()
    rendered_receipt = '\n'.join([header, item_str, total_str, saving_str, footer])
    print(rendered_receipt)
    return rendered_receipt


def print_receipt(tags):
    decoded_items = decode_tags(tags)
    receipt = calculate_receipt(decoded_items)
    return render_receipt(receipt)


if __name__ == '__main__':
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
    result = print_receipt(current_tags)
    print(result)
