from django.shortcuts import render, redirect
from .models import Products, Catogory, Customers
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
# Create your views here.

class Home(View):
    def get(self, request):
        products = None
        catogorys = Catogory.objects.all()
        catogoryID = request.GET.get('catogory')
        if catogoryID:
            products = Products.get_all_products_by_id(catogoryID)
        else:
            products = Products.objects.all()
            print('you are :', request.session.get('email'))
        return render(request, 'store/home.html', {'products':products,'catogorys':catogorys})

    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
            request.session['cart']= cart
            print(request.session['cart'])
        return redirect('home') 
           




class Signup(View):
    def get(self, request):
        return render(request, 'store/signup.html')
    
    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone_number = postData.get('phonenumber')
        email = postData.get('email')
        password = postData.get('password')
#validation
        values = {'first_name':first_name, 'last_name':last_name,'phone_number':phone_number,'email':email} 
        error_message = None
        customer = Customers(first_name=first_name,last_name=last_name,phone_number=phone_number,email=email,password=password)
        if(not first_name):
            error_message = 'First Name required!!'
        elif len(first_name)<2:
            error_message = 'Characters hould be greater than 1 word'
        
        elif not last_name:
            error_message = 'Enter Last Name!!'
        elif len(last_name)<1:
            error_message = 'Characters hould be greater than 1 word'
        elif not phone_number:
            error_message = 'Enter your phone number'
        elif len(phone_number)<10:
            error_message = 'valid 10 digit number!!'
        elif len(password)<5:
            error_message = 'Password must be atleast 6 chars long'
        elif len(email)<5:
            error_message = 'email must be 5 chars long'
        elif customer.isExists():
            error_message = 'Email is already Taken'
    
# saving method 
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('home')
        
        else:
            return render(request, 'store/signup.html', {'error':error_message,'values':values})       





class Login(View):
    def get(self, request):
        return render(request, 'store/login.html') 

    def post(self, request):
         email = request.POST.get('email')
         password = request.POST.get('password')
         customer = Customers.getcustomer_by_email(email)
         error_message = None
         if customer:
             flag = check_password(password, customer.password)
             if flag:
                request.session['customer_id']=customer.id
                request.session['email']=customer.email
                return redirect('home')
             else:
                error_message ='Email or Password invalid'
         else:
             error_message ='Email or Password invalid'
         return render(request,'store/login.html',{'error':error_message})
        
        
            
           
        
            

              
           
            
            
         


         
    
    