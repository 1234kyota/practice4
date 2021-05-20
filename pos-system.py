import csv
import datetime

now = datetime.datetime.now()
filename = "./" + now.strftime('%Y%m%d') + '.txt'

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_master=item_master
        self.sum_price = 0
    
    def add_item_order(self,item_code,count):
        for _ in range(count):
            self.item_order_list.append(item_code)

    def view_item_list(self):
        with open(filename, mode='a') as f:
            for item in self.item_master:
                item_code = item.item_code

            
                if item_code in self.item_order_list:
                    count = self.item_order_list.count(item_code)
                    self.sum_price += item.price * count
                    f.write(f'商品名:{item.item_name},値段:{item.price},個数：{count}\n')

                
        
            
    def total_price(self):
        with open(filename, mode='a') as f:
            f.write(f'合計:{self.sum_price}円')

    def exchange(self):
        pay = input("支払い金額を入力してください")
        exchange = int(pay) - self.sum_price
        with open(filename, mode='a') as f:
            f.write(f'支払い金額は{pay}なので、お釣りは{exchange}円です')              

    
### メイン処理
def main():
    # マスタ登録
    item_master=[]
    # item_master.append(Item("001","りんご",100))
    # item_master.append(Item("002","なし",120))
    # item_master.append(Item("003","みかん",150))
    with open('./item.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            item_master.append(Item(row[0],row[1],int(row[2])))

    
    
    # オーダー登録
    order=Order(item_master)

    while True:
        order_input = input("オーダーを入力してください。中断する場合は0を入力してください")
        if order_input == "0":
            break
        count = int(input("いくつですか？"))
        order.add_item_order(order_input,count)
        
        
    
    
    # オーダー表示
    order.view_item_list()
    order.total_price()
    order.exchange()

    
if __name__ == "__main__":
    main()