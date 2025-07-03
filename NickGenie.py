import random

# Step 1: Get User Input
name1 = input("Enter the first name: ").strip()
name2 = input("Enter the second name: ").strip()

# Step 2: Style Preference
style = input("Preferred nickname style (short/fun/formal): ").strip().lower()

# Step 3: Combine Parts of Names
base1 = name1[:3] + name2[-3:]
base2 = name2[:2] + name1[-2:]
base3 = name1[0] + name2
base4 = name2 + name1[::-1]
base5 = name1[:2] + name2[:2] + name1[-1]

# Step 4: Add Random Creative Elements
symbols = ['_', '.', '-', '24', '99', 'X', '', '007']
stylized = [base1, base2, base3, base4, base5]

creative_nicknames = []
for _ in range(8):  # Generate 8 nicknames
    base = random.choice(stylized)
    symbol = random.choice(symbols)
    nickname = base + symbol
    creative_nicknames.append(nickname)

# Step 5: Style Formatting
if style == "short":
    creative_nicknames = [nick[:6] for nick in creative_nicknames]
elif style == "formal":
    creative_nicknames = [name1.capitalize() + name2.capitalize()]

# Step 6: Display Nicknames
print("\n🧪 Generated Nicknames:")
for nick in creative_nicknames:
    print("-", nick)

# Step 7: Optional Save
save = input("\nDo you want to save the nicknames to a file? (y/n): ").strip().lower()
if save == 'y':
    with open("generated_nicknames.txt", "w") as file:
        for nick in creative_nicknames:
            file.write(nick + "\n")
    print("✅ Nicknames saved to 'generated_nicknames.txt'")

