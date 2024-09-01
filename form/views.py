from django.shortcuts import render
from form.forms import AlunoForm

# Create your views here.


def cadastro_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= AlunoForm()

    form = AlunoForm()
    return render(request,'forms.html', {'form': form})
