# ssdp_upnp

## Introduction   
The acticle [Exploring UPnP with Python](https://www.electricmonk.nl/log/2016/07/05/exploring-upnp-with-python/) gives a realy good insight of UPNP. SSDP is one of it's implementation.

The packege includes **three individual Classes**, ssdp server, ssdp client, nat upnp class. They first two class inherits from Class threading.Thread class, thus the two class instance runs on a single thread of own. They will not block main thread. After the ssdp client find a peer with same product name, it can communicate with main thread by **queue**. Nat upnp class is running on main thread, thus it will not block I/O, it will just search for LAN GDI (router with upnp nap forwarding function), and bind internal port with external port.

The logic of server is just listen a broadcast address with port 1900. If it received a "M-SEARCH" message, it will responce it's service infomation. The client just send a broadcast message with "M-SEARCH", and get server's service infomation.

The package can be used in blockchain solution where peers to find each other in LAN environment. 


## API     

### Server Class

**run()**: run the server in main thread with I/O blocking   
**start()**: run the server in other thread with I/O nonblocking    
**stop()**: stop the server   

### Client

**run()**: run the client in main thread with I/O blocking    
**start()**: run the client in other thread with I/O nonblocking    
**stop()**: stop the client   

### Nat   
**addPortForward(internal_port, external_port)**: run the function in main thread. It returns None if fail to bind, returns a tuple (external_ip, external_port) if succeed.    
**removePortForward(external_port)**: run the function in main thread. It returns True if succeed, and returns False if failed.   


## example
```
pip install ssdp-upnp
```
```
    import sys
    from ssdp_upnp.ssdp import Server, Client, Nat
    from ssdp_upnp.ssdp import gen_logger
    from queue import Queue

    logger = gen_logger('sample')

    if __name__ == '__main__':
        try:
            if sys.argv[1] == 'server':
                upnpServer  = Server(8048, 'blockchain', 'main')
                upnpServer.start()
            elif sys.argv[1] == 'client':
                queue = Queue()
                upnpClient = Client('blockchain', 'main', queue)
                upnpClient.start()
                logger.info(queue.get())
            elif sys.argv[1] == 'nat':
                nat = Nat()
                print(nat.addPortForward(8011, 8015))
            else:
                logger.warning('need params server or clinet')
        except Exception as e:
            logger.error(e)
```