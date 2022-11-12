from django.http import JsonResponse, QueryDict
from django.shortcuts import render

def helper():
    pass

# Create your views here.
# TODO: responds to requests of the form 'convert?from=lb&to=t_oz&value=3.14159'
def convert(request):
    context = {}
    # from is a string which identifies the type of units the input value represents
    fromType = request.GET['from']
    # to is a string representing the type of units the user wants value converted into
    toType = request.GET['to']
    # value is a floating-point number representing the number of from units
    value = request.GET['value']

    # error checking values
    fromTypeValid = False
    toTypeValid = False
    valueTypeValid = False
    # check unit types
    unitTypes = ['T', 'g', 't_oz', 'kg', 'lb', 'oz']
    for unit in unitTypes:
        if fromType == unit:
            fromTypeValid = True
        if toType == unit:
            toTypeValid = True
    # check for valid float
    try:
        float(value)
        valueTypeValid = True
    except ValueError:
        valueTypeValid = False
    # appropriate response
    if not fromTypeValid or not toTypeValid or not valueTypeValid:
        # responses were not valid types
        context['error'] = 'Invalid unit conversion request'
    else:
        context['units'] = toType
        context['value'] = 


    # must be able to convert between all unit types
    return JsonResponse(context)