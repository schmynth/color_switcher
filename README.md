This python script will hopefully become a theme switcher for my hyprland setup.
Right now it extracts four color groups from the current wallpaper set by waypaper and saves them in a .css-file.
This file can be imported to f.e. the waybar style.css, so the colors defined as variables can be used.

To Do:

replace_text.py (module)
1.: replace text in a text file (based on position, not text) DONE
2.: read the file from anywhere in the filesystem   DONE
    2.1: get user input to file path (first to dcol file, later only to image file
    so this script can create the palette automatically) DONE

extract_colors.py (module)
3.: reads color values from wallbash .dcol file (background and text) DONE
4.: returns the colors with names as dict.

update_palette.py (script)
4.: enable selection of accent color group (1-4) to be applied


5.: integrate files (use color_palette.css as import)
    kitty
    waybar
    vscode

6.: let wallbash.sh create color palette for all images in directory (f.e. wallpapers)

7.: automatically detect wallpaper (DONE), if not already existing, create palette (DONE), extract colors, apply colors to config files.
    The wallpaper set by waypaper can be found in line 5 of ~/.config/waypaper/config.ini

Bugs:
automatic execution of wallbash.sh fails "Unsupported image format" 