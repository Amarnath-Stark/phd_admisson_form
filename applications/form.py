from django import forms #type:ignore
from applications.models import ApplicationDetails,SchoolDetails,PersonalDetails,User,BachelorEducationDetails,MasterEducationDetails,DCMember,GuideDetails,Experience_Details



class Personal_Detail(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = [
            'permanent_address_door_no',
            'permanent_address_street_name',
            'permanent_address_location',
            'permanent_address_state',
            'permanent_address_pincode',
            'mobile_number',
            'communication_address_door_no',
            'communication_address_street_name',
            'communication_address_location',
            'communication_address_state',
            'communication_address_pincode',
            'communication_mobile_number',
            'father_name',
            'father_occupation',
            'mother_name',
            'place_of_birth',
            'mother_tongue',
            'professional_society_membership',
            'nationality',
            'state_of_origin',
            'gender',
            'marital_status',
            'appeared_in_gate',
            'physically_challenged'
        ]

class userform(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'Name', 'user_name', 'staff_id', 'Department', 'email','Department_code',
            'role', 'Password', 'confirm_Password'
 ]
        exclude=['Department_code']

class Index(forms.ModelForm):
    class Meta:
        model = ApplicationDetails
        fields=['department','register_number','research_supervisor','area_research','name','age','date_of_birth','self_email_id','type_of_registration','highest_qualification','approval']


class BachelorEducationForm(forms.ModelForm):
    class Meta:
        model = BachelorEducationDetails
        fields = [
            'bachelor_degree', 'bachelor_discipline', 'bachelor_university',
            'bachelor_year', 'bachelor_cgpa', 
            'bachelor_class',
            'bachelor_aggregate'
        ]



class Master(forms.ModelForm):
    class Meta:
        model = MasterEducationDetails
        fields = [
            'master_degree',
            'master_discipline',
            'master_university',
            'master_year',
            'master_cgpa',
            'master_class',
            'master_aggregate'
        ]
class DCMemberForm(forms.ModelForm):
    class Meta:
        model = DCMember
        fields = [
            'name1',
            'designation_and_department1',
            'college_organization_address1',
            'area_of_research1',
            'name2',
            'designation_and_department2',
            'college_organization_address2',
            'area_of_research2'
        ]


class GuideDetailsForm(forms.ModelForm):
    class Meta:
        model = GuideDetails
        fields = [
            'guide_name',
            'guide_designation_and_department',
            'guide_recognition_number',
            'guide_college_organization_address',
            'co_guide_name',
            'co_guide_designation_and_department',
            'co_guide_recognition_number',
            'co_guide_college_organization_address',
        ]


class SchoolDetailsForm(forms.ModelForm):
    class Meta:
        model = SchoolDetails
        fields = [
            'school_name_10th',
            'year_of_passing_10th',
            'std_studied_in_10th',
            'medium_of_study_10th',
            'school_type_10th',
            'total_mark_10th',
            'higher_studies',
            'school_name_12th',
            'year_of_passing_12th',
            'std_studied_in_12th',
            'medium_of_study_12th',
            'school_type_12th',
            'total_mark_12th',
            'polytechnic_name',
            'year_of_passing_diploma',
            'studied_in_polytechnic',
            'medium_of_study_polytechnic',
            'total_mark_polytechnic',
            'total_percentage_polytechnic',
        ]

class ProfessionalExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience_Details
        fields = [
            "professional_experience1",
            "name_of_the_organization1",
            "start_year1",
            "to1",
            "designation1",
            "nature_of_work1",
            "professional_experience2",
            "name_of_the_organization2",
            "start_year2",
            "to2",
            "designation2",
            "nature_of_work2",
            "professional_experience3",
            "name_of_the_organization3",
            "start_year3",
            "to3",
            "designation3",
            "nature_of_work3",
        ]



from django import forms
from .models import UploadedImage

class UploadImagesForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']

    def __init__(self, *args, **kwargs):
        self.application = kwargs.pop('application', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.application:
            instance.application = self.application
        if commit:
            instance.save()
        return instance


