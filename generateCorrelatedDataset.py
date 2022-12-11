import numpy as np, matplotlib.pyplot as plt, pandas as pd, argparse, sys
from datetime import datetime

#Parse arguments :
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--samples", help = "Number of points to sample (Default: 1000)")
parser.add_argument("-d", "--dimensions", help = "Number of dimensions (Default: 2)")
parser.add_argument("-e", "--entropy", help = "Defines how much randomness is added to the correlated dimensions")
parser.add_argument("-l", "--slope", help = "Determines the angle of the data trend line (Default: 1)")
parser.add_argument("-o", "--output", help = "Determines output file to save the dataset")
parser.add_argument("-r", "--random_seed", help = "Random seed")

args = parser.parse_args()

#Mandatory Arguments :
if args.entropy == None:
    parser.print_help()
    exit(0)

#Default values :
if args.samples == None:
    args.samples = 1000
if args.dimensions == None:
    args.dimensions = 2
if args.slope == None:
    args.slope = 1
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
entropy = float(args.entropy)   #Defines how much randomness is added to the correlated dimensions
                                #With big enough entropy they have a weak almost zero correlation
                                #With entropy = 0 the correlation is 1
slope   = float(args.slope)     #Determines the angle of the data trend line

if entropy < 0 : entropy *= -1
dim = dim - 1 #We split the random dimension X from the correlated dimensions Y

#Generate noise :
# [N_11,N_12,...,N_1n]   <= n samples
# [N_21,N_22,...,N_2n]
# . . . . . . . .
# [N_d1,N_d2,...,N_dn]   <= d dimensions
noise = np.random.normal(size=(dim,samples))

#Random Dimension :
x = np.random.normal(size=samples)

#Generate correlated Dimensions :
#We generate the curve x = a_1 * Y_1 + a_2 * Y_1 + ... + a_d * Y_d
#We set a_1 = a_2 = ... = a_d = slope and for each dimension Y_d, we set Y_d = x, so we get the diagonal
Y = slope * np.ones((dim,samples)) * x
#Now we add some noise to all the Y dimensions so we deviate from 100% correlation :
noise_coefficient = 2*entropy #We define this noise coefficient that determines how much noise to add
Y += noise_coefficient * noise

#Join together the x and Y dimensions :
x = np.vstack([x, Y])

#Normalize between 0 and 1 :
x = np.interp(x, (x.min(), x.max()), (0, 1))

dataframe = pd.DataFrame(x.T)
print("Correlations Matrix :")
print(dataframe.corr())

if args.output != None:
    dataframe.to_csv(args.output,index=False,header=False)


print("\nExecution time : %f sec"%((datetime.now()-start).total_seconds()))

#Plot if we don't have a lot of data :
if (samples > 1000): exit(0)

if (dim + 1 == 2):
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.scatter(x[0, :],x[1, :])
    plt.show()
elif (dim + 1 == 3):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(x[0, :], x[1, :], x[2, :])
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_zlim(0,1)
    plt.show()