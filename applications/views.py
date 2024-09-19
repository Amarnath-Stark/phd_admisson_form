import re
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import os
from django.core.paginator import Paginator
from django.conf import settings
from applications.form import userform,SchoolDetailsForm,Index,Personal_Detail,BachelorEducationForm,Master,DCMemberForm,GuideDetailsForm,ProfessionalExperienceForm
from applications.models import User,PersonalDetails,BachelorEducationDetails,MasterEducationDetails,DCMember,GuideDetails,Experience_Details,ApplicationDetails,SchoolDetails




from django.contrib import messages
import pandas as pd
from num2words import num2words
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
dept_code={"ARTIFICIAL INTELLIGENCE AND DATA SCIENCE":"AD",
                "CIVIL ENGINEERING":"CE",
                "COMPUTER SCIENCE AND BUSINESS SYSTEM":"CB",
                "COMPUTER SCIENCE AND ENGINEERING":"CSE",
                "ELECRICAL AND ELECTRONICS ENGINEERING":"EEE",
                "ELECTRONICS AND COMMUNICATION ENGINEERING":"ECE",
                "INFORMATION TECHNOLOGY":"IT",
                "MECHANICAL ENGINEERING":"MECH",}
def generate_unique_admission_number():
    current_year_last_two_digits = datetime.now().strftime("%y")
    
    # Get the last admission number to ensure sequential numbering
    last_admission = ApplicationDetails.objects.order_by('-application_no').first()
    
    if last_admission:
        # Extract the numeric part and increment
        last_number = int(last_admission.application_no.split('-')[-1])
        new_number = last_number + 1
    else:
        new_number = 1

    # Format the new number to be 3 digits long
    formatted_number = f"{new_number:03}"

    # Create the admission number
    admission_number = f"{current_year_last_two_digits}-{formatted_number}"

    print(admission_number)  # For debugging purposes
    return admission_number


def index(request):
    user_data = request.session.get('user_data', {})
    
    if request.method == 'POST':
        form = Index(request.POST)
        if form.is_valid():
            # Generate a unique admission number
            admissionno = generate_unique_admission_number()

            # Store form data in the session if needed
            request.session['index'] = form.cleaned_data
            request.session['index']['date_of_birth'] = form.cleaned_data['date_of_birth'].isoformat()
            
            # Redirect to the personal page
            return redirect('personal')
        else:
            print(form.errors)  # Print form validation errors to debug
    else:
        form = Index()

    context = {
        'form': form,
        'name': user_data.get('name', 'Guest'),
        'Department': user_data.get('Department', 'Not Assigned'),
        'role': user_data.get('role', 'Not Assigned'),
    }

    return render(request, 'application/index.html', context)


def personal(request):
    user_data = request.session.get('user_data', {})
    if request.method == 'POST':
        form = Personal_Detail(request.POST)
        if form.is_valid():
 

            # Optional: If you need to store any information in the session
            request.session['personal_data'] = form.cleaned_data
            
            # Redirect to the next form or page
            return redirect('School_form')  # Replace with the actual URL name for the next page
        else:
            # Handle form errors
            messages.error(request, 'Please correct the errors below.')
            print("Form errors: ", form.errors)  # Debugging: will appear in server logs

    else:
        form = Personal_Detail()
    context = {
        'form' : form,
        'name' : user_data.get('name'),
        'department' : user_data.get('Department'),
        'role' : user_data.get('role')
    }
    return render(request, 'application/personal.html', context)

def School_form(request):
    user_data = request.session.get('user_data', {})
    if request.method == 'POST':
        form = SchoolDetailsForm(request.POST)
        if form.is_valid():

            # Optional: If you need to store any information in the session
            request.session['School_data'] = form.cleaned_data
            highest_qualification = request.session.get('highest_qualification')
            print("Highest Qualification:", highest_qualification)  # Debugging line
            if highest_qualification == "Bachelor's":
                return redirect('bachelor')
            else:
                return redirect('Masterform')

        else:
            # Handle form errors
            messages.error(request, 'Please correct the errors below.')
            print("Form errors: ", form.errors)  # Debugging: will appear in server logs

    else:
        form = Personal_Detail()
    context = {
        'form' : form,
        'name' : user_data.get('name'),
        'department' : user_data.get('Department'),
        'role' : user_data.get('role')

    }
    return render(request, 'application/School_form.html', {'form': form})

