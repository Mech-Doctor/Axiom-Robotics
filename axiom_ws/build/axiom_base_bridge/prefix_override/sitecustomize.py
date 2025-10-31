import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ing-vishwa/Desktop/Axiom_Robotics/axiom_ws/install/axiom_base_bridge'
