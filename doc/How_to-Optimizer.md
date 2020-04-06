#How to use Optimizers.py
##Optimizer base class
All optimizers inherit from the Optimizer Class. To create a new instance, use ``Optimizer(fn)`` where `fn` is a function that return a number.

The `Optimizer` class has a few base properties:
- `Optimizer.fn` is the function that it optimizes
- `Optimizer.params` is an array of parameters that are given to the function
- `Optimizer.configs` is a dictionary containing the configs for specific optimizers
- `Optimizer.x` is an array containing all the different steps during the optimization
- `Optimizer.grads` is an array containing the gradients for each value in `Optimizer.x`

This class also has a few functions that are overwritten by the classes that inherit from it:
- `Optimizer.FillParameters(*params)`:
    - Input parameters in the order that `Optimizer.fn` takes them
    - Equivalent of the feed dictionary in Tensorflow
- `Optimizer.config(*params)`:
    - Input form: `(setting_name, value), ...`
    - Changes the `Optimizer.configs` property
- `Optimizer.Optimize(*params)`:
    - Doesn't do anything unless implemented by a sub-class
    - _prints "Ichi-byo Keika" as a debug value_
- `Optimizer.CallFunction(*values)`:
    - Input values in the order given by the functions
    - Do not put values that stay constant in `*values`. 
    Use `Optimizer.FillParameters(*params)` for those.
    - Executes `Optimizer.fn(*values, *params)`
    
- `Optimizer.GradientApprox(x)`:
    - Approximate gradient around `x` of `Optimizer.fn` with approximation
    quality `.configs['grad_approx']`
    - __Object must have `.configs['grad_approx']` for this to be usable__

##AdamAlgorithm_1D class
This class inherits from the `Optimizer` class and, therefore, has a lot of the same properties
but implements and changes some of the functions and properties. This class only optimizes for __1__ variable.

The `AdamAlgorithm_1D` class has the following `.configs`:
- `.configs['N']` contains the number of iterations the optimizer should do on one run. `Default: 1000`
- `.configs['x0']` contains the starting point of the optimization. `Default: 0`
- `.configs['grad_approx']` contains the quality of the approximation. The smaller
it is the better the approximation. `Default:0.00001`

This class implements the `Optimize(...)` function from `Optimizer`. Its parameters are:
- `alpha`: the learning rate. `Recommended Value Range: 0.01 - 0.001`
- `beta1`: exponential decay rate for `m`. `Recommended Value: 0.9`
- `beta2`: exponential decay rate for `v`. `Recommended Value: 0.999`
- `e`: epsilon `Default: 1e-8`
- `return_array`: if `True`, the functions returns all the optimization steps. else
it returns only the final value.

##SGD_1D
This class implements the SGD algorithm with one variable

The `SGD_1D` class  has the following `.configs`:
- `.configs['N']` contains the number of iterations the optimizer should do on one run. `Default: 1000`
- `.configs['x0']` contains the starting point of the optimization. `Default: 0`
- `.configs['grad_approx']` contains the quality of the approximation. The smaller
it is the better the approximation. `Default:0.00001`

This class implements the `Optimize(...)` function from `Optimizer`. Its parameters are:
- `alpha`: the learning rate. `Recommended Value Range: 0.01 - 0.001`
- `return_array`: if `True`, the functions returns all the optimization steps. else
it returns only the final value.