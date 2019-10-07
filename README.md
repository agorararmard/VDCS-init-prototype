## Objectives: 
A working example that shows how Garbling is done.
Basic communication showing the work of the reRand() implementation.
Basic Evaluation of Garbled Circuit.
Enhancing our understanding of the problem.

## Implementation Scenario:
- A client object has a function a&b that he wants to outsource the computation for.
- The boolean circuit for a&b is present.
- The client object generates the random seeds R1, R2.
- The client reRandin() the input wires 3 times to generate win3.
- The client object sends R1, R2, and the Boolean Circuit for a&b to server 1.
- Server 1 Garbles the circuit to generate GC1.
- Server 1 sends R1, R2, GC1 to server 2.
- Server 2 runs reRand() on GC1 to generate GC2.
- Server 2 sends R1, R2, GC2 to server 3.
- Server 3 runs reRand() on GC2 to generate GC3.
- Server 3 sends R1, R2, GC3 to server 4.
- Server 4 evaluates the circuit for the desired input wires sent by the client.
- Server 4 sends the output wire and win3 to the client.
- The client object compares win3 of Server 4 with his win3. Accept or Reject.
- The client decrypts the output wire. If (valid_output) accept; else reject;

## Class Structure:
### Class message:
    Vars:
        circ                                #Simple Circuit without garbling
        R                                   #3 Random values for garbling
        winx                                #First input wire
        winy                                #Second input wire
    Methods:
        All class vars<-extract()           #Extract message content
YaoGarbledCkt
### Class circuit:
	Vars:
        table                               #The truth table
        cid                                 #Computation ID
        arr_in                              #Input Wires
        arr_out                             #Output Wires
    Methods:
        Constructor(F, cid)                                 #Generate simple Circuit;
        input wires <- YaoGarbledCkt_in(R input)            #Generate input wires
        output wires <- YaoGarbledCkt_out(R output)         #Generate output wires
        YaoGarbledCkt(R)                                    #Garbles the circuit
        Output wire <- eval(input wires[0,1]);              #Evaluates outputwire on given input wires

### Class Client:
    Vars:
        Circuit.                                #Circuit representing the desired function
        Input.                                  #Desired input to be evaluated
        Input wires.                            #Input wires computed by the class object
        Output wires.                           #Output wire computed by the class object
    Methods:
        Constructor(size)                                   #Size for the seedsize of creating the random R values
        messages[]<-intiate_Process(F, win, servers)		            #Creating the messages to be sent to the servers, given the boolean expression, the desired input, and the number of servers
        output<-result(z)			                        #Receiving execution result and decrypting it
       
### Class Server:
    Class Attributes:
        IDs                 #This is a class attribute to help keep track of created servers as well as giving them IDs
    Vars:
        ID                  #Identifier of this server, S0, S1, S2,.....Sn
        Circuit.            #Circuit handled by this class (Garbled)
        GC.                 #Circuit coming from the previous Server
        R.                  #Array of random seeds to be used
        Input wires.        #The input wires carrying the inputs to be computed
    Methods:
        Constructor()                           #assigns an ID for the server
        receiveC(m)		                        #Receiving from client the array of messages.
        receiveS(m,GC)		                    #Receiving from server the array of messages along with the last garbled circuit 
        GC<-garble()				            #Garbling the given circuit
        Output_Wire <- eval()	                #Output evaluation for the given input wire in message
        GC<-reRand()				            #Mimicking the behaviour of reRandamizing the GC
```
Setters, Getters, and destructors are present.
```
### Programming Language:
    Code for this prototype experiment is in Python3.6.

### Requirements:
    ```
        Python3.6
        Crypto Package
    ```
### How to Run:
To run the code simply run the following command in the directory of the project:
    ```
        python main.py
    ```
Note that main.py holds the test case for the classes designed and withit the experimental prototype.