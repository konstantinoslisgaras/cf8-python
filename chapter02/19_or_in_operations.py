choice = "q"

# 1
if choice == "q" or choice == "Q":
    print("Exiting...")
else:
    print("Continue...")

# 2
if choice.lower() == "q":
    print("Exiting...")
else:
    print("Continue...")

# 3
if choice in ("Q", "q", "quit", "Quit"):
    print("Exiting...")
else:
    print("Continue...")