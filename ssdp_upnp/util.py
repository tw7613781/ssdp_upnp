import colorlog
import socket

def gen_logger(name, level='DEBUG'):
    fmt = '%(log_color)s %(levelname)8s [%(asctime)s] %(name)s-%(threadName)-15s %(message)s'
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(fmt))
    logger = colorlog.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger

def get_local_IP(): 
    '''
    get local host and ip address
    '''
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        return host_ip
    except Exception as e:
        raise 'Unable to get Hostname and IP: {}'.format(e) 