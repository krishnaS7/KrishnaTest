#pythonFile
import subprocess
import os
import sys
def get_ip():
    adp="eth0"
    cmd=["ip", "addr", "show", adp]
    p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE)

    p2 = subprocess.Popen(["grep", "\<inet\>"], stdin=p1.stdout, stdout=subprocess.PIPE)

    p3 = subprocess.Popen(["awk", "{ print $2 }"], stdin=p2.stdout, stdout=subprocess.PIPE)

    p4 = subprocess.Popen(["awk", "-F", "/", "{ print $1 }"], stdin=p3.stdout, stdout=subprocess.PIPE)

    output, _ = p4.communicate()

    return output.decode()
res=get_ip()

with open('ipoutput.txt', 'a') as file:
    file.write(f'{res}\n')
print(f"current ip:{res}")

def collison_check(filename):
    unique=set()
    duplicate=[]
    with open(filename,'r') as file:
        for line in file:
            line=line.strip()
            if line in unique:
                duplicate.append(line)
            else:
                unique.add(line)
        if duplicate:
            print("Duplicate values found:")
            print("\n".join(set(duplicate)))  
        else:
            print("No duplicates found.")
    #return duplicate


def main():
    if '--check-collision' in sys.argv:
        filename = sys.argv[sys.argv.index('--check-collision')+1]
        res_check=collison_check(filename)
        #print(res_check)
    else:
        ip_result = get_ip()
        print(ip_result)

if __name__ == '__main__':
    main()
