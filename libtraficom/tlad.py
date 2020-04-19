import pandas as pd
import numpy as np


def tlad_5_8_conv_ensirekisterointipvm(x):
    return pd.to_datetime(x, format='%Y-%m-%d', errors='coerce')

def tlad_5_8_conv_kayttoonottopvm(x):
    return pd.to_datetime(x, format='%Y%m%d', errors='coerce')

def tlad_5_8_conv_int(x):
    if x and len(x) > 0: return int(x)
    else: return 0

TLAD_5_8_PD_READCSV = {
    'sep': ';',
    'encoding': 'iso-8859-15',
    'converters': {
        'ensirekisterointipvm': tlad_5_8_conv_ensirekisterointipvm,
        'kayttoonottopvm': tlad_5_8_conv_kayttoonottopvm,
        'Co2': tlad_5_8_conv_int,
        'matkamittarilukema': tlad_5_8_conv_int
    },
    'dtype': {
        'ajoneuvoluokka': 'category',
        'kaupallinenNimi': 'category'
    },
    'usecols': [
        'ajoneuvoluokka',
        'ensirekisterointipvm',
        'kayttoonottopvm',
        'kaupallinenNimi',
        'Co2',
        'matkamittarilukema',
        'merkkiSelvakielinen'
    ]
}
