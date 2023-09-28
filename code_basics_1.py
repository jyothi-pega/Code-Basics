# Import libraries

print("Hello World!")
frist_name = "jyothi"
age = 32
married = True
address_list = ["42 archer street", "MK404SG", "bedford"]
address_dictionary = {"street_name":"42 archer street", "postcode": "MK404SG","town": "bedford"}
print(type(married))
print(address_list[2])
print(address_dictionary["postcode"])
print(address_dictionary.values())

for val in address_list:
    print("val:",val)
val = None

if val == "42 archer street":
    print("Street name")
elif val == "bedford":
    print("town")
else:
    print(None)

while frist_name == "jyothi":
    print(f"{frist_name}")

