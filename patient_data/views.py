from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DoctorForm, PatientForm, AppointmentForm, PrescriptionForm



from django.contrib.auth.models import User
from.models import *
from django.shortcuts import render,redirect

# Create your views here.
def aboutus(request):
    return render(request, "about.html")
def navigation_bar(request):
    return render(request, "navigation_bar.html")
def contactus(request):
    return render(request, "contact.html")
def home(request):
    return render(request, "home.html")

def index(request):
    if not request.user.is_staff:
        return redirect("login")
    else:
      return render(request, "index.html")


def admin_dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")

    doctor_count = Doctor.objects.count()
    patient_count = patient.objects.count()
    appointment_count = Appointment.objects.count()

    return render(request, "admin_home.html", {
        "doctor_count": doctor_count,
        "patient_count": patient_count,
        "appointment_count": appointment_count,
    })

def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")

        messages.error(request, "Invalid username or password.")
        return redirect("login")

    return render(request, "login.html")

def logout_admin(request):
    logout(request)
    return redirect('login')


def views_doctor(request):
    if not request.user.is_authenticated:
        return redirect("login")

    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, "views_doctor.html", d)

def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('view_doctor')   # Correct

    else:
        form = DoctorForm()

    return render(request, 'add_doctor.html', {'form': form})


def register(request):
    if request.method == "POST":

        fullname = request.POST.get("fullname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Check password
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        # Check username
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        # Create user
        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=fullname
        )

        # Go to Login page
        messages.success(request, "Registration successful! Please login.")
        return redirect("login")

    return render(request, "register.html")


def views_patient(request):
    if not request.user.is_authenticated:
        return redirect("login")

    pat = patient.objects.all()
    p = {'pat': pat}
    return render(request, "views_patient.html", p)


def add_patient(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        name = request.POST['name']
        mobile = request.POST['mobile']
        age = request.POST['age']
        gender = request.POST['gender']
        address = request.POST['address']

        patient.objects.create(
            name=name,
            mobile=mobile,
            age=age,
            gender=gender,
            address=address
        )

        return redirect("view_patient")

    return render(request, "add_patient.html")

def add_appointment(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("view_appointment")

    else:
        form = AppointmentForm()

    return render(request, "add_appointment.html", {"form": form})

def view_appointment(request):
    if not request.user.is_authenticated:
        return redirect("login")

    app = Appointment.objects.all()

    return render(request, "view_appointment.html", {"app": app})

@login_required(login_url='login')
def profile(request):
    return render(request, "profile.html")

def delete_doctor(request, pid):
    if not request.user.is_authenticated:
        return redirect("login")

    doctor = get_object_or_404(Doctor, id=pid)
    doctor.delete()

    return redirect("view_doctor")

def delete_patient(request, pid):
    if not request.user.is_authenticated:
        return redirect("login")

    pat = get_object_or_404(patient, id=pid)
    pat.delete()

    return redirect("view_patient")
def add_prescription(request):

    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":

        form = PrescriptionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("add_prescription")

    else:
        form = PrescriptionForm()

    return render(request, "add_prescription.html", {
        "form": form
    })

def view_prescription(request):

    if not request.user.is_authenticated:
        return redirect("login")

    prescriptions = Prescription.objects.all()

    return render(request, "view_prescription.html", {
        "prescriptions": prescriptions
    })


def delete_prescription(request, pid):
    if not request.user.is_authenticated:
        return redirect("login")

    prescription = get_object_or_404(Prescription, id=pid)
    prescription.delete()

    return redirect("view_prescription")