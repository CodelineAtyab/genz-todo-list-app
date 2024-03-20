import json

CONTACT_STORE_FILE_PATH = "data/contact_store.txt"

# dict_of_contancts = {
#     "0096892011497": {"name": "Atyab", "address": "Al-Ansab"},
#     "0096812345678": {"name": "GenZ", "address": "Omantel HQ, Ghala"},
#     "0096852341233": {"name": "Codeline", "address": "Technopark, Ghala"},
# }

pno_1 = "0096892011497"
name_1 = "Atyab"
address_1 = "Al-Ansab"

pno_2 = "0096812345678"
name_2 = "GenZ"
address_2 = "Omantel HQ, Ghala"

pno_3 = "0096852341233"
name_3 = "Codeline"
address_3 = "Technopark, Ghala"


# with open(CONTACT_STORE_FILE_PATH, "a") as contacts_file:
#     contacts_file.write(json.dumps({"pno": pno_1, "name": name_1, "addr": address_1}) + "\n")
#     contacts_file.write(json.dumps({"pno": pno_2, "name": name_2, "addr": address_2}) + "\n")
#     contacts_file.write(json.dumps({"pno": pno_3, "name": name_3, "addr": address_3}) + "\n")

list_of_contacts = []

with open(CONTACT_STORE_FILE_PATH, "r") as contacts_file:
    list_of_contacts = [line.strip() for line in contacts_file.readlines()]

dict_of_contacts = {}
for record in list_of_contacts:
    curr_dict = json.loads(record)
    dict_of_contacts[curr_dict["pno"]] = {"name": curr_dict["name"], "address": curr_dict["addr"]}

print(dict_of_contacts)
print(dict_of_contacts["0096892011497"])
# dumped_str = json.dumps([dict_of_contancts])
# my_dict = json.loads(dumped_str)
#
# print(dumped_str)
# print(my_dict)

# with open(CONTACT_STORE_FILE_PATH, "w") as contacts_file:
#     json.dump(obj=dict_of_contancts, fp=contacts_file, indent=2)
#
#
# dict_of_contancts = {}
#
# with open(CONTACT_STORE_FILE_PATH, "r") as contacts_file:
#     dict_of_contancts = json.load(fp=contacts_file)


# print(dict_of_contancts)
# print(dict_of_contancts["0096892011497"]["name"])

