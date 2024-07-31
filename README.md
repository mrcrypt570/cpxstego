# picap
hides a short string in the red channel of an image (LSB), creating a PNG called "new.png"</br>
max length is 95 characters</br>
min length is 1 character, but this method is also based on how big the image is</br>
min image size is 8 pixels

RGB or RGBA color mode ONLY!

NO .tif with alpha channel.

records the length of the message in the color data of the first pixel,</br>
so if you don't want to leave a clue with some strange color in the first pixel,</br>
encode your message in an image whose first pixel is close to the value this</br>
script will set.</br>

######## WORK IN PROGRESS ########</br>
- watch this space for improvements

###################################


usage: picap [-h] [-d DECRYPT] [-e ENCRYPT] [-m MESSAGE]

hides a short string in the red channel of an image

options:

  -h, --help            show this help message and exit
  
  -d DECRYPT, --decrypt DECRYPT
  
  -e ENCRYPT, --encrypt ENCRYPT
  
  -m MESSAGE, --message MESSAGE

Examples...

ENCRYPT: python3 picap.py -e cover.jpg -m "secret"

DECRYPT: python3 picap.py -d new.png

BOTH: python3 picap.py -e cover.jpg -m "secret" -d new.png
