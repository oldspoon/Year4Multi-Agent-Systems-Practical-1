#!/usr/bin/env_python3

import asyncio
import random

heaterStatus = False
temp = 20

class Agent():
    async def run(self):
        while True:
            #global temp
            if (temp == 20):
                heaterStatus = False
                print("Temp is good - "+str(temp))
            else:
                heaterStatus = True
                print("Temp is bad - "+str(temp))
                await asyncio.sleep(1)
                
async def environment():
    while True:
        global temp
        temp = random.randrange(19,21)
        
        #if(heaterStatus == False):
        #    temp = random.randrange(-3,-1)
        #    heaterStatus == True
        #else:
        #    temp = random.randrange(1,4)
        
        print(temp)        
        await asyncio.sleep(1)
                        
async def main():
    agent = Agent()
    await asyncio.gather(
        environment(),
        agent.run(),
        )
                            
if __name__ == "__main__":
    asyncio.run(main())