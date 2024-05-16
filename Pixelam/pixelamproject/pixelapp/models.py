from django.db import models

# Create your models here.

class UserAccountDetails(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    emailid = models.CharField(max_length=50)

    phoneno = models.CharField(max_length=50)

    
    def __str__(self):
        return f"{self.id} - {self.user_name} - emailid: {self.emailid} - phoneno: {self.phoneno}"








class ChatsData(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    
    servicemode = models.CharField(max_length=200)

    imgPath = models.CharField(max_length=300)
    userimage_base64 = models.TextField(default='none')  # Store Base64 string here
    prompt = models.TextField(default='none')

    botimage_base64 = models.TextField(default='none')  # Store Base64 string here

    llmresp_imgPath = models.CharField(max_length=300)
    llmresp_text = models.TextField(default='none') # html content


    # Local langs resp in html content:
    Yoruballmresp_text  = models.TextField(default='none')
    Fantellmresp_text = models.TextField(default='none')
    Kimerullmresp_text = models.TextField(default='none')
    Twillmresp_text  = models.TextField(default='none')
    Kikuyullmresp_text  = models.TextField(default='none')


    timestamp = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id} - {self.user_name} - Mode: {self.servicemode} --- Timestamp:{self.timestamp}"


class MyModel(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    image_data = models.TextField()  # Store Base64 string here

    def __str__(self):
        return f"{self.id} - {self.name}"


class TourPlace(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=200, default='none')
    image = models.CharField(max_length=200, default='none')
    description = models.TextField()
    type = models.CharField(max_length=1000, default='none')

    def __str__(self):
        return self.placename



'''

'English': 'en', 
'Yoruba': 'yo', 
'Fante': 'fat', 
'Kimeru': 'mer'
'Twi': 'tw', 
'Kikuyu': 'ki',

'Ewe': 'ee', 
'Ga': 'gaa', 
'Dagbani': 'dag', 
'Gurene': 'gur', 
'Luo': 'luo', 




# eellmresp_text  = models.TextField(default='none')
# gaallmresp_text = models.TextField(default='none')
# dagllmresp_text = models.TextField(default='none')
# gurllmresp_text = models.TextField(default='none')
# luollmresp_text = models.TextField(default='none')
'''





# class SensorData(models.Model):
#     # api_key = models.CharField(max_length=300)
#     nodename = models.CharField(max_length=255)
#     depth_1 = models.FloatField(default=0.0)
#     depth_2 = models.FloatField(default=0.0)
#     depth_3 = models.FloatField(default=0.0)
#     temperature = models.FloatField(default=0.0)
#     humidity = models.FloatField(default=0.0)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     # mode = models.CharField(max_length=10)

#     def __str__(self):
#         return f"{self.nodename} - {self.timestamp}"


# class Nodedata(models.Model):
#     user_name = models.CharField(max_length=255, default="")
#     node_name = models.CharField(max_length=255, default="")
#     Loc_lat = models.CharField(max_length=20, default="")
#     Loc_long = models.CharField(max_length=20, default="")
#     api_key = models.CharField(max_length=300, default="")

#     def __str__(self):
#         return f"{self.user_name} - {self.node_name}"


# class Clusterdata(models.Model):
#     user_name = models.CharField(max_length=255, default="")
#     cluster_name = models.CharField(max_length=255, default="")
#     clust_data = models.CharField(max_length=500, default="")

#     def __str__(self):
#         return f"{self.user_name} - {self.cluster_name}"


# ------------------------------------
# Sample Code Below
# ------------------------------------

# class Product(models.Model):
#     Product_id = models.AutoField(primary_key=True)
#     product_name = models.CharField(max_length=50)
#     category = models.CharField(max_length=50, default="")
#     slug = models.CharField(max_length=100, default="")
#     price = models.IntegerField(default=0)
#     desc = models.CharField(max_length=300)
#     image = models.ImageField(upload_to="tze/images", default="")
#     testimoniallink = models.CharField(max_length=300, default="")
#     ytlink = models.CharField(max_length=300, default="")
#     benifits = models.CharField(max_length=300, default="")
#     how_to_use = models.CharField(max_length=400, default="")
#     doc_link = models.CharField(max_length=300, default="")
#     net_Qty = models.CharField(max_length=100, default="")
#     pack_of = models.CharField(max_length=50, default="")
#     # pub_date = models.DateField()
#     # subcategory = models.CharField(max_length=30, default="")

#     def __str__(self):
#         return self.product_name

# # mem: member
# class Contact(models.Model):
#     mem_id = models.AutoField(primary_key=True)

#     mem_name = models.CharField(max_length=60, default="")
#     mem_image = models.ImageField(upload_to="tze/contactImages", default="")
#     mem_desc = models.CharField(max_length=300, default="")
#     mem_email = models.CharField(max_length=100, default="")
#     mem_phone = models.IntegerField(default=0)
#     mem_fb_link = models.CharField(max_length=100, default="")
#     mem_IG_link = models.CharField(max_length=100, default="")
#     mem_status = models.CharField(max_length=100, default="")
#     mem_tag = models.CharField(max_length=20, default="")

#     def __str__(self):
#         return self.mem_name

# class Contact(models.Model):
#     msg_id = models.AutoField(primary_key=True)

#     name = models.CharField(max_length=50, default="")
#     email = models.CharField(max_length=70, default="")
#     phone = models.IntegerField(default=0)
#     msg = models.CharField(max_length=500, default="")

#     def __str__(self):
#         return self.name
