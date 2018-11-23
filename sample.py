import sys
from ssdp_upnp.ssdp import Server, Client
from ssdp_upnp.ssdp import gen_logger
from queue import Queue

logger = gen_logger('sample')

if __name__ == '__main__':
    try:
        if sys.argv[1] == 'server':
            upnpServer  = Server(8048, 'visiblespectre', 'main')
            upnpServer.start()
        elif sys.argv[1] == 'client':
            queue = Queue()
            upnpClient = Client('visiblespectre', 'main', queue)
            upnpClient.start()
            logger.info(queue.get())
        else:
            logger.warning('need params server or clinet')
    except Exception as e:
        logger.error(e)
