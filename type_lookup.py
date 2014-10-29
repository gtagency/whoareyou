import POSTagger as pos
from os import listdir
from os.path import isfile, join

PATH = "./data"
TYPE_PATH = join(PATH,"types")
RAW_PATH = join(PATH,"texts/raw")

def lookup_type(pers_type):
    names = [f for f in listdir(TYPE_PATH) if (isfile(join(TYPE_PATH, f)) and f[-4:] == ".txt")] 
    names = [f for f in names if "".join([line.decode("utf-8").strip() for line in open(join(TYPE_PATH, f)).readlines()]) == pers_type]
    for f in names:
        if(isfile(join(RAW_PATH, f))):
            print f
            print(pos.process_file(join(RAW_PATH, f)))

lookup_type("INTJ")
