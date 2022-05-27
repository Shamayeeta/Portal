from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
import face_recognition
from .models import *

class FaceIdAuthBackend(ModelBackend):
    def authenticate(self, username=None, password=None, face_id=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if check_password(password,user.password):
                # print("pass")
                # img = Image.open(user.userfaceimage.image)
                # img.show()
                if self.check_face_id(face_id=user.userfaceimage.image, uploaded_face_id=face_id):
                    return user                                                                                   
                                                                                    
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            User().set_password(password)

    def check_face_id(self, face_id=None, uploaded_face_id=None):
        known_image= face_recognition.load_image_file(face_id)
        # sami_image= face_recognition.load_image_file(r"C:\\Users\\TITIR\\Engage\\Loginapp\\media\\content\\yuka\WIN_20220522_00_33_10_Pro.jpg")
        # known_image = face_recognition.load_image_file(face_id)
        unknown_image = face_recognition.load_image_file(uploaded_face_id)
        # print("ki",known_image,"ui",unknown_image)
        # img = Image.open(face_id)
        # img.show() 
        # img = Image.open(uploaded_face_id)
        # img.show() 
        face_locations = face_recognition.face_locations(known_image,model="cnn")
        unknown_face_locations = face_recognition.face_locations(unknown_image,model="cnn")
        # sami_Loc = face_recognition.face_locations(sami_image)
        # print("known location",face_locations)
        # print("unknown location",unknown_face_locations)
        # print("array",face_recognition.face_encodings(known_image,known_face_locations=face_locations))
        known_encoding = face_recognition.face_encodings(known_image,known_face_locations=face_locations)[0]
        # print("ke",known_encoding)
        unknown_encoding = face_recognition.face_encodings(unknown_image,known_face_locations=unknown_face_locations)[0]
        # print("ue",unknown_encoding)

        results = face_recognition.compare_faces([known_encoding], unknown_encoding)

        if results[0]==True:
            return True
        
        return False