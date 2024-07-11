from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Profile, data


# Create your views here.
def home(request):
    return render(request,'home.html')
def vehicle(request):
    return render(request,'vehicle.html')
def tvs(request):
    return render(request,'tvs.html')
def yamaha(request):
    return render(request,'yamaha.html')
def bajaj(request):
    return render(request,'bajaj.html')
def emailotp(request):
    return render(request,'emailotp.html')
def data1(request):
    firstName=request.POST.get("firstName")
    email=request.POST.get("email")
    OTP = "123456"
    subject = 'Your Loan Verification Information'
    message = f'YOUR OTP is :{OTP}'
    rr=Profile(firstName=firstName,email=email)
    rr.save()
    from_email ='raviperumalmech30@gmail.com'
    send_mail(subject,message,from_email,[email])
    return render(request,'otp.html')
def otp1(request):
    Cus_otp=request.POST.get("Cus_otp")
    OTP = "123456"
    if Cus_otp==OTP :
        return render(request,'loanform.html')
    else:
        return render(request,'otp.html')
def customer(request):
        fullname=request.POST.get("fullname")
        fathername=request.POST.get("fathername")
        mobile=request.POST.get("mobile")
        address=request.POST.get("address")
        id_number=request.POST.get("id_number")
        account_number=request.POST.get("account_number")
        bank_name=request.POST.get("bank_name")
        branch=request.POST.get(" branch")
        ex_showroom_price=request.POST.get("ex_showroom_price")
        loan_amount=request.POST.get("loan_amount")
        initial_amount=request.POST.get("initial_amount")
        rr=data(fullname=fullname,fathername=fathername,mobile=mobile,address=address,id_number=id_number,account_number=account_number,bank_name=bank_name,ex_showroom_price=ex_showroom_price,loan_amount=loan_amount,initial_amount=initial_amount)
        rr.save()
        return render(request,'bill.html',{"fullname":fullname,"fathername":fathername,"mobile":mobile,"address":address,"id_number":id_number,"accoun_number":account_number,"bank_name":bank_name,"branch":branch,"ex_showroom_price":ex_showroom_price,"loan_amount":loan_amount,"initial_amount":initial_amount})
# def customer(request):
#     fatherName=request.POST.get("fatherName")
#     DOB=request.POST.get("DOB")
#     Occupation=request.POST.get("Occupation")
#     rr=Profile1(fatherName=fatherName,DOB=DOB,Occupation=Occupation)
#     rr.save()
#     Profile1.objects.create(fatherName=fatherName, DOB=DOB, Occupation=Occupation)
#     return render(request,'kyc.html')
    
# def kyc(request):
#     address=request.POST.get("address")
#     city=request.POST.get("city")
#     state=request.POST.get("state")
#     zipCode=request.POST.get("zipCode")
#     bankName=request.POST.get("bankName")
#     accountNumber=request.POST.get("accountNumber")
#     ifscCode=request.POST.get("ifscCode")
#     rr=Profile2(address=address,city=city,state=state,zipCode=zipCode,bankName=bankName,accountNumber=accountNumber,ifscCode=ifscCode)
#     rr.save()
#     Profile2.objects.create(address=address, city=city, state=state, zipCode=zipCode,bankName=bankName, accountNumber=accountNumber, ifscCode=ifscCode)
#     return render(request, 'loan.html')
# def invoice(request):
#     exShowroomPrice=request.POST.get("exShowroomPrice")
#     initialPayment=request.POST.get("initialPayment")
#     loanAmount=request.POST.get("loanAmount")
#     loanApplicationDate=request.POST.get("loanApplicationDate")
#     rr=Profile3(exShowroomPrice=exShowroomPrice,initialPayment=initialPayment,loanAmount=loanAmount,loanApplicationDate=loanApplicationDate)
#     rr.save()
#     Profiles = Profile.objects.all()
#     Profiles1 = Profile1.objects.all()
#     Profiles2 = Profile2.objects.all()
#         # Here you may want to perform some calculations or processing if needed
#     return render(request, 'bill.html', {"Profiles": Profiles, "Profiles1": Profiles1, "Profiles2": Profiles2, "exShowroomPrice":exShowroomPrice, "initialPayment":initialPayment,"loanAmount":loanAmount})
def about1(request):
    return render(request,'about1.html')