def bachelor(request):
    user_data = request.session.get('user_data', {})
    if request.method == 'POST':
        form = BachelorEducationForm(request.POST)
        if form.is_valid():
     

            # Optional: If you need to store any information in the session
            request.session['bachelor_data'] = form.cleaned_data

            # Redirect to the next form or page
            return redirect('experience')  # Replace with the actual URL name for the next page
        else:
            # Handle form errors
            messages.error(request, 'Please correct the errors below.')
            print("Form errors: ", form.errors)  # Debugging: will appear in server logs

    else:
        form = BachelorEducationForm()

    context = {
        'form' : form,
        'name' : user_data.get('name'),
        'department' : user_data.get('Department'),
        'role' : user_data.get('role')

    }
    return render(request, 'application/Master.html', {'form': form})


def Masterform(request):
    user_data = request.session.get('user_data', {})
    if request.method == 'POST':
        form = Master(request.POST)
        if form.is_valid():
            # Save the form data to the database

            # Optional: If you need to store any information in the session
            request.session['master_data'] = form.cleaned_data

            # Redirect to the next form or page
            return redirect('experience')  # Replace with the actual URL name for the next page
        else:
            # Handle form errors
            messages.error(request, 'Please correct the errors below.')
            print("Form errors: ", form.errors)  # Debugging: will appear in server logs

    else:
        form = Master()
    context = {
        'form' : form,
        'name' : user_data.get('name'),
        'department' : user_data.get('Department'),
        'role' : user_data.get('role')

    }
    return render(request, 'application/Master.html', {'form': form})


def experience(request):
    user_data = request.session.get('user_data', {})
    if request.method == 'POST':
        form = ProfessionalExperienceForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            # experience_detail_instance = form.save()

            # Optional: If you need to store any information in the session
            request.session['experience_data'] = form.cleaned_data

            # Redirect to the next form or page
            return redirect('guide_view')  # Replace with the actual URL name for the next page
        else:
            # Handle form errors
            messages.error(request, 'Please correct the errors below.')
            print("Form errors: ", form.errors)  # Debugging: will appear in server logs

    else:
        form = ProfessionalExperienceForm()
    context = {
        'form' : form,
        'name' : user_data.get('name'),
        'department' : user_data.get('Department'),
        'role' : user_data.get('role')

    }
    return render(request, 'application/experience.html', {'form': form})


def guide_view(request):
    user_data = request.session.get('user_data', {})
    if request.method == 'POST':
        form = GuideDetailsForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            # guide_detail_instance = form.save()

            # Optional: If you need to store any information in the session
            request.session['guide_data'] = form.cleaned_data

            # Redirect to the next form or page
            return redirect('dc_member_view')  # Replace with the actual URL name for the next page
        else:
            # Handle form errors
            messages.error(request, 'Please correct the errors below.')
            print("Form errors: ", form.errors)  # Debugging: will appear in server logs

    else:
        form = GuideDetailsForm()
    context = {
        'form' : form,
        'name' : user_data.get('name'),
        'department' : user_data.get('Department'),
        'role' : user_data.get('role')

    }
    return render(request, 'application/guide.html', {'form': form})


