dvc-NLP-simple-usecase
DVC NLP project

Reference repository:
official reference repo

DVC STUDIO

MY View

Bag of Words- Krish Naik

TF-IDF- Krish Naik

STEPS -
STEP 01- Create a repository by using template repository
STEP 02- Clone the new repository
STEP 03- Create a conda environment after opening the repository in VSCODE
conda create --prefix ./env python=3.7 -y
conda activate ./env
OR

source activate ./env
One shot create and activate environment
conda create --prefix ./env python=3.7 -y && source activate ./env
STEP 04- install the requirements
pip install -r requirements.txt
STEP 05- initialize the dvc project
dvc init
STEP 06- commit and push the changes to the remote repository
extra commands -
echo "*.log" >> logs/.gitignore
git rm --cached logs/running_logs.log
updated by rohan