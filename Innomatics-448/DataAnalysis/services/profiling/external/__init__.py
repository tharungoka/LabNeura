from services.profiling.external.ydata import YdataProfiler

class ExternalManager:
    def __init__(self, filepath):
        self.ydata_profiler = YdataProfiler(filepath)