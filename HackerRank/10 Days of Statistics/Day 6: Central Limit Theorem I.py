'''CENTRAL LIMIT THEOREM - I'''

from math import erf

def cumulative_normal_distribution(x, mu, sigma):
    '''NORMAL PROBABILITY DISTRIBUTION WHERE
        mu      =   MEAN OF THE DISTRIBUTION
        sigma   =   STANDARD DEVIATION OF THE DISTRIBUTION'''
    return 0.5 * (1 + erf((x - mu) / (sigma * 2**0.5)))

def main():
    '''MAIN METHOD'''
    mu, sigma, sample_size = 205, 15, 49
    # APPLYING CENTRAL LIMIT THEOREM
    mu_, sigma_ = mu * sample_size, sigma * (sample_size ** 0.5)
    normal = cumulative_normal_distribution
    print(round(normal(9800, mu_, sigma_), 4))

if __name__ == '__main__':
    main()
