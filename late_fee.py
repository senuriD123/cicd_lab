import config

def calculate_late_fee(days_late):
    fee=days_late*config.RATE_PER_DAY

    if days_late>=10:
        return config.MAX_FEE
    return fee

if __name__=='__main__':
    for d in (0,1,2,3,5,9,10,11,50,100):
        print(d,'days late-Rs.',calculate_late_fee(d))