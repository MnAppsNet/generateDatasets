
import numpy as np, matplotlib.pyplot as plt, pandas as pd, argparse, sys
from datetime import datetime

#Parse arguments :
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--samples", help = "Number of points to sample (Default: 1000)")
parser.add_argument("-d", "--dimensions", help = "Number of dimensions (Default: 2)")
parser.add_argument("-t", "--std", help = "Standard Deviation (Default: 1.0)")
parser.add_argument("-o", "--output", help = "Determines output file to save the dataset")
parser.add_argument("-r", "--random_seed", help = "Random seed ")

args = parser.parse_args()

#Default values :
if args.samples == None:
    args.samples = 1000
if args.dimensions == None:
    args.dimensions = 2
if args.std == None:
    args.std = 0.5
if args.random_seed == None:
    args.random_seed = datetime.now().timestamp()

if args.output == None:
    print("/!\\ Warning /!\\")
    print("No output path defined. Data will not be saved!")
    sys.stdout.flush()

np.random.seed(int(args.random_seed))

start = datetime.now()

samples = int(args.samples)     #Number of points to sample
dim     = int(args.dimensions)  #Dimensions
std     = float(args.std)       #Standard Deviation

#Generate gaussian distribution :
data = np.random.normal(loc=0.5, scale=std, size=(dim,samples))

#Save dataset :
pd.DataFrame(data.T).to_csv(args.output,index=False,header=False)

print("Standard Deviation : %f"%np.std(data))

print("\nExecution time : %f sec"%((datetime.now()-start).total_seconds()))

#Plot if we don't have a lot of data :
if (samples > 1000): exit(0)

if (dim == 2):
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.scatter(data[0, :],data[1, :])
    plt.show()
elif (dim == 3):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(data[0, :], data[1, :], data[2, :])
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_zlim(0,1)
    plt.show()