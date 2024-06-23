from PIL import Image
import binascii as t
import argparse


def str2bin(message):
    binary = bin(int(t.hexlify(message), 16))
    return binary[2:]

def bin2str(binary):
    message = t.unhexlify('%x' % (int('0b' + binary, 2)))
    return message

def main(choice, imgfn, message):
    image1 = Image.open(imgfn)
    size = image1.size
    img1 = image1.load()
    
    if(choice == "e" and message != ''):
        bytearray = message.encode('ascii')
        messagebinary = str2bin(bytearray)
        if(len(messagebinary) > 255): # using 255 until i can figure out why it's not working > 255 (765 MAX)
            print("message is too long - please try again")
        else:
            hideMe(img1, messagebinary, size)
    elif(choice=="d"):
        showMe(img1, size)

def hideMe(img, msg, size):
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
                if(count < msglen):
                    bslist = list(binstr) # R binary string to list
                    bslist[-1] = str(msg[count]) # change last char to msg char at count
                    binstr = "".join(bslist) # update binstr
                    binary = bin(int(binstr, 2)) # update binary
                    pxlist[0] = int(binary, 2) # update the R value of the pixel
                    count+=1 # increment msg char count
                newpx = tuple(pxlist)
                data[x,y] = newpx
            #else:
                #print('first pixel>>> ' + str(data[x,y]))
    print('saving')
    new.save('new.png')
    new.show()
    print('saved')

def showMe(img, size):
    print('showing...')
    fpx = list(img[0,0])
    mlen = int(fpx[0] + fpx[1] + fpx[2])
    #print('decode mlen = ' + str(mlen))
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
                #print(bslist)
                dmsg += bslist[-1]
                count+=1
    #print(dmsg)
    secret = bin2str(dmsg).decode('ascii', 'replace')
    print(secret)


#######################################################
#####RUN ME############################################
#######################################################

def test(str):
    print(str)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='picap', description='hides a short string in the red channel of an image', epilog='thank you for playing')
    parser.add_argument('-d', '--decrypt')
    parser.add_argument('-e', '--encrypt')
    parser.add_argument('-m', '--message')
    args = parser.parse_args()
    if(args.encrypt != None and args.message != None):
        main('e', args.encrypt, args.message)
    if(args.decrypt != None):
        main('d', args.decrypt, '')