import modules.extract_colors as e
import modules.replace_text as r
import os
import linecache
import subprocess

output_filename = "color_palette.css"
user_directory = os.path.expanduser('~') + '/'

def restart_waybar():
    subprocess.call("./.scripts/restart_waybar.sh", shell=True)

# read dcol file of current wallpaper
color_codes_dict = e.get_color_codes_dict_rgba()

# read output file into data
with open(output_filename,'r', encoding='utf-8') as file:
    data = file.readlines()
# color_palette.css File is now stored in data
file.close()

print("readme line 3: ", linecache.getline("README.md", 3))

#print(color_codes_dict)
print("old data:\n", data)
# check if line contains "value0 #..."
for color in color_codes_dict:

    data_list = r.replace_color_rgba(data, color, color_codes_dict[color])
    data_str = ""

# convert file data from list to string for write()-function
for word in data_list:
    data_str = data_str + word




print('new data:\n', data)
# not overwriting color_palette.css for now, hence output_file.txt
with open(output_filename, "w") as f:
    f.write(data_str)
f.close()

with open("color_palette.txt", "w") as f:
    f.write(data_str)
f.close()

restart_waybar()