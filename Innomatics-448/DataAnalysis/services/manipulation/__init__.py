from services.manipulation.internal import InnoManipulator
from services.profiling import InnoProfiler

class ManipulateManager:
    def __init__(self, inno_profiler:InnoProfiler):
        self.manipulator = InnoManipulator(inno_profiler)