from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from .models import ContactForm, QuickLead
from django.shortcuts import get_object_or_404, render,redirect
from .models import Room, TeamMember, House, GalleryImage, Review, AmenityTag



def chunked(iterable, n):
      for i in range(0, len(iterable), n):
          yield iterable[i:i + n]

def index(request):
    if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        contact_number = request.POST.get("contact_number")
        email = request.POST.get("email")

        if first_name and last_name and contact_number and email:
            QuickLead.objects.create(
                first_name=first_name,
                last_name=last_name,
                contact_number=contact_number,
                email=email
            )
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "error": "All fields are required"})

    # Regular GET page load
    house = House.objects.all()
    gallery = GalleryImage.objects.all()
    amenities = AmenityTag.objects.all()
    review = Review.objects.all()
    review_chunks = list(chunked(review, 3))

    return render(request, 'index.html', {
        'house': house,
        'gallery': gallery,
        'review': review,
        'review_chunks': review_chunks,
        'amenities': amenities
    })

def house_detail(request, pk):
    house = get_object_or_404(House, pk=pk)
    rooms = house.rooms.all()
    house_amenities = house.amenities.select_related('tag')

    context = {
        'house': house,
        'rooms': rooms,
        'house_amenities': house_amenities,
    }
    return render(request, 'house_detail.html', context)


def home_schedule_visit(request):
    if request.method == "POST":
        room_id = request.POST.get("room_id")
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        contact_number = request.POST.get("contact_number")
        message = request.POST.get("message", "")

        # Create a new ContactForm instance and save it
        try:
            contact_form = ContactForm(
                room_id=room_id,
                full_name=full_name,
                email=email,
                contact_number=contact_number,
                message=message
            )
            contact_form.save()

            # Show success message
            messages.success(request, "Your request has been submitted successfully!")
        except Exception as e:
            # In case of error, show an error message
            messages.error(request, f"There was an error submitting your request: {str(e)}")
        
        # Redirect back to the referring page or a default page if no referer is found
        return redirect(request.META.get('HTTP_REFERER', '/'))

    return redirect('/') 

def about(request):

 t=TeamMember.objects.all()

 return render(request,'about.html',{'t':t })

def schedule_visit(request):
    if request.method == "POST":
        room_id = request.POST.get("room_id")
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        contact_number = request.POST.get("contact_number")
        message = request.POST.get("message", "")

        # Create a new ContactForm instance and save it
        try:
            contact_form = ContactForm(
                room_id=room_id,
                full_name=full_name,
                email=email,
                contact_number=contact_number,
                message=message
            )
            contact_form.save()

            # Show success message
            messages.success(request, "Your request has been submitted successfully!")
        except Exception as e:
            # In case of error, show an error message
            messages.error(request, f"There was an error submitting your request: {str(e)}")
        
        # Redirect back to the referring page or a default page if no referer is found
        return redirect(request.META.get('HTTP_REFERER', 'rooms'))

    return redirect('rooms') 




def houses(request):
  house = House.objects.all()
  return render(request, 'houses.html', {'house': house})

