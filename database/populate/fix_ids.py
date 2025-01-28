import json
from termcolor import colored as c

def fix_ids(content):
    authors = content["authors"]
    books = content["books"]
    
    old_to_new_id_map = {}
    new_id = 1
    
    for author in authors:
        old_to_new_id_map[author["id"]] = new_id
        author["id"] = new_id
        new_id += 1
    
    for book in books:
        book["author_id"] = old_to_new_id_map.get(book["author_id"], book["author_id"])
    
    return content

with open("database/populate/data.json", 'r') as file:
    content = json.load(file)

content = fix_ids(content)

with open("database/populate/data.json", 'w') as file:
    json.dump(content, file, indent=4)

print(c("IDs fixed for both authors and books. Data successfully updated.", 'green'))



# cd test_graphql
# source venv/bin/activate
# python3 -m database.populate.fix_ids