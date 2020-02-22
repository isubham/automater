import os
import sys
import logging

DELETEFLAG = "d"
SPACEFLAG = "s"
PATHFLAG = "p"


class fsclean:

    def __init__(self, path, space, delete):
        self.path = path
        self.space = space
        self.delete = delete

    def processFiles(self, path, fileName):
        if self.delete.__contains__(self.fileExtension(fileName)):
            os.remove(self.joinPath(path, fileName))
        else:
            os.rename(self.joinPath(path, fileName), self.joinPath(path, self.newFormat(fileName)))

    def processDirectory(self, fileName, fileNames, path, pos):
        directoryName = fileName
        newDirectoryName = self.newFormat(directoryName)
        fileNames[pos] = newDirectoryName
        os.rename(self.joinPath(path, directoryName), self.joinPath(path, newDirectoryName))
        self.clean(self.joinPath(path, newDirectoryName))

    def newFormat(self, fileName):
        delimiter = ""
        if (self.space == "_"):
            delimiter = "_"
        return fileName.replace(" ", delimiter)

    def activate(self):
        self.clean(self.path)

    def clean(self, path):
        file_names = list()
        try:
            file_names = os.listdir(path)
        except FileNotFoundError:
            logging.basicConfig(filename='error.log', level=logging.ERROR)
            logging.error('No folder found with path' + path)
            return

        fileCount = len(file_names)
        if fileCount == 0:
            return
        for pos in range(fileCount):
            file_name = file_names[pos]
            if self.isDirectory(self.joinPath(path, file_name)):
                self.processDirectory(file_name, file_names, path, pos)
            elif self.isFile(self.joinPath(path, file_name)):
                self.processFiles(path, file_name)

    def isDirectory(self, path):
        return os.path.isdir(path)

    def isFile(self, path):
        return os.path.isfile(path)

    def fileExtension(self, path):
        return os.path.splitext(path)[1]

    def joinPath(self, portion1, portion2):
        return os.path.join(portion1, portion2)


    def process(self):
        commands = " ".join(sys.argv[1:])
        command_sequences = commands.split("-")
        command_sets = {DELETEFLAG: [], SPACEFLAG: "", PATHFLAG: ""}
        for command_sequence in command_sequences:
            if command_sequence != "":
                command = command_sequence[0]
                command_input = command_sequence[1:].strip()
                if command_sets.__contains__(command):
                    if command == DELETEFLAG:
                        command_sets[command] = set(command_input.split(" "))
                    else:
                        command_sets[command] = command_input
                else:
                    print("unknown option -" + command_sequence[0])

        self.fsclean(command_sets[PATHFLAG], command_sets[SPACEFLAG], command_sets[DELETEFLAG]).activate()


