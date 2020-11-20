import grpc;
from  strub.proto.helloworld_pb2      import HelloRequest,HelloResponse
from  strub.proto.helloworld_pb2_grpc import HelloServerStub
 


class HelloClient(HelloServerStub):
    def __init__(self, host:str):
        channel =  grpc.insecure_channel(host);
        super().__init__(channel);


def run():
    
    client  =  HelloClient("127.0.0.1:50001");
    response= client.get_message(HelloRequest(message="Obaro"));
    print(response.reply);
    
if __name__ =="__main__":
    run();
   
    
    
