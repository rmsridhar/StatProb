#nueral network example
#intialize data as step 1
import numpy as np
x=[[1,0,1,0],[1,0,1,1],[0,1,0,1]]
y=[[1],[1],[0]]
wh=[[0.42,0.88,0.55],[0.10,0.73,0.68],[0.6,0.18,0.47],[0.92,0.11,0.52]]
bh=[0.46,0.72,0.08]
wout=[[0.30],[0.25],[0.23]]
bout=[0.69]
print(x)
# Forward Propogation
# Step 2
#We take matrix dot product of input and weights assigned to edges between
#the input and hidden layer then add biases of the hidden layer neurons to
#respective inputs, this is known as linear transformation:
for m in range(1):
    #hidden_layer_input= matrix_dot_product(X,wh) + bh
    hidden_layer_input=np.dot(x,wh)+bh
    print(hidden_layer_input)
    #Step 3
    # Perform non-linear transformation using an activation function (Sigmoid).
    #Sigmoid will return the output as 1/(1 + exp(-x)).

    #hiddenlayer_activations = sigmoid(hidden_layer_input)
    hiddenlayer_activations=[]
    a=[]
    for i in range(3):
        a=[]
        for j in range(3):
            a.append(j)
            a[j]=1/(1+np.exp(-hidden_layer_input[i,j]))
        hiddenlayer_activations.append(i)
        hiddenlayer_activations[i]=a
    print(hiddenlayer_activations)
    #Step 4: Perform linear and non-linear transformation of hidden layer activation at
    #output layer
    #output_layer_input = matrix_dot_product (hiddenlayer_activations * wout ) + bout
    #output = sigmoid(output_layer_input)
    output_layer_input=np.dot(hiddenlayer_activations,wout)+bout
    print(output_layer_input)
    output=[]
    for i in range(3):
      #  a=[]
        output.append(i)
        output[i]=1/(1+np.exp(-output_layer_input[i]))

    output1=np.array(output)
        
    print("output1 Transpose",output1.transpose())

    #Step 5: Calculate gradient of Error(E) at output layer
    #E = y-output
    E=y-output1
    print("Error",E)

    #Step 6: Compute slope at output and hidden layer
    #Slope_output_layer= derivatives_sigmoid(output)
    #Slope_hidden_layer = derivatives_sigmoid(hiddenlayer_activations)
    # Compute the slope/ gradient of hidden and output layer neurons
    #( To compute the slope, we calculate the derivatives of non-linear activations
    #x at each layer for each neuron). Gradient of sigmoid can be returned as x * (1 – x).

    slope_output_layer=[]
    for i in range(3):
        slope_output_layer.append(i)
        slope_output_layer[i]=output[i]*(1-output[i])
    print(slope_output_layer)
    slope_output_layer1=np.array(slope_output_layer)
    slope_output_layer2=slope_output_layer1.transpose()
    print("Slope Ouput layer",slope_output_layer2)

    slope_hidden_layer=[]
    for i in range(3):
        a=[]
        for j in range(3):
            a.append(j)
            a[j]=hiddenlayer_activations[i][j]*(1-hiddenlayer_activations[i][j])
        slope_hidden_layer.append(i)
        slope_hidden_layer[i]=a
        
    print("slope hidden layer",slope_hidden_layer)

    #Step 7: Compute delta at output layer
    #d_output = E * slope_output_layer*lr
    lr=0.1
    d_output=E *slope_output_layer
    print("d_output",d_output)


    #Step 8: Calculate Error at hidden layer

    #Error_at_hidden_layer = matrix_dot_product(d_output, wout.Transpose)
    wout1=np.array(wout)
    print(wout1.transpose())
    Error_at_hidden_layer=np.dot(d_output, wout1.transpose())

    print("Error at hidden layer",Error_at_hidden_layer)

    #Step 9: Compute delta at hidden layer

    #d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer
    d_hiddenlayer = np.dot(Error_at_hidden_layer , slope_hidden_layer)
    print("Delta hidden layer",d_hiddenlayer)

    #Step 10: Update weight at both output and hidden layer

    #wout = wout + matrix_dot_product(hiddenlayer_activations.Transpose, d_output)*learning_rate
    #wh =  wh+ matrix_dot_product(X.Transpose,d_hiddenlayer)*learning_rate


    learning_rate=0.1
    hiddenlayer_activations1=np.array(hiddenlayer_activations)
    wout = wout + np.dot(hiddenlayer_activations1.transpose(), d_output)*learning_rate
    print("wout",wout)
    x1=np.array(x)
    wh =  wh+ np.dot(x1.transpose(),d_hiddenlayer)*learning_rate
    print("wh",wh)

    #Step 11: Update biases at both output and hidden layer

    bh = bh +np.sum(d_hiddenlayer, axis=0) * learning_rate
    bout = bout +np.sum(d_output, axis=0)*learning_rate

    print("bh",bh)
    print("bout",bout)
print("Error",E)