def dc_member_view(request):
    user_data = request.session.get('user_data', {})
    index = request.session.get('index', {})
    personal_data = request.session.get('personal_data', {})
    School_data = request.session.get('School_data', {})
    bachelor_data = request.session.get('bachelor_data', {})
    master_data = request.session.get('master_data', {})
    experience_data = request.session.get('experience_data', {})
    guide_data = request.session.get('guide_data', {})
    
    print(index,personal_data,School_data,bachelor_data,master_data,experience_data,guide_data)

    if request.method == 'POST':
        form = DCMemberForm(request.POST)
        if form.is_valid():
            # Save the form data to the database

            # Optional: If you need to store any information in the session
            request.session['dc_member_data'] = form.cleaned_data
            dc_member_data = request.session.get('dc_member_data', {})
            ApplicationDetails.objects.create(**index, application_no=generate_unique_admission_number())
            PersonalDetails.objects.create(**personal_data, application_no=generate_unique_admission_number())
            BachelorEducationDetails.objects.create(**bachelor_data, application_no=generate_unique_admission_number())
            MasterEducationDetails.objects.create(**master_data, application_no=generate_unique_admission_number())
            SchoolDetails.objects.create(**School_data, application_no=generate_unique_admission_number())
            Experience_Details.objects.create(**experience_data, application_no=generate_unique_admission_number())
            GuideDetails.objects.create(**guide_data, application_no=generate_unique_admission_number())
            DCMember.objects.create(**dc_member_data, application_no=generate_unique_admission_number())

            
            print(dc_member_data)

            # Redirect to the next form or page
            return redirect('display_qrcode')  # Replace with the actual URL name for the next page
        else:
            # Handle form errors
            messages.error(request, 'Please correct the errors below.')
            print("Form errors: ", form.errors)  # Debugging: will appear in server logs

    else:
        form = DCMemberForm()
    context = {
        'form' : form,
        'name' : user_data.get('name'),
        'department' : user_data.get('Department'),
        'role' : user_data.get('role')

    }
    return render(request, 'application/Dcmember.html', {'form': form})



def approval_view(request):
    # Check if the request is a POST request to handle form submission
    user_data=request.session.get('user_data', {})
    staff_role=user_data['role']
    user_dept=user_data['Department']
    print(staff_role,user_dept,"DJFISAHFKUASHF")

    

    # if request.method == 'POST':
    #     # Get the application number from the form data
    #     application_no = request.POST.get('application_no')
    #     print(application_no,"workingbcsjafjdashfjhdasjf")
    #     application = get_object_or_404(approver, application_no=application_no)

    #     if staff_role=="Coordinator":
    #         application.coordinate_approval = "Approved"
    #         application.save()
    #     if staff_role=="HOD":
    #         application.hod_approval="Approved"
    #         application.save()
    #     return redirect('approval_view')

    selected_department = request.GET.get('department', None) 
    if selected_department: 
        application = ApplicationDetails.objects.filter(department=selected_department)
        if staff_role == "HOD":
            doc={'data':[],'message':[]}
            for app in application:
                documnet=approver.objects.filter(application_no=app.application_no,hod_approval="Pending",vp_approval="Pending",principal_approval="Pending").exclude(coordinate_approval="Pending").first()
            
                if documnet:
                    doc_data=ApplicationDetails.objects.get(application_no=documnet.application_no)
                    if user_dept==doc_data.department:
                        print("rghfgfgfgfgf")
                        doc['data'].append(doc_data)
                        doc['message'].append(doc_data.application_no)
                    else:
                        doc['data'].append(app)
                        doc['message'].append(None)
                else:
                        doc['data'].append(app)
                        doc['message'].append(None)
            applications=doc
        if staff_role=="Principal":
            doc={'data':[],'message':[]}
            for app in application:
                documnet=approver.objects.filter(application_no=app.application_no,principal_approval="Pending").exclude(vp_approval="Pending",hod_approval="Pending",coordinate_approval="Pending").first()
                if documnet:
                    doc_data=get_object_or_404(ApplicationDetails,application_no=documnet.application_no)
                
                    doc['data'].append(doc_data)
                    doc['message'].append(doc_data.application_no)
                else:
                    doc['data'].append(app)
                    doc['message'].append(None)

            applications=doc
                
        if staff_role=="vice_principal":
            doc={'data':[],'message':[]}
            for app in application:
                documnet=approver.objects.filter(application_no=app.application_no,vp_approval="Pending").exclude(hod_approval="Pending",coordinate_approval="Pending").first()
                if documnet:
                    doc_data=get_object_or_404(ApplicationDetails,application_no=documnet.application_no)
                
                    doc['data'].append(doc_data)
                    doc['message'].append(doc_data.application_no)
                else:
                    doc['data'].append(app)
                    doc['message'].append(None)
            applications=doc

        if staff_role =="Coordinator":
            doc={'data':[],'message':[]}
            for app in application:
                print(app.application_no)
                documnet=approver.objects.filter(application_no=app.application_no,coordinate_approval="Pending").first()
                print(documnet,"fdshfsagfjgs")
        
                if documnet:
                    doc_data=get_object_or_404(ApplicationDetails,application_no=documnet.application_no)
                
                    doc['data'].append(doc_data)
                    doc['message'].append(doc_data.application_no)
                else:
                    doc['data'].append(app)
                    doc['message'].append(None)
            # else:
            #     for app in application:
            #         doc.append()\
            applications=doc
            print(doc,"fhjsadjskafjks")
    else:
        applications=None
            

    context = {
        'applications': applications,
        'selected_department': selected_department,
        'role':staff_role,
        'dept':user_dept,

    }
    print(applications,"hfdsjkhfjkshfkhd")

    return render(request, 'application/Approve.html', context)  
