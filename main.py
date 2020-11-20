from  strub.proto.helloworld_pb2  import HelloRequest,HelloResponse
from  strub.proto.helloworld_pb2_grpc import HelloServerServicer, add_HelloServerServicer_to_server
import grpc;
from concurrent import futures


class HelloServer(HelloServerServicer):

    def __init__(self):
        self.__counter  = 0;
        pass;

    def get_message(self, request, context):
        response  =  HelloResponse(reply= "From server {0} , counting={1}".format(request.message, self.__counter));
        self.__counter +=1;
        return response;

# run it

if __name__ =="__main__":
 hello  =  HelloServer();
 server  =  grpc.server(futures.ThreadPoolExecutor(max_workers=10));
 add_HelloServerServicer_to_server(hello, server);
 

 port  = server.add_insecure_port("[::]:50001");
 server.start();
 print("Running at {0}".format(port))
 server.wait_for_termination();
 
 
 





