import asyncio
import websockets
import pickle

async def sendAsync(value):
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send(pickle.dumps(value))
        message = await websocket.recv()
        return message

def mediator_getValue(param):
    try:
        return_value = asyncio.run(sendAsync([0, param, 0]))
        return return_value
    except Exception as e:
        print("Deforum Mediator Error:" + str(e))

def mediator_setValue(param, value):
    try:
        return_value = asyncio.run(sendAsync([1, param, value]))
        return return_value
    except Exception as e:
        print("Deforum Mediator Error:" + str(e))