def approving(request):
    print("fdslhfksjahdfjk")
    user_data=request.session.get('user_data', {})
    staff_role=user_data['role']
    user_dept=user_data['Department']
    appliction_no= request.GET.get("application_no")
    print(appliction_no,"fdshfkjasfkjg")
    data=get_object_or_404(approver,application_no=appliction_no)
    
    if data:    
        if staff_role=="Coordinator":
            data.coordinate_approval="Approved"
            data.save()
        if staff_role=="HOD":
            print("dsagdasgfhsadfh")
            data.hod_approval="Approved"
            data.save()
        if staff_role=="vice_principal":
            print("dsagdasgfhsadfh")
            data.vp_approval="Approved"
            data.save()
        if staff_role=="Principal":
            print("dsagdasgfhsadfh")
            data.principal_approval="Approved"
            data.save()
        return redirect('approval')
        
    

def encrypt_password(raw_password):
    # Implement your password encryption algorithm (e.g., using hashlib)
    import hashlib
    return hashlib.sha256(raw_password.encode()).hexdigest()

def signup(request):
    if request.method == 'POST':
        form = userform(request.POST)
        if form.is_valid():
            password = form.cleaned_data['Password']
            confirm_password = form.cleaned_data['confirm_Password']

            if password == confirm_password:
                encrypted_password = encrypt_password(password)

                # Save the encrypted password to your user model
                user = form.save(commit=False)  # Don't save the form yet
                user.Password = encrypted_password
                user.confirm_Password = encrypted_password

                user.save()

                # Redirect to a success page or login page
                return redirect('login')
            else:
                # Passwords don't match, return an error
                form.add_error('confirm_password', 'Passwords do not match')
                return render(request, "Auth/signup.html", {'form': form})
        else:
            return render(request, "application/error.html", {'form': form})
    else:
        form = userform()

    return render(request, "auth/signup.html", {'form': form})


