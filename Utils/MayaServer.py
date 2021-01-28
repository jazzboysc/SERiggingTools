import socket
import threading
import cPickle
import os

from SocketServerMaya import SocketServerMaya
from SocketServerMaya import MayaMobuCommands
from SocketDataHelper import MayaMobuSocketData

import maya.utils as mu
import maya.OpenMaya as om

def processCommandsInMaya(MayaCmd):
    try:
        res = mu.executeInMainThreadWithResult(MayaCmd)
        print('result:%s'%res)
        return res
    except Exception as e:
        om.MGlobal.displayError('Encountered exception: %s' %e)

stopMayaServerEvent = threading.Event()
def listenerThread(server):
    global stopMayaServerEvent
    while not stopMayaServerEvent.is_set():
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
                    cmdres = processCommandsInMaya(MayaCommand.processCommand)
                    serialized_obj = cPickle.dumps(cmdres)
                    conn.sendall(serialized_obj)
                    continue
    
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
            
            print('Close Connection.')
            time.sleep(2.0)
            
        except socket.timeout:
            pass

    server.s.close()
    print('Server closed.')

t = None
serverInitialized = False
mServer = None

def startMayaServer():
    global serverInitialized
    global t
    global stopMayaServerEvent
    global mServer

    if not serverInitialized:
        stopMayaServerEvent.clear()

        mServer = SocketServerMaya('', 6001)
        mServer.s.settimeout(0.2)
        mServer.get_socket()
        t = threading.Thread(name = 'MayaServerThread-1', target = listenerThread, args = (mServer,))
        t.daemon = True

        print('Start listener thread.')
        t.start()

        print('Server initialized.')
        serverInitialized = True

def stopMayaServer():
    global stopMayaServerEvent
    global serverInitialized
    global mServer

    try:
        stopMayaServerEvent.set()
        serverInitialized = False
    except Exception as e:
        print('2222')
        print(e)
        return

def  isMayaServerRunning():
    return serverInitialized