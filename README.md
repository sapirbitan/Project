# How to run our code
download processing from here: https://processing.org/download/ extract the tar folder to your computer.

download your prefered python editor, for example https://www.jetbrains.com/pycharm/download/#section=windows

clone the repository to your computer. open processing_code.pde, press ok. in the python code, we want to create a txt file at the processing folder where the code is, so copy the path of the processing folder and put on line 2 under base_dir, and than run the code.

go to processing_code, go to Sketch->import library->add library and search for: "Shapes 3D" -> install and for "Video Export" -> install. now run the code, a video should be created to the processing_code folder.

Software that simulates the behaviour of systems written in the Beacon Calculus. bcs is under development by the Boemo Group at the University of Cambridge.

# Downloading and Compiling bcs
Clone the bcs repository by running:

git clone https://github.com/MBoemo/bcs.git The bcs directory will appear in your current directory. bcs was written in C++11 and uses OpenMP for parallel processing, but these are standard on most systems; there are no other third party dependencies.

# Compile the latest version of bcs by running:
cd bcs

git checkout v1.0.1

make

This will put the bcs executable into the bcs/bin directory. Development was done using gcc 5.4.0 on an Ubuntu 16.04 platform, and bcs was tested to compile and run on both OSX and Linux systems.

# Documentation and Manual
A manual for writing models in the Beacon Calculus and documentation for bcs is available at https://beacon-calculus-simulator.readthedocs.io. It includes:

quick-start tutorials, a bank of examples, a full list of features.

# DNA Replication:
Every time a cell in your body divides, six billion base pairs of DNAs must be replicated. Errors in this process can have severe consequences: problematic DNA replication is often implicated in cancer and other genetic diseases.

Replication begins at sites on a chromosome called origins of replication (ORI), each of which can "fire" with a certain probability to start two replication forks that move in either direction down the chromosome. This stochasticity means that each cell exhibits different patterns of replication origin firing. The movement of replication forks also varies between cells: features in the genome such as nucleotide repeats, actively transcribed genes, and DNA-binding proteins make replication forks more likely to stall or pause, but this may not happen at the same time or place cell-to-cell.

The DNA replication is a stochastic process and that's why the beacon calculus issuited for it; the difference in behavior between simulations mirrors the heterogeneity between replicating cells, and communication via beacons enables origins and forks to keep track of which chromosomal positions have been replicated.

![alt text](https://camo.githubusercontent.com/cf5b7fc4d9410988ef0cd53e41e1a8f5c0d70a87dd38a2ed6ffdbde4e75542b2/68747470733a2f2f7777772e62696f727869762e6f72672f636f6e74656e742f62696f727869762f6561726c792f323031392f30332f31362f3537393032392f46322e6c617267652e6a70673f77696474683d383030266865696768743d363030266361726f7573656c3d31)

In the above code we can see the behavior of the replication. We define 3 processes: FR – fork right with parameter as position, FL – fork left with parameter as position, ORI – the origin of the replication which has 3 parameters: – the position of the chromosome, fire – firing rate and – the licensing probability. The length of the chromosome is , and is between 1 to L. We define all possible ORI of known origin locations on S, to be working in parallel.

An ORI can be licensed or nlicensed (not licensed), ORI has a choice between them, if it's not licensed then we reach deadlock because the origin can't fork anymore. If it's licensed then we perform a beacon check on its position to ensure that it hasn't been replicated yet, if the beacon fires the ORI process continues with two parallel processes FR and FL.

We first launch a beacon on the same channel chr, and check if we reach the end of the chromosome. If we haven't, they do a beacon check on the next position (left or right) to check again that this position hasn't been replicated yet. If it hasn't then the process FR or FL moves to the next position.
