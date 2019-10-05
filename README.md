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

### Class Garbled_Circuit:
	Vars:
        GC.
        Input wires.
        Output wires.
    Methods:
        Constructor(Circuit, input wires, output wires): generate GC;
        Output wire <- eval(input wire);

### Class Client:
    Vars:
        Boolean Expression.
        Input.
        Input wires.
        Output wires.
    Methods:
        Constructor(Boolean Expression, Input)
        Input wires<-reRandin(Input wires)		//Rerandomizing wires
        Receive(output wires, output)			//Receiving execution result
        output <- DecodeVerf(Output wire, Output Wires)    //Verify&Decode result
	
### Class Server:
    Vars:
        Id
        Circuit.
        Garbled Circuit.
        Input wires.
        Output wires.
    Methods:
        Constructor()
        Receive(Boolean Expression,R1,R2)		//Receiving from client
        Receive(Garbled Circuit,R1,R2)		//Receiving from server
        GC<-Garble(F,R1)				//Garbling
        Output Wire, output wires <- eval (GC)	//Output evaluation
        GC<-reRand(GC,R2)				//for reRandamization

```
Setters, Getters, and destructors are present.
```
### Programming Language:
    Code for this prototype experiment will be in Python.

### Requirements:

### How to Run:
    