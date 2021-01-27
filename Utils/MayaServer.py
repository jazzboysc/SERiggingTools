import socket
import threading
import cPickle
import os

from SocketServerMaya import SocketServerMaya
from SocketServerMaya import MayaMobuCommands
from SocketDataHelper import MayaMobuSocketData

import maya.utils as mu
import maya.OpenMaya as om

mServer = SocketServerMaya('', 6001)

def processCommandsInMaya(MayaCmd):
    try:
        res = mu.executeInMainThreadWithResult(MayaCmd)
        print('result:%s'%res)
        return res
    except Exception as e:
        om.MGlobal.displayError('Encountered exception: %s' %e)

def create_conn(server, processFunc = processCommandsInMaya ):
    while True:
        try:
            conn, address = server.s.accept()
            print("Client came in Server")
            while True:
                data = conn.recv(server.SIZE)
                if not data.strip():
                    break
                else:
                    pp = cPickle.loads(data)
                    MayaCommand = MayaMobuCommands(pp)
                    cmdres = processFunc(MayaCommand.processCommand)
                    serialized_obj = cPickle.dumps(cmdres)
                    conn.send(serialized_obj)
                    continue
                    
            conn.shutdown(socket.SHUT_RDWR)    
            conn.close()
            print('Close Connection.')
        except Exception as e:
            print e
            return

def start_Maya_server():
    mServer.get_socket()
    t = threading.Thread(name = 'MayaServerThread-1', target=create_conn, args=(mServer,))
    t.daemon = True
    t.start()
