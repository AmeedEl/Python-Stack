from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    released_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
def get_all_shows():
    return Show.objects.all()

def get_show_by_id(id):
    return Show.objects.get(id = id)

def create_show(data):
    # title = data['title']
    # network = data['network']
    # released_date = data['released_date']
    # desc = data['desc']
    # Show.objects.create(title=title, network=network, released_date=released_date, desc=desc)
    
    # Another way that will do the same job..
    Show.objects.create(title=data['title'], network=data['network'], released_date=data['released_date'], desc=data['desc'])
    
    
def delete_show(id):
    show = Show.objects.get(id=id)
    show.delete()
    
def edit_show(id):
    show = Show.objects.get(id=id)
    return show

def update(id, title, network, released_date, desc):
    show = Show.objects.get(id=id)
    show.title = title
    show.network = network
    show.released_date = released_date
    show.desc = desc
    show.save()
    return show
 
    
    