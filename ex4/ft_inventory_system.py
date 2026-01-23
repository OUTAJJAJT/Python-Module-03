#!/usr/bin/env python3

inventory = {
      "alice": {
         "items": {
            "pixel_sword": 1,
            "code_bow": 1,
            "health_byte": 1,
            "quantum_ring": 3
         },
         "total_value": 1875,
         "item_count": 6
      },
      "bob": {
         "items": {
            "code_bow": 3,
            "pixel_sword": 2
         },
         "total_value": 900,
         "item_count": 5
      },
      "charlie": {
         "items": {
            "pixel_sword": 1,
            "code_bow": 1
         },
         "total_value": 350,
         "item_count": 2
      },
   }


def System_analysis():
    total_inventory = 0
    for value in inventory.values():
        total_inventory += value.get("item_count")
    print("=== Inventory System Analysis ===")
    print("total items in inventory: ", total_inventory)

    print("unique items type: ", len(inventory))
    print()
    return total_inventory


def Current_inventory(total_inventory):
    print("=== Current Inventory ===")
    for name, value in inventory.items():
        qty = value.get("item_count")
        percentage = (qty * 100) / total_inventory
        str_percent = str(percentage)
        print(name, ": ", qty, " units (", str_percent[:4], "%)", sep="")
    print()


def Statistics():
    most_item = None
    least_item = None

    for name, value in inventory.items():
        qty = value.get("item_count")
        if most_item is None or qty > inventory.get(most_item).get("\
item_count"):
            most_item = name
        if least_item is None or qty < inventory.get(least_item).get("\
item_count"):
            least_item = name
    print("=== Inventory Statistics ===")
    print("Most abundant:", most_item,
          "(" + str(inventory.get(most_item).get("item_count")) + " units)")
    print("Least abundant:", least_item,
          "(" + str(inventory.get(least_item).get("item_count")) + " units)")
    print()


def Categories():
    categories = {
        "Moderate": {},
        "Scarce": {}
    }
    for name, value in inventory.items():
        qty = value.get("item_count")
        if qty >= 5:
            categories.get("Moderate").update({name: qty})
        else:
            categories.get("Scarce").update({name: qty})
    print("=== Item Categories ===")
    print("Moderate:", categories.get("Moderate"))
    print("Scarce:", categories.get("Scarce"))
    print()


def management():
    restock = dict()

    for name, value in inventory.items():
        qty = value.get("item_count")
        if qty <= 1:
            restock.update({name: qty})

    print("=== Management Suggestions ===")
    print("Restock needed:", list(restock.keys()))
    print()


def Properties_demo():
    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys:", list(inventory.keys()))
    values = []
    for name, value in inventory.items():
        qty = value.get("item_count")
        values.append(qty)

    print("Dictionary values:", values)
    print("Sample lookup - 'sword' in inventory:",
          inventory.get("sword") is not None)


if __name__ == "__main__":
    total = System_analysis()
    Current_inventory(total)
    Statistics()
    Categories()
    management()
    Properties_demo()
