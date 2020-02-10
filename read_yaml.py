from yaml import load, dump
import os

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

dir = os.path.dirname(os.path.abspath(__file__))
file = open(f"{dir}/new_test.yml", "r")    
data = load(file, Loader=Loader)
output = dump(data, Dumper=Dumper)