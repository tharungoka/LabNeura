from services.profiling.internal.inno import InnoProfiler
from services.profiling.internal.inno import InnoManager
import pandas as pd
class InternalManager:
    def __init__(self, filepath : str):
        self.inno_manager = InnoManager(filepath)
        self.data = self.inno_manager.data