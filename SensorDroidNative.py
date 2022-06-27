from sensordroid import Client
import time
import pygame
data = []
old = 0
pygame.init()

drum = pygame.mixer.Sound("drum.wav")

def devicesDiscoveredEventHandler(devices):
    print(devices)
    if len(devices) > 0:
        client = Client(devices[0])

        client.connectionUpdated = connectionUpdatedEventHandler
        client.sensorsReceived = sensorsReceivedEventHandler
        client.imageReceived = cameraReceivedEventHandler

        client.sensorsSampleRate = 100
        client.cameraResolution = 13

        client.connect()
        

def connectionUpdatedEventHandler(sender, msg):
    if sender is not None:
        if sender.connected:
            print("Connected")
        else:
            print("Disonnected") 

def sensorsReceivedEventHandler(sender, dataCurrent):
    global old
    x,y,z = dataCurrent.Acceleration.Values.AsString.split("\t")
    # print(x.index('.'))
    x = abs(int(x[:x.index('.')]))
    y = abs(int(y[:y.index('.')]))
    z = abs(int(z[:z.index('.')]))
    if x+y+z >25:
        drum.play()


def cameraReceivedEventHandler(sender, image):
    #Process image data bytes
    pass

Client.devicesDiscovered = devicesDiscoveredEventHandler
Client.startDiscovery()

key = input("Press ENTER to exit\n") 

Client.closeAll()

# print(sum(data)/len(data))