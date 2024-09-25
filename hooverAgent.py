#!/usr/bin/env_python3

import asyncio
import random

bool heaterStatus(0)
bool direction = 0 //0 is left, 1 is right
bool cleanliness = 0 //0 is dirty, 1 is clean
environment = random.randomrange(-10,8)
temp = 20
temp = temp + environment
class Agent():

async def run(self):
    while True:
        if (temp == 20):
            cleanliness = 1
            print("Floor is clean")
            # insert a method where the location is updated on device's memory
            else:
                cleanliness = 0
                print("Floor is dirty")
                # insert a method to begin cleaning operation
                await asyncio.sleep(1)
                
                async def environment():
                    while True:
                        global temp
                        temp = random.randrange(12,28)
                        print(temp)
                        await asyncio.sleep(1)
                        
                        async def main():
                            agent = Agent()
                            await = asyncio.gather(
                            environment(),
                            agent.run(),
                            )
                            
                            if __name__ == "__main__":
                                asyncio.run(main())