from django.db import models

class ApplicationDetails(models.Model):
    application_no = models.CharField(max_length=500,primary_key=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)  # Allow NULL values
    date_of_birth = models.DateField(null=True, blank=True)
    self_email_id = models.EmailField(max_length=255, null=True, blank=True)
    type_of_registration = models.CharField(max_length=500, null=True, blank=True)
    highest_qualification = models.CharField(max_length=500, null=True, blank=True)
    department = models.CharField(max_length=200, null=True, blank=True)
    research_supervisor = models.CharField(max_length=200, null=True, blank=True)
    register_number = models.CharField(null=False, blank=False, unique=True, max_length=250)
    area_research = models.CharField(max_length=200, null=True, blank=True)
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.application_no


class PersonalDetails(models.Model):
    application_no = models.CharField(max_length=500,  primary_key=True)
    # Permanent Address Information
    permanent_address_door_no = models.CharField(max_length=100)
    permanent_address_street_name = models.CharField(max_length=500)
    permanent_address_location = models.CharField(max_length=500)
    permanent_address_state = models.CharField(max_length=500)
    permanent_address_pincode = models.CharField(max_length=500)
    mobile_number = models.CharField(max_length=10)
    # Communication Address Information
    communication_address_door_no = models.CharField(max_length=100,null=True, blank=True)
    communication_address_street_name = models.CharField(max_length=500,null=True, blank=True)
    communication_address_location = models.CharField(max_length=500,null=True, blank=True)
    communication_address_state = models.CharField(max_length=500,null=True, blank=True)
    communication_address_pincode = models.CharField(max_length=500,null=True, blank=True)
    communication_mobile_number = models.CharField(max_length=10,null=True, blank=True)

    father_name = models.CharField(max_length=255,null=True, blank=True)
    father_occupation = models.CharField(max_length=255,null=True, blank=True)
    mother_name = models.CharField(max_length=255,null=True, blank=True)
    place_of_birth = models.CharField(max_length=255,null=True, blank=True)
    mother_tongue = models.CharField(max_length=255,null=True, blank=True)
    professional_society_membership = models.CharField(max_length=255,null=True, blank=True)
    nationality = models.CharField(max_length=255,null=True, blank=True)
    state_of_origin = models.CharField(max_length=255,null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    marital_status = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')])
    appeared_in_gate = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')])
    physically_challenged = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No')])


    def __str__(self):
        return str(self.application_no)

class User(models.Model):
    Name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    staff_id = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Department_code=models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    confirm_Password = models.CharField(max_length=100)


class BachelorEducationDetails(models.Model):
    application_no = models.CharField(max_length=500,  primary_key=True)
    bachelor_degree = models.CharField(max_length=50,null=True, blank=True)
    bachelor_discipline = models.CharField(max_length=100,null=True, blank=True)
    bachelor_university = models.CharField(max_length=200,null=True, blank=True)
    bachelor_year = models.IntegerField(null=True, blank=True)
    bachelor_cgpa = models.DecimalField(max_digits=4, decimal_places=2,null=True, blank=True)
    bachelor_branch = models.CharField(max_length=100,null=True, blank=True)
    bachelor_class = models.CharField(max_length=50,null=True, blank=True)
    bachelor_aggregate = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return str(self.application_no)


class MasterEducationDetails(models.Model):
    application_no = models.CharField(max_length=500,  primary_key=True)
    master_degree = models.CharField(max_length=10, null=True, blank=True)
    master_discipline = models.CharField(max_length=100, null=True, blank=True)
    master_university = models.CharField(max_length=100, null=True, blank=True)
    master_year = models.PositiveIntegerField(null=True, blank=True)
    master_cgpa = models.FloatField(null=True, blank=True)
    master_branch = models.CharField(max_length=100, null=True, blank=True)
    master_class = models.CharField(max_length=100, null=True, blank=True)
    master_aggregate = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.application_no)


class DCMember(models.Model):
    application_no = models.CharField(max_length=500,  primary_key=True)
    name1 = models.CharField(max_length=100, null=True, blank=True)
    designation_and_department1 = models.CharField(max_length=100, null=True, blank=True)
    college_organization_address1 = models.CharField(max_length=100, null=True, blank=True)
    area_of_research1 = models.CharField(max_length=100, null=True, blank=True)
    name2 = models.CharField(max_length=100, null=True, blank=True)
    designation_and_department2 = models.CharField(max_length=100, null=True, blank=True)
    college_organization_address2 = models.CharField(max_length=100, null=True, blank=True)
    area_of_research2 = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.application_no)


