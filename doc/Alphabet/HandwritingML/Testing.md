# Increasing the Accuracy of Handwriting Recognition
## Objectives
The purpose of this experiment is to determine the effects of adjusting the:
    hidden_layer_sizes, 
    alpha, 
    solver, 
    random_stat, 
    and learning_rate_init parameters
    as well as changing training and testing datasets on the accuracy of MLPClassifier handwriting prediction.

There will be 3 datasets used. The EMNIST letters dataset, a dataset made of the images constructed from accelerometer handwritten letters, and a dataset made from the accelerometer data.

## 1. Effect of hidden_layer_sizes:
### a. The effect of the number of layers
This section focuses on the effect of increasing the number of layers.

The following parameter values were held constant:

    hidden_layer_sizes: layer size 150
    alpha: 1e-4
    solver: sgd
    random_states: 1
    learning_rate_init: 0.1


|Number of Layers| Cost after 50 iteration|Training Test Score|Number of Layers|
|-|-|-|-|
|1|0.06270702|0.977450|0.877900|
|2|0.12540605|0.961117|0.879100|
|3|0.13883957|0.959167|0.883700|
|4|0.13112121|0.962167|0.893600|
|5|0.12643161|0.960283|0.895700|
|6|0.12152045|0.960617|0.895900|
|7|0.12367285|0.954300|0.888700|
|8|0.11711137|0.963600|0.895900|
|9|0.13175316|0.959700|0.895500|
|10|0.13340327|0.963033|0.900400|
### b. The effect of the size of layers
This section focuses on the effect of increasing the size of layers.

The following parameter values were held constant:

    hidden_layer_sizes: 3 Layers
    alpha: 1e-4
    solver: sgd
    random_states: 1
    learning_rate_init: 0.1


|Size of Layers| Cost after 50 iteration|Training Test Score|Number of Layers|
|-|-|-|-|
|10 |1.05901435|0.676467|0.664900|
|50 |0.28281788|0.913217|0.860100|
|100|0.16804969|0.939983|0.872900|
|150|0.13993959|0.961200|0.885200|
|200|0.10639239|0.962100|0.889100|
|250|0.08865338|0.967750|0.891700|
|300|0.06954487|0.979383|0.901500|
## 2. Effect of Alpha
This section focuses on the effect of increasing alpha.

The following parameter values were held constant:

    hidden_layer_sizes: 3 Layers of size 100
    solver: sgd
    random_states: 1
    learning_rate_init: 0.1

|Alpha| Cost after 50 iteration|Training Test Score|Number of Layers|
|-|-|-|-|
|1e-4|0.17335034|0.946183|0.882800|
|1e-3|0.18441258|0.939000|0.870200|
|1e-2|0.22131285|0.952317|0.891000|
|1e-1|0.36840491|0.941517|0.901500|
|1e0 |0.97043753|0.860783|0.853900|
|1e1 |2.79713432|0.303183|0.307400|

## 3. Effect of solver
This section focuses on the effect of Solver.

The following parameter values were held constant:

    hidden_layer_sizes: 3 Layers of size 100
    alpha: 1e-1
    random_states: 1
    learning_rate_init: 0.1

|Alpha| Cost after 50 iteration|Training Test Score|Number of Layers|
|-|-|-|-|
|sgd  |0.36840491|0.941517|0.901500|
|adam |2.82994585|0.120050|0.120000|
|lbfgs|0.84471473|0.747467|0.742700|

## 4. Effect of Random States
This section focuses on the effect of the number of random states.

The following parameter values were held constant:

    hidden_layer_sizes: 3 Layers of size 100
    alpha: 1e-1
    learning_rate_init: 0.1

|Alpha| Cost after 50 iteration|Training Test Score|Number of Layers|
|-|-|-|-|
|0 |0.37103825|0.941767|0.904700|
|1 |0.36840491|0.941517|0.901500|
|2 |0.37133217|0.941283|0.906400|
|3 |0.37227054|0.935917|0.899000|
|4 |0.36968184|0.935500|0.902100|
|5 |0.37380404|0.940583|0.901700|
|6 |0.37608491|0.930283|0.890100|
|7 |0.37038071|0.935150|0.900500|
|8 |0.36934450|0.940417|0.902200|
|9 |0.37662321|0.936817|0.898800|
|10|0.37923559|0.935033|0.899200|

## 5. Effect of Learning Rate
This section focuses on the effect of the learning rate.

The following parameter values were held constant:

    hidden_layer_sizes: 3 Layers of size 100
    alpha: 1e-1
    random_states: 1

|Alpha| Cost after 50 iteration|Training Test Score|Number of Layers|
|-|-|-|-|
|0.1|0.36840491|0.941517|0.901500|
|0.2|0.51978587|0.903100|0.880900|
|0.3|0.71985817|0.864100|0.850600|
|0.4|0.94701881|0.834067|0.825100|
|0.5|1.23423930|0.721717|0.704500|
|0.6|3.26382727|0.038700|0.039600|
|0.7|3.26563979|0.038417|0.039600|
|0.8|3.26544947|0.038600|0.037100|