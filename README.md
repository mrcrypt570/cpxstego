# cpxstego
hides a short string in the red channel of an image (LSB)</br>
max length is 95 characters</br>
min length is 1 character, but this method is also based on how big the image is</br>
min image size is 8 pixels

RGB or RGBA color mode ONLY!

NO .tif with alpha channel.

records the length of the message in the color data of the first (control) pixel,</br>
so if you don't want to leave a clue with some strange color in the first pixel,</br>
encode your message in an image whose first pixel is close to the value this</br>
script will set.</br>

######## WORK IN PROGRESS ########</p>
more features will be added as i learn more (and as time permits)</br>
this is a code-bash exercise to learn both python and LSB image steganography</br>
the concept and (slightly different) method came from an edureka! video here:</br>
https://youtu.be/xepNoHgNj0w?si=KPxSQbvPT3FeIXvD</br>
and the method extrapolated from a john hammond video here:</br>
https://youtu.be/gxHY43274l4?si=Zrt11_zmRcIUv9O6</br>
So, thanks to them for all of this =D</p>
###################################</p>
usage: cpxstego [-h] [-d DECRYPT] [-e ENCRYPT] [-m MESSAGE] [-f NEWNAME]

hides a short string in the red channel of an image

options:</br>
  -h, --help            show this help message and exit</br>
  -d DECRYPT, --decrypt DECRYPT <b>python3 cpxstego.py -d "(file name)"</b></br>
  -e ENCRYPT, --encrypt ENCRYPT <b>python3 cpxstego.py -e "(cover file name)" -m "(message)" -f "(new file name)"</b></br>
  -m MESSAGE, --message MESSAGE</br>
  -f NEWNAME, --newname NEWNAME

thank you for playing
