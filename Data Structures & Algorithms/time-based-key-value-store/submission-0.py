class TimeMap:

    def __init__(self):
        self.store={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[(key,timestamp)]=value
        

    def get(self, key: str, timestamp: int) -> str:
            for i in range(timestamp,-1,-1):
                if (key,i) in self.store:
                    return self.store[(key,i)]
            return ""

        
