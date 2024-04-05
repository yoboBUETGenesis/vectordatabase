import json
import os

# Function to read JSON files
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to write JSON data to a file
def write_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


# Function to extract category from file name
def extract_category(file_name):
    return file_name.replace('.json', '').replace('_', ' ').lower()


def extract_category2(file_name):
    return file_name.replace('Allen_Solly_', '').replace('.json', '').replace('_', ' ').lower()

def extract_category3(file_name):
    return file_name.replace('Apex_', '').replace('.json', '').replace('_', ' ').lower()
def extract_category4(file_name):
    return file_name.replace('Bata_', '').replace('.json', '').replace('_', ' ').lower()

# List to store combined JSON data
combined_data = []

product_cnt = 0



# Aarong men
json_dir = './men'
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        # Read JSON file
        json_data = read_json_file(file_path)
        # Extract category from file name
        category = extract_category(filename)
        # Take the first 57 elements from the array
        for item in json_data:
            # Add Gender and Category fields
            specifications_list = []
            for key, value in item['Specifications'].items():
                specification_str = f"{key} is {value}"
                specifications_list.append(specification_str)

            str = item['Image_link'].split("?")[0]
            
            item.pop('Image_link', None)
            item['product_id'] = product_cnt 
            item['Image_links'] = [str]  
            item['Specifications'] = ". ".join(specifications_list)
            item['Gender'] = 'Man'
            item['Category'] = category
            item['Company'] = 'Aarong'
            combined_data.append(item)
            product_cnt = product_cnt + 1






# Aarong women
json_dir = './women'
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        # Read JSON file
        json_data = read_json_file(file_path)
        # Extract category from file name
        category = extract_category(filename)
        # Take the first 57 elements from the array
        for item in json_data:
            # Add Gender and Category fields
            specifications_list = []
            for key, value in item['Specifications'].items():
                specification_str = f"{key} is {value}"
                specifications_list.append(specification_str)
            
            str = item['Image_link'].split("?")[0]
            
            item.pop('Image_link', None)
            item['product_id'] = product_cnt 
            item['Image_links'] = [str] 
            item['Specifications'] = ". ".join(specifications_list)
            item['Gender'] = 'Woman'
            item['Category'] = category
            item['Company'] = 'Aarong'
            combined_data.append(item)
            product_cnt = product_cnt + 1



# Aarong Kid Boy
json_dir = './aboy'
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        # Read JSON file
        json_data = read_json_file(file_path)
        # Extract category from file name
        category = extract_category(filename)
        # Take the first 57 elements from the array
        for item in json_data:
            # Add Gender and Category fields
            specifications_list = []
            for key, value in item['Specifications'].items():
                specification_str = f"{key} is {value}"
                specifications_list.append(specification_str)
            
            str = item['Image_link'].split("?")[0]
            
            item.pop('Image_link', None)
            item['product_id'] = product_cnt 
            item['Image_links'] = [str] 
            item['Specifications'] = ". ".join(specifications_list)
            item['Gender'] = 'Boy'
            item['Category'] = category
            item['Company'] = 'Aarong'
            combined_data.append(item)
            product_cnt = product_cnt + 1


# Aarong Kid Girl
json_dir = './agirl'
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        # Read JSON file
        json_data = read_json_file(file_path)
        # Extract category from file name
        category = extract_category(filename)
        # Take the first 57 elements from the array
        for item in json_data:
            # Add Gender and Category fields
            specifications_list = []
            for key, value in item['Specifications'].items():
                specification_str = f"{key} is {value}"
                specifications_list.append(specification_str)
            
            str = item['Image_link'].split("?")[0]
            
            item.pop('Image_link', None)
            item['product_id'] = product_cnt 
            item['Image_links'] = [str] 
            item['Specifications'] = ". ".join(specifications_list)
            item['Gender'] = 'Girl'
            item['Category'] = category
            item['Company'] = 'Aarong'
            combined_data.append(item)
            product_cnt = product_cnt + 1

# Allen solly men
json_dir = './allenmen'
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        # Read JSON file
        json_data = read_json_file(file_path)
        # Extract category from file name
        category = extract_category2(filename)
        # Take the first 57 elements from the array
        for item in json_data:
            # Add Gender and Category fields
            specifications_list = []
            for key, value in item['Specifications'].items():
                if isinstance(value, list):
                    value_str = ', '.join([item.replace('.', '') for item in value])
                    specification_str = f"{key} are {value_str}"
                else:
                    specification_str = f"{key} is {value}"
                specifications_list.append(specification_str)
            
            item['product_id'] = product_cnt  
            item['Specifications'] = ". ".join(specifications_list)
            item['Gender'] = 'Man'
            item['Category'] = category
            combined_data.append(item)
            product_cnt = product_cnt + 1


