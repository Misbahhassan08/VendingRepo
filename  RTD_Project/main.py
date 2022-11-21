from max31865 import MAX31865
from drv8871 import DRV8871
from drv8834_3 import DRV8834_3
from drv8834_4 import DRV8834_4
from pca9535db import PCA9535DB
from time import sleep

class interface:
    def __init__(self):
        self.max31865 = MAX31865()
        self.drv8871 = DRV8871()
        self.drv8834_3 = DRV8834_3()
        self.drv8834_4 = DRV8834_4()
        self.pca9535db = PCA9535DB()
        pass  # end of __init__
    pass  #end of interface
class MAIN(interface):
    def __init__(self):
        interface.__init__(self)
        pass   # end of __init__
    
    pass  # end of MAIN(interface)

if __name__ == "__main__":
    MAIN()
