import sys
import math

def pdf(x, mu=0.0, sigma=1.0):
    x = float(x - mu) / sigma
    return math.exp(-x*x/2.0) / math.sqrt(2.0*math.pi) / sigma

def main():
    x = float(sys.argv[1])
    mu = float(sys.argv[2])
    sigma = float(sys.argv[3])

    print(pdf(x, mu, sigma))

if __name__ == '__main__':
    main()
