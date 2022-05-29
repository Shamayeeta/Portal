# Medical Portal
This medical portal web-app, that helps detect ocular and lung diseases from uploaded scans and incorporating facial authentication was built as a project for Engage'22.
## Features
- The app incorporated TFA (Two-Factor Authentication) which requires the user to enter correct password and have their face match with the picture taken during registration.
- The user is allowed to register as a <b>Doctor</b> or a <b>Patient</b>.
- Upon logging in, the user can upload Eye scans or Chest-XRay scans to be classified. <br>
#### Eye scans are diagnosed as:
 <table><tr><td>Age Related Macular Degeneration</td><td>Glaucoma</td><td>Pathological Myopia<td>Cataract</td><td>Normal</td></tr></table>
 
#### Chest-XRay scans are diagnosed as:
 <table><tr><td>Viral Pneumonia</td><td>Bacterial Pneumonia</td><td>COVID<td> Tubercolosis</td><td>Normal</td></tr></table><br>

- Users can also view their previously uploaded scans under <b>View Database</b>, followed by <b>View Eye Scans</b> and <b>View XRay Scans</b>. 
- The uploaded files, after being classified are saved with their predicted label appended to the file name<br> i.e, if the file you have uploaded is <b>999_right.jpg</b> and it is classified as <b>Cataract</b>, it is saved and displayed with the file name <b>999_right-Cataract.jpg</b>. This helps the user recall the predicted label of a previously uploaded scan without having to upload it again.
- For users registered as doctors, they also have the option of creating and mailing prescriptions.
## Getting Started
#### Note:  It is strongly recommened to create and use a virtual environment with Python 3.7
<b>Built With :</b> <br>Django (using Python 3.7.3), face_recognition (by ageitgey), Tensorflow, Keras and others.
<br>
```shell
git clone https://github.com/Shamayeeta/Portal.git
cd Portal
pip install -r requirements.txt
python manage.py runserver
```
The web-app should now be accessible at <a href="127.0.0.1:8000">127.0.0.1:8000</a>
## Datasets 
 For Ocular Disease Detection, I used the following dataset from Kaggle, after categorising the various images into  different classes. 
<b>Kaggle Dataset:</b><a> https://www.kaggle.com/datasets/andrewmvd/ocular-disease-recognition-odir5k</a>


 For Lung Disease Detection, I used the following datasets from Kaggle, after categorising the various images into  different classes. 
<b>Kaggle Datasets :</b>
 1. Pneumonia :<a> https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia</a>
 2. COVID : <a> https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database</a>
 3.  Normal :<a> https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset</a>
 <br>
<b>Example Dataset</b><br>
A dataset containing 5 images of each class has been uploaded to this link for testing purposes : 
<a>https://iitk-my.sharepoint.com/:f:/g/personal/shamayeeta20_iitk_ac_in/EmDCemNDsxxLpDUGfkrhUmQBj1I3fPioumAG8m6PFVmQFQ?e=oLPbM0</a>

In order to avoid confusion, the Eye scans have their label appended at the end, and the XRay scans have been named according to their labels.
