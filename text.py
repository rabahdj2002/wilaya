# Import the handler class from the module
from wilaya import handler

# Create an instance of the handler class
handler_instance = handler()

# Search for a Wilaya by its code
wilaya_info_by_code = handler_instance.searchByCode(16)
print(wilaya_info_by_code)

# Search for a Wilaya by its name
wilaya_info_by_name = handler_instance.searchByName("Alger")
print(wilaya_info_by_name)

# Get all Baladiyat for a given Wilaya code
baladiyat_list = handler_instance.getBaladiyat(16)
print(baladiyat_list)

# Search for a Baladiya by its name
baladiya_info_by_name = handler_instance.searchBaladiya("Ouled Fayet")
print(baladiya_info_by_name)