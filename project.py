import os.path
import sys

from lemoncheesecake.project import Project


project_dir = os.path.dirname(__file__)
sys.path.append(project_dir)
project = Project(project_dir)

