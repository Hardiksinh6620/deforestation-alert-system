import numpy as np
from src.core import vegetation_loss,change_magnitude
def test_loss_direction():
+    assert vegetation_loss([.8],[.2],[.3],[.3])[0]
+    assert not vegetation_loss([.3],[.3],[.8],[.2])[0]
def test_signed_change(): assert change_magnitude([1,2],[3,1]).tolist()==[2,-1]
