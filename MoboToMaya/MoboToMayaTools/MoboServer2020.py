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

from ...Utils.SocketServerMobo import SocketServer, MayaMoboCommands
from ...Utils.SocketDataHelper import MayaMoboSocketData

mServer = SocketServer('', 6000)
pp = MayaMoboSocketData()
callback_queue = Queue.Queue()
conn = None
address = None


stopServerEvent = threading.Event()

def get_running_thread():
    lists = []
    for thread in threading.enumerate(): 
        print(thread.name)
        lists.append(thread.name)
    return lists

def lisener_thread(server):
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
                    moboCommand = MayaMoboCommands(pp)
                    callback_queue.put(moboCommand.processCommand)
                    #moboCommand.processCommand()
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

def start_Motionbuilder_server():
    global serverInitialized
    global t
    if not serverInitialized:
        print('Server initialized.')
        needThread = mServer.get_socket()
        allRunningthreads = get_running_thread()
        t = threading.Thread(name = 'MotionbuilderServerThread-1', target = lisener_thread, args = (mServer,))
        t.daemon = True

        print('Start lisener thread.')
        t.start()

        serverInitialized = True

    #print('Start lisener thread.')
    #t.start()

    while True:
        try:
            callback = callback_queue.get(False) #blocks until an item is available
            if callback:
                callback()
                break

        except Queue.Empty:
            #mServer.s.close()
            print('Did not receive any command to execute.')
            time.sleep(1.0)

def stop__Motionbuilder_server():
    stopServerEvent.set()

#start_Motionbuilder_server()
