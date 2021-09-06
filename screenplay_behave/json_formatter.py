from .collecting_formatter import CollectingFormatter
from os import path
import json


class JSONFormatter(CollectingFormatter):
    def __init__(self, stream_opener, config):
        super().__init__(stream_opener, config)

        self.outputDirectory = path.join(config.base_dir, config.userdata['behave.formatter.spjson.path'])

        if 'behave.formatter.spjson.single_file' in config.userdata:
            self.singleFile = (config.userdata['behave.formatter.spjson.single_file'] == 'True')
        else:
            self.singleFile = False

        self.features = []

    def eof(self):
        super().eof()

        if self.singleFile:
            self.features.append(self.currentFeature)
        else:
            (_, file_name) = path.split(self.currentFeature.file_name)
            (file_name, _) = path.splitext(file_name)
            filePath = path.join(self.outputDirectory, file_name + '.json')

            with open(filePath, 'wt') as file:
                json.dump(self.currentFeature, file, default=lambda o: o.__dict__, indent=2)

    def close(self):
        super().close()

        if self.singleFile:
            filePath = path.join(self.outputDirectory, 'behave_test_results.json')
            with open(filePath, 'wt') as file:
                json.dump(self.features, file, default=lambda o: o.__dict__, indent=2)
