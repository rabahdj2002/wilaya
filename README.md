# Your Package Name

A brief description of what your package does.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install your_package_name.

## Usage
Here's how you can use this class to search for Wilayas and Communes:

```python
# Create an instance of the handler class
handler_instance = handler()

# Search for a Wilaya by its code
wilaya_info_by_code = handler_instance.searchByCode(16)  # Example code
print(wilaya_info_by_code)

# Search for a Wilaya by its name
wilaya_info_by_name = handler_instance.searchByName("Alger")
print(wilaya_info_by_name)

# Get all Baladiyat for a given Wilaya code
baladiyat_list = handler_instance.getBaladiyat(16)  # Example code
print(baladiyat_list)
```

# Search for a Baladiya by its name
baladiya_info_by_name = handler_instance.searchBaladiya("Sidi M'Hamed")
print(baladiya_info_by_name)
Ensure the JSON files Wilaya_Of_Algeria.json and Commune_Of_Algeria.json are in the correct directory (wilaya/) relative to where you run your script. This will allow the handler class to correctly access and process the data.
