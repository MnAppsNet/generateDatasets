
Some simple python scripts to generate different distributions

# generateCorrelatedDataset.py

    usage: generateCorrelatedDataset.py [-h] [-s SAMPLES] [-d DIMENSIONS]
                                        [-e ENTROPY] [-l SLOPE] [-o OUTPUT]
                                        [-r RANDOM_SEED]

    Arguments:
      -h, --help            show this help message and exit
      -s SAMPLES, --samples SAMPLES
                            Number of points to sample (Default: 1000)
      -d DIMENSIONS, --dimensions DIMENSIONS
                            Number of dimensions (Default: 2)
      -e ENTROPY, --entropy ENTROPY
                            Defines how much randomness is added to the correlated
                            dimensions
      -l SLOPE, --slope SLOPE
                            Determines the angle of the data trend line (Default: 1)
      -o OUTPUT, --output OUTPUT
                            Determines output file to save the dataset
      -r RANDOM_SEED, --random_seed RANDOM_SEED
                            Random seed

# generateGaussianDataset.py

    usage: generateGaussianDataset.py [-h] [-s SAMPLES] [-d DIMENSIONS] [-t STD]
                                      [-o OUTPUT] [-r RANDOM_SEED]
    
    Arguments:
      -h, --help            show this help message and exit
      -s SAMPLES, --samples SAMPLES
                            Number of points to sample (Default: 1000)
      -d DIMENSIONS, --dimensions DIMENSIONS
                            Number of dimensions (Default: 2)
      -t STD, --std STD     Standard Deviation (Default: 1.0)
      -o OUTPUT, --output OUTPUT

# generateUniformDataset.py

    usage: generateUniformDataset.py [-h] [-s SAMPLES] [-d DIMENSIONS] [-o OUTPUT]
                                     [-r RANDOM_SEED]
    
    Arguments:
      -h, --help            show this help message and exit
      -s SAMPLES, --samples SAMPLES
                            Number of points to sample (Default: 1000)
      -d DIMENSIONS, --dimensions DIMENSIONS
                            Number of dimensions (Default: 2)
      -o OUTPUT, --output OUTPUT
                            Determines output file to save the dataset
      -r RANDOM_SEED, --random_seed RANDOM_SEED
                            Random seed  
                            Determines output file to save the dataset
      -r RANDOM_SEED, --random_seed RANDOM_SEED
                            Random seed
