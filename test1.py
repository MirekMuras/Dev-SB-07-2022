import os
import pandas as pd
import subprocess


from faker import Faker


def testing():
    try:
        with open (os.devnull,"w") as devnull:
            subprocess.check_output(devnull, shell=True, stderr=devnull)
            return False
    except subprocess.CalledProcessError:
        return True

#to create and generate a fake generator use the Faker() method
def dummy_data():
    generate_fake_profile = Faker()
    #genarate fake 10000 profile
    data = [generate_fake_profile.profile() for i in range(10000)]
    #cretae fake profile dataframe
    df = pd.DataFrame(data=data)


def split_full_name(data):
    data[['first_name','last_name']] = data['name'].loc[data['name'].str.split().str.len() == 2].str.split(expand=True)

    return data

