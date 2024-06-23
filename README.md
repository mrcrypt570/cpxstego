# picap
hides a short string in the red channel of an image, creating a PNG called new.png
reads JPG, BMP, PNG and others

The maximum string size for now is 32 characters

######## WORK IN PROGRESS ########

usage: picap [-h] [-d DECRYPT] [-e ENCRYPT] [-m MESSAGE]

hides a short string in the red channel of an image

options:
  -h, --help            show this help message and exit
  -d DECRYPT, --decrypt DECRYPT
  -e ENCRYPT, --encrypt ENCRYPT
  -m MESSAGE, --message MESSAGE

ENCRYPT: python3 picap.py -e cover.jpg -m "secret"

DECRYPT: python3 picap.py -d new.png

BOTH: python3 picap.py -e cover.jpg -m "secret" -d new.png
