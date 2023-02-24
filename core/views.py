"""
view to drive landingpage
"""

from django.shortcuts import render


def home(request):
    """landing page"""
    return render(request, 'core/index.html')
