import os
import sys
from PySide2 import QtWidgets, QtGui, QtCore

sys.path.append("C:\Python27\Lib\site-packages")

import pyseq


class UI(QtWidgets.QDialog):

    def __init__(self, *args, **kwargs):
        '''Create the UI'''
        super(UI, self).__init__(*args, **kwargs)
        self.setMinimumSize(350, 150)
        self.setWindowTitle("Upload to Athera")
        self.setParent(hou.ui.mainQtWindow(), QtCore.Qt.Window) 
        self.setStyleSheet(hou.qt.styleSheet())

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.org_label = QtWidgets.QLabel("Org:", self)
        self.gridLayout.addWidget(self.org_label, 0, 0, 1, 1)
        self.org_comboBox = QtWidgets.QComboBox(self)
        self.gridLayout.addWidget(self.org_comboBox, 0, 1, 1, 1)
        self.project_label = QtWidgets.QLabel("Project:", self)
        self.gridLayout.addWidget(self.project_label, 1, 0, 1, 1)
        self.project_comboBox = QtWidgets.QComboBox(self)
        self.gridLayout.addWidget(self.project_comboBox, 1, 1, 1, 1)
        self.destination_label = QtWidgets.QLabel("Destination:", self)
        self.gridLayout.addWidget(self.destination_label, 2, 0, 1, 1)
        self.destination_entry = QtWidgets.QLineEdit(self)
        self.gridLayout.addWidget(self.destination_entry, 2, 1, 1, 1)
        self.upload_button = QtWidgets.QPushButton("Upload", self)
        self.gridLayout.addWidget(self.upload_button, 3, 1, 1, 1)

        self.connect(self.upload_button, QtCore.SIGNAL('clicked()'), self.update_file_paths)


    def update_file_paths(self):
        # Save hip file before making any changes
        hou.hipFile.save()

        # Save as a new hip file
        new_hip_file_name = hou.hipFile.basename().rpartition(".")
        new_hip_file_name = os.path.join(hip_var, new_hip_file_name[0] + "_toAthera." + new_hip_file_name[-1])
        # hou.hipFile.save(new_hip_file_name, True)

        # Replace all parmameter paths by new path and gather files to upload
        files_to_upload = []
        for path in reference_objects.keys():
            parameter = reference_objects[path].parm
            new_path = str(self.destination_entry.text()) + reference_objects[path].new_path
            unexpanded_filename = reference_objects[path].unexpanded_filename

            # Update the parameter to point to the path on Athera
            parameter.set(new_path + unexpanded_filename)

            # Add the file to the queue of files to upload
            if reference_objects[path].is_seq:
                files_to_upload += reference_objects[path].seq_files
            else:
                files_to_upload.append(reference_objects[path].path)

        # Add the new hip file to the list of files to Upload
        files_to_upload.append(new_hip_file_name)

        # Save hip file again
        hou.hipFile.save()

        # Upload the files
        self.upload(files_to_upload)

        # Switch to previous session
        # --Implement


    def upload(files):
        # Use transaction_manager.py
        

    def connect_to_athera(self):
        api = OrbitAPI()
        orgs = OrbitAPI.orgs_get()
        if orgs[0] != 200:
            pass
            #  Raise warning
        # Get projects
        # Get mount ids for every org/proj
        # Populate UI


class ReferencedFile(object):

    def __init__(self, file_path, parm):
        '''Creates an instance of a referenced file in the Hip file'''
        self.parm = parm
        self.path = hou.expandString(file_path)
        self.unexpanded_path = file_path
        self.dir = os.path.split(self.path)[0]
        self.dir_basename = os.path.basename(self.dir)
        self.filename = hou.expandString(os.path.split(self.path)[-1])
        self.unexpanded_filename = os.path.split(self.unexpanded_path)[-1]
        self.ext = self.extension_get(self.path)
        self.group = self.group_get(self.ext)
        self.is_seq = self.parm.isTimeDependent()
        self.seq_obj = self.seq_obj_get(self.dir, self.filename)
        self.seq_files = [os.path.join(self.dir, obj.name) for obj in self.seq_obj]
        self.new_path = "/" + self.group + "/" + self.dir_basename + "/"

    def extension_get(self, filename):
        '''Gets the extension of the file'''
        ext = os.path.splitext(filename)[-1][1:]
        if ext in (".gz", ".sc", ".bz", ".bz2"):
            ext = ".".join(filename.split(".")[-2:])
        return ext

    def group_get(self, ext):
        '''Groups the file into groups depending on the type'''
        if ext == "abc":
            return "abc"
        elif ext == "obj":
            return "obj"
        elif ext in ["bgeo", "bgeo.gz", 'bgeogz', 'bgeo.sc', 'bgeosc', 'bgeo.bz2', 'bgeo.lzma']:
            return "bgeo"
        else:
            return "others"

    def seq_obj_get(self, path, basename):
        '''Checks the directory for sequences and returns a sequence object'''
        dir_contents = pyseq.get_sequences(os.listdir(path))
        for content in dir_contents:
            if content.contains(basename):
                return content
        else:
            return pyseq.Sequence([basename])


valid_ext = ['geo', 'bgeo', 'hclassic', 'bhclassic', 'geo.gz', 'geogz',
             'bgeo.gz', 'bgeogz', 'hclassic.gz', 'hclassicgz',
             'bhclassic.gz', 'bhclassicgz', 'geo.sc', 'geosc', 'bgeo.sc',
             'bgeosc', 'hclassic.sc', 'hclassicsc', 'bhclassic.sc',
             'bhclassicsc', 'json', 'bjson', 'json.gz', 'jsongz',
             'bjson.gz', 'bjsongz', 'json.sc', 'jsonsc', 'bjson.sc',
             'bjsonsc', 'poly', 'bpoly', 'd', 'rib', 'vdb', 'sc',
             'bhclassic.lzma', 'bgeo.lzma', 'hclassic.bz2', 'bgeo.bz2',
             'pc', 'pmap', 'geo.lzma', 'iges', 'igs', 'ply', 'obj',
             'pdb', 'hclassic.lzma', 'lw', 'lwo', 'geo.bz2', 'bstl',
             'eps', 'ai', 'stl', 'dxf', 'bhclassic.bz2', 'abc', 'gz']

reference_paths = [(path, parm) for parm, path in hou.fileReferences() if path.rpartition(".")[-1] in valid_ext]
hip_file = hou.hipFile.path()
hip_var = hou.getenv("HIP")

reference_objects = {}

for path in reference_paths:
    reference_objects[path[0]] = ReferencedFile(path[0], path[1])

ui = UI()
ui.show()


# test = reference_objects[reference_paths[0][0]]
# print "parm:", test.parm
# print "Path:", test.path
# print "Unexpanded Path:", test.unexpanded_path
# print "Dir:", test.dir
# print "Dir Basename:", test.dir_basename
# print "Filename:", test.filename
# print "Unexpanded Filename:", test.unexpanded_filename
# print "Ext:", test.ext
# print "Is seq:", test.is_seq
# print "Seq Obj:", test.seq_obj
# print "Seq Files:", test.seq_files
# print "New Path:", test.new_path