def login(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        password = request.POST.get('password')
        print(staff_id,password)
        # Fetch the user from the database
        try:
            user = User.objects.get(staff_id=staff_id)
        except User.DoesNotExist:
            # User not found, show an error message
            error_message = 'Invalid staff_id or password.'
            return render(request, "auth/login.html", {'error_message': error_message})

        # Check if the password matches
        if user.Password == encrypt_password(password):
            name=user.Name
            # Passwords match, log in the user
            # Set session variables or use Django's login system as needed
            request.session['user_id'] = user.id
            user = get_object_or_404(User, staff_id=staff_id)
            user_dict = {
            'id': user.id,
            'staff_id': user.staff_id,
            'name': user.Name,
            'user_name': user.user_name,
            'Department' : user.Department,
            'email' : user.email,
            'role' : user.role,
            'Password' : user.Password,
            'confirm_Password' : user.confirm_Password           }

            request.session['user_data'] = user_dict
            return redirect('index')
        else:
            # Passwords don't match, show an error message
            error_message = 'Invalid username or password.'
            return render(request, "Auth/login.html", {'error_message': error_message})

    return render(request, "Auth/login.html")
def logout(request):

    print('logout function called')
    auth_logout(request)
    messages.success(request,'You were logged out')
    request.session.flush()  # Flush all session data
    return render(request, "auth/login.html")

from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image
from io import BytesIO  # Add this import statement
import os

def generate_pdf(request):
    register_number=request.GET.get('reg_no')
    print(register_number,"sahfkjshfkjdasghfjg")
    buffer = BytesIO()
    Register = ApplicationDetails.objects.get(register_number=register_number)
    application_no = Register.application_no
    print(application_no)

    # Fetch PersonalDetails based on the application_no
    personal = PersonalDetails.objects.filter(application_no=application_no).first()
    bachelor = BachelorEducationDetails.objects.filter(application_no=application_no).first()
    master = MasterEducationDetails.objects.filter(application_no=application_no).first()
    dc = DCMember.objects.filter(application_no=application_no).first()
    guide = GuideDetails.objects.filter(application_no=application_no).first()
    school = SchoolDetails.objects.filter(application_no=application_no).first()
    experience = Experience_Details.objects.filter(application_no=application_no).filter()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=A4)

    # Draw the content on the PDF
    width, height = A4

    # Title
    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, height - 30, "APPLICATION FOR ADMISSION TO Ph.D. PROGRAMMES")
    
    # Reference and Application Numbers
    p.setFont("Helvetica-Bold", 10)
    p.drawString(50, height - 117, "Reference No.:")
    p.line(120 , height - 117 , 200, height - 117)
    p.drawString(350, height - 117, "Application No.:")
    p.line(420 , height - 117 , 570, height - 117)
    p.drawString(430, height - 117 , Register.application_no)
    # Research Department Information
    p.drawString(50, height - 130, "Name of the Research Department:")
    p.line(220 , height - 130 , 340, height - 130)
    p.drawString(220, height-130 ,Register.department)
    p.drawString(350, height - 130, "AU Research centre recognition no:")
    
    p.drawString(50, height - 143, "Name and Designation of the research supervisor at RIT:")
    p.line(300 , height - 145 , 450, height - 145)
    p.drawString(50, height - 155, "Area of Research: ")
    p.line(130 , height - 157 , 300, height - 157)
    p.drawString(350, height - 155, "Ph.D. Register No: ")
    
    p.rect(40, height - 305, 530, 140)


    # Applicant Information
    p.setFont("Helvetica-Bold", 10)
    p.drawString(50, height - 180, " Name:")
    p.line(100 , height - 180 , 350, height - 180)
    p.drawString(300, height - 195, " Age:")
    p.line(330 , height - 180 , 450, height - 180)
    p.drawString(50, height - 195, " Date of Birth:")
    p.rect(120, height - 200, 150, 15)
    
    p.setFont("Helvetica-Bold", 10)
    p.drawString(50, height - 215, " Address for communication:")
    p.line(50 , height - 230 , 250, height - 230)
    p.line(50 , height - 245 , 250, height - 245)
    p.drawString(50, height - 260, " Pincode:")
    p.rect(100, height - 265, 150, 15)
    p.drawString(50, height - 275, " Mobile No:")
    p.line(100 , height - 280 , 250, height - 280)
    p.drawString(50, height - 290, " Mail id:")
    p.line(85 , height - 295 , 250, height - 295)
    
    
    p.drawString(260, height - 215, " Permanent Address:")
    p.line(260 , height - 230 , 450, height - 230)
    p.line(260 , height - 245 , 450, height - 245)
    p.drawString(260, height - 260, " Pincode:")
    p.rect(310, height - 265, 140, 15)
    p.drawString(260, height - 275, " Mobile No:")
    p.line(310 , height - 280 , 450, height - 280)
    p.drawString(260, height - 290, " Mail id:")
    p.line(295 , height - 295 , 450, height - 295)


    p.rect(40, height - 330, 530, 25)
    p.drawString(50, height - 320, " Types of Registration:")
    p.rect(40, height - 465, 530, 110)
    
    p.drawString(50, height - 350, " School Details")

    p.drawString(230, height - 370, " SSLC:")
    p.drawString(440, height - 370, " HSC:")
    p.line(40 , height - 375 , 570, height - 375)
    p.line(40 , height - 390 , 570, height - 390)
    p.line(40 , height - 405 , 570, height - 405)
    p.line(40 , height - 420 , 570, height - 420)
    p.line(40 , height - 435 , 570, height - 435)
    p.line(40 , height - 450 , 570, height - 450)
    
    p.line(130 , height - 355 , 130, height - 465)
    p.line(350 , height - 355 , 350, height - 465)
    


    p.drawString(50 ,height - 385, " School" )
    
    p.drawString(50 ,height - 400, " Year of passing" )
    
    p.drawString(50 ,height - 415, " Studied In" )
    
    p.drawString(50 ,height - 430, " Medium of Study" )
    
    p.drawString(50 ,height - 445, " Type of Study" )
    
    p.drawString(50 ,height - 460, " Total Mark" )
    
    
    
    p.drawString(50, height - 490, " Higher Studies")
    p.rect(40, height - 635, 530, 140)

    p.drawString(230, height - 510, " Bachelors")
    p.drawString(440, height - 510, " Masters")
    p.line(40 , height - 515 , 570, height - 515)
    p.line(40 , height - 535 , 570, height - 535)
    p.line(40 , height - 555 , 570, height - 555)
    p.line(40 , height - 575 , 570, height - 575)
    p.line(40 , height - 595 , 570, height - 595)
    p.line(40 , height - 615 , 570, height - 615)
    
    p.line(130 , height - 635 , 130, height - 495)
    p.line(350 , height - 635 , 350, height - 495)
    
    p.drawString(50 ,height - 530, " Degree" )
    
    p.drawString(50 ,height - 550, " Branch" )
    
    p.drawString(50 ,height - 570, " University" )
    
    p.drawString(50 ,height - 590, " Year Of Passing" )
    
    p.drawString(50 ,height - 610, " CGPA" )
    
    p.drawString(50 ,height - 630, " Class" )
    
    p.drawString(50, height - 700, " Professional Experience")
    p.rect(40, height - 800, 530, 90)
    p.line(100 , height - 710 , 100, height - 800)
    p.line(250 , height - 710 , 250, height - 800)
    p.line(350 , height - 710 , 350, height - 800)
    p.line(480 , height - 710 , 480, height - 800)
    p.line(415 , height - 725 , 415, height - 800)
    
    p.line(40 , height - 740 , 570, height - 740)
    p.line(40 , height - 760 , 570, height - 760)
    p.line(40 , height - 780 , 570, height - 780)
    p.line(350 , height - 725 , 480, height - 725)

    p.drawString(60 ,height - 730, " Area" )
    p.drawString(140 ,height - 730, " Organization" )
    p.drawString(270 ,height - 730, " Designation" )
    p.drawString(395 ,height - 720, " Period" )
    p.drawString(510 ,height - 730, " Nature" )
    p.drawString(365 ,height - 735, " From" )
    p.drawString(435 ,height - 735, " To" )





    
    # Finalize the PDF
    p.showPage()
    
    p.setFont("Helvetica-Bold", 10)
    p.rect(30 , height - 530 , 540 , 500)
    p.drawString(50, height - 70, "a). Father's /")
    p.drawString(60, height - 80, "Husband Name")
    p.drawString(170,height-73 , personal.father_name)
    
    p.setFont("Helvetica-Bold", 10)
    p.drawString(50, height - 100, "b). Father's / Husband")
    p.drawString(60, height - 110, "Occupation")
    p.drawString(170,height-103 , personal.father_occupation)
    
    p.drawString(50, height - 130, "c). Mother's Name")
    p.drawString(170,height-123,personal.mother_name)
    
    p.drawString(50, height - 150, "d). Place of Brith")
    p.drawString(170,height-143,personal.place_of_birth)
    
    p.drawString(50, height - 170, "e). Mother Tongue")
    p.drawString(170,height-163, personal.mother_tongue)
    
    p.drawString(60, height - 190, " Professional")
    p.drawString(50, height - 200, "f). Society")
    p.drawString(60, height - 210, " Membership, if any")
    p.drawString(170,height-193,personal.mother_tongue)


    p.drawString(350, height - 70, "g). Nationality")
    p.drawString(450,height-73,personal.nationality)
    
    p.drawString(350, height - 100, "h). State to which the")
    p.drawString(360, height - 110, " applicant Belongs")
    p.drawString(452,height-108,personal.state_of_origin)

    p.drawString(350, height - 130, "i). Maritial Status")
    p.drawString(450,height-128,personal.marital_status)

    p.drawString(350, height - 150, "j). Gender:")
    p.drawString(450,height-148,personal.gender)

    p.drawString(350, height - 170, "k). Whethere appeared in GATE:")
    p.drawString(505,height-170,personal.appeared_in_gate)

    p.drawString(350, height - 190, "l). Whethere Physically Challenged:")
    p.drawString(520,height-190,personal.physically_challenged)

    p.line(170 , height - 75 , 330, height - 75)
    p.line(170 , height - 105 , 330, height - 105)
    p.line(170 , height - 125 , 330, height - 125)
    p.line(170 , height - 145 , 330, height - 145)
    p.line(170 , height - 165 , 330, height - 165)
    p.line(170 , height - 195 , 330, height - 195)
    p.line(450 , height - 75 , 560, height - 75)
    p.line(450 , height - 110 , 560, height - 110)
    p.line(450 , height - 130 , 560, height - 130)
    p.line(450 , height - 150 , 560, height - 150)
    
    p.drawString(50, height - 230, "Consent of the Supervisor / Joint Supervisor")
    p.drawString(50, height - 400, "Details of DC Members")



    p.rect(40, height - 385, 520, 145)
    p.line(40 , height - 255 , 560, height - 255)
    p.line(40 , height - 270 , 560, height - 270)
    p.line(40 , height - 285 , 560, height - 285)
    p.line(40 , height - 310 , 560, height - 310)
    p.line(40 , height - 325 , 560, height - 325)
    p.line(40 , height - 340 , 560, height - 340)
    p.line(40 , height - 370 , 560, height - 370)
    p.line(180 , height - 240 , 180, height - 385)
    p.line(380 , height - 240 , 380, height - 385)

    p.drawString(70, height - 250, "Particulars")
    p.drawString(230, height - 250, "Research Guide")
    p.drawString(430, height - 250, "Co-Guide")

    p.setFont("Helvetica", 10)

    p.drawString(50, height - 265, "Name")
    p.drawString(190,height-266,guide.guide_name)
    p.drawString(400,height-266,guide.co_guide_name)
    p.drawString(50, height - 280, "Designation")
    p.drawString(190,height-281,guide.guide_designation_and_department[:27])
    
    p.drawString(190,height-291,guide.guide_designation_and_department[27:])
    p.drawString(400,height-281,guide.co_guide_designation_and_department[:27])
    p.drawString(400,height-291,guide.co_guide_designation_and_department[27:])
    p.drawString(50, height - 295, "Anna University Research")
   
    p.drawString(50, height - 305, "Recongnition number")
    p.drawString(190,height-301,guide.guide_recognition_number)
    p.drawString(400,height-301,guide.co_guide_recognition_number)
    p.drawString(50, height - 320, "College/Organizaton Address")
    p.drawString(190,height-321,guide.guide_college_organization_address)
    p.drawString(400,height-321,guide.co_guide_college_organization_address)
    p.drawString(50, height - 335, "Area of Research")
    
    p.drawString(50, height - 350, "Number of Research")
    
    p.drawString(50, height - 365, "Scholars")
    
    p.drawString(50, height - 380, "Signature")
   

    p.setFont("Helvetica-Bold", 10)
    
    
    p.rect(40, height - 510, 520, 100)
    p.line(40 , height - 430 , 560, height - 430)
    p.line(40 , height - 450 , 560, height - 450)
    p.line(40 , height - 470 , 560, height - 470)
    p.line(40 , height - 490 , 560, height - 490)
    p.line(180 , height - 410 , 180, height - 510)
    p.line(380 , height - 410 , 380, height - 510)


    p.drawString(70, height - 425, "Particulars")
    p.drawString(230, height - 425, "DC Member 1")
    p.drawString(430, height - 425, "DC Member 2")
    p.drawString(50, height - 445, "Name")
    p.drawString(190,height-444,dc.name1)
    p.drawString(400,height-444,dc.name2)
    p.drawString(50, height - 465, "Desgination")
    p.drawString(190,height-464,dc.designation_and_department1)
    p.drawString(400,height-464,dc.designation_and_department2)
    p.drawString(50, height - 485, "OrganiZation Address")
    p.drawString(190,height-484,dc.college_organization_address1)
    p.drawString(400,height-484,dc.college_organization_address1)
    p.drawString(50, height - 505, "Area Of Research")
    p.drawString(190,height-504,dc.area_of_research1)
    p.drawString(400,height-504,dc.area_of_research2)



    p.drawString(250, height - 560, "DECLARATION")
    
    p.setFont("Helvetica", 10)

    p.drawString(100, height - 575, "I hereby declare that all the information provided in this application for admission to the Ph.D.")
    p.drawString(70, height - 585, "programme is accurate and truthful to the best of my knowledge.")
    p.drawString(100, height - 605, "I commit to upholding the highest standards of academic integrity and research ethics as outlined")
    p.drawString(70, height - 615, "in the R&D Policy of Ramco Institute of Technology.")



    # End the second page
    p.showPage()
    p.save()

    # Get the value of the buffer and close it
    pdf = buffer.getvalue()
    buffer.close()

    # Create the HttpResponse object with the appropriate PDF headers
    response = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = f'attachment; filename="{}.pdf"'   # This will prompt a download

    return response



    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="e_approval.pdf"'
    response.write(pdf)
    return response

