import json
import pandas as pd

def lambda_handler(event,context):
    print('pandas deployed and executed........')
    lambda_prabh("hello i am prabh")

def lambda_prabh(a):
    print(a)