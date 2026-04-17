# Fatie a string "It was a bright cold day in April, and the clocks were
# striking thirteen." para que só inclua os caracteres existentes antes da vírgula.

whole = "It was a bright cold day in April, and the clocks were striking thirteen."
finalIndex = whole.index(",")
slice = whole[:finalIndex]

print(slice)
