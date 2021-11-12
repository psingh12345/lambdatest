import json
import pandas as pd

def lambda_handler(event,context):
    print('pandas deployed and executed........')
    lambda_prabh("hello i am rohit")

def lambda_prabh(a):
    print(a)