from django.shortcuts import render


def source_plagiarism(request):
    return render(request, 'html/source_plag.html')
