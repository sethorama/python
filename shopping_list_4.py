shopping_list = []


def remove_item(idx):
	index = idx - 1
	item = shopping_list.pop(index)
	print("Removed {}.".format(item))

def show_help():
	print("\nSeparate each item with a comma.")
	print("Type DONE to quit, SHOW to see the current list, "
				"REMOVE to remove an item, and HELP to get this message")


def show_list():
	count = 1
	for item in shopping_list:
		print("{}: {}".format(count, item))
		count += 1

print("Give me a list of things you want to shop for.")
show_help()

while True:
	new_stuff = input("> ")

	if new_stuff == "DONE":
		print("\nHere's your list:")
		show_list()
		break
	elif new_stuff == "HELP":
		show_help()
		continue
	elif new_stuff == "SHOW":
		show_list()
		continue
	elif new_stuff == "REMOVE":
		show_list()
		idx = input("Which item? Tell me the number. ")
		remove_item(int(idx))
		continue
	else:
		new_list = new_stuff.split(",")
		index = input("Add this at a certain spot? Press enter for the end of the list, "
									"or give me a number. Currently {} items in the list.".format(
										len(shopping_list)))
		if index:
			spot = int(index) - 1
			for item in new_list:
				shopping_list.insert(spot, item.strip())
		else:
			for item in new_list:
				shopping_list.append(item.strip())