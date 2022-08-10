import sys

def hex_to_binary(hex_number: str, num_digits: int = 8) -> str:
    return str(bin(int(hex_number, 16)))[2:].zfill(num_digits)

def parse_pi(filename : str):
    pi = str()
    with open(filename,"r") as f:
            n = f.readline().strip()
            for i in range(0, len(n), 4):
                hex_string = n[i:i+4]
                binary_string = hex_to_binary(hex_string, num_digits = 16)
                pi += binary_string
    return pi

def parse_art(filename : str, zeros : str = '.', ones : str = 'X'):
    art = str()
    w = int()
    h = 0
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip().replace(zeros,'0').replace(ones,'1')
            art += line
            w = len(line)
            h += 1
    return (w, h, art)

class bcolors:
    ENDC = '\033[0m'
    WHITE = '\u001b[37;1m'
    BGBLUE = '\u001b[44m'
    BGLIGHTBLUE = '\u001b[48;5;80m'
    GREY = '\u001b[30;1m'
    BGGREY = '\u001b[48;5;240m'
    BGLIGHTGREY = '\u001b[48;5;248m'

def clean_print(w : int, h : int, idx : int, pi : str, padding : int = 3):
    for i in range(max(0, idx - (padding * w)), idx + (h * w) + (padding + w), w):
        if i >= idx and i < idx + (h * w):
            print(f'{bcolors.WHITE}#{i} :{bcolors.ENDC}\t', end = '')
            print(pi[i:i + w]
                .replace('0',f'{bcolors.BGLIGHTBLUE} {bcolors.ENDC}')
                .replace('1',f'{bcolors.BGBLUE} {bcolors.ENDC}'))
        else:
            print(f'{bcolors.GREY}#{i} :{bcolors.ENDC}\t', end = '')
            print(pi[i:i + w]
                .replace('0',f'{bcolors.BGLIGHTGREY} {bcolors.ENDC}')
                .replace('1',f'{bcolors.BGGREY} {bcolors.ENDC}')) 

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'Usage : ./main.py ART_FILENAME')
        exit(-1)

    filename = sys.argv[1]    
    w, h, art = parse_art(filename)
    pi = parse_pi('pi/pi_hex_1m.txt')

    idx = pi.find(art)
    if idx != -1:
        print(f'Art was found at index {idx} !')
        print(f'Sequence is : {pi[idx:idx + len(art)]}')
        print(f'Formatted is :')
        clean_print(w, h, idx, pi)
    else:
        print('Art wasn\'t found...')