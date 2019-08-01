# Breast-Cancer-Detection
Neural Network architecture has been a mystery for a long time. Trying to solve this mystery by using Genetic Programming

## Description
Applying the concepts of Genetic Programming on Neural Networks by creating a new architecture by the name of Genetically Optimized Neural Networks (GONN)

## Dataset
The dataset that was used is the Wisconsin Breast Cancer Database. The dataset contains information about benign
(non-carcinogenic) and maglignant (carcinogenic) cells. The dataset consists of 11 columns, the first one is the unique
ID of cells and the last one is the class label and the remaining columns are feature values each having a role to play
in helping us classify correctly. The feature values range from 0-10, where 0 being the harmless state and 10 being the
most abnormal state. The dataset has 699 rows out of which 16 have some missing values represented as ”?”. Since
the data is missing it has to be preprocessed and the missing values are dropped. That leaves us with only of a 683
rows

## A brief overview of Genetic Programming and Neural Networks
### Genetic Programming
Genetic Programming [Koza, 1994] is an model of evolutionary algorithms inspired by Darwin’s theory of evolution. The idea is ”survival of the fittest”. Initially a random solution is generated and then it is evolved on the basis
of a fitness function. Solutions or ”individuals” are produced and improved by applying reproduction, crossover and
mutation on the ”individual(s)” produced at the initial stage. The reproduction that is addressed to, here is an asexual
method of reproduction, wherein an individual which is ”fit” enough, copies itself into new generation. The crossover
function is the one where subtrees of a tree is copied to another tree and vice-versa and lastly, the mutation function
changes a node within the tree. The point to be noted is that the subtree and the node selection is totally random. This
way the search space or the solution space is widened and that is how Genetic Progamming tackles the problem of
local maxima. Even though GP tackles the aforementioned problem which is actually one of the biggest problems in
machine learning but there is a drawback to GP. The crossover and mutation function produces individual which can
be poor in fitness as compared to the parents and this can affect the amount of time and space taken by the program to
find an optimal solution.

### Artificial Neural Networks
Artificial Neural Networks (ANN) is probably one of the most famous algorithms. It mimics the working of the human brain and its biological neural network. The plus points of this model are the good adaptation and learning ability. The most common type of ANN is the feed forward neural network in which each and every neuron has a weight assigned to it with the inputs which come from the previous layer, the output of this layer is passed to the next layer after processing. An important class of feed forward neural networks is the Multilayer Perceptron (MLP) and under MLPs the most widely used algorithm is the Back propagation(BPA). In the BPA, the weights in the neural networks are iteratively changed in a direction in which the error is minimal. This learning model is very effective in learning patterns and also it can easily adapt to new trends in the dataset. Although the rate of convergence of ANN is considerably slow and it also comes with the risk of getting stuck in local optima. But there is another impediment in using BPA and its the structure of the BPA. Since the BPA is another neural network at its core, there is still ambiguity lingering about the optimal structure of BPA. The number of hidden layers, the number of neurons in the hidden layers and also how are they to be connected, all of this , is still big mystery. The structure of BPA plays a very crucial role in the performance of the neural networks. Even the slightest of changes can affect it in the greatest way. That is why deducing the optimal structure of ANN in an application problem has been an uphill battle since time immemorable.
Here, a novel hybrid crossover function used to optimize the neural network when genetic programming is applied.
