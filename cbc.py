import sys

def key_file_to_dict(path):
    lst=file_to_string(path).split('\n')
    dict={}
    for pair in lst:
        splited_pair=pair.split(' ')
        dict[splited_pair[0]]=splited_pair[1]
    return dict

def reverse_key(key_dict):
    rev_key = {v: k for k, v in key_dict.iteritems()}
    return rev_key


def file_to_string(path):
    with open(path, mode='rb') as myfile:
        data = myfile.read().rstrip('\n')
    return data


def divide_to_blocks(plaintxt_path):
    plaintxt=file_to_string(plaintxt_path)
    plaintxt_length=len(plaintxt)
    padding_length=10-(plaintxt_length%10)
    padded_txt=plaintxt+padding_length*'0'
    return [ padded_txt[i:i+10] for i in range(0, len(padded_txt),10) ]



def encrypt():
    dummy,plaintxt_path,key_path, iv_path=sys.argv[1:]
    divided_plaintxt=divide_to_blocks(plaintxt_path)
    iv=file_to_string(iv_path)
    key=key_file_to_dict(key_path)
    c=iv
    cipher=""
    for block in divided_plaintxt:
        temp=""
        for char_i in range(len(block)):
            temp+=chr(ord(block[char_i])^ord(c[char_i]))
        c=""
        for char in temp:
            if key.has_key(char):
                c+=key[char]
            else:
                c+=char
        cipher+=c
    with open(plaintxt_path[:-4]+"_encrypted.txt", 'wb') as f:
        f.write(cipher)





def decrypt():
    dummy,ciphertxt_path, key_path, iv_path = sys.argv[1:]
    divided_ciphertxt = divide_to_blocks(ciphertxt_path)
    iv = file_to_string(iv_path)
    key = reverse_key(key_file_to_dict(key_path))
    c = iv
    p_text=''
    for block in divided_ciphertxt:
        temp=''

        for char in block:
            if key.has_key(char):
                temp+=key[char]
            else:
                temp+=char
        if block != divided_ciphertxt[-1]:
            for char_i in range(len(c)):
                p_text+=chr(ord(c[char_i])^ord(temp[char_i]))
            c=block

    with open(ciphertxt_path[:-4]+"_decrypted.txt", 'wb') as f:
        f.write(p_text)

if sys.argv[1]=='Encryption':
    encrypt()
if sys.argv[1]=='Decryption':
    encrypt()

