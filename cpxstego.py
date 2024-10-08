from PIL import Image
from PIL import UnidentifiedImageError
import binascii as t
import argparse


def str2bin(message):
    binary = bin(int(t.hexlify(message), 16))
    return binary[2:]

def bin2str(binary):
    message = t.unhexlify('%x' % (int(binary, 2)))
    return message

def main(choice, imgfn, message, nfname):
    try:
        image1 = Image.open(imgfn)
        if(image1.mode == 'RGB' or image1.mode == 'RGBA'):
            size = image1.size
            sizelst = list(size)
            mlenMAX = int(sizelst[0] * sizelst[1]) #maximum size of message this image can hold
            img1 = image1.load()
            if(choice == "e" and message != ''):
                bytearray = message.encode('utf-8')
                messagebinary = str2bin(bytearray)
                if(len(messagebinary) > 765):
                    print("message is too long - please try again") #message is longer than color channels in control pixel can hold
                elif(mlenMAX < len(messagebinary)):
                    print("message is too long for the image size - please try again") #message is longer than the image can hold
                else:
                    hideMe(img1, messagebinary, size, nfname)
            elif(choice=="d"):
                showMe(img1, size)
        else:
            print('image must be RGB or RGBA. please use another image.')
    except UnidentifiedImageError:
        print('Unidentified Image Error!!! If the file is .tif, make sure it has no alpha channel. Else... I dunno.') #whatever


def hideMe(img, msg, size, nfname):
    print('hiding... ')
    msglen = len(msg)
    new = Image.new('RGBA', size)
    data = new.load()
    #define the control pixel for decoding
    ctrlpx = img[0,0]
    cpxlist = list(ctrlpx)
    if(msglen > 255):
        cpxlist[0] = 255
        msglen = msglen-255
        if(msglen > 255):
            cpxlist[1] = 255
            msglen = msglen-255
            cpxlist[2] = msglen
        else:
            cpxlist[1] = msglen
            cpxlist[2] = 0
    else:
        cpxlist = [msglen, 0, 0]
    newcpx = tuple(cpxlist)
    data[0,0] = newcpx
    #encode
    count = 0 # msg char count
    width = int(size[0])
    height = int(size[1])
    for x in range(width):
        for y in range(height):
            if((x,y) != (0,0)):
                thispx = img[x,y] # get RGB
                pxlist = list(thispx) # RGB tuple to list
                binary = bin(int(pxlist[0])) # get binary of R
                binstr = str(binary) # R binary to string
                #encode here
                if(count < len(msg)):
                    bslist = list(binstr) # R binary string to list
                    bslist[-1] = str(msg[count]) # change last char to msg char at count
                    binstr = "".join(bslist) # update binstr
                    binary = bin(int(binstr, 2)) # update binary
                    pxlist[0] = int(binary, 2) # update the R value of the pixel
                    count+=1 # increment msg char count
                newpx = tuple(pxlist)
                data[x,y] = newpx
    print('saving')
    new.save(nfname + '.png')
    new.show()
    print(nfname + '.png saved')

def showMe(img, size):
    print('showing...')
    fpx = list(img[0,0]) # first pixel
    mlen = int(fpx[0] + fpx[1] + fpx[2])
    count = 0
    dmsg = ''
    for x in range(int(size[0])): #width
        for y in range(int(size[1])): #height
            if((x,y) != (0,0) and count < mlen):
                thispx = img[x,y] # get RGB
                pxlist = list(thispx) # RGB tuple to list
                binary = bin(int(pxlist[0])) # get binary of R
                binstr = str(binary) # R binary to string
                #decode here
                bslist = list(binstr)
                dmsg += bslist[-1]
                count+=1
    secret = bin2str(dmsg).decode('utf-8', 'replace')
    print(secret)


#######################################################
#####RUN ME############################################
#######################################################


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='cpxstego', description='hides a short string in the red channel of an image', epilog='thank you for playing')
    parser.add_argument('-d', '--decrypt', help='python3 cpxstego.py -d "(file name)"')
    parser.add_argument('-e', '--encrypt', help='python3 cpxstego.py -e "(cover file name)" -m "(message)" -f "(new file name)"')
    parser.add_argument('-m', '--message')
    parser.add_argument('-f', '--newname')
    args = parser.parse_args()
    #handle args
    if(args.encrypt != None and args.decrypt == None):
        if(args.message != None and args.newname != None):
            main('e', args.encrypt, args.message, args.newname)
        elif(args.newname == None):
            print('-h for help; please provide a new file name')
        elif(args.message == None):
            print('-h for help; please provide a message to hide')
    elif(args.encrypt == None and args.decrypt != None):
        main('d', args.decrypt, '', '')
    elif(args.encrypt != None and args.decrypt != None):
        print('one at a time, please')


#######################################################
####thanks john hammond and the lady from edureka!#####
#######################################################