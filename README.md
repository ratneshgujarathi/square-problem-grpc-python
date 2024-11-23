# Introduction
This project demonstrates a simple *gRPC-based application in Python*. It includes a server that calculates the square of a number and a client that communicates with the server to get the result.

## What is gRPC?
- gRPC (Google Remote Procedure Call) is a high-performance framework that allows a client and server to communicate seamlessly, even if they are written in different programming languages. It uses Protocol Buffers (Protobuf) for defining data structures and serializing them efficiently into binary format.

## How It Works (Overview)
- Protobuf Definition: We define the service and the messages in a .proto file.
- Code Generation: Two Python files are generated from the .proto file:
  - square_pb2.py: Defines the Protobuf messages.
  - square_pb2_grpc.py: Contains the gRPC service stubs and classes.
- Server: Implements the logic for handling client requests (calculating the square).
- Client: Sends a number to the server and receives the square of that number.

## Internal Mechanism in gRPC
- Protobuf Serialization: gRPC uses Protobuf to serialize data into a compact binary format, making communication efficient.
- Service Stub: The client uses a stub (auto-generated code) to call methods on the server as if they were local functions.
- Server Implementation: The server defines the logic for the service, processes requests, and sends back responses.
- HTTP/2 Protocol: gRPC uses HTTP/2 for communication, supporting multiplexing, compression, and streaming.

## Project Structure
```
├── square.proto           # Protobuf definition file
├── square_pb2.py          # Auto-generated Protobuf code
├── square_pb2_grpc.py     # Auto-generated gRPC service stubs
├── server.py              # Server implementation
├── client.py              # Client implementation
```

## Files Explanation
1. **square.proto**
This is the core definition file where the service and data structures are described.
Example:
```
service SquareService {
    rpc GetSquare (SquareRequest) returns (SquareResponse);
}

message SquareRequest {
    int32 number = 1;
}

message SquareResponse {
    int32 result = 1;
}
```
**Service (SquareService)**: Defines an RPC method GetSquare that takes a SquareRequest and returns a SquareResponse.
**Messages**: SquareRequest contains the input (number), and SquareResponse contains the result (square).

2. **square_pb2.py**
This file is auto-generated from the .proto file and contains Python classes for the Protobuf messages (SquareRequest and SquareResponse).

3. **square_pb2_grpc.py**
This file is auto-generated and contains:

Stub: Used by the client to communicate with the server.
Base Class: Used by the server to implement the service.

4. **server.py**
This implements the server logic:

Extends the SquareServiceServicer class from square_pb2_grpc.py.
Implements the GetSquare method to calculate the square of the number received.
Starts a gRPC server on localhost:50051.

5. **client.py**
This implements the client logic:

Connects to the server on localhost:50051 using a gRPC channel.
Sends a SquareRequest to the server.
Receives and prints the SquareResponse from the server.

## How to run the project
1. **Install Dependencies**
```pip install grpcio grpcio-tools```
2. **Generate gRPC Code**
```python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. square.proto```
3. **Start the Server**
Run:
```python server.py```
4. **Run the Client**
In a separate terminal, run:
```python client.py```

## Key Points to Understand
**Why are two files generated?**

- square_pb2.py: Contains the Protobuf message definitions.
- square_pb2_grpc.py: Contains the gRPC stubs and service classes for communication.

**What is the role of the server?**
- The server listens for requests, processes them, and returns responses.

**What is the role of the client?**
- The client sends requests to the server using the stub and handles the responses.

## Extending the Project
- Add more RPC methods to the .proto file (e.g., cube, factorial, etc.).
- Implement streaming RPCs for sending/receiving continuous data.
- Use advanced gRPC features like authentication or load balancing.
