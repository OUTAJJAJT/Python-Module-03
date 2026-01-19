#!/usr/bin/env python3

inventory = {
    "sword": {
        "type": "weapon",
        "quantity": 1,
        "value": 300
    },
    "potion": {
        "type": "consumable",
        "quantity": 5,
        "value": 20
    },
    "helmet": {
        "type": "armor",
        "quantity": 1,
        "value": 200
    },
    "shield": {
        "type": "armor",
        "quantity": 2,
        "value": 150
    },
    "armor": {
        "type": "armor",
        "quantity": 3,
        "value": 500
    }
}


def System_analysis():
    total_inventory = 0
    for value in inventory.values():
        total_inventory += value.get("quantity")
    print("=== Inventory System Analysis ===")
    print("total items in inventory: ", total_inventory)

    print("unique items type: ", len(inventory))
    print()
    return total_inventory


def Current_inventory(total_inventory):
    print("=== Current Inventory ===")
    for name, value in inventory.items():
        qty = value.get("quantity")
        percentage = (qty * 100) / total_inventory
        str_percent = str(percentage)
        print(name, ": ", qty, " units (", str_percent[:4], "%)", sep="")
    print()


def Statistics():
    most_item = None
    least_item = None

    for name, value in inventory.items():
        qty = value.get("quantity")
        if most_item is None or qty > inventory.get(most_item).get("quantity"):
            most_item = name
        if least_item is None or qty < inventory.get(least_item).get("quantity"
                                                                     ):
            least_item = name
    print("=== Inventory Statistics ===")
    print("Most abundant:", most_item,
          "(" + str(inventory.get(most_item).get("quantity")) + " units)")
    print("Least abundant:", least_item,
          "(" + str(inventory.get(least_item).get("quantity")) + " units)")
    print()


def Categories():
    categories = {
        "Moderate": {},
        "Scarce": {}
    }
    for name, value in inventory.items():
        qty = value.get("quantity")
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
        qty = value.get("quantity")
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
        qty = value.get("quantity")
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
