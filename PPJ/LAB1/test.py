pom = "1rez"
line = 42
out = []  # List to store valid outputs
error = []  # List to store errors

if pom[0].isalpha():
    text = "IDN {} {}".format(line, pom)
    out.append(text)
    pom = ""
elif pom.isnumeric():
    text = "BROJ {} {}".format(line, pom)
    out.append(text)
    pom = ""
else:
    print("ERROR")
    text = "ERROR {} {}".format(line, pom)
    error.append(text)
    pom = ""

print("out:", out)
print("error:", error)