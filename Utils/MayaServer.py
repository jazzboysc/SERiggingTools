import socket
import threading
import cPickle
import os

from SocketServerMaya import SocketServerMaya
from SocketServerMaya import MayaMobuCommands
from SocketDataHelper import MayaMobuSocketData

import maya.utils as mu
import maya.OpenMaya as om
import time

def processCommandsInMaya(MayaCmd):
    try:
        res = mu.executeInMainThreadWithResult(MayaCmd)
        print('result:%s'%res)
        return res
    except Exception as e:
        om.MGlobal.displayError('Encountered exception: %s' %e)

def recv(theSocket,timeout = 2):
    # make socket non blocking
    theSocket.setblocking(0)
    
    # total data partwise in an array
    totalData = []
    data = ''
    
    # beginning time
    begin = time.time()
    while True:
        # if you got some data, then break after timeout
        if totalData and time.time() - begin > timeout:
            break
        
        # if you got no data at all, wait a little longer, twice the timeout
        elif time.time() - begin > timeout * 2:
            break
        
        # recv something
        try:
            data = theSocket.recv(8192)
            if data:
                totalData.append(data)
                # change the beginning time for measurement
                begin = time.time()
            else:
                # sleep for sometime to indicate a gap
                time.sleep(0.1)
        except:
            pass
    
    # join all parts to make final string
    return ''.join(totalData)

stopMayaServerEvent = threading.Event()
def listenerThread(server):
    global stopMayaServerEvent
    while not stopMayaServerEvent.is_set():
        try:
            conn, address = server.s.accept()
            print("Client came in Server")

            data = recv(conn)

            if not data.strip():
                print('Nothing received')
            else:
                print('Data received')
                pp = cPickle.loads(data)

                pp.debugDumpData()

                MayaCommand = MayaMobuCommands(pp)
                cmdres = processCommandsInMaya(MayaCommand.processCommand)
                serialized_obj = cPickle.dumps(cmdres)
                conn.sendall(serialized_obj)
    
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
            
            print('Connection closed.')
            time.sleep(0.1)
            
        except socket.timeout:
            # Non-blocking accept() call.
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
        mServer.s.settimeout(0.2) # Make server socket is non-blocking.
        mServer.get_socket()
        t = threading.Thread(name = 'MayaServerThread-1', target = listenerThread, args = (mServer,))
        t.daemon = True

        print('Start server listener thread.')
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
        print(e)
        return

def  isMayaServerRunning():
    return serverInitialized