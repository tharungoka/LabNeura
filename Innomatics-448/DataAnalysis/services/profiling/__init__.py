from services.profiling.internal import InnoProfiler
from services.profiling.internal import InternalManager
import pandas as pd
from services.profiling.external import ExternalManager, YdataProfiler

class ProfileManager:
    def __init__(self, filepath : str):
        print("Please select one profiler:")
        print("1.Internal Innomatics Profiler")
        print("2.Ydata External Profiler")
        choice = int(input("Choose 1/2"))
        if choice == 1:
            self.internal_manager = InternalManager(filepath)
            self.data = self.internal_manager.data
            self.profiler = self.internal_manager.inno_manager.inno_profiler
        else:
            self.external_manager = ExternalManager(filepath)
            self.profiler = self.external_manager.ydata_profiler
            self.data = self.profiler.data
            self.profiler.analyze()
