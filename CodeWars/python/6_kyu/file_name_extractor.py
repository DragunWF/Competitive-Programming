# https://www.codewars.com/kata/597770e98b4b340e5b000071/train/python

class FileNameExtractor:
    @staticmethod
    def extract_file_name(dirty_file_name):
        without_first = "_".join(dirty_file_name.split("_")[1:])
        return ".".join(without_first.split(".")[:-1])