#Allen Solly Women
json_dir = './allenwomen'
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        # Read JSON file
        json_data = read_json_file(file_path)
        # Extract category from file name
        category = extract_category2(filename)
        # Take the first 57 elements from the array
        for item in json_data:
            # Add Gender and Category fields
            specifications_list = []
            for key, value in item['Specifications'].items():
                if isinstance(value, list):
                    value_str = ', '.join([item.replace('.', '') for item in value])
                    specification_str = f"{key} are {value_str}"
                else:
                    specification_str = f"{key} is {value}"
                specifications_list.append(specification_str) 
            
            item['product_id'] = product_cnt  
            item['Specifications'] = ". ".join(specifications_list)
            item['Gender'] = 'Woman'
            item['Category'] = category
            combined_data.append(item)
            product_cnt = product_cnt + 1    


#Allen Solly Boys
json_dir = './allenboy'
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        # Read JSON file
        json_data = read_json_file(file_path)
        # Extract category from file name
        category = extract_category2(filename)
        # Take the first 57 elements from the array
        for item in json_data:
            # Add Gender and Category fields
            specifications_list = []
            for key, value in item['Specifications'].items():
                if isinstance(value, list):
                    value_str = ', '.join([item.replace('.', '') for item in value])
                    specification_str = f"{key} are {value_str}"
                else:
                    specification_str = f"{key} is {value}"
                specifications_list.append(specification_str) 
            
            item['product_id'] = product_cnt  
            item['Specifications'] = ". ".join(specifications_list)
            item['Gender'] = 'Boy'
            item['Category'] = category
            combined_data.append(item)
            product_cnt = product_cnt + 1      

#Allen Solly Girls
json_dir = './allengirl'
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        # Read JSON file
        json_data = read_json_file(file_path)
        # Extract category from file name
        category = extract_category2(filename)
        # Take the first 57 elements from the array
        for item in json_data:
            # Add Gender and Category fields
            specifications_list = []
            for key, value in item['Specifications'].items():
                if isinstance(value, list):
                    value_str = ', '.join([item.replace('.', '') for item in value])
                    specification_str = f"{key} are {value_str}"
                else:
                    specification_str = f"{key} is {value}"
                specifications_list.append(specification_str) 
            
            item['product_id'] = product_cnt  
            item['Specifications'] = ". ".join(specifications_list)
            item['Gender'] = 'Girl'
            item['Category'] = category
            combined_data.append(item)
            product_cnt = product_cnt + 1    


#Apex Shoe Man
json_dir = './shoes/apex/men'
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        # Read JSON file
        json_data = read_json_file(file_path)
        # Extract category from file name
        category = extract_category3(filename)
        # Take the first 57 elements from the array
        for item in json_data:
            # Add Gender and Category fields
            specifications_list = []
            for key, value in item['Specifications'].items():
                if isinstance(value, list):
                    value_str = ', '.join([item.replace('.', '') for item in value])
                    specification_str = f"{key} are {value_str}"
                else:
                    specification_str = f"{key} is {value}"
                specifications_list.append(specification_str)
            
            item['product_id'] = product_cnt  
            item['Specifications'] = ". ".join(specifications_list)
            item['Gender'] = 'Man'
            item['Category'] = category
            combined_data.append(item)
            product_cnt = product_cnt + 1  

#Apex Shoe Woman
json_dir = './shoes/apex/women'
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        # Read JSON file
        json_data = read_json_file(file_path)
        # Extract category from file name
        category = extract_category3(filename)
        # Take the first 57 elements from the array
        for item in json_data:
            # Add Gender and Category fields
            specifications_list = []
            for key, value in item['Specifications'].items():
                if isinstance(value, list):
                    value_str = ', '.join([item.replace('.', '') for item in value])
                    specification_str = f"{key} are {value_str}"
                else:
                    specification_str = f"{key} is {value}"
                specifications_list.append(specification_str)
            
            item['product_id'] = product_cnt  
            item['Specifications'] = ". ".join(specifications_list)
            item['Gender'] = 'Woman'
            item['Category'] = category
            combined_data.append(item)
            product_cnt = product_cnt + 1 

#Bata Shoe Man
json_dir = './shoes/bata/men'
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        # Read JSON file
        json_data = read_json_file(file_path)
        # Extract category from file name
        category = extract_category4(filename)
        # Take the first 57 elements from the array
        for item in json_data:
            # Add Gender and Category fields
            specifications_list = []
            for key, value in item['Specifications'].items():
                if isinstance(value, list):
                    value_str = ', '.join([item.replace('.', '') for item in value])
                    specification_str = f"{key} are {value_str}"
                else:
                    specification_str = f"{key} is {value}"
                specifications_list.append(specification_str)
            
            item['product_id'] = product_cnt  
            item['Specifications'] = ". ".join(specifications_list)
            item['Gender'] = 'Man'
            item['Category'] = category
            combined_data.append(item)
            product_cnt = product_cnt + 1 


#Infinity all
json_dir = './infa'
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        # Read JSON file
        json_data = read_json_file(file_path)
        # Extract category from file name
       
        # Take the first 57 elements from the array
        for item in json_data:   
            str = item['Image_link'].split("?")[0]
            item.pop('Image_link', None)
            item['Image_links'] = [str]      
            item['product_id'] = product_cnt  
            combined_data.append(item)
            product_cnt = product_cnt + 1 

# Write combined data to a new JSON file
write_json_file(combined_data, 'dataset.json')
