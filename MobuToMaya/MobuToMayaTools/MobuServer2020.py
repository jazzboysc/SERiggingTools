import sys
import socket
import threading
import tempfile
import cPickle
import os
import time

from pyfbsdk import *
from pyfbsdk_additions import *
import Queue

from ...Utils.SocketServerMobu import SocketServer, MayaMobuCommands
from ...Utils.SocketDataHelper import MayaMobuSocketData

mServer = SocketServer('', 6000)
pp = MayaMobuSocketData()
callback_queue = Queue.Queue()
conn = None
address = None


stopServerEvent = threading.Event()

def getRunningThread():
    lists = []
    for thread in threading.enumerate(): 
        print(thread.name)
        lists.append(thread.name)
    return lists

def listenerThread(server):
    while not stopServerEvent.is_set():
        try:
            conn, address = server.s.accept()
            print("Client came in Server")
            while True:
                data = conn.recv(server.SIZE)
                if not data.strip():
                    break
                else:
                    pp = cPickle.loads(data)
                    MobuCommand = MayaMobuCommands(pp)
                    callback_queue.put(MobuCommand.processCommand)
                    conn.send("I received!")
                    continue
    
            conn.shutdown(socket.SHUT_RDWR)            
            conn.close()
            # server.s.close()
            print('Close Connection.')
            time.sleep(2.0)
            
        except Exception as e:
            print(e)
            return

t = None
serverInitialized = False

def customRigCallback(control, event):
    try:
        callback = callback_queue.get(False)
        if callback:
            callback()

    except Queue.Empty:
        pass

def startMotionbuilderServer():
    global serverInitialized
    global t
    if not serverInitialized:
        # Register create custom rig callback function, which is time-consuming and must be called in the main thread.
        FBSystem().OnUIIdle.Add(customRigCallback)

        needThread = mServer.get_socket()
        allRunningthreads = getRunningThread()
        t = threading.Thread(name = 'MotionbuilderServerThread-1', target = listenerThread, args = (mServer,))
        t.daemon = True

        print('Start listener thread.')
        t.start()

        print('Server initialized.')
        serverInitialized = True

def stopMotionbuilderServer():
    stopServerEvent.set()
