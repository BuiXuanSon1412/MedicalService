def home(request):
    return render(request, 'user/home.html')

def developing(request):
    return HttpResponse('')

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email or Password does not correct')

    context = {'page':page}
    return render(request, 'user/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def signup(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        email = request.POST.get('email')
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save() 
            login(request, user)
            membership = Membership.objects.filter(membership_id=1)[0]
            new_patient = Patient.objects.create(user=request.user, membership=membership)
            return redirect('home')
        else:
            messages.error(request," An error occured during registration ")
            return render(request,'user/signup.html', {'form':form})

    context = {'form':form}
    return render(request, 'user/signup.html', context)