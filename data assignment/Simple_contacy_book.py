contact_book = {
    "Tanuj": "8077121062",
    "Vipin": "8126159379",
    "Raj": "9997032040"
}

print("---My Contact Book---")
print(contact_book)
print("-" * 30)

search_name = input("Enter The Name: ")

if search_name in contact_book:
    print(f"Contact Found! {search_name}'s number is: {contact_book[search_name]} ")
else:
    print("Contact Not Found")
    
print("-" * 30)