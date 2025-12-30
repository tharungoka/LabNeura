from openpyxl.descriptors import serialisable
from services.analyzing.internal import InnoAnalyzer
from services.profiling import InnoProfiler

class AnalyzeManager:
    def __init__(self, inno_profiler :  InnoProfiler):
        self.analyzer = InnoAnalyzer(inno_profiler)