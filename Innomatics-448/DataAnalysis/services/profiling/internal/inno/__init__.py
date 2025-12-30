from services.profiling.internal.inno.inno import InnoProfiler
import pandas as pd
class InnoManager:
    def __init__(self, filepath : str):
        self.inno_profiler = InnoProfiler(filepath)
        self.data = self.inno_profiler.get_data()
        self.inno_profiler.analyze()