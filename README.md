# picap
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
	<head>
		<title>_mrcrypt</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<style type="text/css">
		html, body { background-color: #98ff98; font-family:'Courier New', Courier, monospace}
		</style>
	</head>
	<body>
        <b>_mrcrypt | site forever under construction</b></br>
        
	</body>
</html>


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