# views.py
import qrcode


# URL to encode in the QR code
QR_URL = "http://192.168.137.218:8000/Dcmembers/check_register_number"

def generate_qrcode(request):
    # Generate QR code image
    qr = qrcode.QRCode(
        version=1, 
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10, 
        border=4
    )
    qr.add_data(QR_URL)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the image in memory
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response



def display_qrcode(request):
    context = {'qr_url': QR_URL}
    return render(request, 'application/display_qrcode.html', context)


def edit_form(request):
    return render(request, 'application/edit_form.html')




# import tkinter as tk
# from tkinter import messagebox


def check_register_number(request):
    if request.method == 'POST':
        register_number = request.POST.get('register_number')
        if ApplicationDetails.objects.filter(register_number=register_number).exists():
            return redirect('upload_image')
        else:
            return HttpResponse("Register number does not exist.")
    return render(request, 'application/check_register_number.html')



# def edit(request):
#     return render(request, 'RegisterNumber.html')


def check_form(request):
    if request.method == 'POST':
        register_number = request.POST.get('register_number')
        if ApplicationDetails.objects.filter(register_number=register_number).exists():
            return redirect('edit_form')
        else:
            return HttpResponse("Register number does not exist.")
        
    return render(request, 'application/RegisterNumber.html')


# -----------------------------------------


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from applications.models import ApplicationDetails
from .form import UploadImagesForm  # Replace with your actual form

