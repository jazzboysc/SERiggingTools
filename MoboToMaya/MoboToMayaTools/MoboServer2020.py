import sys
import socket
import threading
import tempfile
import cPickle
import os

from pyfbsdk import *
from pyfbsdk_additions import *
import Queue

from ...Utils.MySocketServer2020 import SocketServer, MayaMoboCommands

mServer = SocketServer('', 6000)
pp = MayaMoboCommands()
callback_queue = Queue.Queue()
conn = None
address = None

def get_running_thread():
    lists = []
    for thread in threading.enumerate(): 
        print(thread.name)
        lists.append(thread.name)
    return lists

def create_conn(server):
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
                    callback_queue.put(pp.processCommand)
                    conn.send("I received!")
                    continue
    
            conn.shutdown(socket.SHUT_RDWR)            
            conn.close()
            server.s.close()
            print('Close Connection.')
            return
        except Exception as e:
            print e
            return

def start_Motionbuilder_server():
    needThread = mServer.get_socket()
    allRunningthreads = get_running_thread()
    t = threading.Thread(name = 'MotionbuilderServerThread-1', target=create_conn, args=(mServer,))
    t.daemon = True
    t.start()
    try:
        callback = callback_queue.get(True, 20) #blocks until an item is available
        callback()
    except Queue.Empty:
        mServer.s.close()
        print('Did not receive any command to execute.')

#start_Motionbuilder_server()
