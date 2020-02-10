import os
import re

dir = os.path.dirname(os.path.abspath(__file__))
file = open(f"{dir}/test.yml", "r")
new_file = open(f'{dir}/new_test.yml', "w+")
for line in file:
    search_result = re.search("{.*}", line)
    new_line = ""
    if (search_result):
        json = search_result.string[search_result.start():search_result.end()]
        updated_json = ""
        for char in json:
            new_char = ""
            if (char == '"'):
                new_char = '\\"'
            else:
                new_char = char
            updated_json = f'{updated_json}{new_char}'
        json_start = line.find('"')
        new_line = line[:json_start+1] + updated_json + '"'
    else:
        new_line = line

    new_file.write(new_line)
new_file.close()
file.close()
        
