
expenses = [] # Mảng chi tiêu
# 1 phần có dạng:
# item = {'name': name_input, 'cost':cost_input, 'date':date_input}

def find_item_by_name(arr, item_name):
    """Trả về vị trí đầu tiên tìm thấy trong mảng"""
    for item_index in range(0, len(arr)):
        if arr[item_index]["name"] == item_name:
            return item_index
        
    return -1# Tìm ko thấy

while True:    
    print("What do you want to do?\n"\
            "1. Add\n" \
            "2. Remove")
    option = int(input("Select option 1 or 2: "))
    
    if option == 1:
        name_input = input("Input item name:")
        cost_input = int(input("Item cost: "))
        date_input = input("Date: ")
        item = {
            'name': name_input,
            'cost': cost_input,
            'date': date_input
        }
        expenses.append(item)
        print(expenses)
    elif option == 2:
        name_input = input("Input item name:")
        index_find = find_item_by_name(expenses, name_input)
        if index_find > -1:
            del expenses[index_find]
        print(expenses)
    else:
        print('Invalid choice. Good bye!')