def upload_images(request, register_number):
    if request.method == 'POST':
        # Get the ApplicationDetails instance based on the register_number
        application = get_object_or_404(ApplicationDetails, register_number=register_number)

        # Process uploaded files
        uploaded_files = request.FILES
        file_paths = save_uploaded_images(uploaded_files, application.register_number)

        # Optionally save file paths to the database or do something else
        # ...

        return HttpResponse("Images uploaded successfully!")
    
    # Render the upload form
    form = UploadImagesForm()  # Replace with your actual form
    return render(request, 'application/upload_image.html', {'form': form})


import os
from applications.models import ApplicationDetails

def save_uploaded_images(file_dict, register_number):
    # Create directory path for the given register number
    base_directory = os.path.join('media', str(register_number))
    os.makedirs(base_directory, exist_ok=True)

    file_paths = {}

    for field_name, file_obj in file_dict.items():
        # Base file name using the original image name
        base_file_name = f'{field_name}_{file_obj.name}'
        file_path = os.path.join(base_directory, base_file_name)

        # Check if the file already exists, if yes, append a number to avoid conflicts
        counter = 1
        while os.path.exists(file_path):
            new_file_name = f'{field_name}_{counter}_{file_obj.name}'
            file_path = os.path.join(base_directory, new_file_name)
            counter += 1

        # Save the image in chunks
        with open(file_path, 'wb') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)

        # Store the file path for later use
        file_paths[field_name] = file_path

    return file_paths


