# File ko read mode mein open karna
f = open("demo.txt", "r")

data = f.read()
print("File Content:", data)
print("Data Type:", type(data))

# Pehle read() chalane ki wajah se cursor end par chala jata hai,
# isliye readline() yahan empty string return karega.
line1 = f.readline()
print("First Line:", line1)

f.close()








# Existing file mein data add karna
f = open("demo.txt", "a")
f.write(" hello i am new here what are you doing guys are you ready to learn")
f.close()

word = "shazia"

# 1. File se data read karna
with open("sample.txt", "r") as f:
    data = f.read()

# 2. Word search karna
if data.find(word) != -1:
    print(f"'{word}' found in file!")
else:
    print(f"'{word}' not found in file.")

# 3. Text replace karna
new_data = data.replace("shazia", "kaneez")
print("Updated Data:\n", new_data)

# 4. Overwrite karke naya data save karna
with open("sample.txt", "w") as f:
    f.write(new_data)



    count = 0

with open("sample.txt", "r") as f:
    data = f.read()
    print("Raw Data:", data)

    # Comma ke basis par list banana
    nums = data.split(",")
    print("Numbers List:", nums)

    # Even numbers count karna
    for val in nums:
        val = val.strip()  # Extra spaces remove karne ke liye
        if val.isdigit() and int(val) % 2 == 0:
            count += 1

print("Total Even Numbers:", count)


