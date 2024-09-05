from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon names", ["pikachu", "charmandor", "niggamen", "watastachi"])
table.add_column("Type", ["lightning", "fire", "slavery", "semen"])
table.align = "l"
print(table)
