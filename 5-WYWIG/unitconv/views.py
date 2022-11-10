from django.shortcuts import render

# Create your views here.
def convert(request):
# TODO: responds to requests of the form
    # convert?from=lb&to=t_oz&value=3.14159
        # from is a string which identifies the type of units the input value represents
        # value is a floating-point number representing the number of from units
        # to is a string representing the type of units the user wants value converted into
    # result of a valid request is JSON
        # value is a floating-point number representing the number of units
        # units identify the units of the output value, which must match the to parameter of the request
    # result of an invalid query
        # a JSON object indicating an error message is returned instead
    # makes its calculations through django model
        # sensible schema, one table
        # algorithm for converting units
        # create data migration to initialize db w/ necessary converstion factors
            # this is the only place to hard code factors
            # US Ton (T)
            # Gram (g)
            # Troy Ounce (t_oz)
            # kilogram (kg)
            # imperial pound (lb)
            # ounce (oz)
        # must be able to convert between all unit types
    pass