class GuideDetails(models.Model):
    application_no = models.CharField(max_length=500,  primary_key=True)
    guide_name = models.CharField(max_length=255,null=True, blank=True)
    guide_designation_and_department = models.CharField(max_length=255,null=True, blank=True)
    guide_recognition_number = models.CharField(max_length=50,null=True, blank=True)
    guide_college_organization_address = models.CharField(max_length=500,null=True, blank=True)

    # Fields for Co-Guide
    co_guide_name = models.CharField(max_length=255, blank=True, null=True)
    co_guide_designation_and_department = models.CharField(max_length=255, blank=True, null=True)
    co_guide_recognition_number = models.CharField(max_length=50, blank=True, null=True)
    co_guide_college_organization_address = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.guide_name


class SchoolDetails(models.Model):
    application_no = models.CharField(max_length=500,  primary_key=True)
    school_name_10th = models.CharField(max_length=255,null=True, blank=True)
    year_of_passing_10th = models.IntegerField(null=True, blank=True)
    year_of_passing_10th = models.IntegerField(null=True, blank=True)
    year_of_passing_10th = models.IntegerField(null=True, blank=True)
    std_studied_in_10th = models.CharField(max_length=255,null=True, blank=True)
    medium_of_study_10th = models.CharField(max_length=255,null=True, blank=True)
    school_type_10th = models.CharField(max_length=255,null=True, blank=True)
    total_mark_10th = models.IntegerField(null=True, blank=True)
    higher_studies = models.CharField(max_length=255,blank=True, null=True)

    # 12th Details (optional)
    school_name_12th = models.CharField(max_length=255, blank=True, null=True)
    year_of_passing_12th = models.IntegerField(blank=True,null=True)
    std_studied_in_12th = models.CharField(max_length=255, blank=True, null=True)
    medium_of_study_12th = models.CharField(max_length=255, blank=True, null=True)
    school_type_12th = models.CharField(max_length=255, blank=True, null=True)
    total_mark_12th = models.IntegerField(blank=True, null=True)

    # Diploma Details (optional)
    polytechnic_name = models.CharField(max_length=255, blank=True, null=True)
    year_of_passing_diploma = models.IntegerField(blank=True,null=True)
    studied_in_polytechnic = models.CharField(max_length=255, blank=True, null=True)
    medium_of_study_polytechnic = models.CharField(max_length=255, blank=True, null=True)
    total_mark_polytechnic = models.IntegerField(blank=True, null=True)
    total_percentage_polytechnic = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"School Details for {self.school_name_10th}"

class Experience_Details(models.Model):
    application_no = models.CharField(max_length=500,  primary_key=True)
    professional_experience1 = models.CharField(max_length=255)
    name_of_the_organization1 = models.CharField(max_length=255)
    start_year1 = models.IntegerField()
    to1 = models.IntegerField()
    designation1 = models.CharField(max_length=255)
    nature_of_work1 = models.CharField(max_length=255)

    professional_experience2 = models.CharField(max_length=255, blank=True, null=True)
    name_of_the_organization2 = models.CharField(max_length=255, blank=True, null=True)
    start_year2 = models.IntegerField( blank=True, null=True)
    to2 = models.IntegerField( blank=True, null=True)
    designation2 = models.CharField(max_length=255, blank=True, null=True)
    nature_of_work2 = models.CharField(max_length=255, blank=True, null=True)

    professional_experience3 = models.CharField(max_length=255, blank=True, null=True)
    name_of_the_organization3 = models.CharField(max_length=255, blank=True, null=True)
    start_year3 = models.IntegerField( blank=True, null=True)
    to3 = models.IntegerField( blank=True, null=True)
    designation3 = models.CharField(max_length=255, blank=True, null=True)
    nature_of_work3 = models.CharField(max_length=255, blank=True, null=True)

class approver(models.Model):
    application_no = models.CharField(max_length=500,  primary_key=True)

    coordinate_approval=models.CharField(max_length=200,null=True,blank=True)
    hod_approval=models.CharField(max_length=200,null=True,blank=True)
    vp_approval=models.CharField(max_length=200,null=True,blank=True)
    principal_approval=models.CharField(max_length=200,null=True,blank=True)


# models.py

class UploadedImage(models.Model):
    application = models.ForeignKey(ApplicationDetails, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.application.register_number} - {self.image.name}"


