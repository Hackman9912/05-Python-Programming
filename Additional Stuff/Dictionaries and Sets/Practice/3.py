'''
3. File Encryption and Decryption
Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For
example:
codes = { 'A' : '%', 'a' : '9', 'B' : '@', 'b' : '#', etc...}
Using this example, the letter A would be assigned the symbol %, the letter a would be
assigned the number 9, the letter B would be assigned the symbol @, and so forth.
The program should open a specified text file, read its contents, and then use the dictionary to 
write an encrypted version of the file’s contents to a second file. Each character in
the second file should contain the code for the corresponding character in the first file.
'''
def main():
    plain_file = open('plain.txt', 'r')
    encoded_file = open('encoded.txt', 'w')
    line = plain_file.readline()
#    print(line)
    encryption_code = {
        "a": '1', "b": '3', "c": '5',
        "d": '7',"e": '9', "f": '11',
        "g": '13', "h": '15', "i": '17',
        "j": '19',"k": '21', "l": '23',
        "m": '25', "n": '27', "o": '29',
        "p": '31', "q": '33', "r": '35',
        "s": '37', "t": '39', "u": '41',
        "v": '43',"w": '45',"x": '47',
        "y": '49', "z": '51'
    }
    while line != "":
        print(line)
        for x in line.lower():
            print('x', x)
            if x in encryption_code:
                code = encryption_code[x]
                encoded_file.write(code)
            else:
                
    line = plain_file.readline()



main()