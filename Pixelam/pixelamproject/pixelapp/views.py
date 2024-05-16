#  i have created this file - GTA

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, logout
from django.contrib.auth.decorators import login_required


from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserAccountDetails, ChatsData
# import uuid
# import folium
import random, os, requests, json, time, io
import requests


from geopy.geocoders import Nominatim
import re
import markdown
import base64

# import utils 
from . import utils 

# import ast
from datetime import datetime, timedelta


from django.conf import settings
from django.core.files.storage import FileSystemStorage

from gradio_client import Client, file


# media_full_path = settings.MEDIA_ROOT + "\playapp_data"
upload_file_full_path = settings.STATIC_MEDIA_ROOT + "\\static\\pixelapp\\uploaded_files"


VertexAIdomainUrl = "https://0a60-34-90-50-119.ngrok-free.app/"



from .forms import MyModelForm
from .models import MyModel

def upload_image(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_image')  # Replace with your desired redirect
    else:
        form = MyModelForm()
    return render(request, 'pixelapp/upload_image.html', {'form': form})

def image_detail(request, id):
    instance = get_object_or_404(MyModel, id=id)
    return render(request, 'pixelapp/image_detail.html', {'instance': instance})










doctors_dataset = {
    "dadar": [
        {
            "name": "Dr. Saidu Mukesh Kota",
            "phone": "09004461881",
            "link": "https://maps.app.goo.gl/cr8p5wcpJdZSC5EC8",
            "address": "1st Floor Imperial Mahal Above HDFC Bank and Shabana stores Kkhodadad Circle, Dadar TT Cir, Dadar, Mumbai, Maharashtra 400014"
        },
        {
            "name": "Dr J K Mandot",
            "phone": "02224113094",
            "link": "https://maps.app.goo.gl/Yu2C1b3eAcTftH3B9",
            "address": "5/A, Vissanji Park, Naigaum Cross Road, Near Dadar C Railway Station, Dadar, Dadar, Mumbai, Maharashtra 400014"
        },
        {
            "name": "Dr Kulkarni Ulhas Yashwant",
            "phone": "02224143865",
            "link": "https://maps.app.goo.gl/1XeKxsGLdyEdck8L9",
            "address": "173, Hindu Colony, Sir Bhalchandra Road, Dadar East, Mumbai, Maharashtra 400014"
        },
        {
            "name": "Doctor Mankar",
            "phone": "Not Available",
            "link": "https://maps.app.goo.gl/Z9XZV4yFrHvoBr9XA",
            "address": "Civic Centre, opposite to Rastriya hotel, Dadar East, Dadar, Mumbai, Maharashtra 400014"
        }
    ]
}

tourdata = {
    "nigeria": [
            {
                "placename": "Confluence of the Niger and Benue Rivers (Lokoja)",
                "keyword": "Benue Rivers",
                "imglink": "pixelapp/websiteData/nigeria/river.jpeg",
                "whatsspecial": ["majestic", "meeting point", "important rivers"]
            },
            {
                "placename": "Mount Patti (Lokoja)",
                "keyword": "Mount Patti",
                "imglink": "pixelapp/websiteData/nigeria/mountpatti.jpeg",
                "whatsspecial": ["breathtaking views", "hiking", "guided tours available"]
            },
            {
                "placename": "Wada Dam (near Lokoja)",
                "keyword": "Wada Dam",
                "imglink": "pixelapp/websiteData/nigeria/dam.jpeg",
                "whatsspecial": ["serene artificial lake", "boat rides", "picnics"]
            },
            {
                "placename": "Kogi State University (Anyigba)",
                "keyword": "University",
                "imglink": "pixelapp/websiteData/nigeria/university.jpeg",
                "whatsspecial": ["vibrant campus", "local football matches"]
            },
            {
                "placename": "Local Cuisine",
                "keyword": "Local Cuisine",
                "imglink": "pixelapp/websiteData/nigeria/food-dish.jpeg",
                "whatsspecial": ["authentic local dish"]
            }
        ]
    }


# def print_random_doctors(location, mini=2):
#     # Retrieve the list of doctors from the specified location
#     location_doctors = doctors_dataset.get(location.lower())
    
#     # If location does not exist in the dataset or has fewer than `mini` doctors, return None
#     if not location_doctors or len(location_doctors) < mini:
#         print("Location not found or insufficient doctors data.")
#         return None
    
#     # Select `mini` random doctors
#     random_doctors = random.sample(location_doctors, mini)

#     # Print the details of the selected random doctors
#     for doctor in random_doctors:
#         for name, details in doctor.items():
#             print("Doctor:", name)
#             print("Phone:", details["phone"])
#             print("Address:", details.get("address", "Address not available"))
#             print("Google Maps Link:", details["link"])
#             print()

def dashboard(request, serviceType):
    logedIn_user = request.user.username

    if serviceType == "chathistory":
        chatdata = ChatsData.objects.filter(user_name=logedIn_user).order_by('-timestamp')[:10]
        inverted_chatdata = list(chatdata)[::-1]
    else:
        # chatdata = ChatsData.objects.filter(user_name=logedIn_user)
        chatdata = ChatsData.objects.filter(user_name=logedIn_user, servicemode=serviceType).order_by('-timestamp')[:10]
        inverted_chatdata = list(chatdata)[::-1]

    # request.session['weblang'] = 'English'

    # length = trackDetails.count()

    content = {
        'serviceType' : serviceType,
        'chatdata' : inverted_chatdata,
        'doctors_dataset' : doctors_dataset,
        'tourdata' : tourdata,
    }

    return render(request, 'pixelapp/index.html', content)

# def langtrans(request):
#     return render(request, 'pixelapp/langtrans.html')

def welcome(request):
    request.session['weblang'] = "English"

    return render(request, 'pixelapp/index.html')

def language_selection(request):
    if request.method == 'POST':
        selected_language = request.POST.get('language')
        # Save the selected language to the session variable
        request.session['weblang'] = selected_language

        return redirect(reverse('dashboard', kwargs={'serviceType': 'general'}))

    else:
        return redirect(reverse('dashboard', kwargs={'serviceType': 'general'}))
        # return render(request, 'language_selection.html')
    


'''
    user_name = models.CharField(max_length=50)
    
    servicemode = models.CharField(max_length=200)

    imgPath = models.CharField(max_length=300)
    prompt = models.CharField(max_length=2000)

    llmresp_imgPath = models.CharField(max_length=300)
    llmresp_text = models.CharField(max_length=10000)

    timestamp = models.CharField(max_length=100)

'''






def langtrans(request):
    # if request.method == 'POST':
    if request.method == 'POST':

        if 'image' in request.FILES:
            uploaded_file = request.FILES['image']
        else:
            uploaded_file = "none"

        print("uploaded_file: ", uploaded_file)
        print("request.method: ", request.FILES)

        rawprompt = request.POST['prompt'] if 'prompt' in request.POST else "none"
        
        locationtext = request.POST['location'] if 'location' in request.POST else None
        latitude, longitude = utils.extract_lat_long(str(locationtext))

        location_details = utils.get_location_details(latitude, longitude)

        # finallocationtext = f"\n user location details : latitude={latitude} longitude={longitude} \n address={location_details}"
        finallocationtext = " User location details : Africa - Nigeria. "

        if "@traveljournal" in rawprompt:
            prompt = finallocationtext + rawprompt 
        else:             
            prompt = rawprompt 

        if "@lang" in prompt:
            print("lang")
            promptAction = "lang"
        elif "@medical" in prompt:
            print("medical")
            promptAction = "medical"
        elif "@learn" in prompt:
            print("learn")
            promptAction = "learn"
        elif "@shop" in prompt:
            print("shop")
            promptAction = "shop"
        elif "@upscale" in prompt:
            print("upscale")
            promptAction = "upscale"
        elif "@traveljournal" in prompt:
            print("upscale")
            promptAction = "traveljournal"
        
        elif "@map" in prompt:
            print("map")
            promptAction = "map"
        
        elif "@caption" in prompt:
            print("caption")
            promptAction = "caption"
        
        elif "@imggen" in prompt:
            print("imggen")
            promptAction = "imggen"
        

        else:
            promptAction = "general"

        



        logedIn_user = request.user.username
        current_time = datetime.now()
        formatted_time = current_time.strftime("%d/%m/%y %H:%M:%S")
        timestamp = formatted_time


        if uploaded_file != 'none':
            if uploaded_file.name.lower().endswith(('.png', '.jpeg', '.jpg')):
                formatted_time = formatted_time.replace('/', '_')  # Replace slashes with underscores
                formatted_time = formatted_time.replace(':', '_')  # Replace colons with underscores
                formatted_time = formatted_time.replace(' ', '_')  # Replace spaces with underscores
                
                filename = f"{formatted_time}_{uploaded_file.name}"  # Prepend the formatted time to the filename
                # fs = FileSystemStorage(location=settings.STATIC_MEDIA_ROOT + '/static/pixelapp/uploaded_files')
                # filepath = fs.save(filename, uploaded_file)
                
                # StorageImgPath = f"pixelapp/uploaded_files/{filepath}"
                # imgPath = f"/static/pixelapp/uploaded_files/{filepath}"
                imgPath = 'none'
                imgFullPath = settings.STATIC_MEDIA_ROOT.replace("\\", '/') + imgPath
                StorageImgPath = 'none'

                # print("settings.STATIC_MEDIA_ROOT:", settings.STATIC_MEDIA_ROOT)
                # print("imgPath:", imgPath)
                # print("imgFullPath:", imgFullPath)
                # print("StorageImgPath:", StorageImgPath)
                # Literal['Twi', 'Amharic', 'Dagbani', 'Ewe', 'Ga', 'Gurene', 'Fante', 'Hausa', 'Kikuyu', 'Kimeru', 'Luo', 'Shona', 'Swahili', 'Tigrinya', 'Yoruba'] in 'Choose Language! (default is Twi)' Dropdown component

                image_data = uploaded_file.read()


                # Encode the image to base64
                userimage_base64 = base64.b64encode(image_data).decode('utf-8')
                # print(userimage_base64)


                # settings.STATIC_MEDIA_ROOT: C:\Users\Atharva Pawar\Documents\GitHub\Pixelam\pixelamproject\pixelapp
                # imgPath: /static/pixelapp/uploaded_files/11_05_24_02_23_00_sampledata.jpeg
                # imgFullPath: C:/Users/Atharva Pawar/Documents/GitHub/Pixelam/pixelamproject/pixelapp/static/pixelapp/uploaded_files/11_05_24_02_23_00_sampledata.jpeg
                # StorageImgPath: /pixelapp/uploaded_files/11_05_24_02_23_00_sampledata.jpeg

            else:
                imgPath = 'none'
                StorageImgPath = 'none'
                userimage_base64 = 'none'
        else:
            imgPath = 'none'
            StorageImgPath = 'none'
            userimage_base64 = 'none'


        # prompt = "what is the famous local items in africa list them"

        if userimage_base64 != 'none':

            if "@upscale" in prompt:
                # image_path = 'cat.png'
                # text_prompt = 'a white cat'
                response = utils.upScaleAPI(userimage_base64, rawprompt, VertexAIdomainUrl)

                current_time = datetime.now()
                formatted_time = current_time.strftime("%d/%m/%y %H:%M:%S")


                formatted_time = formatted_time.replace('/', '_')  # Replace slashes with underscores
                formatted_time = formatted_time.replace(':', '_')  # Replace colons with underscores
                formatted_time = formatted_time.replace(' ', '_')  # Replace spaces with underscores
                
                filename = f"refine{formatted_time}_{uploaded_file}.jpeg"  # Prepend the formatted time to the filename

                imgPath = f"/static/pixelapp/uploaded_files/{filename}"
                imgFullPath = settings.STATIC_MEDIA_ROOT.replace("\\", '/') + imgPath
                # print("v2 - imgFullPath: ", imgFullPath)

                # llmresp_imgPath = f"pixelapp/uploaded_files/{filename}"
                llmresp_imgPath = 'none'
                llmresp_text = 'none'
                
                # with open(imgFullPath, 'wb') as f:
                #     f.write(response.content)
                    
                image_data = response.content
                botimage_base64 = base64.b64encode(image_data).decode('utf-8')


            else:
                print("Vertex_Img_text_2_text(imgFullPath, prompt)....")
                llmresp_text = utils.Vertex_Img_text_2_text(userimage_base64, prompt)
                
                llmresp_imgPath = 'none'
                botimage_base64 = 'none'


        else:
            print("vertexAIGen(prompt)....")
            if "@imggen" in prompt:
                prompt_without_imggen = prompt.replace("@imggen", "").strip()
                if str(request.session['weblang']) != 'English':
                    prompt_without_imggen = utils.translate(prompt_without_imggen, str(request.session['weblang']), 'English')
                print("\n---------Img gen prompt_without_imggen : ", prompt_without_imggen)

                botimage_base64 = utils.imgGen(prompt_without_imggen, VertexAIdomainUrl)
                llmresp_text = "none"

            elif "@map" in prompt:
                llmresp_text = 'none'    
                botimage_base64 = 'none'

            else:
                if str(request.session['weblang']) != 'English':
                    if "@lang" in prompt:
                        prompt_without_lang = prompt.replace("@lang", "").strip()
                    else:
                        prompt_without_lang = prompt.strip()
                    
                    if promptAction != "caption":
                        # print(prompt_without_imggen)
                        prompt_without_lang = utils.textSummary(prompt_without_lang)
                        localLan2engprompt = utils.translate(prompt_without_lang, str(request.session['weblang']), 'English')
                        llmresp_text = utils.vertexAIGen(localLan2engprompt)

                elif promptAction == "caption":
                    urls = re.findall(r'\bhttps?://\S+?\.(?:jpg|png|jpeg)\b', rawprompt)
                    client = Client("Ghana-NLP/khaya-image-caption")
                    print("urls[0]", urls[0])
                    if str(request.session['weblang']) != "English":
                        result = client.predict(file(urls[0]),str(request.session['weblang']),api_name="/generate")
                        llmresp_text = f"English :{result[0]} \n\n {str(request.session['weblang'])} : {result[1]}"  
                    else:
                        result = client.predict(file(urls[0]),"Yoruba",api_name="/generate")
                        # result = client.predict(file('https://miro.medium.com/v2/resize:fit:460/0*yuztX2tq7yF4m3WB.jpg'),"Twi",api_name="/generate")
                        llmresp_text = f"English :{result[0]} \n\n Yoruba : {result[1]}"  

                    print(result)



                else:
                    llmresp_text = utils.vertexAIGen(prompt)
                
                botimage_base64 = 'none'
            llmresp_imgPath = 'none'
            # print("---")

        # time.sleep(10) # sleep for 10 sec

        # Gen Part 
        # llmresp_imgPath = "llm-data"
        # llmresp_text = vertexAIGen(prompt)

        if llmresp_text != "none":

            Yoruballmresp_text  = markdown.markdown(utils.translate(llmresp_text, 'English', 'Yoruba')) # Translating from English to Yoruba
            Twillmresp_text     = markdown.markdown(utils.translate(llmresp_text, 'English', 'Twi'))    # Translating from English to Yoruba
            
            # Fantellmresp_text   = markdown.markdown(utils.translate(llmresp_text, 'English', 'Fante'))  # Translating from English to Yoruba
            # Kimerullmresp_text  = markdown.markdown(utils.translate(llmresp_text, 'English', 'Kimeru')) # Translating from English to Yoruba
            # Kikuyullmresp_text  = markdown.markdown(utils.translate(llmresp_text, 'English', 'Kikuyu')) # Translating from English to Yoruba
            Fantellmresp_text   = 'none'
            Kimerullmresp_text  = 'none'
            Kikuyullmresp_text  = 'none'
        
        else:
            Yoruballmresp_text  = 'none'
            Fantellmresp_text   = 'none'
            Kimerullmresp_text  = 'none'
            Twillmresp_text     = 'none'
            Kikuyullmresp_text  = 'none'

        '''
        'English': 'en', 
        'Yoruba': 'yo', 
        'Fante': 'fat', 
        'Kimeru': 'mer'
        'Twi': 'tw', 
        'Kikuyu': 'ki',
        '''
        # print("transllmresp_text: ", transllmresp_text)
        # print(translate(trans, 'Yoruba', 'English'))  # Translating from Yoruba to English


        if llmresp_text != 'none':
            mark2htmldata = markdown.markdown(llmresp_text)
        else:
            mark2htmldata = 'none'

        printdata = f"""
                    uploaded_file = {uploaded_file}\n
                    location = {finallocationtext}\n
                    prompt = {prompt}\n\n

                    ### llmresp_imgPath = {llmresp_imgPath}\n

                    ### Translang Check :
                        Yoruballmresp_text  :   {bool(Yoruballmresp_text)}
                        Fantellmresp_text   :   {bool(Fantellmresp_text)}
                        Kimerullmresp_text  :   {bool(Kimerullmresp_text)}
                        Twillmresp_text     :   {bool(Twillmresp_text)}
                        Kikuyullmresp_text  :   {bool(Kikuyullmresp_text)}


                    """
                    # mark2htmldata = {mark2htmldata}\n
                    # llmresp_text = {llmresp_text}\n\n\n\n
        print(printdata)


        dailyDetails = ChatsData.objects.create(
                user_name           = logedIn_user,
                servicemode         = promptAction,
                
                imgPath             = StorageImgPath,
                prompt              = rawprompt,
                userimage_base64    = userimage_base64,

                llmresp_imgPath     = llmresp_imgPath,
                botimage_base64     = botimage_base64,
                llmresp_text        = mark2htmldata,        # in English

                Yoruballmresp_text  = Yoruballmresp_text ,  # trans in html content
                Fantellmresp_text   = Fantellmresp_text ,   # trans in html content
                Kimerullmresp_text  = Kimerullmresp_text ,  # trans in html content
                Twillmresp_text     = Twillmresp_text ,     # trans in html content
                Kikuyullmresp_text  = Kikuyullmresp_text ,  # trans in html content

                timestamp=timestamp
            )
        print("dailyDetails: ", dailyDetails)
        
        
        
        
        # trackDetails = ChatsData.objects.filter(user_name=logedIn_user)
        # length = trackDetails.count()

        # user_account = UserAccountDetails.objects.get(user_name=logedIn_user)
        # user_account.points = length
        # user_account.save()

        # return HttpResponse('File uploaded successfully!')
        # serviceType = 'example'  # Example value, replace with your actual logic

        # Redirect to the welcome view with the serviceType argument
        return redirect(reverse('dashboard', kwargs={'serviceType': promptAction}))
        # return redirect('dashboard')

        # else:
        #     # return HttpResponse('Only .png, .jpeg, .jpg files are allowed!')
        #     return redirect('welcome')

    return redirect('welcome')





def nearbyattractions(request):
    return render(request, 'pixelapp/mapt.html')





def shop(request):
    return render(request, 'pixelapp/shop.html')

def medical(request):
    return render(request, 'pixelapp/medical.html')

def learn(request):
    return render(request, 'pixelapp/learn.html')




def collage(request):

    logedIn_user = request.user.username

    # Filter ChatsData instances based on user_name
    chats_data = ChatsData.objects.filter(user_name=logedIn_user)

    # Extract userimage_base64 values into a list
    rawuserimage_base64_list = list(chats_data.values_list('userimage_base64', flat=True))
    userimage_base64_list = []
    print("rawuserimage_base64_list: ", len(rawuserimage_base64_list))
    # print("rawuserimage_base64_list: ", rawuserimage_base64_list)

    for baseitem in rawuserimage_base64_list: 
        print("-------", baseitem[:20])
        if baseitem != 'none':
            userimage_base64_list.append(baseitem)

    print("userimage_base64_list: ", len(userimage_base64_list))

    if len(userimage_base64_list) >= 4:
        # Example usage:
        # img_base64_list = userimage_base64_list[:4]
        img_base64_list = random.sample(userimage_base64_list, k=4)

        grid = utils.create_2x2_grid_from_base64(img_base64_list)

        # Save the grid image to a BytesIO object
        img_byte_array = io.BytesIO()
        grid.save(img_byte_array, format='JPEG')

        # Encode the BytesIO object to base64
        base64_img = base64.b64encode(img_byte_array.getvalue()).decode()

        # print(base64_img)  # Print the base64 encoded collage image
    
    else:
        base64_img = 'none'

    content = {
        'allbase64' : userimage_base64_list,
        'collageimg'   : base64_img,
    }

    return render(request, 'pixelapp/collage.html', content)


















def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        phoneno = request.POST['phoneno']
        
        # Check if the username is unique
        if not User.objects.filter(username=username).exists():
            # Create a new user
            user = User.objects.create_user(username=username, password=password, email=email)
            userDetails = UserAccountDetails.objects.create(
                    user_name=username,
                    emailid=email,
                    phoneno=phoneno,

                )
            print("user: ", user)
            print("userDetails: ", userDetails)
            return redirect('welcome')  # Redirect to your login view
        else:
            error_message = 'Username already exists'
    else:
        error_message = None

    return render(request, 'pixelapp/index.html', {'error_message': error_message})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')  # Redirect to your dashboard view
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = None

    return render(request, 'pixelapp/index.html', {'error_message': error_message})


def user_logout(request):
    logout(request)
    return redirect('welcome')  # Redirect to your login view







# Ref Code
# ----------------------------------------------------------------------------------------


# @login_required
# def viewNodes(request):
#     try:

#         user_nodes = Nodedata.objects.filter(user_name=request.user.username)
#         user_clusterdata = Clusterdata.objects.filter(
#             user_name=request.user.username)
#         # print("user_nodes : ", user_nodes)
#         # print("username : ", request.user.username)

#         # Pass the list of nodes to the template
#         context = {
#             'user_nodes': user_nodes,
#             'user_clusterdata': user_clusterdata,
#         }
#         return render(request, 'agroapp/nodes.html', context)

#     except:
#         return render(request, 'agroapp/nodes.html')


# @login_required
# def addnode(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('user_name')
#         node_name = request.POST.get('node_name')
#         Loc_lat = request.POST.get('lat')
#         Loc_long = request.POST.get('long')
#         api_key = generate_unique_api_key()

#         # Create a new node
#         Nodedata.objects.create(user_name=user_name,
#                                 node_name=node_name,
#                                 Loc_lat=Loc_lat,
#                                 Loc_long=Loc_long,
#                                 api_key=api_key)

#         # Redirect to a success page or another view
#         return redirect(
#             'viewNodes'
#         )  # Change 'node_list' to the actual URL name for the node list view

#     return render(request, 'agroapp/addnode.html')


# @login_required
# def addcluster(request):
#     if request.method == 'POST':
#         selected_nodes = request.POST.getlist('selected_nodes')
#         user_name = request.user.username
#         cluster_name = request.POST.get('cluster_name')

#         print("Selected Nodes:", selected_nodes, user_name, cluster_name)

#         # Create a new node
#         Clusterdata.objects.create(user_name=user_name,
#                                    cluster_name=cluster_name,
#                                    clust_data=selected_nodes)

#         # Redirect to a success page or another view
#         return redirect(
#             'viewNodes'
#         )  # Change 'node_list' to the actual URL name for the node list view

#     user_nodes = Nodedata.objects.filter(user_name=request.user.username)
#     context = {
#         'user_nodes': user_nodes,
#     }
#     return render(request, 'agroapp/addcluster.html', context)


# def get_the_map(lat, long, node_name):
#     # Specify the latitude and longitude
#     # lat, lon = 123.13, 123.34

#     # Create a Folium map centered at the specified location
#     my_map = folium.Map(location=[lat, long], zoom_start=16)

#     # Add a marker at the specified location
#     folium.Marker([lat, long], popup=node_name).add_to(my_map)
#     # folium.Marker([lat, long], popup=node_name, icon=folium.Icon(color='red')).add_to(my_map)

#     # Convert the map to HTML
#     map_html = my_map._repr_html_()
#     return map_html

#     # Pass the HTML content to the template
#     # return render(request, 'mymaps.html', {'map_html': map_html})


# def get_the_map_multipal_loc(locations):
#     # Create a Folium map centered at the first location
#     first_location = locations[0]

#     my_map = folium.Map(
#         location=[first_location['lat'], first_location['long']],
#         zoom_start=16)

#     # Add markers for each location
#     for location in locations:
#         folium.Marker([location['lat'], location['long']],
#                       popup=location['node_name']).add_to(my_map)

#     # Convert the map to HTML
#     map_html = my_map._repr_html_()
#     return map_html


# # @login_required
# def viewNodeData(request):
#     # Get parameters from the GET request

#     # username = request.GET.get('username', '')  # Hacker Trap
#     # username = request.user.username
#     nodename = request.GET.get('nodename', '')
#     # lat = request.GET.get('lat', '')
#     # long = request.GET.get('long', '')

#     if Nodedata.objects.filter(node_name=nodename).exists():
#         # Use the parameters as needed in your view logic
#         try:
#             # Example: Retrieve sensor data based on the node name

#             sensor_data = SensorData.objects.filter(
#                 nodename=nodename).order_by('-timestamp')
#             # sensor_data = SensorData.objects.filter(nodename=nodename)

#             # Retrieve the latest data for the specified nodename
#             latest_sensor_data = SensorData.objects.filter(
#                 nodename=nodename).order_by('-timestamp').first()

#             latest_5_sensor_data_list = SensorData.objects.filter(
#                 nodename=nodename).order_by('-timestamp')[:5]
#             latest_5_sensor_data_list = latest_5_sensor_data_list[::-1]

#             # if not latest_5_sensor_data_list:
#             # latest_5_sensor_data_list = latest_sensor_data
#             # latest_sensor_data = "null"

#         except:
#             sensor_data = "null"
#             latest_sensor_data = "null"
#             latest_5_sensor_data_list = "null"

#         user_node_data = Nodedata.objects.filter(node_name=nodename).first()

#         if user_node_data:
#             api_key = user_node_data.api_key
#             user_name = user_node_data.user_name
#             lat = user_node_data.Loc_lat
#             long = user_node_data.Loc_long
#         else:
#             api_key = 'Not available'
#             user_name = 'Not available'
#             lat = 'Not available'
#             long = 'Not available'

#         map_html = get_the_map(lat, long, nodename)

#         # Pass data to the template
#         context = {
#             'username': user_name,
#             'nodename': nodename,
#             'lat': lat,
#             'long': long,
#             'api_key': api_key,
#             'sensor_data': sensor_data,
#             'latest_data': latest_sensor_data,
#             'map_html': map_html,
#             'latest_5_sensor_data_list': latest_5_sensor_data_list,
#         }
#         return render(request, 'agroapp/nodedata.html', context)
#     else:
#         context = {"message": "wrong_route"}
#         return render(request, 'agroapp/nodedata.html', context)


# # @login_required
# def viewclusterData(request):

#     # username = request.GET.get('username', '')  # Hacker Trap
#     # username = request.user.username
#     clustername = request.GET.get('clustername', '')

#     if Clusterdata.objects.filter(cluster_name=clustername).exists():
#         try:

#             cluster_data = Clusterdata.objects.filter(cluster_name=clustername)
#             # Extract 'clust_data' from each object and store it in a list
#             list_of_clust_data = [entry.clust_data for entry in cluster_data]

#             all_node_names = ast.literal_eval(list_of_clust_data[0])
#             all_nodeData = []

#             for item in all_node_names:
#                 __nodedata = Nodedata.objects.filter(node_name=item).first()
#                 all_nodeData.append(__nodedata)

#             locations = []
#             all_sensor_data = {nodeName: [] for nodeName in all_node_names}
#             all_latest_sensor_data = []
#             all_latest_5_sensor_data_list = []

#             for node_D in all_nodeData:
#                 locations.append({
#                     'lat': node_D.Loc_lat,
#                     'long': node_D.Loc_long,
#                     'node_name': node_D.node_name
#                 })

#             for __nodeNames in all_node_names:
#                 # print("__nodeNames : ",__nodeNames)

#                 valu = SensorData.objects.filter(
#                     nodename=__nodeNames).order_by('-timestamp')

#                 # print("valu : ", valu)

#                 all_sensor_data[__nodeNames].append(valu)
#                 # values['dadar'].append('Data 1 for Dadar')

#                 # print("all all_sensor_data :", all_sensor_data)

#                 all_latest_sensor_data.append(
#                     SensorData.objects.filter(
#                         nodename=__nodeNames).order_by('-timestamp').first())

#                 ___all_lat_5_sensor_data_list = SensorData.objects.filter(
#                     nodename=__nodeNames).order_by('-timestamp')[:5]
#                 ___all_lat_5_sensor_data_list = ___all_lat_5_sensor_data_list[::
#                                                                               -1]
#                 all_latest_5_sensor_data_list.append(
#                     ___all_lat_5_sensor_data_list)

#             # print("all_latest_5_sensor_data_list :", all_latest_5_sensor_data_list)

#             # user_node_data = Nodedata.objects.filter(node_name=nodename).first()
#             # sensor_data = SensorData.objects.filter(nodename=nodename)

#             # print("locations : ", locations)
#             map_html = get_the_map_multipal_loc(locations)

#         except:
#             all_sensor_data = "null"
#             all_latest_sensor_data = "null"
#             all_latest_5_sensor_data_list = "null"
#             map_html = "null"

#         # print("all_latest_5_sensor_data_list : " , all_latest_5_sensor_data_list)
#         # Pass data to the template
#         context = {
#             # 'username': user_name,
#             'clustername': clustername,
#             # 'lat': lat,
#             # 'long': long,
#             # 'api_key': api_key,
#             'all_sensor_data': all_sensor_data,
#             'all_latest_sensor_data': all_latest_sensor_data,
#             'all_latest_5_sensor_data_list': all_latest_5_sensor_data_list,
#             'map_html': map_html,
#         }
#         return render(request, 'agroapp/clusterdata.html', context)

#     else:
#         context = {"message": "wrong_route"}
#         return render(request, 'agroapp/clusterdata.html', context)




# route : http://127.0.0.1:8000/read_sensor_data/?username=sahil&api_key=5df155f4-9161-44b9-8ff5-9c821709e1bf&nodename=node_dadar


# def read_sensor_data(request):
#     if request.method == 'GET':
#         username = request.GET.get('username', '')
#         api_key = request.GET.get('api_key', '')
#         nodename = request.GET.get('nodename', '')

#         # Validate the username, API key, and nodename
#         user_node_data = Nodedata.objects.filter(user_name=username,
#                                                  api_key=api_key,
#                                                  node_name=nodename).first()

#         if user_node_data:
#             sensor_data = SensorData.objects.filter(nodename=nodename)
#             # Convert QuerySet to a list of dictionaries
#             sensor_data_list = list(sensor_data.values())

#             ret_data = {
#                 'user_name': username,
#                 'node_name': nodename,
#                 'sensor_Data': sensor_data_list,
#             }
#             return JsonResponse(ret_data)
#         else:
#             return JsonResponse({
#                 'status':
#                 'error',
#                 'message':
#                 'Invalid username, API key, or nodename'
#             })

#     return JsonResponse({
#         'status': 'error',
#         'message': 'Invalid request method'
#     })


# route : http://127.0.0.1:8000/sensordata/?username=sahil&api_key=5df155f4-9161-44b9-8ff5-9c821709e1bf&nodename=node_dadar&Depth_1=45.3&Depth_2=49.3&Depth_3=55.9&temperature=55.9&humidity=55.9


# def get_formatted_datetime():
#     # Get the current date and time
#     now = datetime.now()

#     # Add 6 hours to the current time
#     future_time = now + timedelta(hours=6)

#     # Define the month names
#     month_names = [
#         "January", "February", "March", "April", "May", "June", "July",
#         "August", "September", "October", "November", "December"
#     ]

#     # Extract the components of the date and time
#     month = month_names[future_time.month - 1]  # Adjust index to start from 0
#     day = future_time.day
#     year = future_time.year
#     hour = future_time.strftime("%I")  # 12-hour format
#     minute = future_time.minute
#     ampm = future_time.strftime("%p").lower()  # AM or PM

#     # Format the date and time string
#     formatted_date_time = f"{month} {day}, {year}, {hour}:{minute} {ampm}."

#     return formatted_date_time


# @csrf_exempt
# def sensor_data(request):
#     if request.method == 'GET':
#         # Get parameters from the GET request
#         username = request.GET.get('username', '')
#         api_key = request.GET.get('api_key', '')
#         nodename = request.GET.get('nodename', '')

#         depth_1 = float(request.GET.get('Depth_1', None))
#         depth_2 = float(request.GET.get('Depth_2', None))
#         depth_3 = float(request.GET.get('Depth_3', None))

#         temperature = float(request.GET.get('temperature', None))
#         humidity = float(request.GET.get('humidity', None))

#         timestampManual = get_formatted_datetime()
#         print("timestampManual :", timestampManual)

#         # Validate the username, API key, and nodename
#         user_node_data = Nodedata.objects.filter(user_name=username,
#                                                  api_key=api_key,
#                                                  node_name=nodename).first()

#         if user_node_data:
#             # Save data to the database
#             sensor_data = SensorData(
#                 nodename=nodename,
#                 depth_1=depth_1,
#                 depth_2=depth_2,
#                 depth_3=depth_3,
#                 temperature=temperature,
#                 humidity=humidity,
#                 timestamp=timestampManual  # Set the timestamp manually
#             )
#             sensor_data.save()

#             return JsonResponse({'status': 'success'})
#         else:
#             return JsonResponse({
#                 'status':
#                 'error',
#                 'message':
#                 'Invalid username, API key, or nodename'
#             })

#     return JsonResponse({
#         'status': 'error',
#         'message': 'Invalid request method'
#     })


'''
node_prabhadevi
9650ad02-52e0-4825-8f63-ef2b5235ee77

node_dadar
5df155f4-9161-44b9-8ff5-9c821709e1bf
'''
'''
import random

def generate_api_key():
    key_length = 36  # Length of the API key
    dash_positions = [8, 13, 18, 23]  # Positions of dashes in the API key

    characters = "abcdef0123456789"

    api_key = ''.join(random.choice(characters) if i not in dash_positions else '-' for i in range(key_length))
    return api_key

# Example usage
api_key = generate_api_key()
print(api_key)

'''


# def generate_api_key():
#     key_length = 36  # Length of the API key
#     dash_positions = [8, 13, 18, 23]  # Positions of dashes in the API key

#     characters = "abcdefghijklmnopqrstwxyz0123456789"

#     api_key = ''.join(
#         random.choice(characters) if i not in dash_positions else '-'
#         for i in range(key_length))
#     return api_key


# def generate_unique_api_key():
#     while True:
#         # api_key = str(uuid.uuid4())
#         api_key = str(generate_api_key())
#         if not Nodedata.objects.filter(api_key=api_key).exists():
#             return api_key


# def your_view_function(request):
#     # Your view logic here
#     api_key = generate_unique_api_key()

#     # Use api_key in your view logic or save it to the database

#     return HttpResponse(f"Generated API Key: {api_key}")


# ------------------------------------
# Sample Code Below
# ------------------------------------

# def index(request):
#     products = Product.objects.all()

#     all_prods = []
#     catProds = Product.objects.values('category', 'Product_id')
#     cats = {item['category'] for item in catProds}
#     for cat in cats:
#         prod = Product.objects.filter(category=cat)
#         n = len(products)
#         all_prods.append([prod, n])

#     params = {
#         'catproducts' : all_prods,
#         'allproducts' : products,
#               }

#     return render(request,'tze/index.html', params)

# def business(request):
#     # return HttpResponse('Teamzeffort    |      business Page')
#     return render(request,'tze/business.html')

# def about(request):
#     return render(request,'tze/about.html')

# def contact(request):
#     coreMem = Contact.objects.filter(mem_tag="core")
#     teamMem = Contact.objects.filter(mem_tag="team")
#     # print(f"coreMem: {coreMem} \n teamMem: {teamMem}")

#     return render(request, 'tze/contact.html', {'core':coreMem,'team':teamMem })

# def productView(request, myslug):
#     # Fetch the product using the id
#     product = Product.objects.filter(slug=myslug)
#     prodCat = product[0].category
#     # print(prodCat)
#     recproduct = Product.objects.filter(category=prodCat)
#     # print(recproduct)

#     # randomObjects = random.sample(recproduct, 2)
#     randomObjects = random.sample(list(recproduct), 2)

#     return render(request, 'tze/prodView.html', {'product':product[0],'recprod':randomObjects })

# # def index(request):
# #     return HttpResponse('Teamzeffort    |      index Page')
